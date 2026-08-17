import xml.etree.ElementTree as ET

file_path = 'metal_dashboard.ui'
tree = ET.parse(file_path)
root = tree.getroot()

modified = False

for widget in root.iter('widget'):
    if widget.get('name') == 'page_build_setup':
        for l in widget.iter('layout'):
            if l.get('name') == 'gridLayout_page2':
                l.set('columnstretch', '3,6,2,2')
                l.set('rowstretch', '6,3')
                modified = True
                
        # Remove min size constraints from placeholders
        for child in widget.iter('widget'):
            if child.get('name') == 'lbl_3d_preview_placeholder':
                for prop in list(child):
                    if prop.tag == 'property' and prop.get('name') == 'minimumSize':
                        child.remove(prop)
                
    elif widget.get('name') == 'page_gcode':
        for l in widget.iter('layout'):
            if l.get('name') == 'gridLayout_page3':
                l.set('columnstretch', '2,6,3')
                modified = True
        
        # Remove min size constraints from graphicsView
        for child in widget.iter('widget'):
            if child.get('name') == 'graphicsView_layer':
                for prop in list(child):
                    if prop.tag == 'property' and prop.get('name') == 'minimumSize':
                        child.remove(prop)
                        
    elif widget.get('name') == 'page_machine_control':
        for l in widget.iter('layout'):
            if l.get('name') == 'vLayout_page_mc':
                l.set('stretch', '3,2,1')
                modified = True

if modified:
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print("Successfully added layout stretch properties to core pages.")
else:
    print("No changes made.")
