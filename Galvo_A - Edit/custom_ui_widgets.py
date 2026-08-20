import math
from PySide6.QtCore import Qt, QRectF, QPropertyAnimation, Property, QEasingCurve, QSize, QPointF, Signal
from PySide6.QtGui import QPainter, QColor, QPen, QFont, QBrush, QConicalGradient, QLinearGradient, QPainterPath
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton, QHBoxLayout

# Shared Modern Colors
BG_MAIN = "#0B0F19"
BG_CARD = "#111827"
TEXT_MAIN = "#F9FAFB"
TEXT_MUTED = "#6B7280"
ACCENT_BLUE = "#3B82F6"
ACCENT_GREEN = "#10B981"
BORDER_COLOR = "#2D323F"

class CircularProgressWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 0
        self._max = 100
        self._color = QColor(ACCENT_BLUE)
        self.setMinimumSize(100, 100)

    @Property(int)
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        self.update()
        
    def setColor(self, color):
        if isinstance(color, str):
            self._color = QColor(color)
        else:
            self._color = color
        self.update()

    def setMaxValue(self, m):
        self._max = m
        self.update()

    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        margin = 15
        rect = QRectF(margin, margin, width - margin * 2, height - margin * 2)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw outer thin track
        pen_bg = QPen(QColor(30, 40, 55), 4)
        painter.setPen(pen_bg)
        painter.drawEllipse(rect)

        # Draw active arc
        if self._max > 0:
            span_angle = int(- (self._value / self._max) * 360 * 16)
        else:
            span_angle = 0
            
        # Draw glow
        glow_color = QColor(self._color)
        for i in range(1, 5):
            glow_color.setAlpha(int(60 / i))
            pen_glow = QPen(glow_color, 8 + (i * 3))
            pen_glow.setCapStyle(Qt.RoundCap)
            painter.setPen(pen_glow)
            painter.drawArc(rect, 90 * 16, span_angle)
            
        pen_fg = QPen(self._color, 8)
        pen_fg.setCapStyle(Qt.RoundCap)
        painter.setPen(pen_fg)
        
        # Start at 90 degrees (top)
        painter.drawArc(rect, 90 * 16, span_angle)

        # Draw text
        painter.setPen(QColor(TEXT_MAIN))
        font = QFont("Inter", 18, QFont.Bold)
        painter.setFont(font)
        text = f"{self._value}%"
        painter.drawText(rect, Qt.AlignCenter, text)

        painter.end()


class GaugeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 0
        self._max = 500
        self._unit = "W"
        self._color = QColor(ACCENT_BLUE)
        self.setMinimumSize(180, 140)
        
    @Property(int)
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        self.update()

    def setProperties(self, max_val, unit, color):
        self._max = max_val
        self._unit = unit
        if isinstance(color, str):
            self._color = QColor(color)
        else:
            self._color = color
        self.update()

    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        margin = 25
        
        size = min(width, height * 1.5)
        rect = QRectF((width - size) / 2 + margin, margin, size - margin * 2, size - margin * 2)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        start_angle = 225
        span_angle = -270

        # Draw Tick Marks
        painter.save()
        painter.translate(rect.center())
        num_ticks = 40
        radius = size / 2 - 5
        tick_pen = QPen(QColor(40, 50, 70), 2)
        painter.setPen(tick_pen)
        
        for i in range(num_ticks + 1):
            angle = start_angle + (i / num_ticks) * span_angle
            rad = math.radians(angle)
            x1 = math.cos(rad) * radius
            y1 = -math.sin(rad) * radius
            x2 = math.cos(rad) * (radius - 8)
            y2 = -math.sin(rad) * (radius - 8)
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))
        painter.restore()

        # Draw Background Track Arc
        arc_rect = rect.adjusted(10, 10, -10, -10)
        pen_bg = QPen(QColor(30, 40, 55), 14)
        pen_bg.setCapStyle(Qt.RoundCap)
        painter.setPen(pen_bg)
        painter.drawArc(arc_rect, start_angle * 16, span_angle * 16)

        # Draw Foreground Arc with Gradient
        if self._max > 0:
            val_span = (-self._value / self._max) * 270
        else:
            val_span = 0
            
        gradient = QConicalGradient(arc_rect.center(), -90)
        gradient.setColorAt(0, self._color)
        gradient.setColorAt(1, self._color.lighter(150))
        
        # Draw glow
        glow_color = QColor(self._color)
        for i in range(1, 4):
            glow_color.setAlpha(int(60 / i))
            pen_glow = QPen(glow_color, 14 + (i * 4))
            pen_glow.setCapStyle(Qt.RoundCap)
            painter.setPen(pen_glow)
            painter.drawArc(arc_rect, start_angle * 16, int(val_span * 16))
            
        pen_fg = QPen(QBrush(gradient), 14)
        pen_fg.setCapStyle(Qt.RoundCap)
        painter.setPen(pen_fg)
        painter.drawArc(arc_rect, start_angle * 16, int(val_span * 16))

        # Main Value Text
        painter.setPen(QColor(TEXT_MAIN))
        font = QFont("Inter", 28, QFont.Bold)
        painter.setFont(font)
        
        text_rect = QRectF(rect.x(), rect.y() + rect.height() / 3, rect.width(), rect.height() / 2)
        painter.drawText(text_rect, Qt.AlignCenter, f"{self._value}")
        
        # Unit Text (Below Value)
        painter.setPen(QColor(TEXT_MUTED))
        font_unit = QFont("Inter", 12)
        painter.setFont(font_unit)
        unit_rect = text_rect.translated(0, 30)
        painter.drawText(unit_rect, Qt.AlignCenter, f"Set: 200 {self._unit}")
        
        # Min / Max Text
        font_small = QFont("Inter", 11)
        painter.setFont(font_small)
        
        painter.drawText(rect.x() + 10, rect.y() + rect.height() - 10, "0")
        painter.drawText(rect.x() + rect.width() - 40, rect.y() + rect.height() - 10, str(self._max))

        painter.end()


