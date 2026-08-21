import xml.etree.ElementTree as ET

def condense_ui():
    file_path = 'metal_dashboard.ui'
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    modified = False
    
    # Iterate through all widgets and layouts
    for layout in root.iter('layout'):
        for prop in layout.findall('property'):
            if prop.get('name') in ['spacing']:
                # Reduce spacing to 4
                number = prop.find('number')
                if number is not None:
                    number.text = '4'
                    modified = True
            elif prop.get('name') in ['leftMargin', 'rightMargin', 'topMargin', 'bottomMargin']:
                number = prop.find('number')
                if number is not None:
                    number.text = '2'
                    modified = True

    for widget in root.iter('widget'):
        class_name = widget.get('class')
        if class_name == 'QPushButton':
            for prop in widget.findall('property'):
                if prop.get('name') == 'minimumSize':
                    height = prop.find('size/height')
                    if height is not None:
                        height.text = '20' # Reduce button min height
                        modified = True

    if modified:
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print("UI condensed successfully!")
    else:
        print("No changes needed.")

if __name__ == '__main__':
    condense_ui()
