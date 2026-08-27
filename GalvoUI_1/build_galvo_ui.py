import xml.etree.ElementTree as ET

def get_property(name, value_type, value_text):
    prop = ET.Element("property", name=name)
    val = ET.SubElement(prop, value_type)
    val.text = value_text
    return prop

def create_widget(w_class, w_name):
    w = ET.Element("widget", {"class": w_class, "name": w_name})
    return w

def create_layout(l_class, l_name):
    l = ET.Element("layout", {"class": l_class, "name": l_name})
    return l

def create_item():
    return ET.Element("item")

tree = ET.parse("interface.ui")
root = tree.getroot()

for widget in root.iter("widget"):
    if widget.get("name") == "configgalvoPage":
        configgalvoPage = widget
        break
else:
    print("Could not find configgalvoPage")
    exit(1)

for child in list(configgalvoPage):
    if child.tag in ("widget", "layout", "item"):
        configgalvoPage.remove(child)

main_layout = create_layout("QVBoxLayout", "configGalvoMainLayout")
configgalvoPage.append(main_layout)

tab_item = create_item()
main_layout.append(tab_item)
tab_widget = create_widget("QTabWidget", "configGalvoTabWidget")
tab_item.append(tab_widget)
tab_widget.append(get_property("currentIndex", "number", "0"))

