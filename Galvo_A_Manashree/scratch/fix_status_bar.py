import xml.etree.ElementTree as ET

def fix_status_bar():
    file_path = 'metal_dashboard.ui'
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    modified = False
    
    # Find the statusBarFrame
    status_frame = None
    for widget in root.iter('widget'):
        if widget.get('name') == 'statusBarFrame':
            status_frame = widget
            break
            
    if not status_frame:
        print("Could not find statusBarFrame")
        return
        
    for label in status_frame.findall('.//widget[@class="QLabel"]'):
        # Add textFormat property if it doesn't exist
        has_format = False
        for prop in label.findall('property'):
            if prop.get('name') == 'textFormat':
                has_format = True
                break
                
        if not has_format:
            format_xml = """
            <property name="textFormat">
             <enum>Qt::RichText</enum>
            </property>
            """
            label.append(ET.fromstring(format_xml))
            modified = True
            
        # Also convert the text to full HTML just in case
        for prop in label.findall('property'):
            if prop.get('name') == 'text':
                string_elem = prop.find('string')
                if string_elem is not None and string_elem.text:
                    if not string_elem.text.strip().startswith('<html>'):
                        string_elem.text = '<html><body>' + string_elem.text.replace('\n', '<br>') + '</body></html>'
                        modified = True

    if modified:
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print("Status bar fixed successfully!")
    else:
        print("No changes needed.")

if __name__ == '__main__':
    fix_status_bar()
