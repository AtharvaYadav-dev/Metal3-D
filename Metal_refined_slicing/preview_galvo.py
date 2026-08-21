try:
    from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsTextItem
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QPen, QColor, QPainter, QPainterPath, QBrush, QFont
except ImportError:
    print("Warning: PySide6 not installed. Please run: pip install PySide6")
    class QGraphicsView:
        def __init__(self, parent=None): pass
    class QGraphicsScene:
        def __init__(self, parent=None): pass

import math
from core.coordinate_mapper import galvo_to_mm


class GalvoPreviewWidget(QGraphicsView):
    """
    Expert Pro Industrial 2D Galvo Vector Path Preview & Inspection Canvas (HBD Standard).
    Features:
    - 250mm x 250mm HBD Build Envelope Grid & Center Origin Crosshair [0, 0].
    - High-contrast industrial color coding:
      * Part Contours: Electric Cyan (#00f0ff)
      * Part Hatching: Crimson Red (#ff2a6d) [67.0° rotating serpentine]
      * Support Contours: Bright Gold (#ffb703)
      * Support Grid Cross-Hatching: Bright Orange (#fb8500)
    - Live On-Canvas Telemetry HUD: Layer index, Z-height, vector count, path length (m), exposure time (s).
    """
    def __init__(self, config=None, parent=None):
        super().__init__(parent)
        self.config = config

        if 'QGraphicsScene' in globals():
            self.scene = QGraphicsScene(self)
            self.setScene(self.scene)

            self.setRenderHint(QPainter.Antialiasing)
            self.scene.setBackgroundBrush(QColor(18, 19, 26))  # High-contrast dark theme
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
            self._initial_fit_done = False

            field_size = self.config.field_size if self.config else 250.0
            half_field = field_size / 2.0
            self.scene.setSceneRect(-half_field - 10, -half_field - 10, field_size + 20, field_size + 20)

            # Industry Standard Color Pens
            self.part_contour_pen = QPen(QColor(0, 240, 255), 0.35)     # Cyan Blue
            self.part_hatch_pen = QPen(QColor(255, 42, 109), 0.25)      # Crimson Red
            self.supp_contour_pen = QPen(QColor(255, 183, 3), 0.35)     # Bright Gold
            self.supp_hatch_pen = QPen(QColor(251, 133, 0), 0.25)       # Amber Orange
            self.jump_pen = QPen(QColor(100, 100, 120, 100), 0.15, Qt.DashLine)

            # Grid & Axis Pens
            self.grid_pen = QPen(QColor(40, 42, 54, 150), 0.15, Qt.DotLine)
            self.axis_pen = QPen(QColor(0, 240, 255, 180), 0.3, Qt.DashLine)
            self.border_pen = QPen(QColor(0, 150, 255, 200), 0.5)

    def _draw_hbd_grid(self, field_size=250.0):
        """Draws 250mm x 250mm HBD industrial build platform grid & origin crosshairs [0, 0]."""
        half = field_size / 2.0

        # Outer Build Boundary
        self.scene.addRect(-half, -half, field_size, field_size, self.border_pen)

        # 25mm Grid Lines
        step = 25.0
        x = -half + step
        while x < half:
            self.scene.addLine(x, -half, x, half, self.grid_pen)
            x += step

        y = -half + step
        while y < half:
            self.scene.addLine(-half, y, half, y, self.grid_pen)
            y += step

        # Center Axis Crosshairs [0, 0]
        self.scene.addLine(-half, 0, half, 0, self.axis_pen)
        self.scene.addLine(0, -half, 0, half, self.axis_pen)

    def draw_layer_vectors(self, vector_data, z_height=0.0, layer_idx=1):
        """
        Renders categorized vector dictionary and live on-canvas telemetry HUD:
        vector_data = {
            "part_contours": [...],
            "part_hatches": [...],
            "support_contours": [...],
            "support_hatches": [...]
        }
        """
        if not hasattr(self, 'scene'):
            return
        self.scene.clear()

        field_size = self.config.field_size if self.config else 250.0
        self._draw_hbd_grid(field_size=field_size)

        total_vectors = 0
        total_length_mm = 0.0

        def add_polygons(poly_list, pen):
            nonlocal total_vectors, total_length_mm
            if not poly_list:
                return
            path = QPainterPath()
            for poly in poly_list:
                if len(poly) < 2:
                    continue
                path.moveTo(poly[0][0], -poly[0][1])
                for i in range(1, len(poly)):
                    p1, p2 = poly[i-1], poly[i]
                    path.lineTo(p2[0], -p2[1])
                    total_length_mm += math.hypot(p2[0] - p1[0], p2[1] - p1[1])
                    total_vectors += 1
            self.scene.addPath(path, pen)

        if isinstance(vector_data, dict):
            add_polygons(vector_data.get("support_contours", []), self.supp_contour_pen)
            add_polygons(vector_data.get("support_hatches", []), self.supp_hatch_pen)
            add_polygons(vector_data.get("part_contours", []), self.part_contour_pen)
            add_polygons(vector_data.get("part_hatches", []), self.part_hatch_pen)
        elif isinstance(vector_data, list):
            add_polygons(vector_data, self.part_contour_pen)



        if not getattr(self, '_initial_fit_done', False):
            self.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
            self._initial_fit_done = True

    def reset_view(self):
        if hasattr(self, 'scene'):
            self.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    def wheelEvent(self, event):
        zoom_in_factor = 1.15
        zoom_out_factor = 1.0 / zoom_in_factor
        zoom_factor = zoom_in_factor if event.angleDelta().y() > 0 else zoom_out_factor
        self.scale(zoom_factor, zoom_factor)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.reset_view()
        super().mouseDoubleClickEvent(event)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, 'scene') and not getattr(self, '_initial_fit_done', False):
            self.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