tabs = ["Field", "Laser Control", "Port", "Other", "Hardware info"]
for idx, tab_name in enumerate(tabs):
    tab_page = create_widget("QWidget", f"configGalvoTab_{idx}")
    tab_widget.append(tab_page)
    
    attr = ET.Element("attribute", name="title")
    string_val = ET.SubElement(attr, "string")
    string_val.text = tab_name
    tab_page.append(attr)
    
    if tab_name == "Field":
        field_layout = create_layout("QGridLayout", "configGalvoFieldLayout")
        tab_page.append(field_layout)
        
        gb_aspect = create_widget("QGroupBox", "gbAspect")
        gb_aspect.append(get_property("title", "string", "Aspect"))
        aspect_layout = create_layout("QGridLayout", "layoutAspect")
        gb_aspect.append(aspect_layout)
        
        def add_form_row(layout, row, label_text, widget_name, suffix=None):
            lbl_item = create_item()
            lbl_item.set("row", str(row))
            lbl_item.set("column", "0")
            lbl = create_widget("QLabel", f"lbl_{widget_name}")
            lbl.append(get_property("text", "string", label_text))
            lbl_item.append(lbl)
            layout.append(lbl_item)
            
            le_item = create_item()
            le_item.set("row", str(row))
            le_item.set("column", "1")
            le = create_widget("QLineEdit", widget_name)
            le_item.append(le)
            layout.append(le_item)
            
            if suffix:
                suf_item = create_item()
                suf_item.set("row", str(row))
                suf_item.set("column", "2")
                suf = create_widget("QLabel", f"suf_{widget_name}")
                suf.append(get_property("text", "string", suffix))
                suf_item.append(suf)
                layout.append(suf_item)
        
        add_form_row(aspect_layout, 0, "Field size", "config_field_size", "MM")
        add_form_row(aspect_layout, 1, "Offset X", "config_offset_x", "MM")
        add_form_row(aspect_layout, 2, "Offset Y", "config_offset_y", "MM")
        add_form_row(aspect_layout, 3, "Angle", "config_angle", "Degree")
        
        chk_item = create_item()
        chk_item.set("row", "4")
        chk_item.set("column", "0")
        chk_item.set("colspan", "2")
        chk = create_widget("QCheckBox", "config_use_corfile")
        chk.append(get_property("text", "string", "Use the correction file"))
        chk_item.append(chk)
        aspect_layout.append(chk_item)
        
        le_cor_item = create_item()
        le_cor_item.set("row", "5")
        le_cor_item.set("column", "0")
        le_cor_item.set("colspan", "2")
        le_cor = create_widget("QLineEdit", "config_corfile_path")
        le_cor_item.append(le_cor)
        aspect_layout.append(le_cor_item)
        
        btn_cor_item = create_item()
        btn_cor_item.set("row", "5")
        btn_cor_item.set("column", "2")
        btn_cor = create_widget("QPushButton", "config_corfile_btn")
        btn_cor.append(get_property("text", "string", ">>"))
        btn_cor_item.append(btn_cor)
        aspect_layout.append(btn_cor_item)
        
        rad1_item = create_item()
        rad1_item.set("row", "1")
        rad1_item.set("column", "3")
        rad1 = create_widget("QRadioButton", "config_galvo1_x")
        rad1.append(get_property("text", "string", "Galvo1=X"))
        rad1.append(get_property("checked", "bool", "true"))
        rad1_item.append(rad1)
        aspect_layout.append(rad1_item)
        
        rad2_item = create_item()
        rad2_item.set("row", "2")
        rad2_item.set("column", "3")
        rad2 = create_widget("QRadioButton", "config_galvo2_x")
        rad2.append(get_property("text", "string", "Galvo2=X"))
        rad2_item.append(rad2)
        aspect_layout.append(rad2_item)
        
        item_gb_aspect = create_item()
        item_gb_aspect.set("row", "0")
        item_gb_aspect.set("column", "0")
        item_gb_aspect.set("colspan", "2")
        item_gb_aspect.append(gb_aspect)
        field_layout.append(item_gb_aspect)
        
        def create_galvo_gb(title, prefix):
            gb = create_widget("QGroupBox", f"gb{prefix}")
            gb.append(get_property("title", "string", title))
            layout = create_layout("QGridLayout", f"layout{prefix}")
            gb.append(layout)
            
            chk_neg_item = create_item()
            chk_neg_item.set("row", "0")
            chk_neg_item.set("column", "0")
            chk_neg_item.set("colspan", "2")
            chk_neg = create_widget("QCheckBox", f"config_{prefix}_negate")
            chk_neg.append(get_property("text", "string", "Negate"))
            chk_neg_item.append(chk_neg)
            layout.append(chk_neg_item)
            
            add_form_row(layout, 1, "Scale", f"config_{prefix}_scale")
            btn_scale_item = create_item()
            btn_scale_item.set("row", "1")
            btn_scale_item.set("column", "2")
            btn_scale = create_widget("QPushButton", f"btn_{prefix}_scale")
            btn_scale.append(get_property("text", "string", ">>"))
            btn_scale_item.append(btn_scale)
            layout.append(btn_scale_item)
            
            add_form_row(layout, 2, "Barrel/Bulge", f"config_{prefix}_bulge")
            add_form_row(layout, 3, "Parallelogram", f"config_{prefix}_skew")
            add_form_row(layout, 4, "Trapezoid", f"config_{prefix}_trapezoid")
            return gb
            
        gb_g1 = create_galvo_gb("Galvo 1", "g1")
        item_gb_g1 = create_item()
        item_gb_g1.set("row", "1")
        item_gb_g1.set("column", "0")
        item_gb_g1.append(gb_g1)
        field_layout.append(item_gb_g1)
        
        gb_g2 = create_galvo_gb("Galvo 2", "g2")
        item_gb_g2 = create_item()
        item_gb_g2.set("row", "1")
        item_gb_g2.set("column", "1")
        item_gb_g2.append(gb_g2)
        field_layout.append(item_gb_g2)
        
        gb_pos = create_widget("QGroupBox", "gbPosAfterMark")
        gb_pos.append(get_property("title", "string", "Go to pos. after Mark"))
        pos_layout = create_layout("QVBoxLayout", "layoutPosAfterMark")
        gb_pos.append(pos_layout)
        
        radios = ["No Movement", "Galvo Center", "Top Left", "Top Right", "Bottom Right", "Bottom Left", "Special pos."]
        for r_name in radios:
            r_item = create_item()
            r_id = r_name.replace(" ", "").replace(".", "")
            r = create_widget("QRadioButton", f"config_pos_{r_id}")
            r.append(get_property("text", "string", r_name))
            if r_name == "No Movement":
                r.append(get_property("checked", "bool", "true"))
            r_item.append(r)
            pos_layout.append(r_item)
            
        sp_layout_item = create_item()
        sp_layout = create_layout("QGridLayout", "layoutSpecialPos")
        sp_layout_item.append(sp_layout)
        pos_layout.append(sp_layout_item)
        
        def add_sp_row(layout, row, lbl, name):
            item_l = create_item()
            item_l.set("row", str(row))
            item_l.set("column", "0")
            label = create_widget("QLabel", f"lbl_sp_{name}")
            label.append(get_property("text", "string", lbl))
            item_l.append(label)
            layout.append(item_l)
            
            item_e = create_item()
            item_e.set("row", str(row))
            item_e.set("column", "1")
            le = create_widget("QLineEdit", f"config_sp_{name}")
            item_e.append(le)
            layout.append(item_e)
            
        add_sp_row(sp_layout, 0, "X", "x")
        add_sp_row(sp_layout, 1, "Y", "y")
        
        item_gb_pos = create_item()
        item_gb_pos.set("row", "0")
        item_gb_pos.set("column", "2")
        item_gb_pos.set("rowspan", "2")
        item_gb_pos.append(gb_pos)
        field_layout.append(item_gb_pos)

btn_layout_item = create_item()
btn_layout = create_layout("QHBoxLayout", "configGalvoBtnLayout")
btn_layout_item.append(btn_layout)
main_layout.append(btn_layout_item)

spacer_item = create_item()
spacer = ET.Element("spacer", {"name": "horizontalSpacer_configGalvo"})
spacer.append(get_property("orientation", "enum", "Qt::Horizontal"))
sizeHint = ET.Element("property", name="sizeHint")
sizeHint.set("stdset", "0")
size = ET.SubElement(sizeHint, "size")
w = ET.SubElement(size, "width")
w.text = "40"
h = ET.SubElement(size, "height")
h.text = "20"
spacer.append(sizeHint)
spacer_item.append(spacer)
btn_layout.append(spacer_item)

for b_name in ["OK", "Cancel", "Apply"]:
    b_item = create_item()
    b = create_widget("QPushButton", f"config_btn_{b_name.lower()}")
    b.append(get_property("text", "string", b_name))
    b_item.append(b)
    btn_layout.append(b_item)

ET.indent(tree, space="  ", level=0)
tree.write("interface.ui", encoding="utf-8", xml_declaration=True)
print("Updated interface.ui successfully.")
