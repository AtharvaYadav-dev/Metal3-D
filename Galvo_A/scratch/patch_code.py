import sys, os, math, trimesh, numpy as np

with open('m.py', 'r', encoding='utf-8') as f:
    text = f.read()

gl_init_block = """
    # 2. Swap 3D OpenGL View Widget immediately
    gl_view = None
    lbl_3d = get_widget("lbl_3d_preview_placeholder")
    if lbl_3d:
        parent_3d = lbl_3d.parentWidget()
        layout_3d = parent_3d.layout() if parent_3d else None
        if layout_3d:
            gl_view = CustomGLViewWidget()
            layout_3d.replaceWidget(lbl_3d, gl_view)
            lbl_3d.deleteLater()

            btn_iso = get_widget("btn_view_iso")
            btn_top = get_widget("btn_view_top")
            btn_front = get_widget("btn_view_front")
            btn_rot = get_widget("btn_rotate")
            btn_pan = get_widget("btn_pan")
            btn_zoom = get_widget("btn_zoom")

            if btn_iso: btn_iso.clicked.connect(lambda checked=False: gl_view.setCameraPosition(elevation=30, azimuth=45))
            if btn_top: btn_top.clicked.connect(lambda checked=False: gl_view.setCameraPosition(elevation=90, azimuth=0))
            if btn_front: btn_front.clicked.connect(lambda checked=False: gl_view.setCameraPosition(elevation=0, azimuth=0))
            if btn_rot: btn_rot.clicked.connect(lambda checked=False: setattr(gl_view, "mouse_mode", "rotate"))
            if btn_pan: btn_pan.clicked.connect(lambda checked=False: setattr(gl_view, "mouse_mode", "pan"))
            if btn_zoom: btn_zoom.clicked.connect(lambda checked=False: setattr(gl_view, "mouse_mode", "zoom"))

    # Render 3D Part Mesh helper
    def render_3d_preview(current_layer=None, max_layer=None):
        if gl_view is None:
            return

        gl_view.clear()
        mesh = loaded_mesh[0]

        if mesh is not None:
            points = mesh.triangles.copy()
            min_z = mesh.bounds[0][2]
            max_z = mesh.bounds[1][2]
            height = max_z - min_z

            chk_sec = get_widget("chk_section_view")
            is_section = chk_sec.isChecked() if chk_sec else False

            if current_layer is not None and max_layer is not None and max_layer > 0:
                pct = min(1.0, max(0.01, current_layer / max_layer))
                z_cut = min_z + (pct * height)
                if is_section or current_layer < max_layer:
                    try:
                        sliced = mesh.slice_plane(plane_origin=[0, 0, z_cut], plane_normal=[0, 0, -1])
                        if sliced and len(sliced.triangles) > 0:
                            points = sliced.triangles
                    except Exception:
                        pass

            # Primary 3D Metallic Model Mesh
            mesh_item = gl.GLMeshItem(
                vertexes=points,
                smooth=False,
                computeNormals=True,
                drawFaces=True,
                drawEdges=True,
                edgeColor=(0.12, 0.25, 0.68, 0.8),
                color=(0.2, 0.45, 0.85, 0.95),
                shader="shaded"
            )
            gl_view.addItem(mesh_item)

            # Center Camera on mesh bounds
            center = (mesh.bounds[0] + mesh.bounds[1]) / 2.0
            size = float(np.max(mesh.bounds[1] - mesh.bounds[0]))
            gl_view.opts["center"] = pg.Vector(center[0], center[1], center[2])
            gl_view.setCameraPosition(distance=max(60.0, size * 2.2))

    # Auto-load initial demo 3D model on launch
    if trimesh:
        demo_stl = os.path.join(os.path.dirname(__file__), "stl_files", "demo_cube.stl")
        if os.path.exists(demo_stl):
            loaded_mesh[0] = trimesh.load(demo_stl)
        else:
            loaded_mesh[0] = trimesh.creation.box(extents=[50.0, 50.0, 25.0])
        render_3d_preview()

    # Slider Layer Slicing Listener
    slider_layer = get_widget("slider_layer")
    chk_section = get_widget("chk_section_view")

    def on_slider_layer_changed(val):
        if slider_layer:
            max_val = slider_layer.maximum()
            render_3d_preview(current_layer=val, max_layer=max_val)

    if slider_layer:
        slider_layer.valueChanged.connect(on_slider_layer_changed)
    if chk_section:
        chk_section.clicked.connect(lambda: on_slider_layer_changed(slider_layer.value() if slider_layer else 0))
"""

