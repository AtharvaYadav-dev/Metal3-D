import xml.etree.ElementTree as ET

tree = ET.parse('metal_dashboard.ui')
root = tree.getroot()

for widget in root.iter('widget'):
    if widget.get('name') == 'page_gcode':
        for child in widget.iter('widget'):
            print(f"Widget: {child.get('class')} name={child.get('name')}")
            if child.get('class') == 'QLabel':
                text_prop = child.find("property[@name='text']/string")
                if text_prop is not None:
                    print(f"  Text: {text_prop.text}")
