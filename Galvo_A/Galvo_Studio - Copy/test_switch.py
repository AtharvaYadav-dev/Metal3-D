import sys
import os
import time
from ctypes import c_int32

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core.dll_wrapper import GalvoDLLWrapper
import core.dll_wrapper

def test_switch():
    print("Initializing DLL...")
    core.dll_wrapper.HARDWARE_CONNECTED = True
    dll_wrap = GalvoDLLWrapper()
    dll_wrap.initialize()
    
    if hasattr(dll_wrap.dll, 'GT_PROSYS_U3_get_home_status'):
        dll_wrap.dll.GT_PROSYS_U3_get_home_status.argtypes = [c_int32]
        dll_wrap.dll.GT_PROSYS_U3_get_home_status.restype = c_int32
    else:
        print("Error: GT_PROSYS_U3_get_home_status not found.")
        return

    print("\n--- Testing Z-Axis Limit Switch ---")
    print("Please manually press and hold your limit switch now to see the value change.")
    
    axis_idx = 2  # Z axis
    
    try:
        # Monitor the home status for 15 seconds
        for i in range(30):
            status = dll_wrap.dll.GT_PROSYS_U3_get_home_status(c_int32(axis_idx))
            print(f"[{i}] Home Switch Status: {status} (Press the switch now!)")
            time.sleep(0.5)
            
    except Exception as e:
        print("Error during test:", e)

    dll_wrap.close()

if __name__ == "__main__":
    test_switch()
