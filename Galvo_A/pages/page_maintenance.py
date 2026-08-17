from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class PageMaintenance(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        lbl = QLabel("PageMaintenance - UNDER CONSTRUCTION")
        lbl.setStyleSheet("color: #8A92A3; font-size: 24px; font-weight: bold;")
        lbl.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl)
