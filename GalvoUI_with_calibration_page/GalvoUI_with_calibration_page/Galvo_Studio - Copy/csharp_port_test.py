import time
import math
import sys
from core.dll_wrapper import GalvoDLLWrapper

XORIGIN = 32767
YORIGIN = 32767
GSPEED = 100000
XOFFSET = 0.0
YOFFSET = 0.0
THETA = 0.0

def wait_for_motion(wrapper):
    if hasattr(wrapper.dll, 'GT_PROSYS_U3_galvo_run_status'):
        while wrapper.dll.GT_PROSYS_U3_galvo_run_status() == 1:
            time.sleep(0.001)

def draw_square(wrapper, size=10000):
    half_size = size // 2
    print(f"Drawing Square of size {size} around origin...")
    
    # Bottom Left
    wrapper.dll.GT_PROSYS_U3_galvo_move_XY(XORIGIN - half_size, YORIGIN - half_size, GSPEED, XOFFSET, YOFFSET, THETA)
    wait_for_motion(wrapper)
    
    # Top Left
    wrapper.dll.GT_PROSYS_U3_galvo_move_XY(XORIGIN - half_size, YORIGIN + half_size, GSPEED, XOFFSET, YOFFSET, THETA)
    wait_for_motion(wrapper)
    
    # Top Right
    wrapper.dll.GT_PROSYS_U3_galvo_move_XY(XORIGIN + half_size, YORIGIN + half_size, GSPEED, XOFFSET, YOFFSET, THETA)
    wait_for_motion(wrapper)
    
    # Bottom Right
    wrapper.dll.GT_PROSYS_U3_galvo_move_XY(XORIGIN + half_size, YORIGIN - half_size, GSPEED, XOFFSET, YOFFSET, THETA)
    wait_for_motion(wrapper)
    
    # Back to Bottom Left to close
    wrapper.dll.GT_PROSYS_U3_galvo_move_XY(XORIGIN - half_size, YORIGIN - half_size, GSPEED, XOFFSET, YOFFSET, THETA)
    wait_for_motion(wrapper)
    print("Square complete.")

def draw_line(wrapper):
    print("Drawing Line...")
    wrapper.dll.GT_PROSYS_U3_galvo_move_XY(XORIGIN + 1000, YORIGIN - 500, GSPEED, XOFFSET, YOFFSET, THETA)
    wait_for_motion(wrapper)
    
    wrapper.dll.GT_PROSYS_U3_galvo_move_XY(XORIGIN + 25000, YORIGIN - 15000, GSPEED, XOFFSET, YOFFSET, THETA)
    wait_for_motion(wrapper)
    print("Line complete.")

def draw_circle_continuous(wrapper, radius=10000):
    print(f"Drawing Circle (radius {radius}) using continuous mode...")
    
    # 0 to 180 degrees
    if hasattr(wrapper.dll, 'GT_PROSYS_U3_set_continous_mode_on'):
        wrapper.dll.GT_PROSYS_U3_set_continous_mode_on()
        
    i = 0.0
    while i < 180.0:
        x2 = int(XORIGIN + (radius * math.sin(i * (3.14 / 180.0))))
        y2 = int(YORIGIN + (radius * math.cos(i * (3.14 / 180.0))))
        wrapper.dll.GT_PROSYS_U3_galvo_move_XY(x2, y2, GSPEED, XOFFSET, YOFFSET, THETA)
        i += 0.5
        
    if hasattr(wrapper.dll, 'GT_PROSYS_U3_set_continous_mode_off'):
        wrapper.dll.GT_PROSYS_U3_set_continous_mode_off()
        
    if hasattr(wrapper.dll, 'GT_PROSYS_U3_buffer_ready'):
        while wrapper.dll.GT_PROSYS_U3_buffer_ready() == 1:
            time.sleep(0.001)

    # 180 to 0 degrees (returning)
    if hasattr(wrapper.dll, 'GT_PROSYS_U3_set_continous_mode_on'):
        wrapper.dll.GT_PROSYS_U3_set_continous_mode_on()
        
    i = 180.0
    while i > 0.0:
        x2 = int(XORIGIN + (radius * math.sin(i * (3.14 / 180.0))))
        y2 = int(YORIGIN + (radius * math.cos(i * (3.14 / 180.0))))
        wrapper.dll.GT_PROSYS_U3_galvo_move_XY(x2, y2, GSPEED, XOFFSET, YOFFSET, THETA)
        i -= 0.5
        
    if hasattr(wrapper.dll, 'GT_PROSYS_U3_set_continous_mode_off'):
        wrapper.dll.GT_PROSYS_U3_set_continous_mode_off()
        
    if hasattr(wrapper.dll, 'GT_PROSYS_U3_buffer_ready'):
        while wrapper.dll.GT_PROSYS_U3_buffer_ready() == 1:
            time.sleep(0.001)
            
    print("Circle complete.")

def main():
    print("Initializing Galvo DLL Wrapper (Python Port)...")
    wrapper = GalvoDLLWrapper()
    wrapper.initialize()
    
    if not wrapper.is_initialized:
        print("Failed to initialize Galvo hardware. Exiting.")
        sys.exit(1)
        
    while True:
        print("\n=== Galvo Test Menu ===")
        print("1. Draw Square (button 7)")
        print("2. Draw Line (button 24)")
        print("3. Draw Circle [Continuous] (button 15)")
        print("4. Exit")
        
        choice = input("Select a test to run: ")
        
        if choice == '1':
            draw_square(wrapper)
        elif choice == '2':
            draw_line(wrapper)
        elif choice == '3':
            draw_circle_continuous(wrapper)
        elif choice == '4':
            print("Closing...")
            wrapper.close()
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
