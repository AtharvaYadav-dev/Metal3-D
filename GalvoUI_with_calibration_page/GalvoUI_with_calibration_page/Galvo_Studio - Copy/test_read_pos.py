import sys
import os
import time
from ctypes import c_short, c_int32, byref, POINTER

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.dll_wrapper import GalvoDLLWrapper

def test_status():
    dll_wrap = GalvoDLLWrapper()
    dll_wrap.initialize()
    dll = dll_wrap.dll
    
    dll.GT_PROSYS_U3_get_command.argtypes = [c_short, POINTER(c_int32)]
    
    def print_status(label):
        pos = c_int32(0)
        dll.GT_PROSYS_U3_get_command(c_short(2), byref(pos))
        print(f"[{label}] Pos: {pos.value}")

    print_status("Start")
    dll_wrap.close()

if __name__ == "__main__":
    test_status()
