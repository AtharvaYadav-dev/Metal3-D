import math

class CoordinateConfig:
    def __init__(self):
        # Base Configuration
        self.field_size = 100.0  # mm
        self.offset_x = 0.0      # mm
        self.offset_y = 0.0      # mm
        self.angle = 0.0         # Degrees
        
        # Hardware Axis Mapping (True if Galvo 1 = X)
        self.galvo_1_is_x = True
        
        # Scaling and Negation
        self.negate_x = False
        self.negate_y = False
        self.scale_x = 100.0     # Percentage (100.0 = 1.0)
        self.scale_y = 100.0     # Percentage (100.0 = 1.0)
        
    def apply_transform(self, x_mm, y_mm):
        """
        Takes raw mm coordinates (where 0,0 is center of the design),
        and applies the affine hardware configuration pipeline to convert them
        to absolute Galvo integer units (0 to 65535).
        """
        # 1. Scale
        x = x_mm * (self.scale_x / 100.0)
        y = y_mm * (self.scale_y / 100.0)
        
        # 2. Rotate
        rad = math.radians(self.angle)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)
        x_rot = x * cos_a - y * sin_a
        y_rot = x * sin_a + y * cos_a
        
        # 3. Translate (Offset)
        x = x_rot + self.offset_x
        y = y_rot + self.offset_y
        
        # 4. Invert (Negate)
        if self.negate_x: x = -x
        if self.negate_y: y = -y
        
        # 5. Convert mm to Galvo units (0 to 65535 where 32767 is center)
        galvo_units_per_mm = 65535 / self.field_size
        galvo_x = int(32767 + (x * galvo_units_per_mm))
        galvo_y = int(32767 + (y * galvo_units_per_mm))
        
        # Clamp bounds
        galvo_x = max(0, min(65535, galvo_x))
        galvo_y = max(0, min(65535, galvo_y))
        
        # 6. Axis Mapping (Swap)
        if not self.galvo_1_is_x:
            return galvo_y, galvo_x
        return galvo_x, galvo_y

    def reverse_transform(self, galvo_x, galvo_y):
        """
        Takes absolute Galvo integer units (0 to 65535) and reverses the 
        affine transformation to return the original (X_mm, Y_mm) coordinates.
        """
        if not self.galvo_1_is_x:
            galvo_x, galvo_y = galvo_y, galvo_x
            
        galvo_units_per_mm = 65535 / self.field_size
        x = (galvo_x - 32767) / galvo_units_per_mm
        y = (galvo_y - 32767) / galvo_units_per_mm
        
        if self.negate_x: x = -x
        if self.negate_y: y = -y
        
        x_rot = x - self.offset_x
        y_rot = y - self.offset_y
        
        rad = math.radians(-self.angle)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)
        x_scaled = x_rot * cos_a - y_rot * sin_a
        y_scaled = x_rot * sin_a + y_rot * cos_a
        
        x_mm = x_scaled / (self.scale_x / 100.0)
        y_mm = y_scaled / (self.scale_y / 100.0)
        
        return x_mm, y_mm

# Backwards compatibility wrappers
def mm_to_galvo(mm, field_size=100):
    center_galvo = 32767
    scale = 65535 / field_size
    val = int(center_galvo + (mm * scale))
    return max(0, min(65535, val))

def galvo_to_mm(galvo_val, field_size=100):
    center_galvo = 32767
    scale = field_size / 65535
    return (galvo_val - center_galvo) * scale
