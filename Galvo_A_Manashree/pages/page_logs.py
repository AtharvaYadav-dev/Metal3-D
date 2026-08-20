from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class PageLogs(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        lbl = QLabel("PageLogs - UNDER CONSTRUCTION")
        lbl.setObjectName("construction_label")
        lbl.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl)
