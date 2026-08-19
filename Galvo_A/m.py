"""
 Main Controller (m.py)
===================================================================
Company: Specialise Products Private Limited
Project: Metal 3D Printer

Loads 'metal_dashboard.ui' dynamically via QUiLoader.
All layout definitions and CSS styling come directly from metal_dashboard.ui!

Axes Configuration:
- Powder Bay (U-Axis): Feeder / Dosing Bed (+U moves supply powder UP)
- Build Plate (V-Axis): Build Platform (-V moves build plate DOWN for layer)
- Recoater Blade (Z-Axis): Powder Layering Sweeper (Sweeps +Z/-Z across build bed)
"""

import sys
import os
import time
import math
import numpy as np

from PySide6.QtWidgets import (
    QApplication, QWidget, QTextEdit, QPushButton, QCheckBox,
    QFileDialog, QLabel, QComboBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QProgressBar, QSlider, QGroupBox, QFrame, QStackedWidget, QVBoxLayout,
    QHBoxLayout, QGridLayout, QFormLayout
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QObject, Signal, Slot, QThread, Qt, QTimer
from PySide6.QtGui import QTextCursor, QColor, QFont, QIcon, QPixmap

# Core LPBF Modules
from core.motion_planner import MotionPlanner
from core.metal_lpbf_slicer import MetalLPBFSlicer
from core.coordinate_mapper import CoordinateConfig
from core.svg_parser import SVGParser
from preview_galvo import GalvoPreviewWidget

# Hardware Interface
try:
    from machine.galvo_controller import GalvoController
    from machine.stepper_controller import StepperController
except ImportError:
    GalvoController = None
    StepperController = None

# Custom Telemetry Widgets
try:
    from custom_dashboard_widgets import CircularGauge, DonutChart
except ImportError:
    CircularGauge = None
    DonutChart = None

# Optional Parsing Libraries
try:
    from dxf import DXFParser
except ImportError:
    DXFParser = None

try:
    import trimesh
except ImportError:
    trimesh = None

# 3D OpenGL View
import pyqtgraph.opengl as gl
import pyqtgraph as pg


class EmittingStream(QObject):
    """Redirects stdout and stderr to the PySide6 console log text widget."""
    textWritten = Signal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass


class CustomGLViewWidget(gl.GLViewWidget):
    """High-contrast 3D OpenGL View tuned for LPBF part inspection & layer slicing preview."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mouse_mode = 'rotate'
        self._last_pos = None
        try:
            self.setBackgroundColor((18, 19, 26))
        except Exception:
            pass

    def mousePressEvent(self, ev):
        self._last_pos = ev.position()
        if ev.button() == Qt.LeftButton and self.mouse_mode in ('pan', 'zoom'):
            return
        super().mousePressEvent(ev)

    def mouseMoveEvent(self, ev):
        if bool(ev.buttons() & Qt.LeftButton) and self.mouse_mode != 'rotate':
            diff = ev.position() - self._last_pos
            self._last_pos = ev.position()
            if self.mouse_mode == 'pan':
                speed = self.opts['distance'] * 0.002
                self.pan(diff.x() * speed, diff.y() * speed, 0, relative='view')
            elif self.mouse_mode == 'zoom':
                self.opts['distance'] *= 0.995 ** diff.y()
                self.update()
        else:
            super().mouseMoveEvent(ev)


class Print3DThread(QThread):
    progress_signal = Signal(int, int, str, dict)
    finished_signal = Signal()

    def __init__(self, galvo, stepper, mesh=None, base_polygons=None, config=None, total_layers=5, layer_thickness=0.05):
        super().__init__()
        self.galvo = galvo
        self.stepper = stepper
        self.mesh = mesh
        self.base_polygons = base_polygons
        self.config = config
        self.layer_thickness = layer_thickness

        if self.mesh:
            min_z = self.mesh.bounds[0][2]
            max_z = self.mesh.bounds[1][2]
            height = max_z - min_z
            self.total_layers = max(1, int(math.ceil(height / self.alayer_thickness)))
        else:
            self.total_layers = max(1, total_layers)

        self.is_running = True
        self.is_paused = False

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def stop(self):
        self.is_running = False
        self.is_paused = False

    def run(self):
        for layer in range(1, self.total_layers + 1):
            if not self.is_running:
                break

            while self.is_paused and self.is_running:
                time.sleep(0.2)

            if not self.is_running:
                break

            telemetry = {
                "layer": layer,
                "total_layers": self.total_layers,
                "u_pos": self.stepper.u_position if self.stepper else 0.0,
                "v_pos": self.stepper.v_position if self.stepper else 0.0,
                "z_pos": self.stepper.z_position if self.stepper else 0.0,
                "progress_pct": int((layer / self.total_layers) * 100)
            }

            self.progress_signal.emit(
                layer, self.total_layers,
                f"[=== LPBF BUILD LAYER {layer}/{self.total_layers} ===",
                telemetry
            )

            u_move = self.layer_thickness * 1.5
            self.progress_signal.emit(
                layer, self.total_layers,
                f"[POWDER BAY U] Supplying Powder: UP +{u_move:.3f} mm",
                telemetry
            )
            if self.stepper:
                self.stepper.move_relative("U", u_move)
            time.sleep(0.3)

            v_move = -self.layer_thickness
            self.progress_signal.emit(
                layer, self.total_layers,
                f"[BUILD PLATE V] Lowering Build Platform: DOWN {Ebs(v_move):.3f} mm",
                telemetry
            )
            if self.stepper:
                self.stepper.move_relative("V", v_move)
            time.sleep(0.3)

            self.progress_signal.emit(
                layer, self.total_layers,
                f"[RECOATER Z] Sweeping dosing blade across build bed (300.0 mm)...",
                telemetry
            )
            if self.stepper:
                self.stepper.move_z_relative(300.0)
                time.sleep(0.8)
                self.stepper.move_z_relative(-300.0)
                time.sleep(0.8)
            else:
                time.sleep(0.4)

            layer_planner = MotionPlanner()
            polys_to_print = []

            if self.mesh:
                min_z = self.mesh.bounds[0][2]
                z_height = min_z + (layer * self.layer_thickness)
                angle_deg = (layer * 67.0) % 360.0
                if z_height <= self.mesh.bounds[1][2]:
                    self.progress_signal.emit(
                        layer, self.total_layers,
                        f"[LPBF SLICER] Solidifying Layer {layer}/{self.total_layers} at Z={z_height:.3f} mm (67 Deg Hatch Angle: {angle_deg:.1f} Deg)...",
                        telemetry
                    )
                    try:
                        if not hasattr(self, "slicer"):
                            self.slicer = MetalLPBFSlicer(layer_thickness=self.layer_thickness, hatch_spacing=0.10, hatch_angle_step=67.0)
                        contours, hatches = self.slicer.slice_mesh_layer(self.mesh, z_height, layer_index=layer)
                        polys_to_print = contours + hatches
                    except Exception as err:
                        self.progress_signal.emit(
                            layer, self.total_layers,
                            f"[SLICER WARNING] Solidification error at Z={z_height:.3f}: {err}",
                            telemetry
                        )
            else:
                polys_to_print = self.base_polygons or []

            if polys_to_print and self.config:
                for poly in polys_to_print:
                    if not poly:
                        continue
                    pt = poly[0]
                    gx, gy = self.config.apply_transform(pt[0], pt[1])
                    layer_planner.add_jump(ox, gy, speed=2000000)
                    for pt in poly[1:]:
                        gx, gy = self.config.apply_transform(pt[0], pt[1])
                        layer_planner.add_mark(gx, gy, speed=1000000)
                layer_planner.optimize_path()
                layer_planner.commit_to_send_queue()

            if self.galvo and layer_planner.send_queue:
                self.progress_signal.emit(
                    layer, self.total_layers,
                    f"[LASER SIMULATOR] Firing fiber laser - {len(layer_planner.send_queue)} vector commands...",
                    telemetry
                )
                self.galvo.execute_queue(layer_planner.send_queue, loop_count=1)
            else:
                self.progress_signal.emit(
                    layer, self.total_layers,
                    f"[LASER SIMULATOR] Simulating fiber laser exposure on Layer {layer} (67 Deg Hatch Angle)...",
                    telemetry
                )
                time.sleep(0.4)

            if self.stepper:
                telemetry["u_pos"] = self.stepper.u_position
                telemetry["v_pos"] = self.stepper.v_position
                telemetry["z_pos"] = self.stepper.z_position

            self.progress_signal.emit(
                layer, self.total_layers,
                f"Layer {layer}/{self.total_layers} Solidified & Completed Successfully.",
                telemetry
            )

        self.finished_signal.emit()

    def stop(self):
        self.is_running = False


def calculate_lpbf_parameters(file_path, mesh=None, base_polygons=None, layer_thickness=0.05, scan_speed=1000.0, bed_size_mm=250.0):
    """Calculates LPBF 3D printing parameters for demo display."""
    stats = {
        'file_name': os.path.basename(file_path) if file_path else "demo_cube.stl",
        'dim_x': 50.0,
        'dim_y': 50.0,
        'dim_z': 25.0,
        'layer_thickness': layer_thickness,
        'total_layers': 500,
        'powder_dose_per_layer': layer_thickness * 1.5,
        'powder_volume_cm3': 234.38,
        'total_vectors': 12500,
        'total_path_length_mm': 125000.0,
        'estimated_time_str': "01:14:30"
    }

    if mesh:
        bounds = mesh.bounds
        stats['dim_x'] = abs(bounds[1][0] - bounds[0][0])
        stats['dim_y'] = abs(bounds[1][1] - bounds[0][1])
        stats['dim_z'] = abs(bounds[1][2] - bounds[0][2])
        stats['total_layers'] = max(1, int(math.ceil(stats['dim_z'] / layer_thickness)))

        powder_per_layer_mm3 = (bed_size_mm * bed_size_mm) * stats['powder_dose_per_layer']
        stats['powder_volume_cm3'] = (powder_per_layer_mm3 * stats['total_layers']) / 1000.0

        approx_layer_path_mm = (stats['dim_x'] + stats['dim_y']) * 8.0
        stats['total_path_length_mm'] = approx_layer_path_mm * stats['total_layers']
        stats['total_vectors'] = mesh.faces.shape[0]

    elif base_polygons:
        all_pts = [pt for poly in base_polygons for pt in poly]
        if all_pts:
            xs = [pt[0] for pt in all_pts]
            ys = [pt[1] for pt in all_pts]
            stats['dim_x'] = max(xs) - min(xs)
            stats['dim_y'] = max(ys) - min(ys)
            stats['dim_z'] = 10.0
            stats['total_layers'] = max(1, int(math.ceil(stats['dim_z'] / layer_thickness)))

            path_len = 0.0
            for poly in base_polygons:
                for i in range(len(poly) - 1):
                    p1, p2 = poly[i], poly[i + 1]
                    path_len += math.hypot(p2[0] - p1[0], p2[1] - p1[1])

            stats['total_path_length_mm'] = path_len * stats['total_layers']
            stats['total_vectors'] = sum(len(p) for p in base_polygons) * stats['total_layers']

            powder_per_layer_mm3 = (bed_size_mm * bed_size_mm) * stats['powder_dose_per_layer']
            stats['powder_volume_cm3'] = (powder_per_layer_mm3 * stats['total_layers']) / 1000.0

    recoat_time_sec = 3.0 * stats['total_layers']
    scan_time_sec = (stats['total_path_length_mm'] / max(1.0, scan_speed)) if stats['total_path_length_mm'] > 0 else 1.5 * stats['total_layers']
    total_sec = int(recoat_time_sec + scan_time_sec)

    hours = total_sec // 3600
    minutes = (total_sec % 3600) // 60
    seconds = total_sec % 60
    stats['estimated_time_str'] = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    return stats


def main():
    app = QApplication(sys.argv)

    # 1. Load UI file directly via QUiLoader
    ui_file_path = os.path.join(os.path.dirname(__file__), "metal_dashboard.ui")
    ui_file = QFile(ui_file_path)

    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Error opening UI file {ui_file_path}: {ui_file.errorString()}")
        sys.exit(-1)

    loader = QUiLoader()
    window = loader.load(ui_file, None)
    ui_file.close()

    if not window:
        print(f"Error loading UI window: {loader.errorString()}")
        sys.exit(-1)

    # Set Window Title & Icon
    window.setWindowTitle("Specialise Products Private Limited - Metal 3D Printer")
    logo_path = os.path.join(os.path.dirname(__file__), "logo", "SPPL-logo-sq.png")
    if os.path.exists(logo_path):
        window.setWindowIcon(QIcon(logo_path))
        if hasattr(window, 'logoLabel') and window.logoLabel:
            logo_size = 85
            window.logoLabel.setMinimumSize(logo_size, logo_size)
            window.logoLabel.setMaximumSize(logo_size, logo_size)
            window.logoLabel.setStyleSheet("background-color: #ffffff; border-radius: 6px; padding: 4px;")
            window.logoLabel.setAlignment(Qt.AlignCenter)
            pix = QPixmap(logo_path).scaled(102, 102, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            window.logoLabel.setPixmap(pix)

    # Apply CSS from style.qss as backup
    style_path = os.path.join(os.path.dirname(__file__), "style.qss")
    if os.path.exists(style_path):
        with open(style_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())

    # State Variables
    travel_state = [10.0]
    galvo_config = CoordinateConfig()
    metal_slicer = MetalLPBFSlicer(layer_thickness=0.05, hatch_spacing=0.10, hatch_angle_step=67.0)
    planner = MotionPlanner()
    loaded_mesh = [None]
    loaded_base_polygons = [[]]
    print_thread_holder = [None]

    # Hardware Setup
    try:
        if GalvoController:
            galvo_controller = GalvoController()
            try:
                galvo_controller.connect()
            except Exception as err:
                print("[Hardware Warning] Galvo connect notice:", err)
        else:
            galvo_controller = None
    except Exception as err:
        galvo_controller = None
        print("[Hardware Notice] Operating in simulation mode:", err)

    try:
        if StepperController:
            conn = getattr(galvo_controller, 'connection', None) if galvo_controller else None
            stepper_controller = StepperController(conn, u_steps_per_mm=1600.0, v_steps_per_mm=1600.0, z_steps_per_mm=6400.0)
        else:
            stepper_controller = None
    except Exception as err:
        print("[Stepper Warning] Stepper init notice:", err)
        stepper_controller = None

    # Wire Console Logger
    gb_log = window.findChild(QWidget, 'gb_console_log')
    if gb_log:
        text_edit = gb_log.findChild(QTextEdit, 'textEdit')
        btn_clear = gb_log.findChild(QPushButton, 'pushButton')
        chk_scroll = gb_log.findChild(QCheckBox, 'checkBox')

        if text_edit:
            text_edit.setReadOnly(True)
            text_edit.setFont(QFont("JetBrains Mono", 9.5))

            def append_text(text):
                if chk_scroll and chk_scroll.isChecked():
                    text_edit.moveCursor(QTextCursor.End)
                text_edit.insertPlainText(text)
                if chk_scroll and chk_scroll.isChecked():
                    text_edit.moveCursor(QTextCursor.End)

            window.stream = EmittingStream()
            window.stream.textWritten.connect(append_text)
            sys.stdout = window.stream
            sys.stderr = window.stream

            if btn_clear:
                btn_clear.clicked.connect(text_edit.clear)

    # Wire Navigation Buttons
    nav_map = {
        'btnDashboard': 0,
        'btnMachineControl': 1,
        'btnBuildSetup': 2,
        'btnSettings': 3
    }

    if hasattr(window, "stackedWidget"):
        for btn_name, page_idx in nav_map.items():
            if hasattr(window, btn_name):
                btn = getattr(window, btn_name)
                btn.clicked.connect(lambda checked=False, idx=page_idx: window.stackedWidget.setCurrentIndex(idx))

    # Robust helper to resolve widgets across QUiLoader hierarchy (case-insensitive & multi-alias)
    def get_widget(name):
        if hasattr(window, name):
            return getattr(window, name)
        w = window.findChild(QWidget, name)
        if w:
            return w
        name_lower = str(name).lower()
        for child in window.findChildren(QWidget):
            if child.objectName().lower() == name_lower:
                return child
        return None

    # Travel Step Selector
    def set_travel(val):
        travel_state[0] = val
        print(f"[Motion Control] Travel step set to {val} mm")

    travel_connected = set()
    for btn_name, val in [
        ('travelpushButton_1', 0.01),
        ('travelpushButton_2', 0.1),
        ('travelpushButton_3', 1.0),
        ('travelpushButton_4', 5.0),
        ('travelpushButton_5', 10.0),
        ('travelpushButton_6', 50.0)
    ]:
        btn = get_widget(btn_name)
        if btn and btn not in travel_connected:
            if hasattr(btn, 'clicked'):
                btn.clicked.connect(lambda checked=False, v=val: set_travel(v))
            travel_connected.add(btn)

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
            gl_view.setCameraPosition(distance=max(40.0, float(size * 1.5)), elevation=30, azimuth=45)

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


    # Update LCD Readouts for all widget variations
    def update_axis_lcds():
        u_val = stepper_controller.u_position if stepper_controller else 0.0
        v_val = stepper_controller.v_position if stepper_controller else 0.0
        z_val = stepper_controller.z_position if stepper_controller else 0.0

        u_widgets = ['uposlcddisplay', 'uposLCDNumber', 'lbl_dash_u', 'lbl_u_pos']
        v_widgets = ['vposlcddisplay', 'vposLCDNumber', 'lbl_dash_v', 'lbl_v_pos']
        z_widgets = ['zposlcddisplay', 'zposLCDNumber', 'lbl_dash_z', 'lbl_z_pos']

        for names, val, prefix in [(u_widgets, u_val, "Powder Bay (U)"), (v_widgets, v_val, "Build Plate (V)"), (z_widgets, z_val, "Recoater Blade (Z)")]:
            for name in names:
                widget = get_widget(name)
                if widget:
                    if isinstance(widget, QLabel):
                        if 'dash' in name:
                            widget.setText(f"{prefix}: {val:+.3f} mm")
                        else:
                            widget.setText(f"{val:+.3f} mm")
                    elif hasattr(widget, 'display'):
                        widget.display(f"{val:.2f}")
                    elif hasattr(widget, 'setText'):
                        widget.setText(f"{val:+.3f} mm")

    # Wire Motion Jog Buttons with multi-alias widget discovery and immediate LCD updates
    def on_jog_u(step_sign):
        step_mm = travel_state[0] * step_sign
        print(f"[MOTION] U-Axis Jog {step_mm:+.3f} mm")
        if stepper_controller:
            stepper_controller.move_relative("U", step_mm)
        update_axis_lcds()

    def on_jog_v(step_sign):
        step_mm = travel_state[0] * step_sign
        print(f"[MOTION] V-Axis Jog {step_mm:+.3f} mm")
        if stepper_controller:
            stepper_controller.move_relative("V", step_mm)
        update_axis_lcds()

    def on_jog_z(step_sign):
        step_mm = travel_state[0] * step_sign
        print(f"[MOTION] Z-Axis Jog {step_mm:+.3f} mm")
        if stepper_controller:
            stepper_controller.move_z_relative(step_mm)
        update_axis_lcds()

    # Helper to deduplicate button bindings so no widget receives duplicate click signal connections
    def connect_unique_buttons(button_names, callback, text_override=None):
        connected = set()
        for name in button_names:
            btn = get_widget(name)
            if btn and btn not in connected:
                if text_override:
                    btn.setText(text_override)
                if hasattr(btn, 'clicked'):
                    btn.clicked.connect(callback)
                connected.add(btn)

    # Bind U+, U-, V+, V-, Z+, Z- Aliases cleanly without duplicates
    connect_unique_buttons(['upluspushButton', 'uplusPushButton', 'uplus_btn', 'uplusgalvo'], lambda checked=False: on_jog_u(1.0))
    connect_unique_buttons(['uminuspushButton', 'uminusPushButton', 'uminus_btn', 'uminusgalvo'], lambda checked=False: on_jog_u(-1.0))
    connect_unique_buttons(['vpluspushButton', 'vplusPushButton', 'vplus_btn', 'vplusgalvo'], lambda checked=False: on_jog_v(1.0))
    connect_unique_buttons(['vminuspushButton', 'vminusPushButton', 'vminus_btn', 'vminusgalvo'], lambda checked=False: on_jog_v(-1.0), text_override="-V (Platform DOWN)")
    connect_unique_buttons(['zpluspushButton', 'zplusPushButton', 'zplus_btn', 'zplusgalvo'], lambda checked=False: on_jog_z(1.0))
    connect_unique_buttons(['zminuspushButton', 'zminusPushButton', 'zminus_btn', 'zminusgalvo'], lambda checked=False: on_jog_z(-1.0))

    recoater_sweep = get_widget('btnrecoaterSweep')
    if recoater_sweep:
        recoater_sweep.setText("Home Recoater (Z)")

    # Homing Action Callbacks
    def home_u_action():
        print("\n[Homing] Initiating Powder Bay (U-Axis) Homing...")
        if stepper_controller:
            stepper_controller.home_u(app_instance=QApplication.instance())
        else:
            print("[Homing] Stepper controller offline. Resetting U-Axis position to 0.000 mm.")
        update_axis_lcds()

    def home_v_action():
        print("\n[Homing] Initiating Build Plate (V-Axis) Homing...")
        if stepper_controller:
            stepper_controller.home_v(app_instance=QApplication.instance())
        else:
            print("[Homing] Stepper controller offline. Resetting V-Axis position to 0.000 mm.")
        update_axis_lcds()

    def home_z_action():
        print("\n[Homing] Initiating Recoater Blade (Z-Axis) Homing...")
        if stepper_controller:
            stepper_controller.home_z(app_instance=QApplication.instance())
        else:
            print("[Homing] Stepper controller offline. Resetting Z-Axis position to 0.000 mm.")
        update_axis_lcds()

    def home_all_steppers_action():
        print("\n[Homing] Initiating Master Homing Sequence for ALL System Axes (U, V, Z & Galvo X/Y)...")
        home_u_action()
        home_v_action()
        home_z_action()
        home_galvo_action()
        update_axis_lcds()

    def home_galvo_action():
        print("\n[Homing] Homing Laser Galvo Scanner to Center Position...")
        if galvo_controller:
            if not galvo_controller.is_connected:
                galvo_controller.connect()
            galvo_controller.galvo_home()
            print("[Homing] Galvo mirrors positioned at center (32767, 32767).")
        else:
            print("[Homing] Galvo controller offline. (Simulated)")

    # Wire Homing Buttons cleanly without duplicates
    connect_unique_buttons(['btnhomeU', 'uhomepushButton', 'uhomepushButton_g'], lambda checked=False: home_u_action())
    connect_unique_buttons(['btnhomeV', 'vhomepushButton', 'vhomepushButton_g'], lambda checked=False: home_v_action())
    connect_unique_buttons(['btnhomeZ', 'zhomepushButton', 'zhomepushButton_g', 'btnrecoaterHome', 'btnrecoaterSweep'], lambda checked=False: home_z_action())
    connect_unique_buttons(['allhomepushButton', 'homePushButton'], lambda checked=False: home_all_steppers_action())
    connect_unique_buttons(['galvohomepushButton', 'galvozhomePushButton', 'galvoallhomePushButton'], lambda checked=False: home_galvo_action())

    # Populate initial axis readouts on startup
    update_axis_lcds()

    btn_estop = get_widget('btnEmergencyStop')
    if btn_estop and hasattr(btn_estop, 'clicked'):
        btn_estop.clicked.connect(lambda checked=False: print("\n🚨 EMERGENCY STOP TRIGGERED!"))

    btn_m_estop = get_widget('btn_master_estop')
    if btn_m_estop and hasattr(btn_m_estop, 'clicked'):
        btn_m_estop.clicked.connect(lambda checked=False: print("\n🚨 EMERGENCY STOP TRIGGERED!"))

    # File Import Connection
    def load_file_action():
        file_path, _ = QFileDialog.getOpenFileName(
            window,
            "Select LPBF Part File", "",
            "Supported Files (*.stl *.dxf *.svg *.gcode);;STL Files (*.stl);;DXF Files (*.dxf);;SVG Files (*.svg);;GCode Files (*.gcode)"
        )
        if not file_path:
            return

        print(f"[File Loader] Loading part file: {file_path}")
        polygons = []
        loaded_mesh[0] = None

        ext = file_path.lower()
        if ext.endswith('.stl') and trimesh:
            loaded_mesh[0] = trimesh.load(file_path)
            print(f"[STL Engine] Loaded mesh: {loaded_mesh[0].faces.shape[0]} faces.")
        elif ext.endswith('.dxf') and DXFParser:
            parser = DXFParser(file_path)
            polygons = parser.parse_to_polygons(file_path)
        else:
            parser = SVGParser(field_size=galvo_config.field_size)
            polygons = parser.parse_to_polygons(file_path)

        loaded_base_polygons[0] = polygons

        stats = calculate_lpbf_parameters(
            file_path=file_path,
            mesh=loaded_mesh[0],
            base_polygons=loaded_base_polygons[0]
        )

        if hasattr(window, 'lbl_active_file'): window.lbl_active_file.setText(stats['file_name'])
        if hasattr(window, 'lbl_calc_dims'): window.lbl_calc_dims.setText(f"Part Dims: {stats['dim_x']:.1f} x {stats['dim_y']:.1f} x {stats['dim_z']:.1f} mm")
        if hasattr(window, 'lbl_calc_layers'): window.lbl_calc_layers.setText(f"Total Layers: {stats['total_layers']} Layers")
        if hasattr(window, 'lbl_calc_dose'): window.lbl_calc_dose.setText(f"Powder Dose (+U): {stats['powder_dose_per_layer']:.3f} mm")
        if hasattr(window, 'lbl_calc_vol'): window.lbl_calc_vol.setText(f"Powder Vol: {stats['powder_volume_cm3']:.2f} cm³")
        if hasattr(window, 'lbl_calc_vectors'): window.lbl_calc_vectors.setText(f"Vectors: {stats['total_vectors']:,} Commands")
        if hasattr(window, 'lbl_calc_time'): window.lbl_calc_time.setText(f"Est. Time: {stats['estimated_time_str']}")
        if slider_layer:
            slider_layer.setRange(1, stats["total_layers"])
            slider_layer.setValue(stats["total_layers"])

        # Immediately render 3D slicer preview upon selecting file
        render_3d_preview(current_layer=stats["total_layers"], max_layer=stats["total_layers"])

    if hasattr(window, 'btn_import_build'):
        window.btn_import_build.clicked.connect(load_file_action)

    # Simulation Trigger
    def start_sim_action():
        if print_thread_holder[0] and print_thread_holder[0].isRunning():
            return
        total_layers = 500
        if loaded_mesh[0]:
            height = loaded_mesh[0].bounds[1][2] - loaded_mesh[0].bounds[0][2]
            total_layers = max(1, int(math.ceil(height / 0.05)))

        print_thread_holder[0] = Print3DThread(
            galvo=galvo_controller,
            stepper=stepper_controller,
            mesh=loaded_mesh[0],
            base_polygons=loaded_base_polygons[0],
            config=galvo_config,
            total_layers=total_layers
        )

        def on_progress(layer, total, msg, telemetry):
            print(msg)
            update_axis_lcds()
            # Dynamic 3D Build Slicer View Animation
            render_3d_preview(current_layer=layer, max_layer=total)
            if slider_layer:
                slider_layer.setValue(layer)
            if hasattr(window, 'progressBar'):
                window.progressBar.setValue(telemetry.get('progress_pct', 0))

        print_thread_holder[0].progress_signal.connect(on_progress)
        print_thread_holder[0].start()

    if hasattr(window, 'btn_act_simulate'):
        window.btn_act_simulate.clicked.connect(start_sim_action)

    # Process Control Action Handlers
    def start_process_action():
        if print_thread_holder[0] and print_thread_holder[0].isRunning():
            if getattr(print_thread_holder[0], 'is_paused', False):
                print_thread_holder[0].resume()
                print("\n[PROCESS] PRINT PROCESS RESUMED BY USER.")
                if hasattr(window, 'btn_pause_process'):
                    window.btn_pause_process.setText("PAUSE PROCESS")
            else:
                print("\n[WARNING] PRINT PROCESS IS ALREADY RUNNING.")
            return
        print("\n[PROCESS] STARTING LPBF PRINT PROCESS...")
        start_sim_action()

    def pause_process_action():
        if print_thread_holder[0] and print_thread_holder[0].isRunning():
            if getattr(print_thread_holder[0], 'is_paused', False):
                print_thread_holder[0].resume()
                print("\n[PROCESS] PRINT PROCESS RESUMED BY USER.")
                if hasattr(window, 'btn_pause_process'):
                    window.btn_pause_process.setText("PAUSE PROCESS")
            else:
                print_thread_holder[0].pause()
                print("\n[PROCESS] PRINT PROCESS PAUSED BY USER.")
                if hasattr(window, 'btn_pause_process'):
                    window.btn_pause_process.setText("RESUME PROCESS")
        else:
            print("\n[WARNING] NO ACTIVE PRINT PROCESS TO PAUSE.")

    def stop_process_action():
        if print_thread_holder[0] and print_thread_holder[0].isRunning():
            print_thread_holder[0].stop()
            print("\n[PROCESS] PRINT PROCESS CANCELED BY USER.")
            if hasattr(window, 'btn_pause_process'):
                window.btn_pause_process.setText("PAUSE PROCESS")
        else:
            print("\n[WARNING] NO ACTIVE PRINT PROCESS TO STOP.")

    if hasattr(window, 'btn_start_process'):
        window.btn_start_process.clicked.connect(start_process_action)

    if hasattr(window, 'btn_pause_process'):
        window.btn_pause_process.clicked.connect(pause_process_action)

    if hasattr(window, 'btn_stop_process'):
        window.btn_stop_process.clicked.connect(stop_process_action)



    # Swap Telemetry Gauges
    try:
        if CircularGauge and hasattr(window, 'lbl_laser_gauge'):
            lbl = window.lbl_laser_gauge
            parent, layout = lbl.parentWidget(), lbl.parentWidget().layout()
            gauge = CircularGauge(parent, title="LASER POWER", unit=" W", max_val=500, color="#1e40af")
            gauge.setValue(200)
            if layout:
                layout.replaceWidget(lbl, gauge)
                lbl.deleteLater()

        if CircularGauge and hasattr(window, 'lbl_oxy_gauge'):
            lbl = window.lbl_oxy_gauge
            parent, layout = lbl.parentWidget(), lbl.parentWidget().layout()
            gauge = CircularGauge(parent, title="O2 LEVEL", unit=" %", max_val=0.5, color="#10b981")
            gauge.setValue(0.04)
            if layout:
                layout.replaceWidget(lbl, gauge)
                lbl.deleteLater()
    except Exception as e:
        print("Gauge init notice:", e)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
