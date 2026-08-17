import sys
import os

# Ensure the Galvo_Studio directory is in the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from PySide6.QtWidgets import QApplication
except ImportError:
    print("PySide6 is required for the GUI. Please install it using:")
    print("pip install PySide6 svgpathtools")
    sys.exit(1)

from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Optional: Apply a simple dark style or aesthetic enhancements here
    app.setStyle("Fusion")
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
