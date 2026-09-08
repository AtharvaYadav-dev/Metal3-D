import os
import math
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, 
                               QLabel, QPushButton, QLineEdit, QMessageBox, QWidget, 
                               QGroupBox, QApplication, QFrame, QScrollArea, QSlider)
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QBrush
from PySide6.QtCore import Qt, QRect, QTimer
from core.calibration_generator import generate_cor_file, calculate_analytical_parameters

# 8 Standard EZCAD Orientations
# Mapping of screen positions to physical orientation:
EZCAD_ORIENTATIONS = [
    {"name": "1", "sq": (-1, 1),  "di": (1, -1),  "tick_p1": (0.15, -0.15), "tick_p2": (0.15, 0.15),  "tf": lambda x, y: (x, y)},
    {"name": "2", "sq": (1, 1),   "di": (-1, -1), "tick_p1": (-0.15, -0.15),"tick_p2": (-0.15, 0.15), "tf": lambda x, y: (-x, y)},
    {"name": "3", "sq": (1, -1),  "di": (-1, 1),  "tick_p1": (-0.15, 0.15), "tick_p2": (-0.15, -0.15),"tf": lambda x, y: (-x, -y)},
    {"name": "4", "sq": (-1, -1), "di": (1, 1),   "tick_p1": (0.15, 0.15),  "tick_p2": (0.15, -0.15), "tf": lambda x, y: (x, -y)},
    {"name": "5", "sq": (-1, -1), "di": (1, 1),   "tick_p1": (0.15, 0.15),  "tick_p2": (-0.15, 0.15), "tf": lambda x, y: (-y, x)},
    {"name": "6", "sq": (-1, 1),  "di": (1, -1),  "tick_p1": (0.15, -0.15), "tick_p2": (-0.15, -0.15),"tf": lambda x, y: (-y, -x)},
    {"name": "7", "sq": (1, 1),   "di": (-1, -1), "tick_p1": (-0.15, -0.15),"tick_p2": (0.15, -0.15), "tf": lambda x, y: (y, -x)},
    {"name": "8", "sq": (1, -1),  "di": (-1, 1),  "tick_p1": (-0.15, 0.15), "tick_p2": (0.15, 0.15),  "tf": lambda x, y: (y, x)},
]

class GridPreviewWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(320, 320)
        self.state_idx = 0
        
    def set_state(self, idx):
        self.state_idx = idx % 8
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Background
        painter.fillRect(self.rect(), QColor(255, 255, 255))
        
        w, h = self.width(), self.height()
        margin = 35
        grid_w, grid_h = w - 2 * margin, h - 2 * margin
        cx, cy = w / 2.0, h / 2.0
        
        # Grid frame and crosshair
        pen = QPen(QColor(20, 20, 20), 2)
        painter.setPen(pen)
        painter.drawRect(margin, margin, grid_w, grid_h)
        painter.drawLine(int(cx), margin, int(cx), h - margin)
        painter.drawLine(margin, int(cy), w - margin, int(cy))
        
        # Red numbers 1-9 matching EZCAD positions
        font = QFont("Arial", 11, QFont.Bold)
        painter.setFont(font)
        painter.setPen(QColor(220, 20, 20)) # Red text
        
        num_coords = [
            (margin - 18, margin - 6),     (int(cx) - 5, margin - 6),      (w - margin + 8, margin - 6),
            (margin - 18, int(cy) + 5),     (int(cx) + 6, int(cy) - 6),     (w - margin + 8, int(cy) + 5),
            (margin - 18, h - margin + 18), (int(cx) - 5, h - margin + 18), (w - margin + 8, h - margin + 18)
        ]
        
        for i, (nx, ny) in enumerate(num_coords):
            painter.drawText(nx, ny, str(i + 1))
            
        painter.setPen(QPen(QColor(20, 20, 20), 2))
        
        # Current orientation details
        cur = EZCAD_ORIENTATIONS[self.state_idx]
        
        def map_norm(nx, ny):
            px = cx + nx * (grid_w / 2.0)
            py = cy - ny * (grid_h / 2.0)
            return px, py
            
        # 1. Square marker
        sq_nx, sq_ny = cur["sq"]
        sq_px, sq_py = map_norm(sq_nx * 0.85, sq_ny * 0.85)
        painter.drawRect(int(sq_px) - 6, int(sq_py) - 6, 12, 12)
        
        # 2. Diamond marker
        di_nx, di_ny = cur["di"]
        di_px, di_py = map_norm(di_nx * 0.85, di_ny * 0.85)
        painter.save()
        painter.translate(di_px, di_py)
        painter.rotate(45)
        painter.drawRect(-6, -6, 12, 12)
        painter.restore()
        
        # 3. Center tick mark
        t1 = cur["tick_p1"]
        t2 = cur["tick_p2"]
        p1x, p1y = map_norm(t1[0], t1[1])
        p2x, p2y = map_norm(t2[0], t2[1])
        painter.setPen(QPen(QColor(20, 20, 20), 3))
        painter.drawLine(int(p1x), int(p1y), int(p2x), int(p2y))


