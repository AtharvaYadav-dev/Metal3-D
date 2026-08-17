
with open("m.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("Full Sweep Cycle (300mm)", "Home Recoater (Z)")

# update click logic
old_code = "recoater_sweep.clicked.connect(lambda checked=False: (stepper_controller.move_z_relative(300.0) if stepper_controller else None, time.sleep(1.0), stepper_controller.move_z_relative(-300.0) if stepper_controller else None, update_axis_lcds()))"
new_code = "recoater_sweep.setText(\"Home Recoater (Z)\")\n        recoater_sweep.clicked.connect(lambda checked=False: home_z_action())"

if old_code in text:
    text = text.replace(old_code, new_code)
    print("Replaced sweep click logic with home_z_action!")

with open("m.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated m.py successfully!")
