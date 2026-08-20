import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

# Import the beautiful dashboard UI we built
from metal_dashboard import MetalDashboard

# Import the existing machine backend controllers from the user's legacy code
from machine.stepper_controller import StepperController
from machine.galvo_controller import GalvoController

class DashboardApp(MetalDashboard):
    def __init__(self):
        super().__init__()
        
        self.console_log.clear()
        self.console_log.append("<b>[SYSTEM STARTUP]</b> Initializing Backend Hardware...")
        
        # Initialize Backend Hardware directly
        self.galvo_controller = GalvoController()
        self.galvo_controller.connect()
        
        if self.galvo_controller.is_connected:
            self.console_log.append("Galvo Controller: <font color='#00E676'>CONNECTED</font>")
            self.lbl_machine_status.setText("Ready\nHardware Online")
        else:
            self.console_log.append("Galvo Controller: <font color='#FF3D00'>DISCONNECTED (Demo Mode)</font>")
            self.lbl_machine_status.setText("Demo Mode\nHardware Offline")
            
        self.stepper_controller = StepperController(self.galvo_controller.connection)
        
        # Current Jog Step default
        self.jog_step = 1.0 
        
        self._connect_signals()
        
        # Start a timer to poll axis positions and update UI dynamically
        self.poll_timer = QTimer()
        self.poll_timer.timeout.connect(self._update_status)
        self.poll_timer.start(250) # 4 Hz updates
        
    def _connect_signals(self):
        # Jogging signals
        self.jog_widget.sigJog.connect(self._handle_jog)
        self.jog_widget.sigHome.connect(self._handle_home)
        
        # Job Controls placeholders (until motion planner is fully routed)
        self.btn_start.clicked.connect(lambda: self.console_log.append("<i>[JOB CONTROL] Start/Resume requested.</i>"))
        self.btn_pause.clicked.connect(lambda: self.console_log.append("<i>[JOB CONTROL] Pause requested.</i>"))
        self.btn_stop.clicked.connect(lambda: self.console_log.append("<i>[JOB CONTROL] Stop requested.</i>"))
        self.btn_abort.clicked.connect(lambda: self.console_log.append("<font color='#FF3D00'><i>[JOB CONTROL] Abort Job requested.</i></font>"))
        
    def _handle_jog(self, axis, direction_sign):
        distance = self.jog_step * direction_sign
        self.console_log.append(f"Jogging {axis} axis by {distance:+.1f} mm")
        
        if axis == 'Z':
            self.stepper_controller.move_z_relative(distance)
        else:
            # The backend maps X/Y to U/V in the stepper controller typically
            motor_axis = 'U' if axis == 'X' else 'V'
            self.stepper_controller.move_relative(motor_axis, distance)
            
    def _handle_home(self, axis_group):
        self.console_log.append(f"Homing {axis_group} axes...")
        # Implementation for homing goes here
            
    def _update_status(self):
        # Dynamically update Axis labels from actual hardware state
        z_pos = self.stepper_controller.z_position
        self.lbl_axis_vals["Z"].setText(f"{z_pos:.3f}")
        
        u_pos = self.stepper_controller.u_position
        self.lbl_axis_vals["X"].setText(f"{u_pos:.3f}")
        
        v_pos = self.stepper_controller.v_position
        self.lbl_axis_vals["Y"].setText(f"{v_pos:.3f}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardApp()
    window.showMaximized()
    sys.exit(app.exec())
