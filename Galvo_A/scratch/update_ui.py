import os

def fix_ui_cdata():
    style_file = os.path.join(os.path.dirname(__file__), "..", "style.qss")
    ui_file = os.path.join(os.path.dirname(__file__), "..", "metal_dashboard.ui")

    with open(style_file, "r", encoding="utf-8") as f:
        css = f.read()

    with open(ui_file, "r", encoding="utf-8") as f:
        ui_text = f.read()

    tag_start = '<property name="styleSheet">'
    tag_end = '</property>'

    idx1 = ui_text.find(tag_start)
    idx2 = ui_text.find(tag_end, idx1)

    if idx1 != -1 and idx2 != -1:
        new_text = ui_text[:idx1] + tag_start + '\n  <string><![CDATA[\n' + css + '\n  ]]></string>\n ' + tag_end + ui_text[idx2 + len(tag_end):]
        with open(ui_file, "w", encoding="utf-8") as f:
            f.write(new_text)
        print("Updated metal_dashboard.ui with CDATA CSS wrapper!")

if __name__ == "__main__":
    fix_ui_cdata()
