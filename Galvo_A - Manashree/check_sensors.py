import time
import sys
from core.connection.hardware import HardwareConnection

def show_sensor_status():
    print("Connecting to hardware control card...")
    hw = HardwareConnection()
    res, cards = hw.initialize()
    if not hw.is_initialized:
        print("Hardware connection failed (or in mock mode).")
        return

    print("\n=========================================")
    print(" INDUCTIVE PROXIMITY SENSOR STATUS ")
    print("=========================================")
    # For NPN NO sensors with pull-ups, 0 = TRIGGERED (GND), 1 = NOT TRIGGERED (+24V/+5V)
    for axis in ['Z', 'U', 'V', 'X', 'Y']:
        status = hw.get_home_status(axis)
        state_str = "TRIGGERED (CLOSED)" if status == 0 else "NOT TRIGGERED (OPEN)"
        print(f"  {axis}_org ({axis} Axis) : {state_str} [Value: {status}]")
    print("=========================================\n")

if __name__ == "__main__":
    show_sensor_status()
