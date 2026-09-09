import sys
import os
import time
from ctypes import c_short, c_double

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.dll_wrapper import GalvoDLLWrapper
import core.dll_wrapper

def test_z_movement():
    print("Initializing DLL...")
    core.dll_wrapper.HARDWARE_CONNECTED = True
    dll_wrap = GalvoDLLWrapper()
    res, cards = dll_wrap.initialize()
    
    if not dll_wrap.is_initialized:
        print("DLL initialization failed.")
        return

    print("Disabling all Z limits and resetting axis alarms just in case...")
    if hasattr(dll_wrap.dll, 'GT_PROSYS_U3_ResetAxis'):
        try:
            dll_wrap.dll.GT_PROSYS_U3_ResetAxis.argtypes = [c_short]
            dll_wrap.dll.GT_PROSYS_U3_ResetAxis(c_short(2))
            print("Axis 2 (Z) Reset Command Sent.")
        except Exception as e:
            pass

    if hasattr(dll_wrap.dll, 'GT_PROSYS_U3_disable_hard_limit'):
        dll_wrap.dll.GT_PROSYS_U3_disable_hard_limit(c_short(2))
    if hasattr(dll_wrap.dll, 'GT_PROSYS_U3_disable_home_limit'):
        dll_wrap.dll.GT_PROSYS_U3_disable_home_limit(c_short(2))
    if hasattr(dll_wrap.dll, 'GT_PROSYS_U3_disable_soft_limit'):
        try:
            # Note: We're guessing the signature here as c_short, it may differ slightly.
            dll_wrap.dll.GT_PROSYS_U3_disable_soft_limit(c_short(2))
        except:
            pass
    
    print("\n--- Testing Z Axis Movement ---")
    
    axis_idx = 2  # Z axis
    rel_abs = 1   # 1 for Absolute position (some controllers ignore relative moves)
    no_axis = 1
    
    def try_pulse_mode(mode_val):
        if hasattr(dll_wrap.dll, 'GT_PROSYS_U3_set_pulse_out_mode'):
            print(f"\n--- Setting Pulse Output Mode to {mode_val} ---")
            try:
                dll_wrap.dll.GT_PROSYS_U3_set_pulse_out_mode(c_short(2), c_short(mode_val))
            except Exception as e:
                print("Error setting pulse out mode:", e)

    def move_absolute(distance, max_vel):
        axis_array = (c_short * 1)(axis_idx)
        dist_array = (c_double * 1)(float(distance))
        str_vel = max_vel * 0.1
        tacc = 0.5 # Slow acceleration (0.5s) to prevent stalls
        
        print(f"\nCommanding Absolute move: pos={distance}, max_vel={max_vel}")
        ret = dll_wrap.dll.GT_PROSYS_U3_axis_move(
            c_short(rel_abs), 
            c_short(no_axis), 
            axis_array, 
            dist_array, 
            c_double(str_vel), 
            c_double(max_vel), 
            c_double(tacc)
        )
        print(f"GT_PROSYS_U3_axis_move returned code: {ret}")
        return ret
        
    for mode in [0, 1]:
        try_pulse_mode(mode)
        print(f"\n[Mode {mode}] Trying a larger Absolute move (Pos: 4000 units)")
        move_absolute(4000.0, 800.0)
        
        print("Waiting 5 seconds for move to finish...")
        time.sleep(5)
        
        print(f"\n[Mode {mode}] Trying a larger Absolute move (Pos: 0 units)")
        move_absolute(0.0, 800.0)
        
        print("Waiting 5 seconds for move to finish...")
        time.sleep(5)

    print("\nFinished sending commands.")
    dll_wrap.close()

if __name__ == "__main__":
    test_z_movement()
