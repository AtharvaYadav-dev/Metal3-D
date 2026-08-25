from core.connection import BaseConnection
import time

class StepperController:
    # Axis soft motion bounds (Min mm, Max mm)
    AXIS_LIMITS = {
        'Z': (0.0, 890.0),  # Recoater Blade: 0 to 890 mm
        'U': (0.0, 250.0),  # Build Plate: 0 to 250 mm
        'V': (0.0, 250.0),  # Powder Bay: 0 to 250 mm
    }

    # Motor Driver Alarm & Error Code Definitions
    MOTOR_ERROR_CODES = {
        'Err 001': ("Over-Current Fault", "Output power stage short circuit or motor phase winding shorted."),
        'Err 002': ("Over-Voltage Fault", "DC bus supply voltage exceeded safe operational threshold."),
        'Err 003': ("Power Phase Loss", "Input AC/DC power supply phase or line disconnection."),
        'Err 004': ("Position Following Error", "Motor position out of sync, heavy mechanical bind, or shaft lock."),
        'Err 005': ("Parameter EEPROM Fault", "Driver internal parameter storage corrupted or out of range."),
        'Err 006': ("Auto-Tuning Failure", "Motor phase alignment or auto-tuning failure during boot."),
        'Err 007': ("Motor Driver Alarm (Err 007)", "Motor stall / shaft overload / position loss alarm."),
        'Err 008': ("Under-Voltage Fault", "Input power supply voltage dropped below minimum operating limit."),
        'Err 009': ("Over-Temperature Fault", "Driver power module heatsink temperature exceeded thermal threshold."),
        'Err 010': ("Motor Open Phase Fault", "One or more motor phase winding cables disconnected."),
        'Err 011': ("Current Loop Saturation", "Control current loop exceeded maximum output limit."),
        'Err 012': ("Encoder Feedback Error", "Encoder pulse line broken, disconnected, or signal noise error.")
    }

    def __init__(self, connection: BaseConnection, steps_per_mm=1600.0, z_steps_per_mm=1280.0, u_steps_per_mm=320.0, v_steps_per_mm=320.0):
        self.connection = connection
        self.z_position = 0.0
        self.u_position = 0.0
        self.v_position = 0.0
        self.steps_per_mm = steps_per_mm
        self.z_steps_per_mm = z_steps_per_mm
        self.u_steps_per_mm = u_steps_per_mm
        self.v_steps_per_mm = v_steps_per_mm
        self.next_ready_time = 0.0
        self.trigger_state = 0  # 0 = Triggered (Active-Low / Sinking NPN.NO)

    @classmethod
    def get_error_code_info(cls, code_raw):
        """Converts raw integer or string code into (code_str, title, description)."""
        if not code_raw or code_raw == 0 or code_raw == "0" or code_raw == "NORMAL":
            return None

        if isinstance(code_raw, int):
            code_str = f"Err {code_raw:03d}"
        else:
            s = str(code_raw).strip()
            if s.isdigit():
                code_str = f"Err {int(s):03d}"
            elif s.upper().startswith("ERR"):
                parts = s.split()
                if len(parts) >= 2 and parts[1].isdigit():
                    code_str = f"Err {int(parts[1]):03d}"
                else:
                    code_str = s.upper()
            else:
                code_str = s

        info = cls.MOTOR_ERROR_CODES.get(code_str)
        if info:
            return (code_str, info[0], info[1])
        return (code_str, f"Driver Fault ({code_str})", "Motor driver alarm signal active.")

    def get_axis_driver_error(self, axis='Z'):
        """Queries motor driver error for the specified axis."""
        ax = str(axis).upper()
        if not self.connection:
            return None
        raw_code = self.connection.get_axis_alarm(ax)
        return self.get_error_code_info(raw_code)

    def get_all_driver_errors(self):
        """Returns a dict of all active driver errors across Z, U, V, X, Y axes."""
        errors = {}
        for ax in ['Z', 'U', 'V', 'X', 'Y']:
            err = self.get_axis_driver_error(ax)
            if err:
                errors[ax] = err
        return errors

    def clear_driver_alarms(self, axis=None):
        """Clears driver alarm status for an axis or all axes."""
        if self.connection:
            self.connection.reset_axis_alarm(axis)

    def trigger_simulated_driver_error(self, axis='Z', error_code='Err 007'):
        """Sets a simulated driver error code for UI testing."""
        if self.connection:
            self.connection.set_simulated_alarm(axis, error_code)


    def get_axis_steps_per_mm(self, axis='Z'):
        ax = str(axis).upper()
        if ax == 'Z':
            return self.z_steps_per_mm
        elif ax == 'U':
            return self.u_steps_per_mm
        elif ax == 'V':
            return self.v_steps_per_mm
        return self.steps_per_mm

    def get_physical_z(self):
        """Reads the exact pulse counter from the hardware and converts it to mm."""
        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            return self.z_position
        
        pulses = self.connection.get_axis_position('Z')
        return -pulses / self.z_steps_per_mm

    def get_axis_position(self, axis):
        ax = str(axis).upper()
        if ax == 'Z':
            return self.z_position
        elif ax == 'U':
            return self.u_position
        elif ax == 'V':
            return self.v_position
        return 0.0

    def set_axis_position(self, axis, pos_mm):
        ax = str(axis).upper()
        if ax == 'Z':
            self.z_position = pos_mm
        elif ax == 'U':
            self.u_position = pos_mm
        elif ax == 'V':
            self.v_position = pos_mm

    def apply_limits(self, axis, distance_mm):
        """
        Validates and clamps relative move distance based on defined axis soft bounds.
        Prevents any negative position (< 0.0 mm) or position exceeding maximum limit.
        """
        ax = str(axis).upper()
        if ax not in self.AXIS_LIMITS:
            return distance_mm

        min_lim, max_lim = self.AXIS_LIMITS[ax]
        curr_pos = self.get_axis_position(ax)
        target_pos = curr_pos + distance_mm

        if target_pos < min_lim:
            clamped_dist = min_lim - curr_pos
            print(f"[LIMIT BLOCKED] {ax}-Axis cannot move below {min_lim:.1f} mm! Requested: {target_pos:.3f} mm, Clamped move: {clamped_dist:+.3f} mm")
            return clamped_dist
        elif target_pos > max_lim:
            clamped_dist = max_lim - curr_pos
            print(f"[LIMIT BLOCKED] {ax}-Axis cannot exceed max limit of {max_lim:.1f} mm! Requested: {target_pos:.3f} mm, Clamped move: {clamped_dist:+.3f} mm")
            return clamped_dist

        return distance_mm

    def move_axis(self, axis, position_mm, speed=10000, ignore_limits=False):
        """
        Moves a stepper motor axis to an absolute target position in millimeters.
        """
        ax = str(axis).upper()
        curr_pos = self.get_axis_position(ax)
        distance = position_mm - curr_pos

        if ax == 'Z':
            return self.move_z_relative(distance, speed=speed, ignore_limits=ignore_limits)
        else:
            return self.move_relative(ax, distance, speed=speed, ignore_limits=ignore_limits)

    def move_relative(self, axis, distance_mm, speed=10000, ignore_limits=False):
        """Generic relative move for hardware testing & manual operation of U, V axes."""
        ax = str(axis).upper()

        err_info = self.get_axis_driver_error(ax)
        if err_info:
            code_str, title, desc = err_info
            print(f"[DRIVER ERROR BLOCKED] Axis {ax} has active driver fault: {code_str} ({title})! Motion blocked until alarm is cleared.")
            return False


        if not ignore_limits:
            distance_mm = self.apply_limits(ax, distance_mm)


        if abs(distance_mm) < 0.0001:
            return False

        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            if ax == 'U':
                self.u_position += distance_mm
            elif ax == 'V':
                self.v_position += distance_mm
            print(f"[SIMULATION MOVE] Axis {ax} moved by {distance_mm:+.3f} mm -> U: {self.u_position:.3f}, V: {self.v_position:.3f}")
            return True

        if time.time() < self.next_ready_time:
            wait_time = self.next_ready_time - time.time()
            print(f"{ax} Axis is busy moving. Waiting {wait_time:.2f}s...")
            time.sleep(wait_time)

        pulses = int(distance_mm * self.get_axis_steps_per_mm(ax))
        print(f"Moving Axis {ax} relative by {distance_mm:+.3f} mm ({pulses} pulses) at speed {speed}")
        self.connection.axis_move(ax, pulses, speed, is_relative=True)

        travel_time = (abs(pulses) / speed) + 0.2
        self.next_ready_time = time.time() + travel_time

        if ax == 'U':
            self.u_position += distance_mm
        elif ax == 'V':
            self.v_position += distance_mm

        return True

    def move_z_relative(self, distance_mm, speed=35000, ignore_limits=False):
        """
        Moves the Z axis relative to the current position in mm.
        (Pulses are inverted so that positive distance moves UPWARD physically)
        """
        err_info = self.get_axis_driver_error('Z')
        if err_info:
            code_str, title, desc = err_info
            print(f"[DRIVER ERROR BLOCKED] Z-Axis has active driver fault: {code_str} ({title})! Motion blocked until alarm is cleared.")
            return False


        if not ignore_limits:
            distance_mm = self.apply_limits('Z', distance_mm)


        if abs(distance_mm) < 0.0001:
            return False

        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            self.z_position += distance_mm
            print(f"[SIMULATION MOVE] Z-Axis moved by {distance_mm:+.3f} mm -> New Z: {self.z_position:.3f} mm")
            return True

        if time.time() < self.next_ready_time:
            wait_time = self.next_ready_time - time.time()
            print(f"Z Axis is busy moving. Waiting {wait_time:.2f}s for previous move to finish...")
            time.sleep(wait_time)

        pulses = int(-distance_mm * self.z_steps_per_mm)
        print(f"Moving Axis Z relative by {distance_mm:+.3f} mm ({pulses} pulses) at speed {speed}")
        self.connection.axis_move('Z', pulses, speed, is_relative=True)

        travel_time = (abs(pulses) / speed) + 0.05
        self.next_ready_time = time.time() + travel_time

        self.z_position += distance_mm
        return True

    def move_z_absolute(self, position_mm, speed=35000, ignore_limits=False):
        """Moves the Z axis to an absolute position in mm."""
        distance_mm = position_mm - self.z_position
        return self.move_z_relative(distance_mm, speed=speed, ignore_limits=ignore_limits)

    def home_z(self, app_instance=None):
        """
        Smooth Homing Sequence for Z-Axis (Recoater Blade):
        Moves smoothly in one continuous stroke toward the home sensor until triggered.
        """
        ax = 'Z'
        is_sim = (not self.connection 
                  or not getattr(self.connection, 'is_initialized', False) 
                  or type(self.connection).__name__ == 'MockConnection'
                  or getattr(self.connection, 'dll', None) is None)
        if is_sim:
            print("[SIMULATION HOMING] Z-Axis smoothly reset to 0.000 mm.")
            self.z_position = 0.0
            return True

        print("Starting Smooth Z-Axis Homing Sequence...")

        # 1. Back off if already on sensor
        if self.connection.get_home_status(ax) == self.trigger_state:
            print("Z-Axis sensor currently active. Backing off +2.0 mm...")
            self.move_z_relative(2.0, speed=20000, ignore_limits=True)
            time.sleep(0.1)

        # 2. Initiate ONE smooth continuous move towards home switch
        max_homing_dist = -900.0  # Max travel stroke
        homing_speed = 35000
        pulses = int(-max_homing_dist * self.z_steps_per_mm)

        print(f"Initiating continuous homing move towards Z home sensor...")
        self.connection.axis_move(ax, pulses, homing_speed, is_relative=True)

        # 3. High-frequency sensor status monitoring loop
        start_time = time.time()
        max_timeout = 60.0

        while time.time() - start_time < max_timeout:
            status = self.connection.get_home_status(ax)
            if status == self.trigger_state:
                print("🚨 Z-Axis Home Sensor Triggered! Halting motion smoothly.")
                if hasattr(self.connection, 'sd_stop'):
                    self.connection.sd_stop(ax)
                elif hasattr(self.connection, 'stop'):
                    self.connection.stop()
                time.sleep(0.1)

                # Clear sensor with small backoff
                self.move_z_relative(1.0, speed=5000, ignore_limits=True)
                time.sleep(0.2)

                self.z_position = 0.0
                if hasattr(self.connection, 'set_axis_position'):
                    self.connection.set_axis_position(ax, 0)
                print("Z-Axis Homing Successful! Position set to 0.000 mm.")
                return True

            if app_instance:
                app_instance.processEvents()
            time.sleep(0.015)

        print("Z-Axis Homing failed: Timeout reached without hitting switch.")
        if hasattr(self.connection, 'sd_stop'):
            self.connection.sd_stop(ax)
        return False

    def home_u(self, app_instance=None):
        """
        Smooth Homing Sequence for U-Axis (Build Plate):
        Moves smoothly in one continuous stroke toward the home sensor until triggered.
        """
        ax = 'U'
        is_sim = (not self.connection 
                  or not getattr(self.connection, 'is_initialized', False) 
                  or type(self.connection).__name__ == 'MockConnection'
                  or getattr(self.connection, 'dll', None) is None)
        if is_sim:
            print("[SIMULATION HOMING] U-Axis smoothly reset to 0.000 mm.")
            self.u_position = 0.0
            return True

        print("Starting Smooth U-Axis Homing Sequence...")

        # 1. Back off if already on sensor
        if self.connection.get_home_status(ax) == self.trigger_state:
            print("U-Axis sensor currently active. Backing off +2.0 mm...")
            self.move_relative(ax, 2.0, speed=2500, ignore_limits=True)
            time.sleep(0.3)

        # 2. Initiate ONE smooth continuous move towards home switch (Slow & Steady: ~10 mm/s)
        max_homing_dist = -300.0
        homing_speed = 3200  # 3200 pulses/sec = 10.0 mm/s for U axis (320 steps/mm)
        pulses = int(max_homing_dist * self.u_steps_per_mm)

        print(f"Initiating slow continuous homing move towards U home sensor ({homing_speed} pulses/s)...")
        self.connection.axis_move(ax, pulses, homing_speed, is_relative=True)

        # 3. High-frequency sensor status monitoring loop
        start_time = time.time()
        max_timeout = 60.0

        while time.time() - start_time < max_timeout:
            status = self.connection.get_home_status(ax)
            if status == self.trigger_state:
                print("[SENSOR TRIGGERED] U-Axis Home Sensor Triggered! Halting motion smoothly.")
                if hasattr(self.connection, 'sd_stop'):
                    self.connection.sd_stop(ax)
                elif hasattr(self.connection, 'stop'):
                    self.connection.stop()
                time.sleep(0.1)

                self.move_relative(ax, 1.0, speed=1600, ignore_limits=True)
                time.sleep(0.2)

                self.u_position = 0.0
                if hasattr(self.connection, 'set_axis_position'):
                    self.connection.set_axis_position(ax, 0)
                print("U-Axis Homing Successful! Position set to 0.000 mm.")
                return True

            if app_instance:
                app_instance.processEvents()
            time.sleep(0.015)

        print("U-Axis Homing failed: Timeout reached without hitting switch.")
        if hasattr(self.connection, 'sd_stop'):
            self.connection.sd_stop(ax)
        return False

    def stop_axis(self, axis='V'):
        """Triggers hardware deceleration stop for the specified axis."""
        ax = str(axis).upper()
        if hasattr(self.connection, 'sd_stop'):
            self.connection.sd_stop(ax, dec_time=0.05)
        elif hasattr(self.connection, 'stop'):
            self.connection.stop(ax)

    def home_v(self, app_instance=None):
        """
        Smooth Homing Sequence for V-Axis (Powder Bay):
        Moves smoothly in one continuous stroke toward the home sensor until triggered.
        """
        ax = 'V'
        is_sim = (not self.connection 
                  or not getattr(self.connection, 'is_initialized', False) 
                  or type(self.connection).__name__ == 'MockConnection'
                  or getattr(self.connection, 'dll', None) is None)
        if is_sim:
            print("[SIMULATION HOMING] V-Axis smoothly reset to 0.000 mm.")
            self.v_position = 0.0
            return True

        print("Starting Slow & Smooth V-Axis Homing Sequence...")

        # 1. Back off if already on sensor
        if self.connection.get_home_status(ax) == self.trigger_state:
            print("V-Axis sensor currently active. Backing off +2.0 mm...")
            self.move_relative(ax, 2.0, speed=2500, ignore_limits=True)
            time.sleep(0.3)

        # 2. Initiate ONE smooth continuous move towards home switch (Slow & Steady: ~10 mm/s)
        max_homing_dist = -300.0
        homing_speed = 3200  # 3200 pulses/sec = 10.0 mm/s for V axis (320 steps/mm)
        pulses = int(max_homing_dist * self.v_steps_per_mm)

        print(f"Initiating slow continuous homing move towards V home sensor ({homing_speed} pulses/s)...")
        self.connection.axis_move(ax, pulses, homing_speed, is_relative=True)

        # 3. High-frequency sensor status monitoring loop
        start_time = time.time()
        max_timeout = 60.0

        while time.time() - start_time < max_timeout:
            status = self.connection.get_home_status(ax)
            if status == self.trigger_state:
                print("[SENSOR TRIGGERED] V-Axis Home Sensor Triggered! Halting motion smoothly.")
                self.stop_axis(ax)
                time.sleep(0.1)

                self.move_relative(ax, 1.0, speed=1600, ignore_limits=True)
                time.sleep(0.2)

                self.v_position = 0.0
                if hasattr(self.connection, 'set_axis_position'):
                    self.connection.set_axis_position(ax, 0)
                print("V-Axis Homing Successful! Position set to 0.000 mm.")
                return True

            if app_instance:
                app_instance.processEvents()
            time.sleep(0.015)

        print("V-Axis Homing failed: Timeout reached without hitting switch.")
        self.stop_axis(ax)
        return False

