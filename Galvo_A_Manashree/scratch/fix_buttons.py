import xml.etree.ElementTree as ET

def fix_buttons():
    file_path = 'metal_dashboard.ui'
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    modified = False
    
    # Iterate through all widgets
    for widget in root.iter('widget'):
        class_name = widget.get('class')
        
        # Remove minimumSize from QGroupBox if we added it, it might be messing up proportions
        if class_name == 'QGroupBox':
            for prop in list(widget.findall('property')):
                if prop.get('name') == 'minimumSize':
                    widget.remove(prop)
                    modified = True
                    
        # Give QPushButtons a solid minimum height directly in XML
        if class_name == 'QPushButton':
            has_min = False
            for prop in widget.findall('property'):
                if prop.get('name') == 'minimumSize':
                    has_min = True
            if not has_min:
                min_size_xml = """
                <property name="minimumSize">
                    <size>
                        <width>0</width>
                        <height>30</height>
                    </size>
                </property>
                """
                widget.append(ET.fromstring(min_size_xml))
                modified = True

    if modified:
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print("Buttons fixed successfully!")
    else:
        print("No changes needed.")

if __name__ == '__main__':
    fix_buttons()
