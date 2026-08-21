"""
 Main Controller (main.py)
===================================================================
Company: Specialise Products Private Limited
Project: Metal 3D Printer

Loads 'metal_dashboard.ui' dynamically via QUiLoader.
All layout definitions and CSS styling come directly from metal_dashboard.ui!

Axes Configuration:
- Build Plate (U-Axis): Build Platform (-U moves build plate DOWN for layer)
- Powder Bay (V-Axis): Feeder / Dosing Bed (+V moves supply powder UP)
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
from core.support_generator import ConeSupportGenerator
from preview_galvo import GalvoPreviewWidget

# Hardware Interface
try:
    from machine.galvo_card import GalvoCardHandler
    from machine.galvo_controller import GalvoController
    from machine.stepper_controller import StepperController
except ImportError:
    GalvoCardHandler = None
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

    def __init__(self, galvo, stepper, mesh=None, support_mesh=None, base_polygons=None, config=None, total_layers=5, layer_thickness=0.05):
        super().__init__()
        self.galvo = galvo
        self.stepper = stepper
        self.mesh = mesh
        self.support_mesh = support_mesh
        self.base_polygons = base_polygons
        self.config = config
        self.layer_thickness = layer_thickness

        if self.mesh:
            min_z = 0.0  # Build plate Z=0
            max_z = self.mesh.bounds[1][2]
            height = max_z - min_z
            self.total_layers = max(1, int(math.ceil(height / self.layer_thickness)))
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

            u_move = abs(self.layer_thickness)
            self.progress_signal.emit(
                layer, self.total_layers,
                f"[BUILD PLATE U] Lowering Build Platform: DOWN +{u_move:.3f} mm",
                telemetry
            )
            if self.stepper:
                self.stepper.move_relative("U", u_move)
            time.sleep(0.2)

            v_move = self.layer_thickness * 1.5
            self.progress_signal.emit(
                layer, self.total_layers,
                f"[POWDER BAY V] Supplying Powder: UP +{v_move:.3f} mm",
                telemetry
            )
            if self.stepper:
                self.stepper.move_relative("V", v_move)
            time.sleep(0.2)

            self.progress_signal.emit(
                layer, self.total_layers,
                f"[RECOATER Z] Sweeping dosing blade across build bed (300.0 mm)...",
                telemetry
            )
            if self.stepper:
                self.stepper.move_z_relative(300.0)
                time.sleep(0.4)
                self.stepper.move_z_relative(-300.0)
                time.sleep(0.4)
            else:
                time.sleep(0.3)

            layer_planner = MotionPlanner()
            polys_to_print = []

            if self.mesh:
                z_height = layer * self.layer_thickness
                angle_deg = (layer * 67.0) % 360.0
                if z_height <= self.mesh.bounds[1][2]:
                    self.progress_signal.emit(
                        layer, self.total_layers,
                        f"[LPBF SLICER] Solidifying Layer {layer}/{self.total_layers} at Z={z_height:.3f} mm (Bottom Cones + Part, 67° Hatch Angle: {angle_deg:.1f}°)...",
                        telemetry
                    )
                    try:
                        if not hasattr(self, "slicer"):
                            self.slicer = MetalLPBFSlicer(layer_thickness=self.layer_thickness, hatch_spacing=0.10, hatch_angle_step=67.0)
                        vec_data = self.slicer.slice_build_layer(self.mesh, self.support_mesh, z_height, layer_index=layer)
                        polys_to_print = vec_data.get("all_vectors", [])
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
                    layer_planner.add_jump(gx, gy, speed=2000000)
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
                if hasattr(self.galvo, 'execute_queue'):
                    self.galvo.execute_queue(layer_planner.send_queue, loop_count=1)
            else:
                self.progress_signal.emit(
                    layer, self.total_layers,
                    f"[LASER SIMULATOR] Simulating fiber laser exposure on Layer {layer} (67° Hatch Angle)...",
                    telemetry
                )
                time.sleep(0.3)

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


def calculate_lpbf_parameters(file_path, mesh=None, support_mesh=None, base_polygons=None, layer_thickness=0.05, scan_speed=1000.0, bed_size_mm=250.0):
    """Calculates LPBF 3D printing parameters for display."""
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
        stats['dim_z'] = abs(bounds[1][2] - 0.0)  # Total height from Z=0 build plate
        stats['total_layers'] = max(1, int(math.ceil(stats['dim_z'] / layer_thickness)))

        powder_per_layer_mm3 = (bed_size_mm * bed_size_mm) * stats['powder_dose_per_layer']
        stats['powder_volume_cm3'] = (powder_per_layer_mm3 * stats['total_layers']) / 1000.0

        approx_layer_path_mm = (stats['dim_x'] + stats['dim_y']) * 8.0
        if support_mesh:
            approx_layer_path_mm *= 1.35
        stats['total_path_length_mm'] = approx_layer_path_mm * stats['total_layers']
        stats['total_vectors'] = mesh.faces.shape[0] + (support_mesh.faces.shape[0] if support_mesh else 0)

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


class Metal3DPrinterApp:
    """
    Main Controller Class for the LPBF Metal 3D Printer Application.
    Encapsulates UI loading, hardware controllers, 3D visualization,
    jog/homing motion routines, file loading, build setup (supports & slicing), and print process lifecycle.
    """
    def __init__(self):
        self.app = QApplication.instance() or QApplication(sys.argv)
        self.window = None
        self.gl_view = None
        self.build_setup_galvo_preview = None

        # State Variables
        self.travel_step = 10.0
        self.active_file_path = None
        self.galvo_config = CoordinateConfig()
        self.metal_slicer = MetalLPBFSlicer(layer_thickness=0.05, hatch_spacing=0.10, hatch_angle_step=67.0)
        self.support_generator = ConeSupportGenerator(cone_diameter=0.5, grid_spacing=2.0, base_elevation=5.0)
        self.planner = MotionPlanner()
        self.loaded_mesh = None
        self.loaded_support_mesh = None
        self.loaded_base_polygons = []
        self.print_thread = None

        # Hardware Controllers
        self.galvo_card_handler = GalvoCardHandler() if GalvoCardHandler else None
        self.galvo_controller = None
        self.stepper_controller = None

    def initialize(self):
        """Initializes UI, hardware, signal connections, and component setups."""
        self._load_ui()
        self._apply_stylesheet()
        self._setup_hardware()
        self._setup_console_logger()
        self._setup_navigation()
        self._setup_3d_view()
        self._setup_powder_prep()
        self._setup_build_setup_page()
        self._setup_motion_controls()
        self._setup_homing_controls()
        self._setup_file_loader()
        self._setup_process_controls()
        self._setup_telemetry_gauges()
        self.update_axis_lcds()

    def get_widget(self, name):
        """Resolves widget by name across UI hierarchy with case-insensitive fallback."""
        if not self.window:
            return None
        if hasattr(self.window, name):
            return getattr(self.window, name)
        w = self.window.findChild(QWidget, name)
        if w:
            return w
        name_lower = str(name).lower()
        for child in self.window.findChildren(QWidget):
            if child.objectName().lower() == name_lower:
                return child
        return None

    def _load_ui(self):
        """Loads metal_dashboard.ui dynamically via QUiLoader."""
        ui_file_path = os.path.join(os.path.dirname(__file__), "metal_dashboard.ui")
        ui_file = QFile(ui_file_path)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Error opening UI file {ui_file_path}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        self.window = loader.load(ui_file, None)
        ui_file.close()

        if not self.window:
            print(f"Error loading UI window: {loader.errorString()}")
            sys.exit(-1)

        self.window.setWindowTitle("Specialise Products Private Limited - Metal 3D Printer")
        logo_path = os.path.join(os.path.dirname(__file__), "logo", "SPPL-logo-sq.png")
        if os.path.exists(logo_path):
            self.window.setWindowIcon(QIcon(logo_path))
            if hasattr(self.window, 'logoLabel') and self.window.logoLabel:
                logo_size = 85
                self.window.logoLabel.setObjectName("logoLabel")
                self.window.logoLabel.setMinimumSize(logo_size, logo_size)
                self.window.logoLabel.setMaximumSize(logo_size, logo_size)
                self.window.logoLabel.setAlignment(Qt.AlignCenter)
                pix = QPixmap(logo_path).scaled(102, 102, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.window.logoLabel.setPixmap(pix)

        # Handle window close gracefully to prevent focus-loss motor triggers during teardown
        orig_close = getattr(self.window, 'closeEvent', None)
        def safe_close_event(event):
            if self.print_thread and hasattr(self.print_thread, 'isRunning') and self.print_thread.isRunning():
                self.print_thread.stop()
            if orig_close:
                orig_close(event)
            else:
                event.accept()
        self.window.closeEvent = safe_close_event

    def _apply_stylesheet(self):
        """Applies style.qss stylesheet to the application."""
        style_path = os.path.join(os.path.dirname(__file__), "style.qss")
        if os.path.exists(style_path):
            with open(style_path, "r", encoding="utf-8") as f:
                self.app.setStyleSheet(f.read())

    def _setup_hardware(self):
        """Initializes Galvo card and Stepper motor controllers."""
        if self.galvo_card_handler:
            self.galvo_card_handler.initialize()
            self.galvo_controller = self.galvo_card_handler.controller
        else:
            self.galvo_controller = None

        try:
            if StepperController:
                conn = getattr(self.galvo_controller, 'connection', None) if self.galvo_controller else None
                self.stepper_controller = StepperController(
                    conn, u_steps_per_mm=320.0, v_steps_per_mm=320.0, z_steps_per_mm=1280.0
                )
            else:
                self.stepper_controller = None
        except Exception as err:
            print("[Stepper Warning] Stepper init notice:", err)
            self.stepper_controller = None

    def _setup_console_logger(self):
        """Wires stdout/stderr to PySide6 console log text edit."""
        gb_log = self.window.findChild(QWidget, 'gb_console_log')
        if not gb_log:
            return

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

            self.window.stream = EmittingStream()
            self.window.stream.textWritten.connect(append_text)
            sys.stdout = self.window.stream
            sys.stderr = self.window.stream

            if btn_clear:
                btn_clear.clicked.connect(text_edit.clear)

                parent_layout = btn_clear.parentWidget().layout() if btn_clear.parentWidget() else None
                if parent_layout:
                    btn_sensor_debug = QPushButton("🔍 SENSOR DEBUGGER")
                    btn_sensor_debug.setObjectName("btn_sensor_debug")
                    btn_sensor_debug.setToolTip("Click to query live state of Z, U, V, X, Y inductive proximity sensors")
                    btn_sensor_debug.clicked.connect(lambda checked=False: self.check_sensors_action())
                    parent_layout.addWidget(btn_sensor_debug)

    def _setup_navigation(self):
        """Maps sidebar buttons to stackedWidget pages."""
        nav_map = {
            'btnDashboard': 0,
            'btnMachineControl': 1,
            'btnBuildSetup': 2,
            'btnSettings': 3
        }
        if hasattr(self.window, "stackedWidget"):
            for btn_name, page_idx in nav_map.items():
                if hasattr(self.window, btn_name):
                    btn = getattr(self.window, btn_name)
                    btn.clicked.connect(lambda checked=False, idx=page_idx: self.window.stackedWidget.setCurrentIndex(idx))

    def _setup_3d_view(self):
        """Swaps 3D preview placeholder label with CustomGLViewWidget and sets up controls."""
        lbl_3d = self.get_widget("lbl_3d_preview_placeholder")
        if lbl_3d:
            parent_3d = lbl_3d.parentWidget()
            layout_3d = parent_3d.layout() if parent_3d else None
            if layout_3d:
                self.gl_view = CustomGLViewWidget()
                layout_3d.replaceWidget(lbl_3d, self.gl_view)
                lbl_3d.deleteLater()

                btn_iso = self.get_widget("btn_view_iso")
                btn_top = self.get_widget("btn_view_top")
                btn_front = self.get_widget("btn_view_front")
                btn_rot = self.get_widget("btn_rotate")
                btn_pan = self.get_widget("btn_pan")
                btn_zoom = self.get_widget("btn_zoom")

                if btn_iso: btn_iso.clicked.connect(lambda checked=False: self.gl_view.setCameraPosition(elevation=30, azimuth=45))
                if btn_top: btn_top.clicked.connect(lambda checked=False: self.gl_view.setCameraPosition(elevation=90, azimuth=0))
                if btn_front: btn_front.clicked.connect(lambda checked=False: self.gl_view.setCameraPosition(elevation=0, azimuth=0))
                if btn_rot: btn_rot.clicked.connect(lambda checked=False: setattr(self.gl_view, "mouse_mode", "rotate"))
                if btn_pan: btn_pan.clicked.connect(lambda checked=False: setattr(self.gl_view, "mouse_mode", "pan"))
                if btn_zoom: btn_zoom.clicked.connect(lambda checked=False: setattr(self.gl_view, "mouse_mode", "zoom"))

        if trimesh:
            demo_stl = os.path.join(os.path.dirname(__file__), "stl_files", "demo_cube.stl")
            if os.path.exists(demo_stl):
                self.loaded_mesh = trimesh.load(demo_stl)
                min_z = self.loaded_mesh.bounds[0][2]
                translation = trimesh.transformations.translation_matrix([0, 0, 5.0 - min_z])
                self.loaded_mesh.apply_transform(translation)
                self.active_file_path = demo_stl
            else:
                self.loaded_mesh = trimesh.creation.box(extents=[50.0, 50.0, 25.0])
                # Elevate box base to Z=5.0mm (center Z=17.5mm)
                translation = trimesh.transformations.translation_matrix([0, 0, 17.5])
                self.loaded_mesh.apply_transform(translation)

            # Auto-generate 0.5mm cone supports for elevated model bottom base
            self.loaded_support_mesh = self.support_generator.generate_supports_for_mesh(self.loaded_mesh, base_elevation=5.0)
            self.render_3d_preview()

        slider_layer = self.get_widget("slider_layer")
        chk_section = self.get_widget("chk_section_view")

        def on_slider_changed(val):
            if slider_layer:
                max_val = slider_layer.maximum()
                self.render_3d_preview(current_layer=val, max_layer=max_val)

        if slider_layer:
            slider_layer.valueChanged.connect(on_slider_changed)
        if chk_section:
            chk_section.clicked.connect(lambda: on_slider_changed(slider_layer.value() if slider_layer else 0))

    def _setup_powder_prep(self):
        """Initializes Powder Preparation controls (custom mass 0.5kg-7.0kg, density, target depth calculation, V-axis move)."""
        dspn_weight = self.get_widget("dspn_powder_weight")
        dspn_density = self.get_widget("dspn_powder_density")
        lbl_calc = self.get_widget("lbl_calc_powder_depth")
        btn_set = self.get_widget("btn_set_powder_depth")

        if dspn_weight:
            dspn_weight.setRange(0.50, 7.00)
            dspn_weight.setSingleStep(0.10)

        def recalculate():
            w = dspn_weight.value() if dspn_weight else 4.90
            # Strictly enforce 0.5 kg to 7.0 kg limit
            if w < 0.50:
                w = 0.50
                if dspn_weight: dspn_weight.setValue(0.50)
            elif w > 7.00:
                w = 7.00
                if dspn_weight: dspn_weight.setValue(7.00)

            d = dspn_density.value() if dspn_density else 0.50
            if d <= 0.0:
                d = 0.50
            # Feeder Bay internal area: 44.5 cm * 19.4 cm = 863.3 cm^2
            area_cm2 = 863.3
            vol_cm3 = (w * 1000.0) / d
            height_cm = vol_cm3 / area_cm2
            height_mm = height_cm * 10.0
            if lbl_calc:
                lbl_calc.setText(f"Target Depth (V-Axis): {height_mm:.2f} mm ({height_cm:.1f} cm)")
            return height_mm, w, d

        def on_set_powder_depth():
            depth_mm, weight_kg, density = recalculate()
            if self.stepper_controller:
                print(f"\n[Powder Prep] Setting Powder Bay (V-Axis) depth to {depth_mm:.2f} mm for {weight_kg:.2f} kg powder (Density: {density:.2f} g/cm³)...")
                self.stepper_controller.move_axis('V', depth_mm)
                self.update_axis_lcds()
            else:
                print(f"\n[Powder Prep (Simulated)] Powder Bay (V-Axis) depth set to {depth_mm:.2f} mm for {weight_kg:.2f} kg powder.")

        if dspn_weight:
            dspn_weight.valueChanged.connect(lambda v: recalculate())

        if dspn_density:
            dspn_density.valueChanged.connect(lambda v: recalculate())

        if btn_set:
            btn_set.clicked.connect(lambda checked=False: on_set_powder_depth())

        recalculate()

    def _setup_build_setup_page(self):
        """Initializes Build Setup controls, replaces 2D Galvo preview placeholder, and connects action buttons."""
        lbl_preview = self.get_widget("graphicsView_layer")
        if lbl_preview:
            parent = lbl_preview.parentWidget()
            layout = parent.layout() if parent else None
            if layout:
                self.build_setup_galvo_preview = GalvoPreviewWidget(config=self.galvo_config)
                layout.replaceWidget(lbl_preview, self.build_setup_galvo_preview)
                lbl_preview.deleteLater()

        btn_import = self.get_widget("btn_build_import")
        if btn_import:
            btn_import.clicked.connect(lambda checked=False: self.load_build_file_action())

        btn_gen_supp = self.get_widget("btn_gen_supports")
        if btn_gen_supp:
            btn_gen_supp.clicked.connect(lambda checked=False: self.generate_supports_action())

        btn_slice = self.get_widget("btn_slice_build")
        if btn_slice:
            btn_slice.clicked.connect(lambda checked=False: self.slice_build_action())

        btn_apply = self.get_widget("btn_apply_dashboard")
        if btn_apply:
            btn_apply.clicked.connect(lambda checked=False: self.apply_to_dashboard_action())

        slider_layer = self.get_widget("slider_build_layer")
        if slider_layer:
            slider_layer.valueChanged.connect(self._on_build_layer_slider_changed)

    def generate_supports_action(self):
        """Generates 0.5mm cone support structures strictly underneath the elevated bottom base of the model."""
        if not self.loaded_mesh or not trimesh:
            print("\n[Build Setup Warning] No valid 3D mesh loaded to generate supports.")
            return

        spn_dia = self.get_widget("spn_cone_dia")
        spn_spacing = self.get_widget("spn_support_spacing")
        spn_elev = self.get_widget("spn_base_height")

        dia = spn_dia.value() if spn_dia else 0.50
        spacing = spn_spacing.value() if spn_spacing else 2.00
        elev = spn_elev.value() if spn_elev else 5.00

        # Position mesh elevated at Z = elev above build platform Z=0
        min_z = self.loaded_mesh.bounds[0][2]
        if abs(min_z - elev) > 0.01:
            translation = trimesh.transformations.translation_matrix([0, 0, elev - min_z])
            self.loaded_mesh.apply_transform(translation)

        print(f"\n[Build Setup] Elevating Model Base to Z={elev:.2f} mm & Generating Bottom 0.5mm Cone Supports (Diameter={dia:.2f} mm, Grid Spacing={spacing:.2f} mm)...")

        self.support_generator.cone_diameter = dia
        self.support_generator.grid_spacing = spacing
        self.support_generator.base_elevation = elev

        self.loaded_support_mesh = self.support_generator.generate_supports_for_mesh(self.loaded_mesh, base_elevation=elev)

        if self.loaded_support_mesh:
            print(f"[Build Setup] Bottom Base 0.5mm Cone Supports Generated Successfully: {len(self.loaded_support_mesh.faces)} faces.")
        else:
            print("[Build Setup] No support cones generated.")

        self.render_3d_preview()
        self.slice_build_action()

    def slice_build_action(self):
        """Slices part and support meshes at the currently selected layer thickness and updates 2D Galvo preview."""
        if not self.loaded_mesh or not trimesh:
            return

        spn_thick = self.get_widget("spn_layer_thick")
        spn_hatch_sp = self.get_widget("spn_hatch_spacing")
        spn_hatch_ang = self.get_widget("spn_hatch_angle")
        spn_cnt = self.get_widget("spn_contour_count")

        thick = spn_thick.value() if spn_thick else 0.050
        hatch_sp = spn_hatch_sp.value() if spn_hatch_sp else 0.100
        hatch_ang = spn_hatch_ang.value() if spn_hatch_ang else 67.00
        contour_cnt = spn_cnt.value() if spn_cnt else 2

        self.metal_slicer.layer_thickness = thick
        self.metal_slicer.hatch_spacing = hatch_sp
        self.metal_slicer.hatch_angle_step = hatch_ang
        self.metal_slicer.contour_count = contour_cnt

        max_z = self.loaded_mesh.bounds[1][2]
        total_layers = max(1, int(math.ceil(max_z / thick)))

        slider_layer = self.get_widget("slider_build_layer")
        if slider_layer:
            slider_layer.setRange(1, total_layers)

        current_layer = slider_layer.value() if slider_layer else 1
        z_cut = current_layer * thick

        vec_data = self.metal_slicer.slice_build_layer(self.loaded_mesh, self.loaded_support_mesh, z_cut, layer_index=current_layer)

        if self.build_setup_galvo_preview:
            self.build_setup_galvo_preview.draw_layer_vectors(vec_data, z_height=z_cut, layer_idx=current_layer)

        lbl_info = self.get_widget("lbl_build_layer_info")
        if lbl_info:
            lbl_info.setText(f"Layer {current_layer} / {total_layers} (Z={z_cut:.3f} mm)")

        print(f"[Build Slicer] Layer {current_layer}/{total_layers} Sliced & Hatched (Part: {len(vec_data['part_contours'])} contours, {len(vec_data['part_hatches'])} hatches | Supports: {len(vec_data['support_contours'])} contours, {len(vec_data['support_hatches'])} hatches).")

    def _on_build_layer_slider_changed(self, layer_idx):
        """Updates 2D Galvo preview and 3D Hatching overlay when Build Setup layer slider moves."""
        if not self.loaded_mesh or not trimesh:
            return

        thick = self.metal_slicer.layer_thickness
        max_z = self.loaded_mesh.bounds[1][2]
        total_layers = max(1, int(math.ceil(max_z / thick)))

        self.render_3d_preview(current_layer=layer_idx, max_layer=total_layers)

    def apply_to_dashboard_action(self):
        """Pushes sliced build setup parameters and combined meshes to Main Dashboard."""
        if not self.loaded_mesh:
            print("[Build Setup Warning] No mesh to apply to dashboard.")
            return

        stats = calculate_lpbf_parameters(
            file_path=self.active_file_path or "user_part.stl",
            mesh=self.loaded_mesh,
            support_mesh=self.loaded_support_mesh,
            layer_thickness=self.metal_slicer.layer_thickness
        )

        if hasattr(self.window, 'lbl_active_file'): self.window.lbl_active_file.setText(stats['file_name'])
        if hasattr(self.window, 'lbl_calc_dims'): self.window.lbl_calc_dims.setText(f"Part Dims: {stats['dim_x']:.1f} x {stats['dim_y']:.1f} x {stats['dim_z']:.1f} mm")
        if hasattr(self.window, 'lbl_calc_layers'): self.window.lbl_calc_layers.setText(f"Total Layers: {stats['total_layers']} Layers")
        if hasattr(self.window, 'lbl_calc_dose'): self.window.lbl_calc_dose.setText(f"Powder Dose (+U): {stats['powder_dose_per_layer']:.3f} mm")
        if hasattr(self.window, 'lbl_calc_vol'): self.window.lbl_calc_vol.setText(f"Powder Vol: {stats['powder_volume_cm3']:.2f} cm³")
        if hasattr(self.window, 'lbl_calc_vectors'): self.window.lbl_calc_vectors.setText(f"Vectors: {stats['total_vectors']:,} Commands")
        if hasattr(self.window, 'lbl_calc_time'): self.window.lbl_calc_time.setText(f"Est. Time: {stats['estimated_time_str']}")

        slider_dash = self.get_widget("slider_layer")
        if slider_dash:
            slider_dash.setRange(1, stats["total_layers"])
            slider_dash.setValue(stats["total_layers"])

        self.render_3d_preview(current_layer=stats["total_layers"], max_layer=stats["total_layers"])

        if hasattr(self.window, "stackedWidget"):
            self.window.stackedWidget.setCurrentIndex(0)  # Switch to Dashboard

        print(f"\n🚀 [Build Setup] Sliced LPBF Build with Bottom 0.5mm Cone Supports applied to Main Dashboard!")

    def load_build_file_action(self):
        """Loads STL part file from Build Setup page."""
        file_path, _ = QFileDialog.getOpenFileName(
            self.window,
            "Select LPBF Part File for Build Setup", "",
            "Supported Files (*.stl *.dxf *.svg *.gcode);;STL Files (*.stl);;DXF Files (*.dxf);;SVG Files (*.svg)"
        )
        if not file_path:
            return

        self.load_file_path(file_path)

    def load_file_path(self, file_path):
        """Core file importer routine."""
        print(f"\n[File Importer] Loading LPBF part file: {file_path}")
        self.active_file_path = file_path
        polygons = []
        self.loaded_mesh = None
        self.loaded_support_mesh = None

        ext = file_path.lower()
        if ext.endswith('.stl') and trimesh:
            self.loaded_mesh = trimesh.load(file_path)

            # Elevate mesh so bottom base sits at Z = base_height (default 5.0mm clearance)
            spn_elev = self.get_widget("spn_base_height")
            elev = spn_elev.value() if spn_elev else 5.0
            min_z = self.loaded_mesh.bounds[0][2]
            translation = trimesh.transformations.translation_matrix([0, 0, elev - min_z])
            self.loaded_mesh.apply_transform(translation)

            print(f"[STL Engine] Loaded mesh: {self.loaded_mesh.faces.shape[0]} faces (Elevated base at Z={elev:.1f} mm).")

            # Auto-generate 0.5mm cone supports for bottom base
            self.loaded_support_mesh = self.support_generator.generate_supports_for_mesh(self.loaded_mesh, base_elevation=elev)
        elif ext.endswith('.dxf') and DXFParser:
            parser = DXFParser(file_path)
            polygons = parser.parse_to_polygons(file_path)
        else:
            parser = SVGParser(field_size=self.galvo_config.field_size)
            polygons = parser.parse_to_polygons(file_path)

        self.loaded_base_polygons = polygons

        lbl_file = self.get_widget("lbl_build_file_name")
        if lbl_file:
            lbl_file.setText(f"Selected File: {os.path.basename(file_path)}")

        self.render_3d_preview()
        self.slice_build_action()
        self.apply_to_dashboard_action()

    def render_3d_preview(self, current_layer=None, max_layer=None):
        """Renders 3D GL mesh, bottom supports, and 3D/2D laser hatching vector pattern overlay."""
        if self.gl_view is None:
            return

        self.gl_view.clear()
        mesh = self.loaded_mesh
        supp_mesh = self.loaded_support_mesh

        chk_sec = self.get_widget("chk_section_view")
        is_section = chk_sec.isChecked() if chk_sec else False

        # Calculate cut Z height
        z_cut = None
        if mesh is not None and current_layer is not None and max_layer is not None and max_layer > 0:
            max_z = mesh.bounds[1][2]
            pct = min(1.0, max(0.01, current_layer / max_layer))
            z_cut = pct * max_z
        elif mesh is not None:
            max_z = mesh.bounds[1][2]
            z_cut = max_z / 2.0  # Default middle slice cut preview

        # 1. Render Support Cones (Copper / Amber Translucent)
        if supp_mesh is not None and hasattr(supp_mesh, 'triangles') and len(supp_mesh.triangles) > 0:
            supp_pts = supp_mesh.triangles.copy()
            if z_cut is not None and (is_section or (current_layer is not None and max_layer is not None and current_layer < max_layer)):
                try:
                    sliced_supp = supp_mesh.slice_plane(plane_origin=[0, 0, z_cut], plane_normal=[0, 0, -1])
                    if sliced_supp and len(sliced_supp.triangles) > 0:
                        supp_pts = sliced_supp.triangles
                except Exception:
                    pass

            supp_item = gl.GLMeshItem(
                vertexes=supp_pts,
                smooth=False,
                computeNormals=True,
                drawFaces=True,
                drawEdges=True,
                edgeColor=(0.8, 0.35, 0.05, 0.9),
                color=(0.95, 0.55, 0.1, 0.85),
                shader="shaded"
            )
            self.gl_view.addItem(supp_item)

        # 2. Render Part Mesh (Metallic Blue)
        if mesh is not None and hasattr(mesh, 'triangles') and len(mesh.triangles) > 0:
            points = mesh.triangles.copy()
            if z_cut is not None and (is_section or (current_layer is not None and max_layer is not None and current_layer < max_layer)):
                try:
                    sliced = mesh.slice_plane(plane_origin=[0, 0, z_cut], plane_normal=[0, 0, -1])
                    if sliced and len(sliced.triangles) > 0:
                        points = sliced.triangles
                except Exception:
                    pass

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
            self.gl_view.addItem(mesh_item)

            center = (mesh.bounds[0] + mesh.bounds[1]) / 2.0
            size = float(np.max(mesh.bounds[1] - mesh.bounds[0]))
            self.gl_view.opts["center"] = pg.Vector(center[0], center[1], center[2])
            self.gl_view.setCameraPosition(distance=max(40.0, float(size * 1.5)), elevation=30, azimuth=45)

        # 3. Render 3D Laser Hatching Pattern Lines at Z = z_cut
        if mesh is not None and z_cut is not None:
            try:
                layer_idx = current_layer if current_layer is not None else 1
                vec_data = self.metal_slicer.slice_build_layer(
                    part_mesh=mesh,
                    support_mesh=supp_mesh,
                    z_height=z_cut,
                    layer_index=layer_idx
                )

                # 3.1 Part Hatch Lines in 3D (Crimson Red)
                part_hatches = vec_data.get("part_hatches", [])
                if part_hatches:
                    pts_list = []
                    for seg in part_hatches:
                        for i in range(len(seg) - 1):
                            pts_list.append([seg[i][0], seg[i][1], z_cut])
                            pts_list.append([seg[i+1][0], seg[i+1][1], z_cut])
                    if pts_list:
                        arr = np.array(pts_list, dtype=np.float32)
                        hatch_3d = gl.GLLinePlotItem(pos=arr, mode='lines', color=(1.0, 0.16, 0.43, 1.0), width=2.0, antialias=True)
                        self.gl_view.addItem(hatch_3d)

                # 3.2 Part Contours in 3D (Cyan Blue)
                part_contours = vec_data.get("part_contours", [])
                if part_contours:
                    pts_list = []
                    for poly in part_contours:
                        for i in range(len(poly) - 1):
                            pts_list.append([poly[i][0], poly[i][1], z_cut])
                            pts_list.append([poly[i+1][0], poly[i+1][1], z_cut])
                    if pts_list:
                        arr = np.array(pts_list, dtype=np.float32)
                        contour_3d = gl.GLLinePlotItem(pos=arr, mode='lines', color=(0.0, 0.94, 1.0, 1.0), width=2.5, antialias=True)
                        self.gl_view.addItem(contour_3d)

                # 3.3 Support Hatch Lines in 3D (Orange)
                supp_hatches = vec_data.get("support_hatches", [])
                if supp_hatches:
                    pts_list = []
                    for seg in supp_hatches:
                        for i in range(len(seg) - 1):
                            pts_list.append([seg[i][0], seg[i][1], z_cut])
                            pts_list.append([seg[i+1][0], seg[i+1][1], z_cut])
                    if pts_list:
                        arr = np.array(pts_list, dtype=np.float32)
                        supp_hatch_3d = gl.GLLinePlotItem(pos=arr, mode='lines', color=(0.98, 0.52, 0.0, 1.0), width=2.0, antialias=True)
                        self.gl_view.addItem(supp_hatch_3d)

                # 3.4 Support Contours in 3D (Yellow)
                supp_contours = vec_data.get("support_contours", [])
                if supp_contours:
                    pts_list = []
                    for poly in supp_contours:
                        for i in range(len(poly) - 1):
                            pts_list.append([poly[i][0], poly[i][1], z_cut])
                            pts_list.append([poly[i+1][0], poly[i+1][1], z_cut])
                    if pts_list:
                        arr = np.array(pts_list, dtype=np.float32)
                        supp_contour_3d = gl.GLLinePlotItem(pos=arr, mode='lines', color=(1.0, 0.72, 0.01, 1.0), width=2.5, antialias=True)
                        self.gl_view.addItem(supp_contour_3d)

                # 4. Update 2D Galvo Preview Canvas with current vector hatching pattern & telemetry HUD
                if self.build_setup_galvo_preview:
                    self.build_setup_galvo_preview.draw_layer_vectors(vec_data, z_height=z_cut, layer_idx=layer_idx)

            except Exception as err:
                print(f"[Hatching Preview Notice] {err}")

    def update_axis_lcds(self):
        """Updates U, V, and Z position LCD readouts and Labels across the GUI."""
        u_val = self.stepper_controller.u_position if self.stepper_controller else 0.0
        v_val = self.stepper_controller.v_position if self.stepper_controller else 0.0
        z_val = self.stepper_controller.z_position if self.stepper_controller else 0.0

        u_widgets = ['uposlcddisplay', 'uposLCDNumber', 'lbl_dash_u', 'lbl_u_pos']
        v_widgets = ['vposlcddisplay', 'vposLCDNumber', 'lbl_dash_v', 'lbl_v_pos']
        z_widgets = ['zposlcddisplay', 'zposLCDNumber', 'lbl_dash_z', 'lbl_z_pos']

        for names, val, prefix in [(u_widgets, u_val, "Build Plate (U)"), (v_widgets, v_val, "Powder Bay (V)"), (z_widgets, z_val, "Recoater Blade (Z)")]:
            for name in names:
                widget = self.get_widget(name)
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

    def _connect_unique_buttons(self, button_names, callback, text_override=None):
        """Helper to deduplicate button bindings across UI aliases."""
        connected = set()
        for name in button_names:
            btn = self.get_widget(name)
            if btn and btn not in connected:
                if text_override:
                    btn.setText(text_override)
                if hasattr(btn, 'clicked'):
                    btn.clicked.connect(callback)
                connected.add(btn)

    def _setup_motion_controls(self):
        """Wires travel step selector and U, V, Z jog buttons."""
        def set_travel(val):
            self.travel_step = val
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
            btn = self.get_widget(btn_name)
            if btn and btn not in travel_connected:
                if hasattr(btn, 'clicked'):
                    btn.clicked.connect(lambda checked=False, v=val: set_travel(v))
                travel_connected.add(btn)

        def on_jog_u(step_sign):
            step_mm = self.travel_step * step_sign
            print(f"[MOTION] U-Axis Jog {step_mm:+.3f} mm")
            if self.stepper_controller:
                self.stepper_controller.move_relative("U", step_mm)
            self.update_axis_lcds()

        def on_jog_v(step_sign):
            step_mm = self.travel_step * step_sign
            print(f"[MOTION] V-Axis Jog {step_mm:+.3f} mm")
            if self.stepper_controller:
                self.stepper_controller.move_relative("V", step_mm)
            self.update_axis_lcds()

        def on_jog_z(step_sign):
            step_mm = self.travel_step * step_sign
            print(f"[MOTION] Z-Axis Jog {step_mm:+.3f} mm")
            if self.stepper_controller:
                self.stepper_controller.move_z_relative(step_mm)
            self.update_axis_lcds()

        self._connect_unique_buttons(['upluspushButton', 'uplusPushButton', 'uplus_btn', 'uplusgalvo'], lambda checked=False: on_jog_u(1.0))
        self._connect_unique_buttons(['uminuspushButton', 'uminusPushButton', 'uminus_btn', 'uminusgalvo'], lambda checked=False: on_jog_u(-1.0), text_override="-U (Platform DOWN)")
        self._connect_unique_buttons(['vpluspushButton', 'vplusPushButton', 'vplus_btn', 'vplusgalvo'], lambda checked=False: on_jog_v(1.0), text_override="+V (Supply Powder UP)")
        self._connect_unique_buttons(['vminuspushButton', 'vminusPushButton', 'vminus_btn', 'vminusgalvo'], lambda checked=False: on_jog_v(-1.0))
        self._connect_unique_buttons(['zpluspushButton', 'zplusPushButton', 'zplus_btn', 'zplusgalvo'], lambda checked=False: on_jog_z(1.0))
        self._connect_unique_buttons(['zminuspushButton', 'zminusPushButton', 'zminus_btn', 'zminusgalvo'], lambda checked=False: on_jog_z(-1.0))

        recoater_sweep = self.get_widget('btnrecoaterSweep')
        if recoater_sweep:
            recoater_sweep.setText("Home Recoater (Z)")

    def _setup_homing_controls(self):
        """Wires individual and master homing buttons."""
        def home_u_action():
            print("\n[Homing] Initiating Build Plate (U-Axis) Homing...")
            if self.stepper_controller:
                self.stepper_controller.home_u(app_instance=self.app)
            else:
                print("[Homing] Stepper controller offline. Resetting U-Axis position to 0.000 mm.")
            self.update_axis_lcds()

        def home_v_action():
            print("\n[Homing] Initiating Powder Bay (V-Axis) Homing...")
            if self.stepper_controller:
                self.stepper_controller.home_v(app_instance=self.app)
            else:
                print("[Homing] Stepper controller offline. Resetting V-Axis position to 0.000 mm.")
            self.update_axis_lcds()

        def home_z_action():
            print("\n[Homing] Initiating Recoater Blade (Z-Axis) Homing...")
            if self.stepper_controller:
                self.stepper_controller.home_z(app_instance=self.app)
            else:
                print("[Homing] Stepper controller offline. Resetting Z-Axis position to 0.000 mm.")
            self.update_axis_lcds()

        def home_all_steppers_action():
            print("\n[Homing] Initiating Master Homing Sequence for ALL System Axes (U, V, Z & Galvo X/Y)...")
            home_u_action()
            home_v_action()
            home_z_action()
            self.home_galvo_action()
            self.update_axis_lcds()

        self._connect_unique_buttons(['btnhomeU', 'uhomepushButton', 'uhomepushButton_g'], lambda checked=False: home_u_action())
        self._connect_unique_buttons(['btnhomeV', 'vhomepushButton', 'vhomepushButton_g'], lambda checked=False: home_v_action())
        self._connect_unique_buttons(['btnhomeZ', 'zhomepushButton', 'zhomepushButton_g', 'btnrecoaterHome', 'btnrecoaterSweep'], lambda checked=False: home_z_action())
        self._connect_unique_buttons(['allhomepushButton', 'homePushButton'], lambda checked=False: home_all_steppers_action())
        self._connect_unique_buttons(['galvohomepushButton', 'galvozhomePushButton', 'galvoallhomePushButton'], lambda checked=False: self.home_galvo_action())

        self._connect_unique_buttons([
            'btn_check_sensors', 'btnCheckSensors', 'btn_sensor_debug',
            'btnSensorDebug', 'btn_debug_sensors', 'sensor_debug_btn', 'inspectionPushButton'
        ], lambda checked=False: self.check_sensors_action())

        btn_estop = self.get_widget('btnEmergencyStop')
        if btn_estop and hasattr(btn_estop, 'clicked'):
            btn_estop.clicked.connect(lambda checked=False: print("\n🚨 EMERGENCY STOP TRIGGERED!"))

        btn_m_estop = self.get_widget('btn_master_estop')
        if btn_m_estop and hasattr(btn_m_estop, 'clicked'):
            btn_m_estop.clicked.connect(lambda checked=False: print("\n🚨 EMERGENCY STOP TRIGGERED!"))

    def home_galvo_action(self):
        """Triggers Galvo scanner mirror homing."""
        if self.galvo_card_handler:
            self.galvo_card_handler.home_galvo()
        elif self.galvo_controller:
            self.galvo_controller.galvo_home()
        else:
            print("[Homing] Galvo controller offline. (Simulated)")

    def check_sensors_action(self):
        """Triggers live query on inductive proximity homing sensors."""
        if self.galvo_card_handler:
            self.galvo_card_handler.query_sensors(self.stepper_controller)
        else:
            print("[Sensor Debugger] Galvo card handler offline.")

    def _setup_file_loader(self):
        """Wires LPBF Part file importer on main dashboard."""
        if hasattr(self.window, 'btn_import_build'):
            self.window.btn_import_build.clicked.connect(lambda checked=False: self.load_build_file_action())

    def _setup_process_controls(self):
        """Wires Start, Pause, Resume, and Stop print process control buttons."""
        slider_layer = self.get_widget("slider_layer")

        def start_sim_action():
            if self.print_thread and self.print_thread.isRunning():
                return
            total_layers = 500
            if self.loaded_mesh:
                height = self.loaded_mesh.bounds[1][2]
                total_layers = max(1, int(math.ceil(height / self.metal_slicer.layer_thickness)))

            self.print_thread = Print3DThread(
                galvo=self.galvo_controller,
                stepper=self.stepper_controller,
                mesh=self.loaded_mesh,
                support_mesh=self.loaded_support_mesh,
                base_polygons=self.loaded_base_polygons,
                config=self.galvo_config,
                total_layers=total_layers,
                layer_thickness=self.metal_slicer.layer_thickness
            )

            def on_progress(layer, total, msg, telemetry):
                print(msg)
                self.update_axis_lcds()
                self.render_3d_preview(current_layer=layer, max_layer=total)
                if slider_layer:
                    slider_layer.setValue(layer)
                if hasattr(self.window, 'progressBar'):
                    self.window.progressBar.setValue(telemetry.get('progress_pct', 0))

            self.print_thread.progress_signal.connect(on_progress)
            self.print_thread.start()

        if hasattr(self.window, 'btn_act_simulate'):
            self.window.btn_act_simulate.clicked.connect(start_sim_action)

        def start_process_action():
            if self.print_thread and self.print_thread.isRunning():
                if getattr(self.print_thread, 'is_paused', False):
                    self.print_thread.resume()
                    print("\n[PROCESS] PRINT PROCESS RESUMED BY USER.")
                    if hasattr(self.window, 'btn_pause_process'):
                        self.window.btn_pause_process.setText("PAUSE PROCESS")
                else:
                    print("\n[WARNING] PRINT PROCESS IS ALREADY RUNNING.")
                return
            print("\n[PROCESS] STARTING LPBF PRINT PROCESS...")
            start_sim_action()

        def pause_process_action():
            if self.print_thread and self.print_thread.isRunning():
                if getattr(self.print_thread, 'is_paused', False):
                    self.print_thread.resume()
                    print("\n[PROCESS] PRINT PROCESS RESUMED BY USER.")
                    if hasattr(self.window, 'btn_pause_process'):
                        self.window.btn_pause_process.setText("PAUSE PROCESS")
                else:
                    self.print_thread.pause()
                    print("\n[PROCESS] PRINT PROCESS PAUSED BY USER.")
                    if hasattr(self.window, 'btn_pause_process'):
                        self.window.btn_pause_process.setText("RESUME PROCESS")
            else:
                print("\n[WARNING] NO ACTIVE PRINT PROCESS TO PAUSE.")

        def stop_process_action():
            if self.print_thread and self.print_thread.isRunning():
                self.print_thread.stop()
                print("\n[PROCESS] PRINT PROCESS CANCELED BY USER.")
                if hasattr(self.window, 'btn_pause_process'):
                    self.window.btn_pause_process.setText("PAUSE PROCESS")
            else:
                print("\n[WARNING] NO ACTIVE PRINT PROCESS TO STOP.")

        if hasattr(self.window, 'btn_start_process'):
            self.window.btn_start_process.clicked.connect(start_process_action)
        if hasattr(self.window, 'btn_pause_process'):
            self.window.btn_pause_process.clicked.connect(pause_process_action)
        if hasattr(self.window, 'btn_stop_process'):
            self.window.btn_stop_process.clicked.connect(stop_process_action)

    def _setup_telemetry_gauges(self):
        """Swaps static labels with CircularGauge widgets."""
        try:
            if CircularGauge and hasattr(self.window, 'lbl_laser_gauge'):
                lbl = self.window.lbl_laser_gauge
                parent, layout = lbl.parentWidget(), lbl.parentWidget().layout()
                gauge = CircularGauge(parent, title="LASER POWER", unit=" W", max_val=500, color="#1e40af")
                gauge.setValue(200)
                if layout:
                    layout.replaceWidget(lbl, gauge)
                    lbl.deleteLater()

            if CircularGauge and hasattr(self.window, 'lbl_oxy_gauge'):
                lbl = self.window.lbl_oxy_gauge
                parent, layout = lbl.parentWidget(), lbl.parentWidget().layout()
                gauge = CircularGauge(parent, title="O2 LEVEL", unit=" %", max_val=0.5, color="#10b981")
                gauge.setValue(0.04)
                if layout:
                    layout.replaceWidget(lbl, gauge)
                    lbl.deleteLater()
        except Exception as e:
            print("Gauge init notice:", e)

    def run(self):
        """Shows the main window and runs the application event loop."""
        self.window.show()
        sys.exit(self.app.exec())


def main():
    app = Metal3DPrinterApp()
    app.initialize()
    app.run()


if __name__ == "__main__":
    main()
