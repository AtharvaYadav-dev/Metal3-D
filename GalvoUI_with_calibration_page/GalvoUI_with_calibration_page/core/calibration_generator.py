import struct
import math

def interp1d(x, W, v_neg, v_0, v_pos):
    """Quadratic interpolation for 3 points: -W, 0, W"""
    if W == 0: return v_0
    a = (v_pos + v_neg - 2.0 * v_0) / (2.0 * W * W)
    b = (v_pos - v_neg) / (2.0 * W)
    return a * (x**2) + b * x + v_0

def interp2d(x, y, W_x, W_y, v_grid):
    """
    Biquadratic interpolation.
    v_grid is a 3x3 array:
    [[v_top_left, v_top_mid, v_top_right],
     [v_mid_left, v_center,  v_mid_right],
     [v_bot_left, v_bot_mid, v_bot_right]]
    """
    v_top = interp1d(x, W_x, v_grid[0][0], v_grid[0][1], v_grid[0][2])
    v_mid = interp1d(x, W_x, v_grid[1][0], v_grid[1][1], v_grid[1][2])
    v_bot = interp1d(x, W_x, v_grid[2][0], v_grid[2][1], v_grid[2][2])
    
    return interp1d(y, W_y, v_bot, v_mid, v_top)

def calculate_analytical_parameters(W, measured_points, current_g1_scale=100.0, current_g2_scale=100.0, galvo_1_is_x=False):
    """
    Calculates EZCAD-standard optical distortion parameters from the 9 measured points:
    measured_points: 9 (x, y) tuples ordered:
      0: Top-Left (-W, +W)
      1: Top-Mid (0, +W)
      2: Top-Right (+W, +W)
      3: Mid-Left (-W, 0)
      4: Center (0, 0)
      5: Mid-Right (+W, 0)
      6: Bot-Left (-W, -W)
      7: Bot-Mid (0, -W)
      8: Bot-Right (+W, -W)
    """
    nom_dim = 2.0 * W
    if nom_dim <= 0:
        nom_dim = 100.0

    # Measured widths (X spans)
    w_mid = abs(measured_points[5][0] - measured_points[3][0])
    w_top = abs(measured_points[2][0] - measured_points[0][0])
    w_bot = abs(measured_points[8][0] - measured_points[6][0])
    w_avg = (w_mid * 2.0 + w_top + w_bot) / 4.0 if (w_mid + w_top + w_bot) > 0 else nom_dim

    # Measured heights (Y spans)
    h_mid = abs(measured_points[1][1] - measured_points[7][1])
    h_left = abs(measured_points[0][1] - measured_points[6][1])
    h_right = abs(measured_points[2][1] - measured_points[8][1])
    h_avg = (h_mid * 2.0 + h_left + h_right) / 4.0 if (h_mid + h_left + h_right) > 0 else nom_dim

    # 1. Scale multipliers
    scale_mult_x = nom_dim / w_avg if w_avg > 0 else 1.0
    scale_mult_y = nom_dim / h_avg if h_avg > 0 else 1.0

    # 2. Trapezoid (Keystone)
    trap_x = 1.0 + ((w_top - w_bot) / (2.0 * w_avg)) if w_avg > 0 else 1.0
    trap_y = 1.0 + ((h_right - h_left) / (2.0 * h_avg)) if h_avg > 0 else 1.0

    # 3. Parallelogram (Skew)
    x_shift_top = measured_points[1][0] - measured_points[4][0]
    x_shift_bot = measured_points[7][0] - measured_points[4][0]
    skew_x = 1.0 + ((x_shift_top - x_shift_bot) / nom_dim)

    y_shift_right = measured_points[5][1] - measured_points[4][1]
    y_shift_left = measured_points[3][1] - measured_points[4][1]
    skew_y = 1.0 + ((y_shift_right - y_shift_left) / nom_dim)

    # 4. Bulge (Barrel/Pincushion)
    corner_dists = []
    for idx in [0, 2, 6, 8]:
        mx, my = measured_points[idx]
        corner_dists.append(math.hypot(mx, my))
    avg_corner_dist = sum(corner_dists) / 4.0 if corner_dists else (math.sqrt(2) * W)
    exp_corner_dist = math.hypot(w_avg / 2.0, h_avg / 2.0)
    bulge = 1.0 + ((avg_corner_dist / exp_corner_dist) - 1.0) if exp_corner_dist > 0 else 1.0

    # Clamp parameters to reasonable physical ranges
    clamp = lambda v, lo, hi: max(lo, min(hi, v))
    scale_mult_x = clamp(scale_mult_x, 0.5, 2.0)
    scale_mult_y = clamp(scale_mult_y, 0.5, 2.0)
    trap_x = clamp(trap_x, 0.8, 1.2)
    trap_y = clamp(trap_y, 0.8, 1.2)
    skew_x = clamp(skew_x, 0.8, 1.2)
    skew_y = clamp(skew_y, 0.8, 1.2)
    bulge = clamp(bulge, 0.8, 1.2)

    # Assign to Galvo 1 and Galvo 2 based on axis mapping
    if galvo_1_is_x:
        new_g1_scale = current_g1_scale * scale_mult_x
        new_g2_scale = current_g2_scale * scale_mult_y
        g1_trap, g2_trap = trap_x, trap_y
        g1_skew, g2_skew = skew_x, skew_y
    else:
        new_g2_scale = current_g2_scale * scale_mult_x
        new_g1_scale = current_g1_scale * scale_mult_y
        g2_trap, g1_trap = trap_x, trap_y
        g2_skew, g1_skew = skew_x, skew_y

    g1_bulge, g2_bulge = bulge, bulge

    ideal_pts = [
        (-W, W), (0, W), (W, W),
        (-W, 0), (0, 0), (W, 0),
        (-W, -W), (0, -W), (W, -W)
    ]
    errs = [math.hypot(m[0] - i[0], m[1] - i[1]) for m, i in zip(measured_points, ideal_pts)]
    max_err = max(errs)
    rms_err = math.sqrt(sum(e*e for e in errs) / len(errs))

    return {
        "scale_x_mult": scale_mult_x,
        "scale_y_mult": scale_mult_y,
        "new_g1_scale": new_g1_scale,
        "new_g2_scale": new_g2_scale,
        "g1_barrel": g1_bulge,
        "g2_barrel": g2_bulge,
        "g1_par": g1_skew,
        "g2_par": g2_skew,
        "g1_trapezoid": g1_trap,
        "g2_trapezoid": g2_trap,
        "w_avg": w_avg,
        "h_avg": h_avg,
        "max_err_mm": max_err,
        "rms_err_mm": rms_err
    }

