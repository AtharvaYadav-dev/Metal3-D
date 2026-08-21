from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QFont, QBrush
from PySide6.QtCore import Qt, QRectF

class CircularGauge(QWidget):
    def __init__(self, parent=None, title="", unit="%", max_val=100.0, color="#3B82F6"):
        super().__init__(parent)
        self.title = title
        self.unit = unit
        self.max_val = max_val
        self.value = 0.0
        self.color = QColor(color)
        self.setMinimumSize(60, 60)
        
    def setValue(self, val):
        self.value = val
        self.update()
        
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        width = self.width()
        height = self.height()
        size = min(width, height) - 10
        if size < 10: return
        
        rect = QRectF((width - size) / 2, (height - size) / 2, size, size)
        
        thickness = max(3, int(size / 10))
        
        # Draw background arc
        pen_bg = QPen(QColor("#1E293B"))
        pen_bg.setWidth(thickness)
        pen_bg.setCapStyle(Qt.RoundCap)
        painter.setPen(pen_bg)
        # Start angle is 3/4 circle: 210 degrees span 240
        start_angle = 210 * 16
        span_angle = -240 * 16
        painter.drawArc(rect, start_angle, span_angle)
        
        # Draw active arc
        pen_fg = QPen(self.color)
        pen_fg.setWidth(thickness)
        pen_fg.setCapStyle(Qt.RoundCap)
        painter.setPen(pen_fg)
        val_span = -240 * (self.value / max(self.max_val, 1)) * 16
        painter.drawArc(rect, start_angle, val_span)
        
        # Draw text
        painter.setPen(QColor("#F8FAFC"))
        val_font_size = max(6, int(size / 5))
        font = QFont("Inter", val_font_size, QFont.Bold)
        painter.setFont(font)
        text_rect = QRectF(rect.x(), rect.y() + size/3 - val_font_size/2, rect.width(), size/2)
        if val_font_size > 6:
            painter.drawText(text_rect, Qt.AlignCenter, f"{self.value:.1f}{self.unit}")
        
        painter.setPen(QColor("#94A3B8"))
        title_font_size = max(5, int(size / 10))
        font = QFont("Inter", title_font_size)
        painter.setFont(font)
        title_rect = QRectF(rect.x(), rect.y() + size/1.6, rect.width(), size/3)
        if title_font_size > 5:
            painter.drawText(title_rect, Qt.AlignCenter, self.title)
        
        painter.end()


class DonutChart(QWidget):
    def __init__(self, parent=None, title="", total_text=""):
        super().__init__(parent)
        self.title = title
        self.total_text = total_text
        self.data = [] # List of tuples: (value, QColor)
        self.setMinimumSize(60, 60)
        
    def setData(self, data, total_text=""):
        self.data = data
        self.total_text = total_text
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        width = self.width()
        height = self.height()
        size = min(width, height) - 10
        if size < 10: return
        
        rect = QRectF((width - size) / 2, (height - size) / 2, size, size)
        thickness = max(3, int(size / 8))
        
        total_val = sum(val for val, _ in self.data)
        
        start_angle = 90 * 16
        
        if total_val == 0:
            # Draw empty gray circle
            pen = QPen(QColor("#1E293B"))
            pen.setWidth(thickness)
            painter.setPen(pen)
            painter.drawEllipse(rect)
        else:
            for val, color in self.data:
                span_angle = -360 * (val / total_val) * 16
                pen = QPen(color)
                pen.setWidth(thickness)
                pen.setCapStyle(Qt.FlatCap)
                painter.setPen(pen)
                painter.drawArc(rect, start_angle, span_angle)
                start_angle += span_angle
                
        # Draw center text
        painter.setPen(QColor("#F8FAFC"))
        val_font_size = max(6, int(size / 5))
        font = QFont("Inter", val_font_size, QFont.Bold)
        painter.setFont(font)
        if val_font_size > 6:
            painter.drawText(rect, Qt.AlignCenter, self.title if self.title else self.total_text)
        
        painter.end()
