import xml.etree.ElementTree as ET

def list_pages():
    file_path = 'metal_dashboard.ui'
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Find stackedWidget
    stacked = None
    for widget in root.iter('widget'):
        if widget.get('name') == 'stackedWidget':
            stacked = widget
            break
            
    if not stacked:
        print("No stackedWidget found")
        return
        
    for child in stacked.findall('widget'):
        print(child.get('name'))

if __name__ == '__main__':
    list_pages()
