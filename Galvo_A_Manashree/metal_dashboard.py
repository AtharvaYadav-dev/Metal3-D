import sys
from pages import (
    PageDashboard, PageBuildSetup, PageLayerViewer, PageMachineControl, 
    PageLaserGalvo, PageMotors, PageSensors, PageAlarmEvents, 
    PageLogs, PageMaintenance, PageSettings
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QFont, QColor, QPalette
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QGridLayout, QLabel, QPushButton, QFrame, QSizePolicy, QScrollArea, QComboBox, QProgressBar,
    QStackedWidget, QButtonGroup
)

# Import our custom components
from custom_ui_widgets import CircularProgressWidget, GaugeWidget, JogWidget, LayerControlWidget
import os
from pages import (
    PageDashboard, PageBuildSetup, PageLayerViewer, PageMachineControl, 
    PageLaserGalvo, PageMotors, PageSensors, PageAlarmEvents, 
    PageLogs, PageMaintenance, PageSettings
)

ICONS_DIR = r"d:\TeamDev\DLL_Galvo\Galvo_for_metal\icons"

# Styling constants to match the image
BG_MAIN = "#12151B"
BG_CARD = "#1A1D24"
BG_SIDEBAR = "#1A1D24"
TEXT_MAIN = "#FFFFFF"
TEXT_MUTED = "#8A92A3"
ACCENT_BLUE = "#2979FF"
ACCENT_GREEN = "#00E676"
ACCENT_RED = "#FF3D00"
BORDER_COLOR = "#2D323F"

class StatusCardWidget(QFrame):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setObjectName("StatusCard")
        self.setStyleSheet(f"""
            #StatusCard {{
                background-color: {BG_CARD};
                border: 1px solid {BORDER_COLOR};
                border-radius: 8px;
            }}
        """)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(15, 15, 15, 15)
        
        self.title_label = QLabel(title.upper())
        self.title_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.title_label.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 11px; font-weight: bold; border: none;")
        self.layout.addWidget(self.title_label)
        
        self.content_layout = QHBoxLayout()
        # Give the content layout a stretch of 1 so the title stays at the top
        self.layout.addLayout(self.content_layout, 1)
        
    def addContent(self, widget):
        self.content_layout.addWidget(widget)

class MetalDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metal 3D Printer Control Panel")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.resize(1000, 700)
        self.setStyleSheet(f"background-color: {BG_MAIN}; color: {TEXT_MAIN}; font-family: 'Inter', sans-serif;")
        self.drag_pos = None
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Main Layout: Sidebar + Content Area
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self._build_sidebar()
        
        # Right Side (Content Area)
        self.content_area = QWidget()
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(20, 20, 20, 20)
        self.content_layout.setSpacing(20)
        
        self._build_top_bar()
        
        self.stacked_widget = QStackedWidget()
        self.content_layout.addWidget(self.stacked_widget, 1)
        
        self.page_dashboard = QWidget()
        self.page_dashboard_layout = QVBoxLayout(self.page_dashboard)
        self.page_dashboard_layout.setContentsMargins(0, 0, 0, 0)
        self._build_dashboard_grid(self.page_dashboard_layout)
        self.stacked_widget.addWidget(self.page_dashboard)
        
        self._build_pages()
        
        self._build_status_bar()
        
        self.main_layout.addWidget(self.content_area, 1)

    def _build_sidebar(self):
        import os
        from PySide6.QtGui import QIcon
        from PySide6.QtCore import QSize
        
        ICONS_DIR = r"d:\TeamDev\DLL_Galvo\Galvo_for_metal\icons"
        
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(200)
        self.sidebar.setStyleSheet(f"""
            QFrame {{
                background-color: {BG_SIDEBAR};
                border-right: 1px solid {BORDER_COLOR};
            }}
            QPushButton {{
                text-align: left;
                padding: 12px 20px;
                border: none;
                color: {TEXT_MUTED};
                font-weight: 600;
                font-size: 13px;
                background: transparent;
            }}
            QPushButton:hover {{
                color: {TEXT_MAIN};
                background-color: {BORDER_COLOR};
            }}
            QPushButton:checked {{
                color: {TEXT_MAIN};
                background-color: {ACCENT_BLUE};
                border-radius: 6px;
            }}
        """)
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(10, 20, 10, 20)
        
        # Logo Area
        logo_layout = QHBoxLayout()
        logo_icon = QLabel()
        logo_svg = os.path.join(ICONS_DIR, "box.svg") # using box as a cube proxy
        if os.path.exists(logo_svg):
            logo_icon.setPixmap(QIcon(logo_svg).pixmap(QSize(32, 32)))
            
        logo_label = QLabel("METAL 3D PRINTER\nCONTROL PANEL")
        logo_label.setStyleSheet(f"color: {TEXT_MAIN}; font-weight: bold; font-size: 12px; border: none;")
        
        logo_layout.addWidget(logo_icon)
        logo_layout.addWidget(logo_label)
        logo_layout.addStretch()
        sidebar_layout.addLayout(logo_layout)
        sidebar_layout.addSpacing(30)
        
        # Menu Items
        self.menu_btn_group = QButtonGroup(self)
        self.menu_btn_group.setExclusive(True)
        self.menu_btn_group.buttonClicked.connect(self._on_menu_clicked)

        menus = [
            ("DASHBOARD", "home.svg"),
            ("BUILD SETUP", "box.svg"),
            ("LAYER VIEWER", "layers.svg"),
            ("MACHINE CONTROL", "sliders.svg"),
            ("LASER / GALVO", "sun.svg"),
            ("MOTORS", "disc.svg"),
            ("SENSORS", "thermometer.svg"),
            ("ALARM / EVENTS", "bell.svg"),
            ("LOGS", "list.svg"),
            ("MAINTENANCE", "tool.svg"),
            ("SETTINGS", "settings.svg")
        ]
        
        for i, (menu_name, icon_name) in enumerate(menus):
            btn = QPushButton("  " + menu_name)
            icon_path = os.path.join(ICONS_DIR, icon_name)
            if os.path.exists(icon_path):
                btn.setIcon(QIcon(icon_path))
                btn.setIconSize(QSize(20, 20))
            
            btn.setCheckable(True)
            if i == 0:
                btn.setChecked(True)
            self.menu_btn_group.addButton(btn, i)
            sidebar_layout.addWidget(btn)
            
        sidebar_layout.addStretch()
        
        # Estop
        estop_btn = QPushButton("  EMERGENCY STOP")
        estop_icon = os.path.join(ICONS_DIR, "octagon.svg")
        if os.path.exists(estop_icon):
            estop_btn.setIcon(QIcon(estop_icon))
            estop_btn.setIconSize(QSize(20, 20))
            
        estop_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                border: 1px solid {ACCENT_RED};
                color: {ACCENT_RED};
                border-radius: 6px;
                text-align: center;
                padding: 10px;
            }}
            QPushButton:hover {{
                background-color: {ACCENT_RED};
                color: {TEXT_MAIN};
            }}
        """)
        sidebar_layout.addWidget(estop_btn)
        
        self.main_layout.addWidget(self.sidebar)

    def _build_pages(self):
        self.pages = []
        page_classes = [
            PageDashboard, PageBuildSetup, PageLayerViewer, PageMachineControl,
            PageLaserGalvo, PageMotors, PageSensors, PageAlarmEvents,
            PageLogs, PageMaintenance, PageSettings
        ]
        
        for cls in page_classes:
            page = cls(self)
            self.stacked_widget.addWidget(page)
            self.pages.append(page)
            
    def _on_menu_clicked(self, btn):
        idx = self.menu_btn_group.id(btn)
        self.stacked_widget.setCurrentIndex(idx)

    def _build_top_bar(self):
        import os
        from PySide6.QtGui import QIcon
        from PySide6.QtCore import QSize
        
        ICONS_DIR = r"d:\TeamDev\DLL_Galvo\Galvo_for_metal\icons"
        
        top_bar = QWidget()
        top_bar.setFixedHeight(50)
        layout = QHBoxLayout(top_bar)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Connection
        conn_lbl = QLabel("CONNECTION\nConnected")
        conn_lbl.setStyleSheet(f"color: {ACCENT_GREEN}; font-size: 11px;")
        layout.addWidget(conn_lbl)
        
        com_combo = QComboBox()
        com_combo.addItems(["COM5"])
        com_combo.setStyleSheet(f"background: {BG_CARD}; color: {TEXT_MAIN}; border: 1px solid {BORDER_COLOR}; padding: 5px; border-radius: 4px;")
        layout.addWidget(com_combo)
        
        disconn_btn = QPushButton("Disconnect")
        disconn_btn.setStyleSheet(f"border: 1px solid {ACCENT_RED}; color: {ACCENT_RED}; border-radius: 4px; padding: 5px 15px;")
        layout.addWidget(disconn_btn)
        
        layout.addSpacing(40)
        
        # Job Info
        job_lbl = QLabel("JOB\ngear_sample.gcode | Layer: 245 / 1250")
        job_lbl.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 11px;")
        layout.addWidget(job_lbl)
        
        folder_btn = QPushButton()
        folder_icon = os.path.join(ICONS_DIR, "folder.svg")
        if os.path.exists(folder_icon):
            folder_btn.setIcon(QIcon(folder_icon))
            folder_btn.setIconSize(QSize(20, 20))
        folder_btn.setStyleSheet("border: none; background: transparent;")
        layout.addWidget(folder_btn)
        
        layout.addStretch()
        
        # User
        user_lbl = QLabel("USER\nOperator")
        user_lbl.setStyleSheet(f"color: {TEXT_MAIN}; font-size: 11px;")
        layout.addWidget(user_lbl)
        
        user_btn = QPushButton()
        user_icon = os.path.join(ICONS_DIR, "user.svg")
        if os.path.exists(user_icon):
            user_btn.setIcon(QIcon(user_icon))
            user_btn.setIconSize(QSize(20, 20))
        user_btn.setStyleSheet("border: none; background: transparent;")
        layout.addWidget(user_btn)
        
        # Settings
        settings_btn = QPushButton()
        settings_icon = os.path.join(ICONS_DIR, "settings.svg")
        if os.path.exists(settings_icon):
            settings_btn.setIcon(QIcon(settings_icon))
            settings_btn.setIconSize(QSize(20, 20))
        settings_btn.setStyleSheet("border: none; background: transparent;")
        layout.addWidget(settings_btn)
        
        layout.addSpacing(10)
        
        # Window Controls
        btn_minimize = QPushButton()
        min_icon = os.path.join(ICONS_DIR, "minus.svg")
        if os.path.exists(min_icon): btn_minimize.setIcon(QIcon(min_icon))
        btn_minimize.setStyleSheet("border: none; background: transparent; padding: 5px;")
        btn_minimize.clicked.connect(self.showMinimized)
        layout.addWidget(btn_minimize)
        
        btn_maximize = QPushButton()
        max_icon = os.path.join(ICONS_DIR, "square.svg")
        if os.path.exists(max_icon): btn_maximize.setIcon(QIcon(max_icon))
        btn_maximize.setStyleSheet("border: none; background: transparent; padding: 5px;")
        btn_maximize.clicked.connect(self._toggle_maximize)
        layout.addWidget(btn_maximize)
        
        btn_close = QPushButton()
        close_icon = os.path.join(ICONS_DIR, "x.svg")
        if os.path.exists(close_icon): btn_close.setIcon(QIcon(close_icon))
        btn_close.setStyleSheet("border: none; background: transparent; padding: 5px;")
        btn_close.clicked.connect(self.close)
        layout.addWidget(btn_close)
        
        self.content_layout.addWidget(top_bar)

    def _toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_pos is not None:
            self.move(event.globalPosition().toPoint() - self.drag_pos)
            event.accept()

    def _load_stl(self, preview_widget):
        from PySide6.QtWidgets import QFileDialog, QMessageBox
        import numpy as np
        try:
            from stl import mesh
            import pyqtgraph.opengl as gl
            import pyqtgraph as pg
        except ImportError:
            QMessageBox.warning(self, "Missing Dependency", "Please install numpy-stl to load 3D models:\npip install numpy-stl")
            return
            
        file_path, _ = QFileDialog.getOpenFileName(self, "Open STL File", "", "STL Files (*.stl)")
        if file_path:
            try:
                stl_mesh = mesh.Mesh.from_file(file_path)
                points = stl_mesh.vectors
                
                mesh_item = gl.GLMeshItem(
                    vertexes=points, 
                    smooth=True,        # Enable smooth shading for high-quality detailing
                    computeNormals=True,
                    drawFaces=True,
                    drawEdges=False, 
                    color=(1.0, 0.79, 0.15, 1.0), # Solid Cura Yellow
                    shader='shaded' 
                )
                
                # Remove any existing loaded meshes
                for item in list(preview_widget.items):
                    if hasattr(item, '_is_loaded_stl'):
                        preview_widget.removeItem(item)
                
                mesh_item._is_loaded_stl = True
                preview_widget.addItem(mesh_item)
                
                # Auto center and zoom
                min_bounds = points.min(axis=(0,1))
                max_bounds = points.max(axis=(0,1))
                center = (min_bounds + max_bounds) / 2
                size = np.max(max_bounds - min_bounds)
                
                preview_widget.opts['center'] = pg.Vector(center[0], center[1], center[2])
                preview_widget.setCameraPosition(distance=size * 2)
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load STL:\n{e}")

    def _build_dashboard_grid(self, parent_layout):
        # 3 Rows of content
        grid = QGridLayout()
        grid.setSpacing(20)
        
        # ROW 1 (Top Cards)
        # 1. Status
        status_card = StatusCardWidget("MACHINE STATUS")
        self.lbl_machine_status = QLabel("Ready\nAll systems normal")
        self.lbl_machine_status.setStyleSheet(f"color: {ACCENT_GREEN}; font-weight: bold;")
        status_card.addContent(self.lbl_machine_status)
        grid.addWidget(status_card, 0, 0, 1, 1)
        
        # 2. Build Progress
        progress_card = StatusCardWidget("BUILD PROGRESS")
        self.prog_build = CircularProgressWidget()
        self.prog_build.value = 19
        self.prog_build.setFixedSize(80, 80)
        progress_card.addContent(self.prog_build)
        
        self.lbl_build_info = QLabel("Layer: 245 / 1250\nTime Elapsed: 01:24:30\nEst. Remaining: 05:38:15")
        self.lbl_build_info.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 11px;")
        progress_card.addContent(self.lbl_build_info)
        grid.addWidget(progress_card, 0, 1, 1, 2)
        
        # 3. Laser Power
        laser_card = StatusCardWidget("LASER POWER")
        self.gauge_laser = GaugeWidget()
        self.gauge_laser.setProperties(500, "W", ACCENT_BLUE)
        self.gauge_laser.value = 195
        self.gauge_laser.setFixedSize(140, 90)
        laser_card.addContent(self.gauge_laser)
        grid.addWidget(laser_card, 0, 3, 1, 1)
        
        # 4. Chamber Temp
        temp_card = StatusCardWidget("CHAMBER TEMP.")
        self.lbl_chamber_temp = QLabel("32.5 °C\nSet: 35 °C\nGas: Argon\nFlow: 12.5 L/min")
        temp_card.addContent(self.lbl_chamber_temp)
        grid.addWidget(temp_card, 0, 4, 1, 1)
        
        # 5. Oxygen Level
        o2_card = StatusCardWidget("OXYGEN LEVEL")
        self.prog_o2 = CircularProgressWidget()
        self.prog_o2.setMaxValue(100) # Assuming 100% is full scale, we'll just display 0.05
        self.prog_o2.value = 5 # Scaled for visual
        self.prog_o2.setColor(ACCENT_GREEN)
        self.prog_o2.setFixedSize(80, 80)
        o2_card.addContent(self.prog_o2)
        grid.addWidget(o2_card, 0, 5, 1, 1)
        
        # ROW 2 & 3 (Main Content)
        # Left side: Build Preview
        preview_card = StatusCardWidget("BUILD PREVIEW")
        try:
            import pyqtgraph.opengl as gl
            
            # Create a basic 3D widget with a grid
            preview_widget = gl.GLViewWidget()
            # Match card background using a slightly darker shade to give depth
            preview_widget.setBackgroundColor('#161920') 
            preview_widget.setMinimumSize(250, 200)
            
            # Add grid (print bed)
            grid_item = gl.GLGridItem()
            grid_item.setSize(200, 200)
            grid_item.setSpacing(10, 10)
            # Center the grid slightly if needed
            preview_widget.addItem(grid_item)
            
            # Add an axis system for reference (X, Y, Z arrows)
            axis = gl.GLAxisItem()
            axis.setSize(x=50, y=50, z=50)
            preview_widget.addItem(axis)
            
            # Position the camera to match an isometric view like the image
            preview_widget.setCameraPosition(distance=250, elevation=30, azimuth=45)
            
            btn_load_stl = QPushButton(" Load STL")
            icon_folder = os.path.join(ICONS_DIR, "folder.svg")
            if os.path.exists(icon_folder):
                btn_load_stl.setIcon(QIcon(icon_folder))
            btn_load_stl.setStyleSheet(f"background-color: {BG_MAIN}; color: {TEXT_MAIN}; border: 1px solid {BORDER_COLOR}; padding: 5px 15px; border-radius: 4px;")
            btn_load_stl.clicked.connect(lambda: self._load_stl(preview_widget))
            
            preview_layout = QVBoxLayout()
            preview_layout.setContentsMargins(0, 0, 0, 0)
            preview_layout.addWidget(btn_load_stl, alignment=Qt.AlignRight)
            preview_layout.addWidget(preview_widget)
            
            preview_container = QWidget()
            preview_container.setLayout(preview_layout)
            preview_card.addContent(preview_container)
            
        except ImportError:
            # Fallback if pyqtgraph is not installed
            preview_placeholder = QLabel("(pyqtgraph is missing. Run 'pip install pyqtgraph')\n\nInstall pyqtgraph to view 3D models.")
            preview_placeholder.setAlignment(Qt.AlignCenter)
            preview_placeholder.setStyleSheet(f"border: 1px dashed {BORDER_COLOR}; color: {ACCENT_RED};")
            preview_placeholder.setMinimumSize(250, 200)
            preview_card.addContent(preview_placeholder)
            
        grid.addWidget(preview_card, 1, 0, 2, 3)
        
        # Middle Right: Axis Position & Jog Control
        axis_card = StatusCardWidget("AXIS POSITION (mm)")
        axis_layout = QGridLayout()
        self.lbl_axis_vals = {}
        for i, (axis, val) in enumerate([("X", "125.300"), ("Y", "83.450"), ("Z", "45.670")]):
            lbl_name = QLabel(axis)
            lbl_name.setAlignment(Qt.AlignCenter)
            color_val = '#FFB300' if axis == 'Z' else ACCENT_BLUE
            lbl_name.setStyleSheet(f"color: {color_val}; font-weight: bold;")
            lbl_val = QLabel(val)
            lbl_val.setAlignment(Qt.AlignCenter)
            lbl_val.setStyleSheet(f"background: {BG_MAIN}; border: 1px solid {BORDER_COLOR}; padding: 10px; border-radius: 4px; font-family: monospace;")
            axis_layout.addWidget(lbl_name, 0, i)
            axis_layout.addWidget(lbl_val, 1, i)
            self.lbl_axis_vals[axis] = lbl_val
        
        axis_container = QWidget()
        axis_container.setLayout(axis_layout)
        axis_card.addContent(axis_container)
        grid.addWidget(axis_card, 1, 3, 1, 2)
        
        # Jog Control
        jog_card = StatusCardWidget("JOG CONTROL")
        
        jog_top_layout = QHBoxLayout()
        for step in ["0.1", "1.0", "10.0", "100.0"]:
            btn_step = QPushButton(step)
            if step == "1.0":
                btn_step.setStyleSheet(f"background-color: {ACCENT_BLUE}; color: {TEXT_MAIN}; border: none; padding: 5px; border-radius: 3px;")
            else:
                btn_step.setStyleSheet(f"background-color: {BG_MAIN}; color: {TEXT_MUTED}; border: 1px solid {BORDER_COLOR}; padding: 5px; border-radius: 3px;")
            jog_top_layout.addWidget(btn_step)
            
        jog_container = QWidget()
        jog_layout = QVBoxLayout(jog_container)
        jog_layout.addLayout(jog_top_layout)
        jog_layout.addSpacing(10)
        self.jog_widget = JogWidget()
        jog_layout.addWidget(self.jog_widget, alignment=Qt.AlignCenter)
        
        jog_card.addContent(jog_container)
        grid.addWidget(jog_card, 2, 3, 1, 2)
        
        # Far Right: Job Control & Overrides
        
        job_card = StatusCardWidget("JOB CONTROL")
        job_layout = QVBoxLayout()
        job_layout.setSpacing(8)
        
        self.btn_start = QPushButton("  Start / Resume")
        icon_play = os.path.join(ICONS_DIR, "play.svg")
        if os.path.exists(icon_play): self.btn_start.setIcon(QIcon(icon_play))
        self.btn_start.setStyleSheet(f"background-color: {ACCENT_BLUE}; color: {TEXT_MAIN}; padding: 12px; border-radius: 4px; font-weight: bold; text-align: left;")
        
        self.btn_pause = QPushButton("  Pause")
        icon_pause = os.path.join(ICONS_DIR, "pause.svg")
        if os.path.exists(icon_pause): self.btn_pause.setIcon(QIcon(icon_pause))
        self.btn_pause.setStyleSheet(f"background-color: transparent; color: {TEXT_MAIN}; border: 1px solid {BORDER_COLOR}; padding: 10px; border-radius: 4px; text-align: left;")
        
        self.btn_stop = QPushButton("  Stop")
        icon_square = os.path.join(ICONS_DIR, "square.svg")
        if os.path.exists(icon_square): self.btn_stop.setIcon(QIcon(icon_square))
        self.btn_stop.setStyleSheet(f"background-color: transparent; color: {ACCENT_RED}; border: 1px solid {BORDER_COLOR}; padding: 10px; border-radius: 4px; text-align: left;")
        
        self.btn_abort = QPushButton("  Abort Job")
        icon_x = os.path.join(ICONS_DIR, "x-circle.svg")
        if os.path.exists(icon_x): self.btn_abort.setIcon(QIcon(icon_x))
        self.btn_abort.setStyleSheet(f"background-color: transparent; color: {ACCENT_RED}; border: 1px solid {BORDER_COLOR}; padding: 10px; border-radius: 4px; text-align: left;")
        
        job_layout.addWidget(self.btn_start)
        job_layout.addWidget(self.btn_pause)
        job_layout.addWidget(self.btn_stop)
        job_layout.addWidget(self.btn_abort)
        
        job_container = QWidget()
        job_container.setLayout(job_layout)
        job_card.addContent(job_container)
        grid.addWidget(job_card, 1, 5, 1, 1)
        
        # Layer Control (goes at row 2, col 5)
        layer_card = StatusCardWidget("")
        layer_card.title_label.hide()
        self.layer_control = LayerControlWidget()
        layer_card.addContent(self.layer_control)
        grid.addWidget(layer_card, 2, 5, 1, 1)
        
        override_card = StatusCardWidget("OVERRIDES")
        over_layout = QHBoxLayout()
        self.override_gauges = {}
        for name in ["Laser Power", "Scan Speed", "Hatch Spacing"]:
            g = GaugeWidget()
            g.setProperties(200, "%", ACCENT_BLUE)
            g.value = 100
            g.setFixedSize(80, 60)
            over_layout.addWidget(g)
            self.override_gauges[name] = g
        over_container = QWidget()
        over_container.setLayout(over_layout)
        override_card.addContent(over_container)
        grid.addWidget(override_card, 3, 5, 1, 1)
        
        # ROW 4 (Logs)
        from PySide6.QtWidgets import QTextEdit
        log_card = StatusCardWidget("CONSOLE LOG")
        log_layout = QHBoxLayout()
        self.console_log = QTextEdit()
        self.console_log.setReadOnly(True)
        self.console_log.setStyleSheet(f"background-color: transparent; color: {ACCENT_GREEN}; font-family: monospace; border: none;")
        self.console_log.setHtml("[10:42:11] System initialized...<br>[10:42:13] Connection established on COM5<br>[10:42:15] File loaded: gear_sample.gcode<br>[10:42:17] Build job ready<br>[10:42:20] Build started<br>[10:43:33] Layer 100 completed<br>[10:45:12] Layer 200 completed<br>[10:46:23] <font color='#FFB300'>Layer 245 in progress</font>")
        
        log_controls = QVBoxLayout()
        btn_clear = QPushButton("Clear")
        btn_clear.setStyleSheet(f"background-color: {BG_MAIN}; color: {TEXT_MAIN}; border: 1px solid {BORDER_COLOR}; border-radius: 4px; padding: 5px 15px;")
        btn_clear.clicked.connect(self.console_log.clear)
        
        from PySide6.QtWidgets import QCheckBox
        chk_scroll = QCheckBox("Auto Scroll")
        chk_scroll.setChecked(True)
        chk_scroll.setStyleSheet(f"color: {TEXT_MAIN};")
        
        log_controls.addWidget(btn_clear)
        log_controls.addWidget(chk_scroll)
        log_controls.addStretch()
        
        log_layout.addWidget(self.console_log, 1)
        log_layout.addLayout(log_controls)
        
        log_container = QWidget()
        log_container.setLayout(log_layout)
        log_card.addContent(log_container)
        grid.addWidget(log_card, 3, 0, 1, 5)

        # Set column stretches
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setColumnStretch(2, 1)
        grid.setColumnStretch(3, 1)
        grid.setColumnStretch(4, 1)
        grid.setColumnStretch(5, 1)
        
        parent_layout.addLayout(grid)

    def _build_status_bar(self):
        status_bar = QWidget()
        status_bar.setFixedHeight(50)
        status_bar.setStyleSheet(f"background-color: {BG_CARD}; border-top: 1px solid {BORDER_COLOR};")
        layout = QHBoxLayout(status_bar)
        layout.setContentsMargins(20, 0, 20, 0)
        
        stats = [
            ("SYSTEM UPTIME\n2d 14h 32m", "clock.svg"),
            ("BUILD PLATE TEMP.\n160.5 °C", "thermometer.svg"),
            ("BASE PLATE TEMP.\n118.3 °C", "thermometer.svg"),
            ("SCAN HEAD TEMP.\n36.2 °C", "thermometer.svg"),
            ("POWDER LEVEL\n78%", "database.svg"),
            ("FILTER STATUS\nGood", "shield.svg")
        ]
        
        import os

        from PySide6.QtGui import QIcon
        from PySide6.QtCore import QSize
        ICONS_DIR = r"d:\TeamDev\DLL_Galvo\Galvo_for_metal\icons"
        
        for text, icon in stats:
            lbl = QPushButton(" " + text)
            icon_path = os.path.join(ICONS_DIR, icon)
            if os.path.exists(icon_path):
                lbl.setIcon(QIcon(icon_path))
                lbl.setIconSize(QSize(20, 20))
            lbl.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 10px; text-align: left; border: none; background: transparent;")
            layout.addWidget(lbl)
            layout.addSpacing(20)
            
        layout.addStretch()
        
        lbl_date = QLabel("07 Jul 2026\n10:46:23 AM")
        lbl_date.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 10px;")
        layout.addWidget(lbl_date)
            
        self.content_layout.addWidget(status_bar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MetalDashboard()
    window.showMaximized()
    sys.exit(app.exec())
