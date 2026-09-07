import ctypes
from ctypes import *

dll_path = r"D:\GitHub\RuthvijR-ES\WORKS\DLL_Galvo\Galvo_Scribing\gt5motion_GT.dll"

dll = ctypes.WinDLL(dll_path)

# ==================================================
# DEFINE FUNCTION SIGNATURE
# ==================================================

dll.GT_PROSYS_U3_Initialize.argtypes = [
    POINTER(c_int32)
]

dll.GT_PROSYS_U3_Initialize.restype = c_int32

# ==================================================
# INITIALIZE
# ==================================================

cards = c_int32(0)

result = dll.GT_PROSYS_U3_Initialize(
    byref(cards)
)

print("Result:", result)
print("Cards Found:", cards.value)