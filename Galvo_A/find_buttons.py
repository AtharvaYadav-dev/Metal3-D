import xml.etree.ElementTree as ET

try:
    tree = ET.parse('d:/Atharva/Metal_3D/Galvo_A/metal_dashboard.ui')
    root = tree.getroot()
    buttons = []
    for widget in root.iter('widget'):
        if widget.get('class') == 'QPushButton':
            buttons.append(widget.get('name'))
    
    with open('d:/Atharva/Metal_3D/Galvo_A/buttons.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(buttons))
    print("Done")
except Exception as e:
    print(f"Error: {e}")