target_anchor = "    def get_widget(name):\n        if hasattr(window, name):\n            return getattr(window, name)\n        return window.findChild(QWidget, name)"

if target_anchor in text and "gl_view = None" not in text:
    text = text.replace(target_anchor, target_anchor + "\n" + gl_init_block)
    print("Inserted gl_init_block after get_widget!")

target_file_line = 'if hasattr(window, \'lbl_calc_time\'): window.lbl_calc_time.setText(f"Est. Time: {stats[\'estimated_time_str\']}")'
replacement_file_action = target_file_line + """
        if slider_layer:
            slider_layer.setRange(1, stats["total_layers"])
            slider_layer.setValue(stats["total_layers"])

        # Immediately render 3D slicer preview upon selecting file
        render_3d_preview(current_layer=stats["total_layers"], max_layer=stats["total_layers"])"""

if target_file_line in text and "render_3d_preview(current_layer=stats" not in text:
    text = text.replace(target_file_line, replacement_file_action)
    print("Updated load_file_action!")

target_on_progress = "update_axis_lcds()\n            if hasattr(window, \'progressBar\'):"
replacement_on_progress = """update_axis_lcds()
            # Dynamic 3D Build Slicer View Animation
            render_3d_preview(current_layer=layer, max_layer=total)
            if slider_layer:
                slider_layer.setValue(layer)
            if hasattr(window, 'progressBar'):"""

if target_on_progress in text and "render_3d_preview(current_layer=layer" not in text:
    text = text.replace(target_on_progress, replacement_on_progress)
    print("Updated on_progress!")

old_gl_block = """    # Swap 3D OpenGL Preview Widget
    if hasattr(window, \'lbl_3d_preview_placeholder\'):
        lbl_3d = window.lbl_3d_preview_placeholder
        parent_3d = lbl_3d.parentWidget()
        layout_3d = parent_3d.layout() if parent_3d else None
        if layout_3d:
            gl_view = CustomGLViewWidget()
            layout_3d.replaceWidget(lbl_3d, gl_view)
            lbl_3d.deleteLater()

            if hasattr(window, \'btn_view_iso\'): window.btn_view_iso.clicked.connect(lambda checked=False: gl_view.setCameraPosition(elevation=30, azimuth=45))
            if hasattr(window, \'btn_view_top\'): window.btn_view_top.clicked.connect(lambda checked=False: gl_view.setCameraPosition(elevation=90, azimuth=0))
            if hasattr(window, \'btn_view_front\'): window.btn_view_front.clicked.connect(lambda checked=False: gl_view.setCameraPosition(elevation=0, azimuth=0))
            if hasattr(window, \'btn_rotate\'): window.btn_rotate.clicked.connect(lambda checked=False: setattr(gl_view, \'mouse_mode\', \'rotate\'))
            if hasattr(window, \'btn_pan\'): window.btn_pan.clicked.connect(lambda checked=False: setattr(gl_view, \'mouse_mode\', \'pan\'))
            if hasattr(window, \'btn_zoom\'): window.btn_zoom.clicked.connect(lambda checked=False: setattr(gl_view, \'mouse_mode\', \'zoom\'))"""

if old_gl_block in text:
    text = text.replace(old_gl_block, "")
    print("Removed old GLView block from bottom!")

with open("m.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated m.py successfully!")
