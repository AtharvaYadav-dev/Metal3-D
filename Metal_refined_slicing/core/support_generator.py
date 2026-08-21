"""
Cone Support Generator (support_generator.py)
===================================================================
Generates 0.5mm cone support structures strictly up to the base clearance height (e.g., Z=5.0mm).
Supports are anchored to the build plate at Z=0 and stop strictly at the base elevation line under the model,
preventing any supports from extending up the sides or top of the model.
"""

import math
import numpy as np

try:
    import trimesh
except ImportError:
    trimesh = None


class ConeSupportGenerator:
    """
    Generates 3D 0.5mm cone support structures strictly capped at the base clearance height (Z=base_elevation).
    """
    def __init__(self, cone_diameter=0.5, grid_spacing=2.0, base_elevation=5.0, min_support_height=0.5):
        """
        :param cone_diameter: Tip and body diameter of cone support in mm (default 0.5mm).
        :param grid_spacing: Grid spacing between adjacent support cones in mm (default 2.0mm).
        :param base_elevation: Base clearance height of model above build plate in mm (default 5.0mm).
        :param min_support_height: Minimum height for support generation in mm.
        """
        self.cone_diameter = float(cone_diameter)
        self.grid_spacing = float(grid_spacing)
        self.base_elevation = float(base_elevation)
        self.min_support_height = float(min_support_height)

    def generate_supports_for_mesh(self, mesh, base_elevation=None):
        """
        Generates vertical 0.5mm cone supports extending from Z=0 up to base_elevation (e.g. 5.0mm).
        Supports NEVER extend past base_elevation up into the sides or top of the model.
        :param mesh: trimesh.Trimesh object
        :param base_elevation: Clearance height in mm. If specified, overrides self.base_elevation.
        :return: trimesh.Trimesh containing combined 0.5mm cone support meshes, or None.
        """
        if trimesh is None or mesh is None or len(mesh.faces) == 0:
            return None

        elevation = self.base_elevation if base_elevation is None else float(base_elevation)

        # Bounding box of the model
        min_x, min_y, min_z = mesh.bounds[0]
        max_x, max_y, max_z = mesh.bounds[1]

        # Downward-facing normals (bottom facets facing towards build platform)
        normals = mesh.face_normals
        centers = mesh.triangles.mean(axis=1)

        downward_mask = normals[:, 2] < -0.1
        bottom_centers = centers[downward_mask]

        if len(bottom_centers) == 0:
            bottom_centers = centers

        # Filter bottom centers to those near the bottom base elevation (near min_z)
        base_bottom_mask = bottom_centers[:, 2] <= (min_z + 2.0)
        base_bottom_centers = bottom_centers[base_bottom_mask] if np.any(base_bottom_mask) else bottom_centers

        # Sample grid across model bottom base footprint (XY bounding box)
        xs = np.arange(min_x + self.grid_spacing / 2.0, max_x, self.grid_spacing)
        ys = np.arange(min_y + self.grid_spacing / 2.0, max_y, self.grid_spacing)

        support_points = []
        for x in xs:
            for y in ys:
                # Find bottom-most Z coordinate of part base near (x, y)
                dists_sq = (base_bottom_centers[:, 0] - x)**2 + (base_bottom_centers[:, 1] - y)**2
                close_mask = dists_sq <= (self.grid_spacing * 0.75)**2
                if np.any(close_mask):
                    support_points.append((x, y, elevation))

        if not support_points:
            # Fallback: uniform grid under bounding box up to base elevation
            for x in xs:
                for y in ys:
                    support_points.append((x, y, elevation))

        cone_meshes = []
        radius_top = self.cone_diameter / 2.0
        radius_bottom = (self.cone_diameter * 1.2) / 2.0  # Slightly flared base for build plate adhesion

        for pt in support_points:
            x, y, z_top = pt[0], pt[1], pt[2]
            z_bottom = 0.0  # Anchored to build plate at Z=0

            # Strict capping: maximum top Z of any support is elevation
            total_height = min(z_top, elevation)
            if total_height < self.min_support_height:
                continue

            try:
                # 1. Main vertical cylinder body (0.5mm diameter)
                # trimesh.creation.cylinder is centered at Z=0 (from -total_height/2 to +total_height/2)
                cylinder = trimesh.creation.cylinder(
                    radius=radius_top,
                    height=total_height,
                    sections=16
                )
                translation = trimesh.transformations.translation_matrix([x, y, total_height / 2.0])
                cylinder.apply_transform(translation)

                # 2. Conical contact tip (0.5mm tip cone at top)
                # trimesh.creation.cone has base at Z=0 and apex tip at Z=tip_height
                tip_height = min(1.0, total_height * 0.25)
                tip_cone = trimesh.creation.cone(
                    radius=radius_top,
                    height=tip_height,
                    sections=16
                )
                tip_trans = trimesh.transformations.translation_matrix([x, y, total_height - tip_height])
                tip_cone.apply_transform(tip_trans)

                # 3. Flared base cone at Z=0 for build plate adhesion
                base_cone_height = min(0.8, total_height * 0.15)
                base_cone = trimesh.creation.cone(
                    radius=radius_bottom,
                    height=base_cone_height,
                    sections=16
                )
                base_trans = trimesh.transformations.translation_matrix([x, y, 0.0])
                base_cone.apply_transform(base_trans)

                cone_meshes.append(cylinder)
                cone_meshes.append(tip_cone)
                cone_meshes.append(base_cone)
            except Exception as err:
                print(f"[Support Gen Warning] Error creating bottom cone support at ({x:.1f}, {y:.1f}): {err}")

        if not cone_meshes:
            return None

        try:
            combined_supports = trimesh.util.concatenate(cone_meshes)
            return combined_supports
        except Exception as e:
            print("[Support Generator] Concatenation error:", e)
            return cone_meshes[0]
