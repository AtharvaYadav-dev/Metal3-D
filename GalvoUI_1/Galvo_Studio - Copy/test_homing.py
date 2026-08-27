import sys
import os
import time
from ctypes import c_short, c_int32

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core.dll_wrapper import GalvoDLLWrapper
import core.dll_wrapper

def test_homing():
    print("Initializing DLL...")
    core.dll_wrapper.HARDWARE_CONNECTED = True
    dll_wrap = GalvoDLLWrapper()
    res, cards = dll_wrap.initialize()
    
    if not dll_wrap.is_initialized:
        print("DLL initialization failed.")
        return

    # Map the homing function
    if hasattr(dll_wrap.dll, 'GT_PROSYS_U3_home_axis'):
        dll_wrap.dll.GT_PROSYS_U3_home_axis.argtypes = [c_short]
        dll_wrap.dll.GT_PROSYS_U3_home_axis.restype = c_short
    else:
        print("Error: GT_PROSYS_U3_home_axis not found in DLL.")
        return
        
    if hasattr(dll_wrap.dll, 'GT_PROSYS_U3_get_home_status'):
        dll_wrap.dll.GT_PROSYS_U3_get_home_status.argtypes = [c_int32]
        dll_wrap.dll.GT_PROSYS_U3_get_home_status.restype = c_int32

    print("\n--- Testing Z-Axis Native Homing ---")
    print("WARNING: Be ready to press the limit switch manually or cut power if it goes the wrong way!")
    time.sleep(3)
    
    axis_idx = 2  # Z axis
    
    try:
        print("Sending Homing Command to Axis 2 (Z)...")
        ret = dll_wrap.dll.GT_PROSYS_U3_home_axis(c_short(axis_idx))
        print(f"Homing command returned: {ret}")
        
        # Monitor the home status
        for i in range(50):
            if hasattr(dll_wrap.dll, 'GT_PROSYS_U3_get_home_status'):
                status = dll_wrap.dll.GT_PROSYS_U3_get_home_status(c_int32(axis_idx))
                print(f"[{i}] Home Switch Status: {status}")
            time.sleep(0.5)
            
    except Exception as e:
        print("Error during homing test:", e)

    print("\nFinished sending commands.")
    dll_wrap.close()

if __name__ == "__main__":
    test_homing()
