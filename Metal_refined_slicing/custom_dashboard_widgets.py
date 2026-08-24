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


class PowderChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model_height = 42.17
        self.powder_bay_depth = 84.80
        self.powder_kg = 31.90
        self.powder_name = "316L Stainless Steel"
        self.max_model_height = 130.0
        self.max_powder_bay = 250.0
        self.min_powder_bay = 10.0
        self.setMinimumSize(180, 140)

    def set_data(self, model_h, bay_depth, kg, powder_name="316L Stainless Steel"):
        self.model_height = float(model_h)
        self.powder_bay_depth = float(bay_depth)
        self.powder_kg = float(kg)
        self.powder_name = str(powder_name)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()

        # Background
        painter.fillRect(0, 0, w, h, QColor("#0d0e14"))
        painter.setPen(QPen(QColor("#2d3142"), 1))
        painter.drawRect(0, 0, w - 1, h - 1)

        # Margins for axes
        pad_l = 38
        pad_r = 15
        pad_t = 22
        pad_b = 25

        pw = w - pad_l - pad_r
        ph = h - pad_t - pad_b

        if pw < 20 or ph < 20:
            painter.end()
            return

        # Title
        painter.setPen(QColor("#b8c4ff"))
        font_title = QFont("JetBrains Mono", 8, QFont.Bold)
        painter.setFont(font_title)
        painter.drawText(pad_l, 14, f"POWDER BAY DEPTH VS MODEL HEIGHT ({self.powder_name})")

        # Grid lines
        painter.setPen(QPen(QColor("#1e2230"), 1, Qt.DashLine))
        for y_step in range(0, 251, 50):
            y_pos = pad_t + ph - (y_step / 250.0) * ph
            painter.drawLine(pad_l, y_pos, pad_l + pw, y_pos)

        for x_step in range(0, 131, 30):
            x_pos = pad_l + (x_step / 130.0) * pw
            painter.drawLine(x_pos, pad_t, x_pos, pad_t + ph)

        # Draw Axis Labels
        painter.setPen(QColor("#6c7293"))
        font_axis = QFont("JetBrains Mono", 7)
        painter.setFont(font_axis)

        # Y-axis labels
        painter.drawText(4, pad_t + 4, "250mm")
        painter.drawText(4, pad_t + ph / 2 + 4, "125mm")
        painter.drawText(4, pad_t + ph - 2, "10mm")

        # X-axis labels
        painter.drawText(pad_l - 6, h - 6, "0")
        painter.drawText(pad_l + pw / 2 - 12, h - 6, "65mm")
        painter.drawText(pad_l + pw - 28, h - 6, "130mm")

        # Plot Trend Line (10mm depth @ 4.97mm model height to 250mm depth @ 124.33mm model height)
        x1 = pad_l + (4.97 / 130.0) * pw
        y1 = pad_t + ph - (10.0 / 250.0) * ph
        x2 = pad_l + (124.33 / 130.0) * pw
        y2 = pad_t + ph - (250.0 / 250.0) * ph

        pen_line = QPen(QColor("#00f0ff"))
        pen_line.setWidth(2)
        painter.setPen(pen_line)
        painter.drawLine(int(x1), int(y1), int(x2), int(y2))

        # Active Data Point
        curr_x = pad_l + (min(self.model_height, 130.0) / 130.0) * pw
        curr_y = pad_t + ph - (min(self.powder_bay_depth, 250.0) / 250.0) * ph

        # Outer glow
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor(236, 106, 6, 90)))
        painter.drawEllipse(QRectF(curr_x - 7, curr_y - 7, 14, 14))

        # Inner dot
        painter.setBrush(QBrush(QColor("#ffb690")))
        painter.drawEllipse(QRectF(curr_x - 3.5, curr_y - 3.5, 7, 7))

        # Text banner for current point
        painter.setPen(QColor("#ffb690"))
        font_callout = QFont("JetBrains Mono", 8, QFont.Bold)
        painter.setFont(font_callout)
        callout_str = f"Depth: {self.powder_bay_depth:.1f} mm | Req: {self.powder_kg:.2f} kg"
        painter.drawText(int(w - 210), int(pad_t + 16), callout_str)

        painter.end()

