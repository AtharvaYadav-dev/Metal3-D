import math
from shapely.geometry import Polygon, MultiPolygon, LineString
from shapely.ops import unary_union

class MetalLPBFSlicer:
    def __init__(self, layer_thickness=0.05, hatch_spacing=0.10, hatch_angle_step=67.0, contour_count=2, contour_offset=0.08):
        self.layer_thickness = layer_thickness
        self.hatch_spacing = hatch_spacing
        self.hatch_angle_step = hatch_angle_step
        self.contour_count = contour_count
        self.contour_offset = contour_offset

    def slice_mesh_layer(self, mesh, z_height, layer_index=1):
        if mesh is None: return [], []
        try:
            slice_3d = mesh.section(plane_origin=[0, 0, z_height], plane_normal=[0, 0, 1])
            if slice_3d is None: return [], []
            try: slice_2d, _ = slice_3d.to_2D()
            except Exception: slice_2d, _ = slice_3d.to_planar()
            if slice_2d is None or len(slice_2d.polygons_full) == 0: return [], []
        except Exception: return [], []

        shapely_polys = []
        for poly in slice_2d.polygons_full:
            try:
                sp = Polygon(poly.exterior.coords, [i.coords for i in poly.interiors])
                if sp.is_valid and not sp.is_empty: shapely_polys.append(sp)
            except Exception: pass

        if not shapely_polys: return [], []
        domain = unary_union(shapely_polys)
        return self.generate_galvo_vectors(domain, layer_index)

    def generate_galvo_vectors(self, domain, layer_index=1):
        contour_vectors = []
        hatch_vectors = []
        if domain is None or domain.is_empty: return contour_vectors, hatch_vectors
        polygons = [domain] if isinstance(domain, Polygon) else list(domain.geoms) if isinstance(domain, MultiPolygon) else []

        for c_idx in range(self.contour_count):
            offset_dist = c_idx * self.contour_offset
            for poly in polygons:
                target_poly = poly.buffer(-offset_dist) if offset_dist > 0 else poly
                if target_poly.is_empty: continue
                target_subs = [target_poly] if isinstance(target_poly, Polygon) else list(target_poly.geoms) if isinstance(target_poly, MultiPolygon) else []
                for sp in target_subs:
                    ext_coords = list(sp.exterior.coords)
                    if len(ext_coords) > 1: contour_vectors.append(ext_coords)
                    for interior in sp.interiors:
                        int_coords = list(interior.coords)
                        if len(int_coords) > 1: contour_vectors.append(int_coords)

        angle_deg = (layer_index * self.hatch_angle_step) % 360.0
        angle_rad = math.radians(angle_deg)
        minx, miny, maxx, maxy = domain.bounds
        cx, cy = (minx + maxx) / 2.0, (miny + maxy) / 2.0
        diag = math.hypot(maxx - minx, maxy - miny) * 1.25
        cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)
        normal_x, normal_y = -sin_a, cos_a
        dir_x, dir_y = cos_a, sin_a
        num_lines = int(math.ceil(diag / self.hatch_spacing))
        start_offset = -diag / 2.0
        reverse_dir = False
        for i in range(num_lines):
            offset = start_offset + (i * self.hatch_spacing)
            lx, ly = cx + (normal_x * offset), cy + (normal_y * offset)
            p1 = (lx - dir_x * (diag / 2.0), ly - dir_y * (diag / 2.0))
            p2 = (lx + dir_x * (diag / 2.0), ly + dir_y * (diag / 2.0))
            line = LineString([p1, p2])
            inter = domain.intersection(line)
            if inter.is_empty: continue
            segments = [list(inter.coords)] if inter.geom_type == "LineString" else [list(geom.coords) for geom in inter.geoms] if inter.geom_type == "MultiLineString" else []
            for seg in segments:
                if len(seg) >= 2:
                    if reverse_dir: seg = list(reversed(seg))
                    hatch_vectors.append(seg)
                    reverse_dir = not reverse_dir
        return contour_vectors, hatch_vectors
