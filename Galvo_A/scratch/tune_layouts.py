import xml.etree.ElementTree as ET

def add_size_policy(element, h_policy="Expanding", v_policy="Expanding"):
    # Check if sizepolicy already exists
    for prop in element.findall('property'):
        if prop.get('name') == 'sizePolicy':
            return
            
    policy_xml = f"""
    <property name="sizePolicy">
        <sizepolicy hsizetype="{h_policy}" vsizetype="{v_policy}">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
        </sizepolicy>
    </property>
    """
    element.append(ET.fromstring(policy_xml))

def tune_layouts():
    file_path = 'metal_dashboard.ui'
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    modified = False
    
    # Iterate through all widgets
    for widget in root.iter('widget'):
        class_name = widget.get('class')
        
        # Make GroupBoxes and Tables expanding
        if class_name in ('QGroupBox', 'QTableWidget', 'QTabWidget', 'QStackedWidget', 'QTextEdit', 'QGraphicsView'):
            add_size_policy(widget, "Expanding", "Expanding")
            modified = True
            
        # Give some minimum sizes to groupboxes to prevent collapse
        if class_name == 'QGroupBox':
            has_min_size = False
            for prop in widget.findall('property'):
                if prop.get('name') == 'minimumSize':
                    has_min_size = True
                    break
            if not has_min_size:
                min_size_xml = """
                <property name="minimumSize">
                    <size>
                        <width>200</width>
                        <height>150</height>
                    </size>
                </property>
                """
                widget.append(ET.fromstring(min_size_xml))
                modified = True

    # Tune layouts (spacing and margins)
    for layout in root.iter('layout'):
        # Just ensure they aren't zero if not specified
        # Actually, let's inject a standard spacing if missing
        has_spacing = False
        for prop in layout.findall('property'):
            if prop.get('name') in ['spacing']:
                has_spacing = True
        
        if not has_spacing:
            spacing_xml = '<property name="spacing"><number>12</number></property>'
            layout.append(ET.fromstring(spacing_xml))
            modified = True

    if modified:
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print("Layouts tuned successfully!")
    else:
        print("No changes needed.")

if __name__ == '__main__':
    tune_layouts()
