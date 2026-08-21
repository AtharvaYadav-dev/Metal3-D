"""
Galvo Card Interface & Controller (machine/galvo_card.py)
===================================================================
Company: Specialise Products Private Limited
Project: Metal 3D Printer

Provides high-level GalvoCardHandler to encapsulate all Galvo scanner card
operations: initialization, mirror homing, vector execution queue,
inductive sensor diagnostics, and test pattern generation.
"""

import time
from machine.galvo_controller import GalvoController


class GalvoCardHandler:
    """
    High-level handler for Galvo Card hardware interface and operation controls.
    """
    def __init__(self):
        self.controller = None
        self.is_connected = False

    def initialize(self, force_mock=False):
        """Initializes and connects to the Galvo scanner card."""
        try:
            self.controller = GalvoController()
            self.is_connected = self.controller.connect(force_mock=force_mock)
            if self.is_connected:
                print("[Galvo Card] Connected to physical Galvo hardware card.")
            else:
                print("[Galvo Card] Operating in simulated Galvo card mode.")
        except Exception as err:
            print("[Galvo Card] Initialization notice:", err)
            self.controller = None
            self.is_connected = False
        return self.is_connected

    def home_galvo(self):
        """Homes the laser galvo mirrors to center position (32767, 32767)."""
        print("\n[Galvo Homing] Homing Laser Galvo Scanner to Center Position...")
        if self.controller:
            if not self.controller.is_connected:
                self.controller.connect()
            success = self.controller.galvo_home()
            print("[Galvo Homing] Galvo mirrors positioned at center (32767, 32767).")
            return success
        else:
            print("[Galvo Homing] Galvo controller offline. (Simulated)")
            return False

    def execute_queue(self, send_queue, loop_count=1, progress_callback=None, abort_check=None):
        """Executes vector command queue on the Galvo card."""
        if self.controller:
            return self.controller.execute_queue(
                send_queue=send_queue,
                loop_count=loop_count,
                progress_callback=progress_callback,
                abort_check=abort_check
            )
        else:
            print("[Galvo Card] Controller offline, simulating vector execution.")
            time.sleep(0.4)
            return True

    def query_sensors(self, stepper_controller=None):
        """Prints a diagnostic status report for Galvo and system homing sensors."""
        print("\n" + "=" * 52)
        print("🔍 INDUCTIVE PROXIMITY HOMING SENSOR DEBUGGER REPORT")
        print("=" * 52)
        conn = getattr(self.controller, 'connection', None) if self.controller else None
        if not conn:
            print("[Sensor Debugger] Hardware connection offline (Simulation Mode).")
            print("  Z-Axis (Z_org Recoater Blade) : [SIMULATED OPEN]")
            print("  U-Axis (U_org Build Plate)    : [SIMULATED OPEN]")
            print("  V-Axis (V_org Powder Bay)     : [SIMULATED OPEN]")
            print("  X-Axis (X_org Galvo Scanner X): [SIMULATED OPEN]")
            print("  Y-Axis (Y_org Galvo Scanner Y): [SIMULATED OPEN]")
        else:
            trigger_val = getattr(stepper_controller, 'trigger_state', 0) if stepper_controller else 0
            axes = [
                ('Z', 'Z-Axis (Recoater Blade Z_org)'),
                ('U', 'U-Axis (Build Plate U_org)  '),
                ('V', 'V-Axis (Powder Bay V_org)   '),
                ('X', 'X-Axis (Galvo Scanner X_org)'),
                ('Y', 'Y-Axis (Galvo Scanner Y_org)')
            ]
            for ax_code, ax_name in axes:
                try:
                    val = conn.get_home_status(ax_code)
                    is_triggered = (val == trigger_val)
                    status_text = "🚨 TRIGGERED (CLOSED / SENSING)" if is_triggered else "🟢 CLEAR (OPEN / OFF)"
                    print(f"  {ax_name} : {status_text}  [Raw Value: {val}]")
                except Exception as err:
                    print(f"  {ax_name} : Error reading sensor -> {err}")
        print("=" * 52 + "\n")

    def run_test_pattern(self):
        """Runs a test calibration pattern on the Galvo card."""
        if self.controller:
            return self.controller.test_pattern()
        else:
            print("[Galvo Card] Controller offline, cannot run hardware test pattern.")
            return False
