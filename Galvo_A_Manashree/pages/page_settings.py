from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class PageSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        lbl = QLabel("PageSettings - UNDER CONSTRUCTION")
        lbl.setObjectName("construction_label")
        lbl.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl)
