import sys
import os
import time

# Ensure the Galvo_Studio directory is in the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.dll_wrapper import GalvoDLLWrapper
import core.dll_wrapper

def main():
    print("Initializing Galvo DLL...")
    core.dll_wrapper.HARDWARE_CONNECTED = True
    dll = GalvoDLLWrapper()
    dll.initialize()
    
    if not dll.is_initialized:
        print("Failed to initialize hardware.")
        return

    print("Testing Z-Axis Limit Switch (Pin 19)...")
    print("Press CTRL+C to exit.")
    print("Waiting for signal change...")

    try:
        last_status = -1
        while True:
            # Axis 'Z' is passed to get_home_status
            status = dll.get_home_status('Z')
            
            if status != last_status:
                if status == 1:
                    print(f"[{time.strftime('%H:%M:%S')}] Z-Axis Limit Switch: HIGH (1)")
                elif status == 0:
                    print(f"[{time.strftime('%H:%M:%S')}] Z-Axis Limit Switch: LOW (0)")
                else:
                    print(f"[{time.strftime('%H:%M:%S')}] Z-Axis Limit Switch: Unknown status: {status}")
                last_status = status
                
            time.sleep(0.05) # Poll every 50ms
            
    except KeyboardInterrupt:
        print("\nExiting test...")
    finally:
        dll.close()

if __name__ == "__main__":
    main()
