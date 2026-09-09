import os
import time
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                               QPushButton, QFileDialog, QMessageBox, QFrame,
                               QGroupBox, QLineEdit, QCheckBox)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from core.calibration import GalvoCalibration
from core.calibration_generator_ui import CalibrationGeneratorDialog

class ScaleCalibrationDialog(QDialog):
    """
    EZCAD-style Scale Calibration dialog.
    Allows user to mark a test line or square, measure the actual length with calipers,
    and calculates:
        New Scale = Current Scale * (Goal Size / Real Size)
    """
    def __init__(self, axis_name="Galvo 1 (X)", current_scale=100.0, galvo_controller=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Scale Calibration - {axis_name}")
        self.setFixedWidth(420)
        self.axis_name = axis_name
        self.current_scale = current_scale
        self.galvo_controller = galvo_controller
        self.calculated_scale = current_scale
        self.is_framing = False
        self.frame_timer = None
        
        self.setup_ui()
        
    def setup_ui(self):
        self.setStyleSheet("""
            QDialog { background-color: #f8fafc; }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #cbd5e1;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 10px;
                background-color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 4px;
                color: #1e3a8a;
            }
            QLineEdit {
                border: 1px solid #94a3b8;
                border-radius: 4px;
                padding: 5px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #1e3a8a;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 6px 14px;
            }
            QPushButton:hover { background-color: #2563eb; }
        """)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        
        title_lbl = QLabel(f"📐 Calibration for {self.axis_name}")
        title_lbl.setFont(QFont("Segoe UI", 11, QFont.Bold))
        title_lbl.setStyleSheet("color: #1e3a8a;")
        layout.addWidget(title_lbl)
        
        desc = QLabel("Mark a reference dimension, measure the true marked dimension with calipers, and apply the exact scaling ratio.")
        desc.setWordWrap(True)
        desc.setStyleSheet("color: #475569; font-size: 11px;")
        layout.addWidget(desc)
        
        # Inputs Group
        grp_calc = QGroupBox("Measurement & Calculation")
        grid = QVBoxLayout()
        
        h1 = QHBoxLayout()
        h1.addWidget(QLabel("Goal / Desired Size (mm):"))
        self.input_goal = QLineEdit("50.00")
        self.input_goal.setAlignment(Qt.AlignCenter)
        self.input_goal.textChanged.connect(self.recompute)
        h1.addWidget(self.input_goal)
        grid.addLayout(h1)
        
        h2 = QHBoxLayout()
        h2.addWidget(QLabel("Real / Measured Size (mm):"))
        self.input_real = QLineEdit("50.00")
        self.input_real.setAlignment(Qt.AlignCenter)
        self.input_real.textChanged.connect(self.recompute)
        h2.addWidget(self.input_real)
        grid.addLayout(h2)
        
        h3 = QHBoxLayout()
        h3.addWidget(QLabel("Current Scale (%):"))
        self.input_cur = QLineEdit(f"{self.current_scale:.4f}")
        self.input_cur.setAlignment(Qt.AlignCenter)
        self.input_cur.textChanged.connect(self.recompute)
        h3.addWidget(self.input_cur)
        grid.addLayout(h3)
        
        h4 = QHBoxLayout()
        lbl_res_title = QLabel("New Calculated Scale (%):")
        lbl_res_title.setFont(QFont("Segoe UI", 9, QFont.Bold))
        h4.addWidget(lbl_res_title)
        self.lbl_res = QLabel(f"{self.current_scale:.4f} %")
        self.lbl_res.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.lbl_res.setStyleSheet("color: #16a34a;")
        self.lbl_res.setAlignment(Qt.AlignCenter)
        h4.addWidget(self.lbl_res)
        grid.addLayout(h4)
        
        grp_calc.setLayout(grid)
        layout.addWidget(grp_calc)
        
        # Test Marking Tools
        grp_test = QGroupBox("Test Mark Tools")
        test_lay = QHBoxLayout()
        
        self.btn_frame = QPushButton("🔴 Red Dot Frame")
        self.btn_frame.setStyleSheet("background-color: #dc2626; color: white;")
        self.btn_frame.clicked.connect(self.toggle_framing)
        test_lay.addWidget(self.btn_frame)
        
        self.btn_mark = QPushButton("⚡ Mark Test Line")
        self.btn_mark.setStyleSheet("background-color: #0284c7; color: white;")
        self.btn_mark.clicked.connect(self.mark_test)
        test_lay.addWidget(self.btn_mark)
        
        grp_test.setLayout(test_lay)
        layout.addWidget(grp_test)
        
        # Dialog Buttons
        btn_box = QHBoxLayout()
        self.btn_apply = QPushButton("Apply to Galvo")
        self.btn_apply.setStyleSheet("background-color: #16a34a; color: white; padding: 8px 16px;")
        self.btn_apply.clicked.connect(self.accept)
        btn_box.addWidget(self.btn_apply)
        
        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.setStyleSheet("background-color: #64748b; color: white; padding: 8px 16px;")
        self.btn_cancel.clicked.connect(self.reject)
        btn_box.addWidget(self.btn_cancel)
        
        layout.addLayout(btn_box)

    def recompute(self):
        try:
            goal = float(self.input_goal.text())
            real = float(self.input_real.text())
            cur = float(self.input_cur.text())
            if real > 0:
                self.calculated_scale = cur * (goal / real)
                self.lbl_res.setText(f"{self.calculated_scale:.4f} %")
                self.btn_apply.setEnabled(True)
            else:
                self.lbl_res.setText("Invalid Real Size")
                self.btn_apply.setEnabled(False)
        except ValueError:
            self.lbl_res.setText("Invalid Numbers")
            self.btn_apply.setEnabled(False)

    def toggle_framing(self):
        if self.is_framing:
            self.stop_framing()
        else:
            self.start_framing()

    def start_framing(self):
        if not self.galvo_controller or not self.galvo_controller.is_connected:
            QMessageBox.warning(self, "Not Connected", "Galvo card is not connected.")
            return
            
        try:
            goal = float(self.input_goal.text())
        except ValueError:
            goal = 50.0
            
        half = goal / 2.0
        # Determine endpoints based on axis
        if "1" in self.axis_name or "X" in self.axis_name:
            pts = [(-half, 0.0), (half, 0.0)]
        else:
            pts = [(0.0, -half), (0.0, half)]
            
        self.is_framing = True
        self.btn_frame.setText("⏹ Stop Red Dot")
        
        conn = self.galvo_controller.connection
        if hasattr(conn, 'red_dot_on'):
            conn.red_dot_on()
            
        self.frame_timer = QTimer(self)
        self.frame_timer.setInterval(25)
        self.frame_idx = 0
        def step():
            if not self.is_framing: return
            p = pts[self.frame_idx % len(pts)]
            self.frame_idx += 1
            if hasattr(conn, 'raw_goto'):
                conn.raw_goto(p[0], p[1])
            elif hasattr(conn, 'goto'):
                conn.goto(p[0], p[1])
        self.frame_timer.timeout.connect(step)
        self.frame_timer.start()

    def stop_framing(self):
        self.is_framing = False
        if self.frame_timer:
            self.frame_timer.stop()
            self.frame_timer = None
        self.btn_frame.setText("🔴 Red Dot Frame")
        if self.galvo_controller and self.galvo_controller.is_connected:
            conn = self.galvo_controller.connection
            if hasattr(conn, 'red_dot_off'):
                conn.red_dot_off()

    def mark_test(self):
        if not self.galvo_controller or not self.galvo_controller.is_connected:
            QMessageBox.warning(self, "Not Connected", "Galvo card is not connected.")
            return
            
        self.stop_framing()
        
        reply = QMessageBox.question(
            self, "Confirm Laser Marking",
            f"Laser will mark a test line of {self.input_goal.text()} mm for {self.axis_name}.\nEnsure safety goggles are worn!",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply != QMessageBox.Yes:
            return
            
        try:
            goal = float(self.input_goal.text())
        except ValueError:
            goal = 50.0
            
        half = goal / 2.0
        if "1" in self.axis_name or "X" in self.axis_name:
            p1 = (-half, 0.0)
            p2 = (half, 0.0)
        else:
            p1 = (0.0, -half)
            p2 = (0.0, half)
            
        conn = self.galvo_controller.connection
        try:
            if hasattr(conn, 'set_laser_power'): conn.set_laser_power(15.0)
            if hasattr(conn, 'set_mark_speed'): conn.set_mark_speed(500000)
            if hasattr(conn, 'set_jump_speed'): conn.set_jump_speed(2000000)
            
            # Jump to start
            if hasattr(conn, 'goto'): conn.goto(p1[0], p1[1])
            time.sleep(0.05)
            # Mark line
            if hasattr(conn, 'mark'): conn.mark(p2[0], p2[1])
            time.sleep(0.05)
            if hasattr(conn, 'goto'): conn.goto(0.0, 0.0)
            
            QMessageBox.information(self, "Done", f"Test line marked! Please measure its true length with a caliper and enter it in 'Real / Measured Size'.")
        except Exception as e:
            QMessageBox.critical(self, "Marking Error", f"Error during marking: {e}")

    def closeEvent(self, event):
        self.stop_framing()
        super().closeEvent(event)


class CalibrationDialog(QDialog):
    """
    Main Calibration Management Dialog.
    Allows loading/unloading 65x65 EZCAD .cor files, toggling calibration,
    and launching the EZCAD 9-Point Calibration Studio or Scale Calibration.
    """
    def __init__(self, galvo_calibration: GalvoCalibration, parent=None, galvo_controller=None, config_handler=None):
        super().__init__(parent)
        self.setWindowTitle("EZCAD Galvo Calibration Manager")
        self.resize(520, 360)
        self.calibration = galvo_calibration
        self.galvo_controller = galvo_controller
        self.config_handler = config_handler
        self.main_window = parent
        
        self.setup_ui()
        self.update_ui()
        
    def setup_ui(self):
        self.setStyleSheet("""
            QDialog { background-color: #f8fafc; }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #cbd5e1;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 10px;
                background-color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 4px;
                color: #1e3a8a;
            }
            QPushButton {
                background-color: #1e3a8a;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 7px 14px;
            }
            QPushButton:hover { background-color: #2563eb; }
        """)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        
        # Title
        hdr = QHBoxLayout()
        title_lbl = QLabel("🎯 Laser Galvo Calibration & Distortion Correction")
        title_lbl.setFont(QFont("Segoe UI", 11, QFont.Bold))
        title_lbl.setStyleSheet("color: #1e3a8a;")
        hdr.addWidget(title_lbl)
        layout.addLayout(hdr)
        
        # Status Box
        status_grp = QGroupBox("Active Correction Map (.cor)")
        s_lay = QVBoxLayout()
        
        self.status_label = QLabel()
        self.status_label.setFont(QFont("Segoe UI", 10, QFont.Bold))
        s_lay.addWidget(self.status_label)
        
        self.path_label = QLabel()
        self.path_label.setWordWrap(True)
        self.path_label.setStyleSheet("color: #475569; font-size: 11px;")
        s_lay.addWidget(self.path_label)
        
        self.chk_enabled = QCheckBox("Enable Correction Map During Laser Output")
        self.chk_enabled.setChecked(getattr(self.calibration, 'enabled', True))
        self.chk_enabled.toggled.connect(self.toggle_calibration_enabled)
        s_lay.addWidget(self.chk_enabled)
        
        status_grp.setLayout(s_lay)
        layout.addWidget(status_grp)
        
        # Actions Box
        act_grp = QGroupBox("Calibration Operations")
        act_lay = QVBoxLayout()
        act_lay.setSpacing(8)
        
        # 9-point wizard button
        self.btn_create = QPushButton("🌟 Open EZCAD 9-Point Calibration Studio...")
        self.btn_create.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.btn_create.setStyleSheet("background-color: #0284c7; color: white; padding: 9px;")
        self.btn_create.clicked.connect(self.create_new_cor)
        act_lay.addWidget(self.btn_create)
        
        # File load/unload buttons
        f_lay = QHBoxLayout()
        self.btn_load = QPushButton("📂 Load Existing .cor File...")
        self.btn_load.clicked.connect(self.load_file)
        f_lay.addWidget(self.btn_load)
        
        self.btn_unload = QPushButton("❌ Reset / Disable .cor")
        self.btn_unload.setStyleSheet("background-color: #64748b; color: white;")
        self.btn_unload.clicked.connect(self.unload_file)
        f_lay.addWidget(self.btn_unload)
        act_lay.addLayout(f_lay)
        
        act_grp.setLayout(act_lay)
        layout.addWidget(act_grp)
        
        # Close button
        b_box = QHBoxLayout()
        b_box.addStretch()
        self.btn_close = QPushButton("Close")
        self.btn_close.setStyleSheet("background-color: #334155; color: white; min-width: 90px;")
        self.btn_close.clicked.connect(self.accept)
        b_box.addWidget(self.btn_close)
        layout.addLayout(b_box)

    def toggle_calibration_enabled(self, checked):
        if hasattr(self.calibration, 'set_enabled'):
            self.calibration.set_enabled(checked)
        if self.galvo_controller and hasattr(self.galvo_controller, 'connection'):
            conn = self.galvo_controller.connection
            if hasattr(conn, 'set_calibration_enabled'):
                conn.set_calibration_enabled(checked)
        if self.config_handler:
            self.config_handler.addParameter("GalvoField", "cor_enabled", str(checked))
            if hasattr(self.main_window, 'config_file_path'):
                self.config_handler.updateFile(self.main_window.config_file_path)
        self.update_ui()

    def create_new_cor(self):
        dlg = CalibrationGeneratorDialog(
            self.galvo_controller, 
            parent=self, 
            config_handler=self.config_handler, 
            main_window=self.main_window
        )
        if dlg.exec() == QDialog.Accepted:
            self.update_ui()
        
    def update_ui(self):
        if self.calibration.is_valid:
            if getattr(self.calibration, 'enabled', True):
                self.status_label.setText("Status: ✅ Active (65x65 Grid Distortion Compensation Applied)")
                self.status_label.setStyleSheet("color: #16a34a;")
            else:
                self.status_label.setText("Status: ⏸ Loaded but Bypassed (Disabled)")
                self.status_label.setStyleSheet("color: #d97706;")
            self.path_label.setText(f"File: {self.calibration.config_path}")
            self.chk_enabled.setEnabled(True)
        else:
            self.status_label.setText("Status: ❌ No .cor correction map active (Using Identity)")
            self.status_label.setStyleSheet("color: #dc2626;")
            self.path_label.setText("File: (None)")
            self.chk_enabled.setEnabled(False)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Calibration File", "", "EZCAD Cor Files (*.cor);;All Files (*)"
        )
        if file_path:
            success = False
            if self.galvo_controller and hasattr(self.galvo_controller, 'connection'):
                conn = self.galvo_controller.connection
                if hasattr(conn, 'set_calibration_file'):
                    success = conn.set_calibration_file(file_path)
            else:
                success = self.calibration.load_calibration(file_path)
                
            if success:
                if self.config_handler:
                    self.config_handler.addParameter("GalvoField", "cor_file", file_path)
                    self.config_handler.addParameter("GalvoField", "cor_enabled", "True")
                    if hasattr(self.main_window, 'config_file_path'):
                        self.config_handler.updateFile(self.main_window.config_file_path)
                self.update_ui()
                QMessageBox.information(self, "Success", "Binary .cor file loaded successfully!\nThe 65x65 correction map is now active.")
            else:
                QMessageBox.warning(self, "Error", "Failed to load the selected file. Ensure it is a valid EZCAD .cor file.")

    def unload_file(self):
        self.calibration.is_valid = False
        self.calibration.config_path = ""
        self.calibration.grid_x = None
        self.calibration.grid_y = None
        if self.config_handler:
            self.config_handler.addParameter("GalvoField", "cor_file", "")
            if hasattr(self.main_window, 'config_file_path'):
                self.config_handler.updateFile(self.main_window.config_file_path)
        self.update_ui()
        QMessageBox.information(self, "Reset", "Correction map unloaded. Standard identity mapping is now active.")