def generate_cor_file(output_path, scale, W, measured_points):
    """
    Generates a .cor file from 9 measured points.
    measured_points: List of 9 tuples (Mx, My) representing the measured 
                     physical coordinates for the 9 ideal points.
    W: the absolute distance of the 9 points from the center in physical units (e.g., 50mm)
    scale: bits per mm scale factor (e.g., 655.35)
    """
    # Define ideal points T_x and T_y
    T_x = [-W, 0, W,
           -W, 0, W,
           -W, 0, W]
    
    T_y = [ W,  W,  W,
            0,  0,  0,
           -W, -W, -W]
           
    # Calculate error in galvo units (M - T) * scale
    error_x_grid = [
        [(measured_points[0][0] - T_x[0])*scale, (measured_points[1][0] - T_x[1])*scale, (measured_points[2][0] - T_x[2])*scale],
        [(measured_points[3][0] - T_x[3])*scale, (measured_points[4][0] - T_x[4])*scale, (measured_points[5][0] - T_x[5])*scale],
        [(measured_points[6][0] - T_x[6])*scale, (measured_points[7][0] - T_x[7])*scale, (measured_points[8][0] - T_x[8])*scale],
    ]
    
    error_y_grid = [
        [(measured_points[0][1] - T_y[0])*scale, (measured_points[1][1] - T_y[1])*scale, (measured_points[2][1] - T_y[2])*scale],
        [(measured_points[3][1] - T_y[3])*scale, (measured_points[4][1] - T_y[4])*scale, (measured_points[5][1] - T_y[5])*scale],
        [(measured_points[6][1] - T_y[6])*scale, (measured_points[7][1] - T_y[7])*scale, (measured_points[8][1] - T_y[8])*scale],
    ]
    
    grid = []
    # 65x65 grid of 32-bit signed integer deltas
    for r in range(65):
        row = []
        # Galvo commands
        x_cmd = r * 1024
        # physical ideal X
        ideal_x = (x_cmd - 32768) / scale
        
        for c in range(65):
            y_cmd = c * 1024
            ideal_y = (y_cmd - 32768) / scale
            
            # Interpolate error
            dx = interp2d(ideal_x, ideal_y, W, W, error_x_grid)
            dy = interp2d(ideal_x, ideal_y, W, W, error_y_grid)
            
            row.append((int(round(dx)), int(round(dy))))
        grid.append(row)
        
    # Build binary file
    # 40 byte header
    header = bytearray(40)
    signature = b"JCZ_COR_2_1\0"
    header[0:len(signature)] = signature
    
    # Scale factor at offset 28
    struct.pack_into('d', header, 28, scale)
    
    with open(output_path, 'wb') as f:
        f.write(header)
        for r in range(65):
            for c in range(65):
                f.write(struct.pack('<ii', grid[r][c][0], grid[r][c][1]))
    return True