class CalibrationGeneratorDialog(QDialog):
    def __init__(self, galvo_controller, parent=None, config_handler=None, main_window=None):
        super().__init__(parent)
        self.setWindowTitle("EZCAD 9-Point Calibration Studio")
        self.resize(880, 680)
        self.galvo_controller = galvo_controller
        self.config_handler = config_handler
        self.main_window = main_window
        
        self.state_idx = 0
        self.default_w = 50.0
        self.is_stopped = False
        self.reddot_timer = None
        self.is_reddot_framing = False
        
        # Retrieve field size from main window or config
        if self.main_window and hasattr(self.main_window, 'galvo_config'):
            field_sz = getattr(self.main_window.galvo_config, 'field_size', 100.0)
            self.default_w = field_sz / 2.0
            
        self.setup_ui()
        self.update_status_display()
        
    def setup_ui(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #f8fafc;
                color: #0f172a;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #cbd5e1;
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 10px;
                background-color: #ffffff;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 5px;
                color: #1e3a8a;
            }
            QLineEdit {
                border: 1px solid #94a3b8;
                border-radius: 5px;
                padding: 4px;
                background-color: #ffffff;
                color: #0f172a;
                font-weight: bold;
            }
            QLineEdit:disabled {
                background-color: #f1f5f9;
                color: #94a3b8;
            }
            QPushButton {
                background-color: #1e3a8a;
                color: white;
                font-weight: bold;
                border-radius: 6px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #2563eb;
            }
            QPushButton:disabled {
                background-color: #94a3b8;
            }
        """)
        
        main_layout = QHBoxLayout(self)
        main_layout.setSpacing(15)
        
        # ==========================================
        # LEFT SIDE: Visual Diagram & Orientation & Laser Controls
        # ==========================================
        left_layout = QVBoxLayout()
        
        # Diagram
        diag_group = QGroupBox("1. Visual Orientation (Match Physical Mark)")
        diag_layout = QVBoxLayout()
        
        self.preview = GridPreviewWidget()
        diag_layout.addWidget(self.preview, alignment=Qt.AlignCenter)
        
        # Change image controls
        btn_bar = QHBoxLayout()
        self.lbl_state = QLabel("Image: 1 / 8")
        self.lbl_state.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.lbl_state.setStyleSheet("color: #1e3a8a;")
        
        self.btn_change_img = QPushButton("Change image >>")
        self.btn_change_img.setFixedHeight(34)
        self.btn_change_img.clicked.connect(self.next_state)
        
        btn_bar.addWidget(self.lbl_state)
        btn_bar.addWidget(self.btn_change_img)
        diag_layout.addLayout(btn_bar)
        diag_group.setLayout(diag_layout)
        left_layout.addWidget(diag_group)
        
        # Laser Controls Box
        laser_group = QGroupBox("Laser Marking Controls")
        laser_layout = QGridLayout()
        
        laser_layout.addWidget(QLabel("Power (%):"), 0, 0)
        self.slider_power = QSlider(Qt.Horizontal)
        self.slider_power.setRange(0, 100)
        self.slider_power.setValue(100)
        self.lbl_power_val = QLabel("100")
        pow_lay = QHBoxLayout()
        pow_lay.addWidget(self.slider_power)
        pow_lay.addWidget(self.lbl_power_val)
        self.slider_power.valueChanged.connect(lambda v: self.lbl_power_val.setText(str(v)))
        laser_layout.addLayout(pow_lay, 0, 1)
        
        laser_layout.addWidget(QLabel("Freq (kHz):"), 0, 2)
        self.slider_freq = QSlider(Qt.Horizontal)
        self.slider_freq.setRange(20, 80)
        self.slider_freq.setValue(30)
        self.lbl_freq_val = QLabel("30")
        freq_lay = QHBoxLayout()
        freq_lay.addWidget(self.slider_freq)
        freq_lay.addWidget(self.lbl_freq_val)
        self.slider_freq.valueChanged.connect(lambda v: self.lbl_freq_val.setText(str(v)))
        laser_layout.addLayout(freq_lay, 0, 3)
        
        # Sync with main window if available
        if self.main_window and hasattr(self.main_window, 'ui'):
            if hasattr(self.main_window.ui, 'galvolaserpowerHorizontalSlider_2'):
                main_pwr = self.main_window.ui.galvolaserpowerHorizontalSlider_2
                self.slider_power.setRange(main_pwr.minimum(), main_pwr.maximum())
                self.slider_power.setValue(main_pwr.value())
                self.slider_power.valueChanged.connect(main_pwr.setValue)
                main_pwr.valueChanged.connect(self.slider_power.setValue)
                
            if hasattr(self.main_window.ui, 'galvolaserfreqHorizontalSlider'):
                main_freq = self.main_window.ui.galvolaserfreqHorizontalSlider
                self.slider_freq.setRange(main_freq.minimum(), main_freq.maximum())
                self.slider_freq.setValue(main_freq.value())
                self.slider_freq.valueChanged.connect(main_freq.setValue)
                main_freq.valueChanged.connect(self.slider_freq.setValue)
        
        laser_layout.addWidget(QLabel("Mark Speed:"), 1, 0)
        self.input_mark_speed = QLineEdit("100000")
        self.input_mark_speed.setMaximumWidth(70)
        laser_layout.addWidget(self.input_mark_speed, 1, 1)
        
        laser_layout.addWidget(QLabel("Jump Speed:"), 1, 2)
        self.input_jump_speed = QLineEdit("200000")
        self.input_jump_speed.setMaximumWidth(70)
        laser_layout.addWidget(self.input_jump_speed, 1, 3)
        
        btn_action_layout = QHBoxLayout()
        self.btn_reddot = QPushButton("🔴 Red Dot Frame")
        self.btn_reddot.setStyleSheet("background-color: #dc2626; color: white;")
        self.btn_reddot.clicked.connect(self.toggle_reddot_framing)
        btn_action_layout.addWidget(self.btn_reddot)
        
        self.btn_draw = QPushButton("⚡ Mark Calibration Grid")
        self.btn_draw.setStyleSheet("background-color: #0284c7; color: white;")
        self.btn_draw.clicked.connect(self.draw_pattern)
        btn_action_layout.addWidget(self.btn_draw)
        
        self.btn_stop = QPushButton("⏹ Stop")
        self.btn_stop.setStyleSheet("background-color: #475569; color: white;")
        self.btn_stop.clicked.connect(self.stop_all)
        btn_action_layout.addWidget(self.btn_stop)
        
        laser_layout.addLayout(btn_action_layout, 2, 0, 1, 4)
        laser_group.setLayout(laser_layout)
        left_layout.addWidget(laser_group)
        
        main_layout.addLayout(left_layout, 1)
        
        # ==========================================
        # RIGHT SIDE: Distances Table & Calibration Actions
        # ==========================================
        right_layout = QVBoxLayout()
        
        # Distances
        input_group = QGroupBox("2. Measured Distances from Center (mm)")
        input_layout = QVBoxLayout()
        
        # Target distance W header
        w_layout = QHBoxLayout()
        w_layout.addWidget(QLabel("Target Half-Width (W):"))
        self.input_w = QLineEdit(f"{self.default_w:.2f}")
        self.input_w.setFixedWidth(80)
        self.input_w.textChanged.connect(self.on_w_changed)
        w_layout.addWidget(self.input_w)
        w_layout.addWidget(QLabel("mm (Nominal Field = 2×W)"))
        w_layout.addStretch()
        
        btn_reset_nom = QPushButton("Reset to Nominal")
        btn_reset_nom.setStyleSheet("background-color: #64748b; color: white; padding: 3px 8px;")
        btn_reset_nom.clicked.connect(self.reset_to_nominal)
        w_layout.addWidget(btn_reset_nom)
        input_layout.addLayout(w_layout)
        
        # 9-Point table
        grid = QGridLayout()
        grid.addWidget(QLabel("<b>Pt</b>"), 0, 0, alignment=Qt.AlignCenter)
        grid.addWidget(QLabel("<b>X Distance (mm)</b>"), 0, 1, alignment=Qt.AlignCenter)
        grid.addWidget(QLabel("<b>Y Distance (mm)</b>"), 0, 2, alignment=Qt.AlignCenter)
        grid.addWidget(QLabel("<b>Description</b>"), 0, 3)
        
        self.inputs_x = []
        self.inputs_y = []
        
        pt_descs = [
            "Top-Left Corner", "Top Center", "Top-Right Corner",
            "Left Center", "Center (0,0)", "Right Center",
            "Bottom-Left Corner", "Bottom Center", "Bottom-Right Corner"
        ]
        
        w_val = self.default_w
        default_vals = [
            (w_val, w_val), (0, w_val), (w_val, w_val),
            (w_val, 0),     (0, 0),     (w_val, 0),
            (w_val, w_val), (0, w_val), (w_val, w_val)
        ]
        
        for i in range(9):
            lbl = QLabel(f"<b>{i+1}</b>")
            lbl.setStyleSheet("color: #dc2626; font-size: 13px;")
            grid.addWidget(lbl, i+1, 0, alignment=Qt.AlignCenter)
            
            le_x = QLineEdit(f"{default_vals[i][0]:.3f}")
            le_x.setAlignment(Qt.AlignCenter)
            le_y = QLineEdit(f"{default_vals[i][1]:.3f}")
            le_y.setAlignment(Qt.AlignCenter)
            
            if default_vals[i][0] == 0:
                le_x.setText("0.000")
                le_x.setEnabled(False)
            if default_vals[i][1] == 0:
                le_y.setText("0.000")
                le_y.setEnabled(False)
                
            self.inputs_x.append(le_x)
            self.inputs_y.append(le_y)
            grid.addWidget(le_x, i+1, 1)
            grid.addWidget(le_y, i+1, 2)
            
            desc_lbl = QLabel(pt_descs[i])
            desc_lbl.setStyleSheet("color: #64748b; font-size: 11px;")
            grid.addWidget(desc_lbl, i+1, 3)
            
        input_layout.addLayout(grid)
        input_group.setLayout(input_layout)
        right_layout.addWidget(input_group)
        
        # Status & Action Group
        action_group = QGroupBox("3. Apply & Verify Calibration")
        action_layout = QVBoxLayout()
        
        self.lbl_status = QLabel("Status: Ready")
        self.lbl_status.setStyleSheet("font-weight: bold; color: #0284c7;")
        action_layout.addWidget(self.lbl_status)
        
        btn_action_box = QHBoxLayout()
        self.btn_calculate = QPushButton("✔ Calculate & Apply Calibration")
        self.btn_calculate.setFixedHeight(40)
        self.btn_calculate.setStyleSheet("background-color: #16a34a; font-size: 13px; font-weight: bold;")
        self.btn_calculate.clicked.connect(self.calculate_and_apply)
        btn_action_box.addWidget(self.btn_calculate)
        
        self.btn_verify = QPushButton("🎯 Mark Verification Shape")
        self.btn_verify.setFixedHeight(40)
        self.btn_verify.setStyleSheet("background-color: #0284c7; font-size: 13px; font-weight: bold;")
        self.btn_verify.clicked.connect(self.mark_verification_shape)
        btn_action_box.addWidget(self.btn_verify)
        
        action_layout.addLayout(btn_action_box)
        action_group.setLayout(action_layout)
        right_layout.addWidget(action_group)
        
        # Bottom Close Button
        btn_close_box = QHBoxLayout()
        btn_close_box.addStretch()
        self.btn_close = QPushButton("Close")
        self.btn_close.setFixedWidth(100)
        self.btn_close.setStyleSheet("background-color: #64748b;")
        self.btn_close.clicked.connect(self.close)
        btn_close_box.addWidget(self.btn_close)
        right_layout.addLayout(btn_close_box)
        
        main_layout.addLayout(right_layout, 1)

    def on_w_changed(self, text):
        try:
            val = float(text)
            if val > 0:
                self.default_w = val
        except ValueError:
            pass

    def reset_to_nominal(self):
        w = self.default_w
        default_vals = [
            (w, w), (0, w), (w, w),
            (w, 0), (0, 0), (w, 0),
            (w, w), (0, w), (w, w)
        ]
        for i in range(9):
            if default_vals[i][0] != 0:
                self.inputs_x[i].setText(f"{default_vals[i][0]:.3f}")
            if default_vals[i][1] != 0:
                self.inputs_y[i].setText(f"{default_vals[i][1]:.3f}")

    def next_state(self):
        self.state_idx = (self.state_idx + 1) % 8
        self.lbl_state.setText(f"Image: {self.state_idx + 1} / 8")
        self.preview.set_state(self.state_idx)

    def stop_all(self):
        self.is_stopped = True
        self.stop_reddot()
        if self.galvo_controller and self.galvo_controller.connection:
            try:
                self.galvo_controller.connection.laser_off()
                self.galvo_controller.connection.reddot_off()
            except:
                pass

    def toggle_reddot_framing(self):
        if self.is_reddot_framing:
            self.stop_reddot()
        else:
            self.start_reddot()

    def start_reddot(self):
        if not self.galvo_controller or not self.galvo_controller.connection:
            QMessageBox.warning(self, "Error", "Galvo controller not connected.")
            return
            
        self.is_reddot_framing = True
        self.btn_reddot.setText("⏹ Stop Red Dot")
        self.btn_reddot.setStyleSheet("background-color: #475569; color: white;")
        
        conn = self.galvo_controller.connection
        if hasattr(conn, 'reddot_on'):
            conn.reddot_on()
            
        scale = 65535.0 / (2.0 * self.default_w) if self.default_w > 0 else 655.35
        hw = int(self.default_w * scale)
        c = 32767
        
        pts = [
            (c - hw, c + hw),
            (c + hw, c + hw),
            (c + hw, c - hw),
            (c - hw, c - hw),
            (c - hw, c + hw)
        ]
        
        self.reddot_step = 0
        
        has_continuous = hasattr(conn.dll, 'GT_PROSYS_U3_set_continous_mode_on') if hasattr(conn, 'dll') else False
        if has_continuous:
            conn.dll.GT_PROSYS_U3_set_continous_mode_on()
            
        def _step():
            if not self.is_reddot_framing:
                return
            try:
                # Push the whole box at once so the buffer doesn't starve
                for x, y in pts:
                    conn.galvo_move_xy(int(x), int(y), 2000000)
                # Close the loop
                conn.galvo_move_xy(int(pts[0][0]), int(pts[0][1]), 2000000)
            except Exception:
                pass
                
        self.reddot_timer = QTimer(self)
        self.reddot_timer.timeout.connect(_step)
        self.reddot_timer.start(25)

    def stop_reddot(self):
        self.is_reddot_framing = False
        self.btn_reddot.setText("🔴 Red Dot Frame")
        self.btn_reddot.setStyleSheet("background-color: #dc2626; color: white;")
        if self.reddot_timer:
            self.reddot_timer.stop()
            self.reddot_timer = None
        if self.galvo_controller and self.galvo_controller.connection:
            try:
                conn = self.galvo_controller.connection
                has_continuous = hasattr(conn.dll, 'GT_PROSYS_U3_set_continous_mode_off') if hasattr(conn, 'dll') else False
                if has_continuous:
                    conn.dll.GT_PROSYS_U3_set_continous_mode_off()
                conn.reddot_off()
            except:
                pass

    def draw_pattern(self):
        if self.is_stopped:
            return  # Currently executing, ignore extra clicks
            
        self.stop_reddot()
        self.is_stopped = False
        
        if not self.galvo_controller or not self.galvo_controller.connection:
            QMessageBox.warning(self, "Error", "Galvo controller not connected.")
            return
            
        # Disable buttons to prevent re-entrancy during processEvents()
        self.btn_draw.setEnabled(False)
        self.btn_reddot.setEnabled(False)
        
        conn = self.galvo_controller.connection
        
        try:
            pwr = float(self.slider_power.value())
            freq = float(self.slider_freq.value())
            mark_speed = int(self.input_mark_speed.text())
            jump_speed = int(self.input_jump_speed.text())
            w_val = float(self.input_w.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid parameters entered. Please check inputs.")
            return

        scale = 65535.0 / (2.0 * w_val) if w_val > 0 else 655.35
        hw = int(w_val * scale)
        c = 32767
        
        min_x = c - hw
        max_x = c + hw
        min_y = c - hw
        max_y = c + hw
        
        freq_hz = freq
        crt_val = 100.0 - pwr
        if hasattr(conn, 'set_analog_do_bit'):
            for test_bit in [0, 1, 2]:
                conn.set_analog_do_bit(100.0, crt_val, freq_hz, test_bit)

        # Temporary bypass calibration so RAW lens distortion is burned!
        if hasattr(conn, 'set_calibration_enabled'):
            conn.set_calibration_enabled(False)
            
        queue = []
        def jump(x, y):
            queue.append({'type': 'jump', 'x': int(x), 'y': int(y), 'speed': jump_speed})
            
        def mark(x, y):
            queue.append({'type': 'mark', 'x': int(x), 'y': int(y), 'speed': mark_speed})

        try:
            self.lbl_status.setText("Status: Marking calibration pattern...")
            self.lbl_status.setStyleSheet("color: #eab308; font-weight: bold;")
            
            # 1. Outer square
            jump(min_x, max_y)
            mark(max_x, max_y)
            mark(max_x, min_y)
            mark(min_x, min_y)
            mark(min_x, max_y)
            
            # 2. Vertical center line
            jump(c, max_y)
            mark(c, min_y)
            
            # 3. Horizontal center line
            jump(min_x, c)
            mark(max_x, c)
            
            # 4. Marker size (2.5mm)
            ms = int(2.5 * scale)
            
            # 5. Square at Top-Left (-W, +W)
            jump(min_x - ms, max_y + ms)
            mark(min_x + ms, max_y + ms)
            mark(min_x + ms, max_y - ms)
            mark(min_x - ms, max_y - ms)
            mark(min_x - ms, max_y + ms)
            
            # 6. Diamond at Bottom-Right (+W, -W)
            jump(max_x, min_y + ms)
            mark(max_x + ms, min_y)
            mark(max_x, min_y - ms)
            mark(max_x - ms, min_y)
            mark(max_x, min_y + ms)
            
            # 7. Tick mark: Vertical line at x = c + hw * 0.15, from y = c - hw * 0.15 to c + hw * 0.15
            tick_x = c + int(hw * 0.15)
            tick_y_top = c + int(hw * 0.15)
            tick_y_bot = c - int(hw * 0.15)
            jump(tick_x, tick_y_top)
            mark(tick_x, tick_y_bot)
            
            # Return to center
            jump(c, c)
            
            # Execute the sequence via controller (identical to normal operation)
            success = self.galvo_controller.execute_queue(
                queue,
                loop_count=1,
                abort_check=lambda: self.is_stopped,
                progress_callback=lambda idx, tot, x, y, ctype: QApplication.processEvents()
            )
            
            if self.is_stopped or not success:
                raise InterruptedError("Stopped by user or failed execution")
            
            self.lbl_status.setText("Status: Pattern marked! Measure the 9 points.")
            self.lbl_status.setStyleSheet("color: #16a34a; font-weight: bold;")
            QMessageBox.information(self, "Pattern Marked", 
                "Calibration pattern marked successfully!\n\n"
                "1. Rotate/flip your metal plate to match one of the 8 images (click 'Change image').\n"
                "2. Measure the physical distances with calipers from the centerlines.\n"
                "3. Enter the 9 points and click 'Calculate & Apply Calibration'.")
                
        except InterruptedError:
            self.lbl_status.setText("Status: Marking stopped by user.")
            self.lbl_status.setStyleSheet("color: #ef4444; font-weight: bold;")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to mark pattern: {e}")
            self.lbl_status.setText(f"Status: Error: {e}")
            self.lbl_status.setStyleSheet("color: #ef4444; font-weight: bold;")
        finally:
            if hasattr(conn, 'set_calibration_enabled'):
                conn.set_calibration_enabled(True)
            if conn:
                conn.laser_off()
            
            self.btn_draw.setEnabled(True)
            self.btn_reddot.setEnabled(True)

    def calculate_and_apply(self):
        try:
            w_val = float(self.input_w.text())
            if w_val <= 0: raise ValueError()
        except ValueError:
            QMessageBox.warning(self, "Invalid Half-Width", "Please enter a valid positive number for Target Half-Width W.")
            return
            
        ui_distances = []
        for i in range(9):
            try:
                x = float(self.inputs_x[i].text())
                y = float(self.inputs_y[i].text())
                ui_distances.append((x, y))
            except ValueError:
                QMessageBox.warning(self, "Input Error", f"Point {i+1} has invalid distance numbers.")
                return

        # Map screen points with chosen orientation
        # Screen sign coordinates:
        screen_signs = [
            (-1, 1),  (0, 1),  (1, 1),
            (-1, 0),  (0, 0),  (1, 0),
            (-1, -1), (0, -1), (1, -1)
        ]
        
        # Screen physical points:
        screen_physical = []
        for i in range(9):
            dist_x, dist_y = ui_distances[i]
            sx, sy = screen_signs[i]
            screen_physical.append((dist_x * sx, dist_y * sy))

        # Transform screen coordinates to actual galvo axes using orientation transform
        tf = EZCAD_ORIENTATIONS[self.state_idx]["tf"]
        galvo_measured = [tf(pt[0], pt[1]) for pt in screen_physical]

        # Determine current scale and mapping
        galvo_1_is_x = False
        curr_g1 = 100.0
        curr_g2 = 100.0
        
        if self.main_window and hasattr(self.main_window, 'galvo_config'):
            galvo_1_is_x = getattr(self.main_window.galvo_config, 'galvo_1_is_x', False)
            curr_g1 = getattr(self.main_window.galvo_config, 'g1_scale', 100.0)
            curr_g2 = getattr(self.main_window.galvo_config, 'g2_scale', 100.0)

        # 1. Compute analytical parameters
        res = calculate_analytical_parameters(
            W=w_val,
            measured_points=galvo_measured,
            current_g1_scale=curr_g1,
            current_g2_scale=curr_g2,
            galvo_1_is_x=galvo_1_is_x
        )

        # 2. Compute 65x65 .cor file
        scale_bits_per_mm = 65535.0 / (2.0 * w_val)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cor_filename = "calibrated_ezcad.cor"
        cor_filepath = os.path.join(base_dir, cor_filename)
        
        generate_cor_file(cor_filepath, scale_bits_per_mm, w_val, galvo_measured)

        # 3. Apply to active hardware
        if self.galvo_controller and self.galvo_controller.connection:
            conn = self.galvo_controller.connection
            if hasattr(conn, 'set_calibration_file'):
                conn.set_calibration_file(cor_filepath)
            if hasattr(conn, 'set_calibration_enabled'):
                conn.set_calibration_enabled(True)

        # 4. Apply to main_window and configgalvoPage UI
        if self.main_window:
            mw = self.main_window
            if hasattr(mw, 'configgalvo_widgets'):
                cgw = mw.configgalvo_widgets
                mw.wh.invokeMethod(cgw.confscalegalvo1, "set", f"{res['new_g1_scale']:.4f}")
                mw.wh.invokeMethod(cgw.confscalegalvo2, "set", f"{res['new_g2_scale']:.4f}")
                mw.wh.invokeMethod(cgw.confbargalvo1, "set", f"{res['g1_barrel']:.4f}")
                mw.wh.invokeMethod(cgw.confbargalvo2, "set", f"{res['g2_barrel']:.4f}")
                mw.wh.invokeMethod(cgw.confpargalvo1, "set", f"{res['g1_par']:.4f}")
                mw.wh.invokeMethod(cgw.confpargalvo2, "set", f"{res['g2_par']:.4f}")
                mw.wh.invokeMethod(cgw.conftrapgalvo1, "set", f"{res['g1_trapezoid']:.4f}")
                mw.wh.invokeMethod(cgw.conftrapgalvo2, "set", f"{res['g2_trapezoid']:.4f}")

            # Persist to config.ini
            if hasattr(mw, 'ch'):
                def _save(key, val): mw.ch.addParameter("GalvoField", key, str(val))
                _save("g1_scale", f"{res['new_g1_scale']:.4f}")
                _save("g2_scale", f"{res['new_g2_scale']:.4f}")
                _save("g1_barrel", f"{res['g1_barrel']:.4f}")
                _save("g2_barrel", f"{res['g2_barrel']:.4f}")
                _save("g1_par", f"{res['g1_par']:.4f}")
                _save("g2_par", f"{res['g2_par']:.4f}")
                _save("g1_trapezoid", f"{res['g1_trapezoid']:.4f}")
                _save("g2_trapezoid", f"{res['g2_trapezoid']:.4f}")
                _save("cor_file", cor_filename)
                
                if hasattr(mw, 'config_file_path'):
                    mw.ch.updateFile(mw.config_file_path)

            # Sync in-memory coordinate mapper
            if hasattr(mw, '_apply_galvo_config_to_core'):
                mw._apply_galvo_config_to_core()

        self.update_status_display()
        
        report = (
            f"<b>EZCAD Calibration Applied Successfully!</b><br><br>"
            f"• <b>65×65 Grid .cor File:</b> {cor_filename}<br>"
            f"• <b>Galvo 1 Scale:</b> {res['new_g1_scale']:.4f}%<br>"
            f"• <b>Galvo 2 Scale:</b> {res['new_g2_scale']:.4f}%<br>"
            f"• <b>Barrel / Bulge:</b> {res['g1_barrel']:.4f}<br>"
            f"• <b>Parallelogram (Skew):</b> {res['g1_par']:.4f}<br>"
            f"• <b>Trapezoid:</b> {res['g1_trapezoid']:.4f}<br>"
            f"• <b>Max Pre-Correction Error:</b> {res['max_err_mm']:.3f} mm<br>"
            f"• <b>RMS Error:</b> {res['rms_err_mm']:.3f} mm<br><br>"
            f"<i>The new calibration is now active and saved permanently. Click 'Mark Verification Shape' to verify accuracy.</i>"
        )
        QMessageBox.information(self, "Calibration Complete", report)

    def mark_verification_shape(self):
        if not self.galvo_controller or not self.galvo_controller.connection:
            QMessageBox.warning(self, "Error", "Galvo controller not connected.")
            return
            
        conn = self.galvo_controller.connection
        try:
            w_val = float(self.input_w.text())
            mark_speed = int(self.input_mark_speed.text())
            jump_speed = int(self.input_jump_speed.text())
            pwr = float(self.slider_power.value())
            freq = float(self.slider_freq.value())
        except ValueError:
            w_val, mark_speed, jump_speed, pwr, freq = 50.0, 100000, 200000, 100.0, 30.0

        scale = 65535.0 / (2.0 * w_val)
        hw = int(w_val * scale)
        c = 32767
        
        # Ensure calibration IS ENABLED for verification
        if hasattr(conn, 'set_calibration_enabled'):
            conn.set_calibration_enabled(True)
            
        freq_hz = freq
        crt_val = 100.0 - pwr
        if hasattr(conn, 'set_analog_do_bit'):
            for test_bit in [0, 1, 2]:
                conn.set_analog_do_bit(100.0, crt_val, freq_hz, test_bit)

        try:
            self.is_stopped = False
            queue = [
                {'type': 'jump', 'x': c - hw, 'y': c + hw, 'speed': jump_speed},
                {'type': 'mark', 'x': c + hw, 'y': c + hw, 'speed': mark_speed},
                {'type': 'mark', 'x': c + hw, 'y': c - hw, 'speed': mark_speed},
                {'type': 'mark', 'x': c - hw, 'y': c - hw, 'speed': mark_speed},
                {'type': 'mark', 'x': c - hw, 'y': c + hw, 'speed': mark_speed},
                {'type': 'jump', 'x': c,      'y': c,      'speed': jump_speed},
            ]
            
            success = self.galvo_controller.execute_queue(
                queue,
                loop_count=1,
                abort_check=lambda: self.is_stopped,
                progress_callback=lambda idx, tot, x, y, ctype: QApplication.processEvents()
            )
            
            if not success or self.is_stopped:
                QMessageBox.warning(self, "Aborted", "Verification shape aborted.")
            else:
                QMessageBox.information(self, "Verification Complete", 
                    f"Calibrated test square ({2*w_val:.1f} × {2*w_val:.1f} mm) marked!\n"
                    "Measure the marked square with calipers to verify zero error.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to mark verification shape: {e}")
        finally:
            if conn:
                conn.laser_off()

    def update_status_display(self):
        calib = None
        if self.galvo_controller and self.galvo_controller.connection:
            calib = getattr(self.galvo_controller.connection, 'calibration', None)
            
        if calib and calib.is_valid:
            fname = os.path.basename(calib.config_path)
            self.lbl_status.setText(f"Status: Active | File: {fname} | 65×65 Grid: Loaded")
            self.lbl_status.setStyleSheet("color: #16a34a; font-weight: bold;")
        else:
            self.lbl_status.setText("Status: No active .cor calibration | Raw Galvo DAC")
            self.lbl_status.setStyleSheet("color: #dc2626; font-weight: bold;")

    def closeEvent(self, event):
        self.stop_all()
        super().closeEvent(event)

