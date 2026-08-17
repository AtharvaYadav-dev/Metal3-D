
with open("m.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(len(lines)):
    if "Solidifying Layer" in lines[i]:
        lines[i] = "                        f\"[LPBF SLICER] Solidifying Layer {layer}/{self.total_layers} at Z={z_height:.3f} mm (67 deg Hatch Angle: {angle_deg:.1f} deg)...\",\n"

with open("m.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("[PASS] Fixed m.py syntax!")
