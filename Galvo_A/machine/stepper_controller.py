from core.connection import BaseConnection

class StepperController:
    AXIS_LIMITS = {
        'Z': (0.0, 890.0),
        'U': (0.0, 250.0),
        'V': (0.0, 250.0)
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
        self.z_trigger_state = 0  # Z active-low microswitch
        self.u_trigger_state = 1  # U active-high inductive sensor (LED ON -> 1)
        self.v_trigger_state = 1  # V active-high inductive sensor (LED ON -> 1)

    def get_axis_steps_per_mm(self, axis='Z'):
        ax = str(axis).upper()
        if ax == 'Z':
            return self.z_steps_per_mm
        elif ax == 'U':
            return self.u_steps_per_mm
        elif ax == 'V':
            return self.v_steps_per_mm
        return self.steps_per_mm

    def is_sensor_triggered(self, axis):
        """Returns True if the limit/home sensor is active/triggered for the given axis."""
        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            return False
        try:
            status = self.connection.get_home_status(axis)
            ax = str(axis).upper()
            if ax == 'Z':
                return status == self.z_trigger_state
            elif ax == 'U':
                return status == self.u_trigger_state or status != 0
            elif ax == 'V':
                return status == self.v_trigger_state or status != 0
            return status != 0
        except Exception:
            return False

    def get_physical_z(self):
        """Reads the exact pulse counter from the hardware and converts it to mm."""
        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            return self.z_position
        
        pulses = self.connection.get_axis_position('Z')
        return -pulses / self.z_steps_per_mm

    def move_axis(self, axis, position_mm, speed=10000):
        """
        Moves a stepper motor axis (e.g., Z-axis for focus, or XY table).
        Position is given in millimeters.
        """
        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            print("Cannot move axis, system not initialized.")
            return False
            
        if axis.upper() == 'Z':
            distance = position_mm - self.z_position
            return self.move_z_relative(distance, speed)
            
        pulses = int(position_mm * self.get_axis_steps_per_mm(axis))
        print(f"Moving Axis {axis} to {position_mm} mm ({pulses} pulses) at speed {speed}")
        self.connection.axis_move(axis, pulses, speed)
        
        return True

    def move_relative(self, axis, distance_mm, speed=10000, ignore_limits=False, is_homing=False):
        """Generic relative move with soft limits (0 to 250mm) and negative block at 0."""
        if abs(distance_mm) < 0.0001:
            return False

        ax = str(axis).upper()
        curr_pos = self.u_position if ax == 'U' else (self.v_position if ax == 'V' else self.z_position)
        min_lim, max_lim = self.AXIS_LIMITS.get(ax, (0.0, 250.0))

        if not ignore_limits:
            if curr_pos <= min_lim and distance_mm < 0:
                print(f"[LIMIT BLOCKED] {ax}-Axis is at {curr_pos:.3f} mm. Blocked negative movement.")
                return False

            new_pos = curr_pos + distance_mm
            clamped_pos = max(min_lim, min(max_lim, new_pos))
            distance_mm = clamped_pos - curr_pos

            if abs(distance_mm) < 0.0001:
                print(f"[LIMIT BLOCKED] {ax}-Axis reached boundary limit ({clamped_pos:.3f} mm).")
                return False

        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            if ax == 'U':
                self.u_position += distance_mm
            elif ax == 'V':
                self.v_position += distance_mm
            print(f"[SIMULATION MOVE] Axis {ax} moved by {distance_mm:+.3f} mm -> U: {self.u_position:.3f}, V: {self.v_position:.3f}")
            return True

        import time
        if time.time() < self.next_ready_time:
            wait_time = self.next_ready_time - time.time()
            if not is_homing:
                print(f"{axis} Axis is busy moving. Waiting {wait_time:.2f}s...")
            time.sleep(wait_time)
            
        pulses = int(distance_mm * self.get_axis_steps_per_mm(axis))
        print(f"Moving Axis {axis} relative by {distance_mm:.3f} mm ({pulses} pulses) at speed {speed}")
        self.connection.axis_move(axis, pulses, speed, is_relative=True)
        
        # During homing, use exact physical pulse duration without extra delay for smooth continuous motion
        travel_time = (abs(pulses) / float(speed)) if is_homing else ((abs(pulses) / float(speed)) + 0.2)
        self.next_ready_time = time.time() + travel_time
        
        if ax == 'U':
            self.u_position += distance_mm
        elif ax == 'V':
            self.v_position += distance_mm
            
        return True

    def move_z_relative(self, distance_mm, speed=10000, ignore_limits=False, is_homing=False):
        """Moves Z axis with soft limits (0 to 890mm) and negative block at 0."""
        if abs(distance_mm) < 0.0001:
            return False

        curr_pos = self.z_position
        min_lim, max_lim = 0.0, 890.0

        if not ignore_limits:
            if curr_pos <= min_lim and distance_mm < 0:
                print(f"[LIMIT BLOCKED] Z-Axis is at {curr_pos:.3f} mm. Blocked negative movement.")
                return False

            new_pos = curr_pos + distance_mm
            clamped_pos = max(min_lim, min(max_lim, new_pos))
            distance_mm = clamped_pos - curr_pos

            if abs(distance_mm) < 0.0001:
                print(f"[LIMIT BLOCKED] Z-Axis reached boundary limit ({clamped_pos:.3f} mm).")
                return False

        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            self.z_position += distance_mm
            print(f"[SIMULATION MOVE] Z-Axis moved by {distance_mm:+.3f} mm -> New Z: {self.z_position:.3f} mm")
            return True
            
        import time
        if time.time() < self.next_ready_time:
            wait_time = self.next_ready_time - time.time()
            if not is_homing:
                print(f"Z Axis is busy moving. Waiting {wait_time:.2f}s for previous move to finish...")
            time.sleep(wait_time)

        pulses = int(-distance_mm * self.z_steps_per_mm)
        print(f"Moving Axis Z relative by {distance_mm:.3f} mm ({pulses} pulses) at speed {speed}")
        self.connection.axis_move('Z', pulses, speed, is_relative=True)
        
        travel_time = (abs(pulses) / float(speed)) if is_homing else ((abs(pulses) / float(speed)) + 0.2)
        self.next_ready_time = time.time() + travel_time
        
        self.z_position += distance_mm
        return True

    def move_z_absolute(self, position_mm, speed=10000, ignore_limits=False):
        """Moves Z axis to absolute position clamped between 0 and 890mm."""
        if not ignore_limits:
            position_mm = max(0.0, min(890.0, position_mm))

        distance_mm = position_mm - self.z_position
        if abs(distance_mm) < 0.001:
            return False
            
        import time
        if time.time() < self.next_ready_time:
            wait_time = self.next_ready_time - time.time()
            print(f"Z Axis is busy moving. Waiting {wait_time:.2f}s for previous move to finish...")
            time.sleep(wait_time)
            
        pulses = int(-distance_mm * self.z_steps_per_mm)
        print(f"Moving Axis Z absolute to {position_mm:.3f} mm (distance: {distance_mm:.3f} mm, {pulses} pulses) at speed {speed}")
        self.connection.axis_move('Z', pulses, speed, is_relative=True)
from core.connection import BaseConnection

class StepperController:
    AXIS_LIMITS = {
        'Z': (0.0, 890.0),
        'U': (0.0, 250.0),
        'V': (0.0, 250.0)
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
        self.z_trigger_state = 0  # Z active-low microswitch
        self.u_trigger_state = 1  # U active-high inductive sensor (LED ON -> 1)
        self.v_trigger_state = 1  # V active-high inductive sensor (LED ON -> 1)

    def get_axis_steps_per_mm(self, axis='Z'):
        ax = str(axis).upper()
        if ax == 'Z':
            return self.z_steps_per_mm
        elif ax == 'U':
            return self.u_steps_per_mm
        elif ax == 'V':
            return self.v_steps_per_mm
        return self.steps_per_mm

    def is_sensor_triggered(self, axis):
        """Returns True if the limit/home sensor is active/triggered for the given axis."""
        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            return False
        try:
            status = self.connection.get_home_status(axis)
            ax = str(axis).upper()
            if ax == 'Z':
                return status == self.z_trigger_state
            elif ax == 'U':
                return status == self.u_trigger_state
            elif ax == 'V':
                return status == self.v_trigger_state
            return status == 1
        except Exception:
            return False

    def get_physical_z(self):
        """Reads the exact pulse counter from the hardware and converts it to mm."""
        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            return self.z_position
        
        pulses = self.connection.get_axis_position('Z')
        return -pulses / self.z_steps_per_mm

    def move_axis(self, axis, position_mm, speed=10000):
        """
        Moves a stepper motor axis (e.g., Z-axis for focus, or XY table).
        Position is given in millimeters.
        """
        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            print("Cannot move axis, system not initialized.")
            return False
            
        if axis.upper() == 'Z':
            distance = position_mm - self.z_position
            return self.move_z_relative(distance, speed)
            
        pulses = int(position_mm * self.get_axis_steps_per_mm(axis))
        print(f"Moving Axis {axis} to {position_mm} mm ({pulses} pulses) at speed {speed}")
        self.connection.axis_move(axis, pulses, speed)
        
        return True

    def move_relative(self, axis, distance_mm, speed=10000, ignore_limits=False, is_homing=False):
        """Generic relative move with soft limits (0 to 250mm) and negative block at 0."""
        if abs(distance_mm) < 0.0001:
            return False

        ax = str(axis).upper()
        curr_pos = self.u_position if ax == 'U' else (self.v_position if ax == 'V' else self.z_position)
        min_lim, max_lim = self.AXIS_LIMITS.get(ax, (0.0, 250.0))

        if not ignore_limits:
            if curr_pos <= min_lim and distance_mm < 0:
                print(f"[LIMIT BLOCKED] {ax}-Axis is at {curr_pos:.3f} mm. Blocked negative movement.")
                return False

            new_pos = curr_pos + distance_mm
            clamped_pos = max(min_lim, min(max_lim, new_pos))
            distance_mm = clamped_pos - curr_pos

            if abs(distance_mm) < 0.0001:
                print(f"[LIMIT BLOCKED] {ax}-Axis reached boundary limit ({clamped_pos:.3f} mm).")
                return False

        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            if ax == 'U':
                self.u_position += distance_mm
            elif ax == 'V':
                self.v_position += distance_mm
            print(f"[SIMULATION MOVE] Axis {ax} moved by {distance_mm:+.3f} mm -> U: {self.u_position:.3f}, V: {self.v_position:.3f}")
            return True

        import time
        if time.time() < self.next_ready_time:
            wait_time = self.next_ready_time - time.time()
            if not is_homing:
                print(f"{axis} Axis is busy moving. Waiting {wait_time:.2f}s...")
            time.sleep(wait_time)
            
        pulses = int(distance_mm * self.get_axis_steps_per_mm(axis))
        print(f"Moving Axis {axis} relative by {distance_mm:.3f} mm ({pulses} pulses) at speed {speed}")
        self.connection.axis_move(axis, pulses, speed, is_relative=True)
        
        # During homing, use exact physical pulse duration without extra delay for smooth continuous motion
        travel_time = (abs(pulses) / float(speed)) if is_homing else ((abs(pulses) / float(speed)) + 0.2)
        self.next_ready_time = time.time() + travel_time
        
        if ax == 'U':
            self.u_position += distance_mm
        elif ax == 'V':
            self.v_position += distance_mm
            
        return True

    def move_z_relative(self, distance_mm, speed=10000, ignore_limits=False, is_homing=False):
        """Moves Z axis with soft limits (0 to 890mm) and negative block at 0."""
        if abs(distance_mm) < 0.0001:
            return False

        curr_pos = self.z_position
        min_lim, max_lim = 0.0, 890.0

        if not ignore_limits:
            if curr_pos <= min_lim and distance_mm < 0:
                print(f"[LIMIT BLOCKED] Z-Axis is at {curr_pos:.3f} mm. Blocked negative movement.")
                return False

            new_pos = curr_pos + distance_mm
            clamped_pos = max(min_lim, min(max_lim, new_pos))
            distance_mm = clamped_pos - curr_pos

            if abs(distance_mm) < 0.0001:
                print(f"[LIMIT BLOCKED] Z-Axis reached boundary limit ({clamped_pos:.3f} mm).")
                return False

        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            self.z_position += distance_mm
            print(f"[SIMULATION MOVE] Z-Axis moved by {distance_mm:+.3f} mm -> New Z: {self.z_position:.3f} mm")
            return True
            
        import time
        if time.time() < self.next_ready_time:
            wait_time = self.next_ready_time - time.time()
            if not is_homing:
                print(f"Z Axis is busy moving. Waiting {wait_time:.2f}s for previous move to finish...")
            time.sleep(wait_time)

        pulses = int(-distance_mm * self.z_steps_per_mm)
        print(f"Moving Axis Z relative by {distance_mm:.3f} mm ({pulses} pulses) at speed {speed}")
        self.connection.axis_move('Z', pulses, speed, is_relative=True)
        
        travel_time = (abs(pulses) / float(speed)) if is_homing else ((abs(pulses) / float(speed)) + 0.2)
        self.next_ready_time = time.time() + travel_time
        
        self.z_position += distance_mm
        return True

    def move_z_absolute(self, position_mm, speed=10000, ignore_limits=False):
        """Moves Z axis to absolute position clamped between 0 and 890mm."""
        if not ignore_limits:
            position_mm = max(0.0, min(890.0, position_mm))

        distance_mm = position_mm - self.z_position
        if abs(distance_mm) < 0.001:
            return False
            
        import time
        if time.time() < self.next_ready_time:
            wait_time = self.next_ready_time - time.time()
            print(f"Z Axis is busy moving. Waiting {wait_time:.2f}s for previous move to finish...")
            time.sleep(wait_time)
            
        pulses = int(-distance_mm * self.z_steps_per_mm)
        print(f"Moving Axis Z absolute to {position_mm:.3f} mm (distance: {distance_mm:.3f} mm, {pulses} pulses) at speed {speed}")
        self.connection.axis_move('Z', pulses, speed, is_relative=True)
        
        travel_time = (abs(pulses) / float(speed)) + 0.2
        self.next_ready_time = time.time() + travel_time
        
        self.z_position = position_mm
        return True
        
    def home_z(self, app_instance=None):
        """Safe & Smooth Incremental Homing Sequence for Z-Axis (890 mm max travel)."""
        import time
        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            print("[SIMULATION HOMING] Z-Axis reset to 0.000 mm.")
            self.z_position = 0.0
            return True
            
        print("Starting Z-Axis Safe Homing Sequence...")
        if self.is_sensor_triggered('Z'):
            print("Z Limit Switch already triggered at start. Backing off 2mm...")
            self.move_z_relative(2.0, speed=4000, ignore_limits=True, is_homing=True)
            time.sleep(0.3)

        initial_status = self.connection.get_home_status('Z')
        speed = int(4.0 * self.z_steps_per_mm)
        step_mm = 0.5
        max_dist_mm = 900.0
        steps = int(max_dist_mm / step_mm)

        for _ in range(steps):
            curr_status = self.connection.get_home_status('Z')
            if self.is_sensor_triggered('Z') or curr_status != initial_status:
                print(f"Z Limit Switch Triggered! Light ON (Status: {curr_status}). Stopping motion.")
                self.move_z_relative(2.0, speed=speed, ignore_limits=True, is_homing=True)
                time.sleep(0.3)
                self.z_position = 0.0
                if hasattr(self.connection, 'set_axis_position'):
                    self.connection.set_axis_position('Z', 0)
                return True

            self.move_z_relative(-step_mm, speed=speed, ignore_limits=True, is_homing=True)
            time.sleep(0.005)
            if app_instance:
                app_instance.processEvents()

        print("Z Homing reached travel limit.")
        self.z_position = 0.0
        return False

    def home_u(self, app_instance=None):
        """Safe & Smooth Incremental Homing Sequence for U-Axis (Powder Bay, 250 mm max travel)."""
        import time
        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            print("[SIMULATION HOMING] U-Axis reset to 0.000 mm.")
            self.u_position = 0.0
            return True
            
        print("Starting U-Axis Safe Homing Sequence...")
        if self.is_sensor_triggered('U'):
            print("U Inductive Sensor Light ON at start! Backing off 2mm...")
            self.move_relative('U', 2.0, speed=2000, ignore_limits=True, is_homing=True)
            time.sleep(0.3)

        initial_status = self.connection.get_home_status('U')
        speed = int(4.0 * self.u_steps_per_mm)
        step_mm = 0.5
        max_dist_mm = 260.0
        steps = int(max_dist_mm / step_mm)

        for _ in range(steps):
            curr_status = self.connection.get_home_status('U')
            if self.is_sensor_triggered('U') or curr_status != initial_status:
                print(f"U Inductive Sensor Light ON! Status changed ({initial_status} -> {curr_status}). Stopping motion.")
                self.move_relative('U', 2.0, speed=speed, ignore_limits=True, is_homing=True)
                time.sleep(0.3)
                self.u_position = 0.0
                if hasattr(self.connection, 'set_axis_position'):
                    self.connection.set_axis_position('U', 0)
                return True

            self.move_relative('U', -step_mm, speed=speed, ignore_limits=True, is_homing=True)
            time.sleep(0.005)
            if app_instance:
                app_instance.processEvents()

        print("U Homing reached travel limit.")
        self.u_position = 0.0
        return False

    def home_v(self, app_instance=None):
        """Safe & Smooth Incremental Homing Sequence for V-Axis (Build Plate, 250 mm max travel)."""
        import time
        if not self.connection or not getattr(self.connection, 'is_initialized', False):
            print("[SIMULATION HOMING] V-Axis reset to 0.000 mm.")
            self.v_position = 0.0
            return True
            
        print("Starting V-Axis Safe Homing Sequence...")
        if self.is_sensor_triggered('V'):
            print("V Inductive Sensor Light ON at start! Backing off 2mm...")
            self.move_relative('V', 2.0, speed=2000, ignore_limits=True, is_homing=True)
            time.sleep(0.3)

        initial_status = self.connection.get_home_status('V')
        speed = int(4.0 * self.v_steps_per_mm)
        step_mm = 0.5
        max_dist_mm = 260.0
        steps = int(max_dist_mm / step_mm)

        for _ in range(steps):
            curr_status = self.connection.get_home_status('V')
            if self.v_position <= 0 and (self.is_sensor_triggered('V') or curr_status != initial_status):
                print(f"V Inductive Sensor Light ON! Status changed ({initial_status} -> {curr_status}). Stopping motion.")
                self.move_relative('V', 2.0, speed=speed, ignore_limits=True, is_homing=True)
                time.sleep(0.3)
                self.v_position = 0.0
                if hasattr(self.connection, 'set_axis_position'):
                    self.connection.set_axis_position('V', 0)
                return True

            self.move_relative('V', -step_mm, speed=speed, ignore_limits=True, is_homing=True)
            time.sleep(0.005)
            if app_instance:
                app_instance.processEvents()

        print("V Homing reached travel limit.")
        self.v_position = 0.0
        return False
