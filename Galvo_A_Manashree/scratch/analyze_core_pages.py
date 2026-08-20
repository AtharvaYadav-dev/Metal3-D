import xml.etree.ElementTree as ET

tree = ET.parse('metal_dashboard.ui')
root = tree.getroot()

for page_name in ['page_build_setup', 'page_gcode', 'page_machine_control']:
    for widget in root.iter('widget'):
        if widget.get('name') == page_name:
            print(f"--- {page_name} ---")
            layouts = list(widget.findall('./layout'))
            for l in layouts:
                print(f"Top-level layout: {l.get('class')} name={l.get('name')}")
                if l.get('class') == 'QGridLayout':
                    print("  Row/Col items:")
                    for item in l.findall('item'):
                        print(f"    row={item.get('row')} col={item.get('column')} colspan={item.get('colspan')} rowspan={item.get('rowspan')}")
                elif l.get('class') in ['QVBoxLayout', 'QHBoxLayout']:
                    for item in l.findall('item'):
                        inner_l = item.find('layout')
                        if inner_l is not None:
                            print(f"  Inner layout: {inner_l.get('class')} name={inner_l.get('name')}")
                        else:
                            inner_w = item.find('widget')
                            if inner_w is not None:
                                print(f"  Inner widget: {inner_w.get('class')} name={inner_w.get('name')}")
