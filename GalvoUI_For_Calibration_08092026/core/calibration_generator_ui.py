import os
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, 
                               QLabel, QPushButton, QLineEdit, QMessageBox, QWidget, QGroupBox, QApplication)
from PySide6.QtGui import QPainter, QPen, QColor, QFont
from PySide6.QtCore import Qt, QRect
from core.calibration_generator import generate_cor_file

# 8 Transformations mapping the 9 UI boxes to the 9 Galvo points
TRANSFORMS = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8], # 1
    [2, 5, 8, 1, 4, 7, 0, 3, 6], # 2
    [8, 7, 6, 5, 4, 3, 2, 1, 0], # 3
    [6, 3, 0, 7, 4, 1, 8, 5, 2], # 4
    [2, 1, 0, 5, 4, 3, 8, 7, 6], # 5
    [6, 7, 8, 3, 4, 5, 0, 1, 2], # 6
    [0, 3, 6, 1, 4, 7, 2, 5, 8], # 7
    [8, 5, 2, 7, 4, 1, 6, 3, 0], # 8
]

TRANSFORMS_MATH = [
    lambda x, y: (x, y),
    lambda x, y: (y, -x),
    lambda x, y: (-x, -y),
    lambda x, y: (-y, x),
    lambda x, y: (-x, y),
    lambda x, y: (x, -y),
    lambda x, y: (-y, -x),
    lambda x, y: (y, x),
]

class GridPreviewWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(300, 300)
        self.state_idx = 0
        
    def set_state(self, idx):
        self.state_idx = idx % 8
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        w, h = self.width(), self.height()
        margin = 40
        grid_w, grid_h = w - 2*margin, h - 2*margin
        cx, cy = w / 2.0, h / 2.0
        
        # Draw grid lines
        pen = QPen(Qt.black, 2)
        painter.setPen(pen)
        
        # Outer box
        painter.drawRect(margin, margin, grid_w, grid_h)
        # Crosshair
        painter.drawLine(w//2, margin, w//2, h - margin)
        painter.drawLine(margin, h//2, w - margin, h//2)
        
        # Draw numbers 1-9 on the outside
        font = QFont("Arial", 10, QFont.Bold)
        painter.setFont(font)
        painter.setPen(QColor(255, 0, 0)) # Red text
        
        # Hardcoded number positions to exactly match EZCAD layout
        num_coords = [
            (margin - 10, margin - 10),     (w//2 - 5, margin - 10),      (w - margin + 5, margin - 10),
            (margin - 20, h//2 + 5),        (w//2 + 5, h//2 - 5),         (w - margin + 10, h//2 + 5),
            (margin - 10, h - margin + 20), (w//2 - 5, h - margin + 20),  (w - margin + 5, h - margin + 20)
        ]
        
        for i, (nx, ny) in enumerate(num_coords):
            painter.drawText(nx, ny, str(i + 1))
            
        painter.setPen(QPen(Qt.black, 2))
        
        # Helper to map -1..1 galvo space to pixel space
        def map_pt(x, y):
            # Apply transformation
            tx, ty = TRANSFORMS_MATH[self.state_idx](x, y)
            px = cx + tx * (grid_w / 2.0)
            py = cy - ty * (grid_h / 2.0)
            return px, py
            
        # 1. Square (Base: Top-Left, inside)
        sq_px, sq_py = map_pt(-0.85, 0.85)
        painter.drawRect(sq_px - 5, sq_py - 5, 10, 10)
        
        # 2. Diamond (Base: Bot-Right, inside)
        di_px, di_py = map_pt(0.85, -0.85)
        painter.save()
        painter.translate(di_px, di_py)
        painter.rotate(45)
        painter.drawRect(-5, -5, 10, 10)
        painter.restore()
        
        # 3. Tick mark (Base: vertical line at x=-0.3)
        t1_px, t1_py = map_pt(-0.3, 0.2)
        t2_px, t2_py = map_pt(-0.3, -0.2)
        painter.drawLine(t1_px, t1_py, t2_px, t2_py)


class CalibrationGeneratorDialog(QDialog):
    def __init__(self, galvo_controller, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Calibration File (.cor)")
        self.galvo_controller = galvo_controller
        self.state_idx = 0
        self.default_w = 50.0
        self.is_stopped = False
        
        self.setup_ui()
        
    def setup_ui(self):
        main_layout = QHBoxLayout(self)
        
        # Left side: Preview
        left_layout = QVBoxLayout()
        self.preview = GridPreviewWidget()
        left_layout.addWidget(self.preview)
        main_layout.addLayout(left_layout)
        
        # Right side: Controls
        right_layout = QVBoxLayout()
        
        # Change image btn
        img_group = QGroupBox("Orientation")
        img_layout = QVBoxLayout()
        self.lbl_state = QLabel("1")
        self.lbl_state.setAlignment(Qt.AlignCenter)
        btn_change_img = QPushButton("Change image")
        btn_change_img.clicked.connect(self.next_state)
        img_layout.addWidget(self.lbl_state)
        img_layout.addWidget(btn_change_img)
        img_group.setLayout(img_layout)
        right_layout.addWidget(img_group)
        
        # Inputs
        input_group = QGroupBox("Distances")
        grid = QGridLayout()
        grid.addWidget(QLabel("X"), 0, 1, alignment=Qt.AlignCenter)
        grid.addWidget(QLabel("Y"), 0, 2, alignment=Qt.AlignCenter)
        
        self.inputs_x = []
        self.inputs_y = []
        
        default_vals = [
            (50, 50), (0, 50), (50, 50),
            (50, 0),  (0, 0),  (50, 0),
            (50, 50), (0, 50), (50, 50)
        ]
        
        for i in range(9):
            grid.addWidget(QLabel(str(i+1)), i+1, 0)
            
            le_x = QLineEdit(str(default_vals[i][0]))
            le_y = QLineEdit(str(default_vals[i][1]))
            
            if default_vals[i][0] == 0:
                le_x.setEnabled(False)
            if default_vals[i][1] == 0:
                le_y.setEnabled(False)
                
            self.inputs_x.append(le_x)
            self.inputs_y.append(le_y)
            grid.addWidget(le_x, i+1, 1)
            grid.addWidget(le_y, i+1, 2)
            
        input_group.setLayout(grid)
        right_layout.addWidget(input_group)
        
        # Laser Parameters
        param_group = QGroupBox("Laser Settings")
        param_layout = QGridLayout()
        
        param_layout.addWidget(QLabel("Power (%):"), 0, 0)
        self.input_power = QLineEdit("100")
        param_layout.addWidget(self.input_power, 0, 1)
        
        param_layout.addWidget(QLabel("Freq (kHz):"), 1, 0)
        self.input_freq = QLineEdit("30")
        param_layout.addWidget(self.input_freq, 1, 1)
        
        param_layout.addWidget(QLabel("Mark Speed:"), 2, 0)
        self.input_mark_speed = QLineEdit("5000")
        param_layout.addWidget(self.input_mark_speed, 2, 1)
        
        param_layout.addWidget(QLabel("Jump Speed:"), 3, 0)
        self.input_jump_speed = QLineEdit("20000")
        param_layout.addWidget(self.input_jump_speed, 3, 1)
        
        param_group.setLayout(param_layout)
        right_layout.addWidget(param_group)
        
        # Actions
        btn_draw = QPushButton("Draw Test Pattern")
        btn_draw.clicked.connect(self.draw_pattern)
        right_layout.addWidget(btn_draw)
        
        btn_stop = QPushButton("Stop")
        btn_stop.clicked.connect(self.stop_pattern)
        right_layout.addWidget(btn_stop)
        
        btn_generate = QPushButton("Generate & Save .cor")
        btn_generate.clicked.connect(self.generate)
        right_layout.addWidget(btn_generate)
        
        main_layout.addLayout(right_layout)

    def next_state(self):
        self.state_idx = (self.state_idx + 1) % 8
        self.lbl_state.setText(str(self.state_idx + 1))
        self.preview.set_state(self.state_idx)
        
    def stop_pattern(self):
        self.is_stopped = True
        
    def draw_pattern(self):
        self.is_stopped = False
        if not self.galvo_controller or not self.galvo_controller.connection:
            QMessageBox.warning(self, "Error", "Galvo controller not connected.")
            return
            
        scale = 533.89
        hw = int(self.default_w * scale)
        c = 32767
        
        # Galvo coordinates (Y goes up in standard coords, assuming standard mapping)
        min_x = c - hw
        max_x = c + hw
        min_y = c - hw
        max_y = c + hw
        
        conn = self.galvo_controller.connection
        
        try:
            pwr = float(self.input_power.text())
            freq = float(self.input_freq.text())
            mark_speed = int(self.input_mark_speed.text())
            jump_speed = int(self.input_jump_speed.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid laser parameters. Using defaults.")
            pwr, freq, mark_speed, jump_speed = 100.0, 30.0, 5000, 20000

        # Note: 100% power corresponds to crt_val = 0.0 in reverse voltage setup
        crt_val = 100.0 - pwr

        # Set to power and freq
        if hasattr(conn, 'set_analog_do_bit'):
            for test_bit in [0, 1, 2]:
                conn.set_analog_do_bit(100.0, crt_val, freq, test_bit)
            import time
            time.sleep(0.05) # Small delay to ensure DAC is set before drawing
        
        def jump(x, y):
            QApplication.processEvents()
            if self.is_stopped:
                raise InterruptedError("Drawing stopped by user")
            conn.laser_off()
            conn.galvo_move_xy(int(x), int(y), jump_speed)
            if hasattr(conn, 'wait_for_motion'):
                conn.wait_for_motion()
            
        def mark(x, y):
            QApplication.processEvents()
            if self.is_stopped:
                raise InterruptedError("Drawing stopped by user")
            conn.laser_on()
            conn.galvo_move_xy(int(x), int(y), mark_speed)
            if hasattr(conn, 'wait_for_motion'):
                conn.wait_for_motion()
            
        try:
            # Outer square
            jump(min_x, max_y)
            mark(max_x, max_y)
            mark(max_x, min_y)
            mark(min_x, min_y)
            mark(min_x, max_y)
            
            # Vertical line
            jump(c, max_y)
            mark(c, min_y)
            
            # Horizontal line
            jump(min_x, c)
            mark(max_x, c)
            
            # Marker size (2mm)
            ms = int(2.0 * scale)
            
            # Square at Top-Left (min_x, max_y)
            jump(min_x - ms, max_y + ms)
            mark(min_x + ms, max_y + ms)
            mark(min_x + ms, max_y - ms)
            mark(min_x - ms, max_y - ms)
            mark(min_x - ms, max_y + ms)
            
            # Diamond at Bot-Right (max_x, min_y)
            jump(max_x, min_y + ms)
            mark(max_x + ms, min_y)
            mark(max_x, min_y - ms)
            mark(max_x - ms, min_y)
            mark(max_x, min_y + ms)
            
            # Tick mark (vertical line between center and left)
            # Center is `c`, left is `min_x`. Base x=-0.3 -> x_pos = c - hw * 0.3
            tick_x = c - int(hw * 0.3)
            tick_y_top = c + int(hw * 0.2)
            tick_y_bot = c - int(hw * 0.2)
            jump(tick_x, tick_y_top)
            mark(tick_x, tick_y_bot)
            
            conn.laser_off()
            conn.galvo_move_xy(c, c)
            
            QMessageBox.information(self, "Info", "Pattern drawn! Please measure the 9 points and enter the values.")
        except Exception as e:
            if not isinstance(e, InterruptedError):
                QMessageBox.critical(self, "Error", f"Failed to draw pattern: {e}")
        finally:
            if conn:
                conn.laser_off()
        
    def generate(self):
        # Read inputs
        ui_measurements = []
        for i in range(9):
            try:
                x = float(self.inputs_x[i].text())
                y = float(self.inputs_y[i].text())
                ui_measurements.append((x, y))
            except ValueError:
                QMessageBox.warning(self, "Error", f"Invalid input at point {i+1}")
                return
                
        # Transform UI boxes to Galvo ideal points
        transform = TRANSFORMS[self.state_idx]
        galvo_measurements = [None] * 9
        
        # Signs for the 9 Galvo points: 
        # (Top-Left is -X, +Y in typical cartesian)
        signs = [
            (-1, 1),  (0, 1),  (1, 1),
            (-1, 0),  (0, 0),  (1, 0),
            (-1, -1), (0, -1), (1, -1)
        ]
        
        for galvo_idx in range(9):
            ui_idx = transform.index(galvo_idx)
            raw_x, raw_y = ui_measurements[ui_idx]
            
            # Apply the expected sign to the absolute distance
            sx, sy = signs[galvo_idx]
            meas_x = raw_x * sx if sx != 0 else 0
            meas_y = raw_y * sy if sy != 0 else 0
            
            galvo_measurements[galvo_idx] = (meas_x, meas_y)
            
        # Hardcoded scale for now (could be an input field)
        scale = 533.89 
        
        try:
            generate_cor_file("generated_calibration.cor", scale, self.default_w, galvo_measurements)
            QMessageBox.information(self, "Success", "generated_calibration.cor created successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate: {e}")
