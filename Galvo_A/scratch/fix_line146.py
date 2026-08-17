
with open("m.py", "r", encoding="utf-8") as f:
    text = f.read()

bad_snippet = "contours, hatches = self.slicer.slice_mesh_layer(self.mesh, z_height, layer_index=layer)"
idx = text.find(bad_snippet)
if idx != -1:
    end_idx = text.find("polys_to_print =", idx)
    if end_idx != -1:
        text = text[:idx] + "contours, hatches = self.slicer.slice_mesh_layer(self.mesh, z_height, layer_index=layer)\n                        polys_to_print = contours + hatches" + text[end_idx+len("polys_to_print = contours + hatches"):]

with open("m.py", "w", encoding="utf-8") as f:
    f.write(text)

print("[PASS] Fixed line 146 in m.py!")