class JogWidget(QWidget):
    sigJog = Signal(str, float)  # axis, direction_sign
    sigHome = Signal(str)        # axis ('XY' or 'Z')
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(220, 160)
        
        layout = QGridLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {BG_MAIN};
                color: {TEXT_MAIN};
                border: 1px solid #2D323F;
                border-radius: 6px;
                font-weight: bold;
                font-size: 11px;
                min-width: 45px;
                min-height: 45px;
            }}
            QPushButton:hover {{
                background-color: {ACCENT_BLUE};
                border: 1px solid {ACCENT_BLUE};
            }}
        """)
        
        # Center Home Button
        btn_home = QPushButton("⌂\nXY")
        layout.addWidget(btn_home, 1, 1)
        
        # Directional Arrows
        btn_up = QPushButton("↑\n+Y")
        layout.addWidget(btn_up, 0, 1)
        
        btn_down = QPushButton("↓\n-Y")
        layout.addWidget(btn_down, 2, 1)
        
        btn_left = QPushButton("←\n-X")
        layout.addWidget(btn_left, 1, 0)
        
        btn_right = QPushButton("→\n+X")
        layout.addWidget(btn_right, 1, 2)
        
        # Z Controls Spacer
        layout.setColumnMinimumWidth(3, 10)
        
        # Z Controls
        btn_z_up = QPushButton("+Z\n↑")
        layout.addWidget(btn_z_up, 0, 4)
        
        btn_z_mid = QPushButton("⌂\nZ")
        layout.addWidget(btn_z_mid, 1, 4)
        
        btn_z_down = QPushButton("-Z\n↓")
        layout.addWidget(btn_z_down, 2, 4)
        
        # Connect signals
        btn_home.clicked.connect(lambda: self.sigHome.emit('XY'))
        btn_z_mid.clicked.connect(lambda: self.sigHome.emit('Z'))
        
        btn_up.clicked.connect(lambda: self.sigJog.emit('Y', 1.0))
        btn_down.clicked.connect(lambda: self.sigJog.emit('Y', -1.0))
        btn_left.clicked.connect(lambda: self.sigJog.emit('X', -1.0))
        btn_right.clicked.connect(lambda: self.sigJog.emit('X', 1.0))
        btn_z_up.clicked.connect(lambda: self.sigJog.emit('Z', 1.0))
        btn_z_down.clicked.connect(lambda: self.sigJog.emit('Z', -1.0))


from PySide6.QtWidgets import QSlider, QHBoxLayout

class LayerControlWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(15)
        
        # Top label row
        top_layout = QHBoxLayout()
        lbl_title = QLabel("LAYER CONTROL")
        lbl_title.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 11px; font-weight: bold;")
        lbl_val = QLabel("245 / 1250")
        lbl_val.setStyleSheet(f"color: {TEXT_MAIN}; font-size: 11px;")
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        top_layout.addWidget(lbl_val)
        self.layout.addLayout(top_layout)
        
        # Slider row
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setStyleSheet(f"""
            QSlider::groove:horizontal {{
                border-radius: 2px;
                height: 4px;
                background: {BG_MAIN};
            }}
            QSlider::handle:horizontal {{
                background: {ACCENT_BLUE};
                width: 14px;
                height: 14px;
                margin: -5px 0;
                border-radius: 7px;
            }}
            QSlider::sub-page:horizontal {{
                background: {ACCENT_BLUE};
                border-radius: 2px;
            }}
        """)
        self.slider.setRange(1, 1250)
        self.slider.setValue(245)
        self.layout.addWidget(self.slider)
        
        # Buttons row
        self.btn_layout = QHBoxLayout()
        self.btn_layout.setSpacing(10)
        for val in ["-10", "-1", "+1", "+10"]:
            btn = QPushButton(val)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {BG_MAIN};
                    color: {TEXT_MAIN};
                    border: 1px solid {BORDER_COLOR};
                    border-radius: 4px;
                    padding: 8px;
                    font-weight: bold;
                }}
                QPushButton:hover {{
                    border: 1px solid {ACCENT_BLUE};
                    color: {ACCENT_BLUE};
                }}
            """)
            self.btn_layout.addWidget(btn)
        self.layout.addLayout(self.btn_layout)
        
        # Go to Layer button
        self.go_btn = QPushButton("Go to Layer")
        self.go_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                color: {TEXT_MAIN};
                border: 1px solid {BORDER_COLOR};
                border-radius: 4px;
                padding: 10px;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: {BORDER_COLOR};
            }}
        """)
        self.layout.addWidget(self.go_btn)
