
with open("m.py", "r", encoding="utf-8") as f:
    text = f.read()

old_block = """    def home_all_steppers_action():
        print("\\n[Homing] Initiating All Stepper Axes (U, V, Z) Homing Sequence...")
        if stepper_controller:
            stepper_controller.home_u(app_instance=QApplication.instance())
            stepper_controller.home_v(app_instance=QApplication.instance())
            stepper_controller.home_z(app_instance=QApplication.instance())
        else:
            print("[Homing] Stepper controller offline. Resetting all axes to 0.000 mm.")
        update_axis_lcds()"""

new_block = """    def home_all_steppers_action():
        print("\\n[Homing] Initiating Master Homing Sequence for ALL System Axes (U, V, Z & Galvo X/Y)...")
        home_u_action()
        home_v_action()
        home_z_action()
        home_galvo_action()
        update_axis_lcds()"""

if old_block in text:
    text = text.replace(old_block, new_block)
    print("Replaced home_all_steppers_action with comprehensive multi-axis homing sequence!")

with open("m.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated m.py successfully!")
