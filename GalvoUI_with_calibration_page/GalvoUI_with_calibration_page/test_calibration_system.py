import os
import tempfile
import numpy as np
from core.calibration import GalvoCalibration
from core.calibration_generator import calculate_analytical_parameters, generate_cor_file
from core.connection.mock import MockConnection

def test_analytical_parameters():
    print("--- 1. Testing Analytical Parameters ---")
    nominal_w = 50.0
    
    # 9 points ordered:
    # 0: TL (-W, +W)
    # 1: TM (0, +W)
    # 2: TR (+W, +W)
    # 3: ML (-W, 0)
    # 4: Center (0, 0)
    # 5: MR (+W, 0)
    # 6: BL (-W, -W)
    # 7: BM (0, -W)
    # 8: BR (+W, -W)
    measured_pts = [
        (-47.8, 51.8),   # 0: TL
        (0.0, 52.3),     # 1: TM
        (47.9, 51.9),    # 2: TR
        (-47.6, 0.0),    # 3: ML
        (0.0, 0.0),      # 4: Center
        (47.7, 0.0),     # 5: MR
        (-47.9, -51.8),  # 6: BL
        (0.0, -52.2),    # 7: BM
        (47.8, -51.9)    # 8: BR
    ]
    
    results = calculate_analytical_parameters(nominal_w, measured_pts, current_g1_scale=100.0, current_g2_scale=100.0, galvo_1_is_x=False)
    print("Analytical Results:", results)
    # Since galvo_1_is_x=False, G1 is Y and G2 is X
    assert results["new_g2_scale"] > 100.0, "Galvo 2 (X) scale should increase to correct undersized X (measured ~95.4 vs 100)"
    assert results["new_g1_scale"] < 100.0, "Galvo 1 (Y) scale should decrease to correct oversized Y (measured ~104.2 vs 100)"
    print("[OK] Analytical calibration math verified.")

def test_cor_generation_and_loading():
    print("--- 2. Testing .cor File Generation and Core Loading ---")
    nominal_w = 50.0
    measured_pts = [
        (-49.0, 49.0),   # 0: TL
        (0.0, 50.5),     # 1: TM
        (49.0, 49.0),    # 2: TR
        (-50.5, 0.0),    # 3: ML
        (0.0, 0.0),      # 4: Center
        (50.5, 0.0),     # 5: MR
        (-49.0, -49.0),  # 6: BL
        (0.0, -50.5),    # 7: BM
        (49.0, -49.0)    # 8: BR
    ]
    
    with tempfile.NamedTemporaryFile(suffix=".cor", delete=False) as f:
        tmp_cor_path = f.name
        
    try:
        generate_cor_file(tmp_cor_path, scale=655.35, W=nominal_w, measured_points=measured_pts)
        assert os.path.exists(tmp_cor_path), ".cor file was not written"
        assert os.path.getsize(tmp_cor_path) == 33840, f"Expected 33840 bytes, got {os.path.getsize(tmp_cor_path)}"
        
        calib = GalvoCalibration()
        loaded = calib.load_calibration(tmp_cor_path)
        assert loaded is True, "GalvoCalibration failed to load .cor file"
        assert calib.is_valid is True, "GalvoCalibration is_valid is False"
        assert calib.grid is not None and len(calib.grid) == 65 and len(calib.grid[0]) == 65
        
        # Test applying correction in DAC coordinates (0-65535 range, e.g. center ~32768)
        # Test an off-center point (40000, 40000)
        corrected_x, corrected_y = calib.apply(40000, 40000)
        print(f"Original (40000, 40000) -> Corrected ({corrected_x:.1f}, {corrected_y:.1f})")
        assert (corrected_x, corrected_y) != (40000, 40000), "Correction should shift coordinates"
        
        # Test disabling correction
        calib.set_enabled(False)
        raw_x, raw_y = calib.apply(40000, 40000)
        assert (raw_x, raw_y) == (40000, 40000), "Disabled calibration must return unshifted coordinates"
        print("[OK] .cor file generation, loading, and bypass toggling verified.")
    finally:
        if os.path.exists(tmp_cor_path):
            os.remove(tmp_cor_path)

def test_mock_hardware_calibration_switching():
    print("--- 3. Testing Mock Hardware Connection Calibration Switching ---")
    mock_conn = MockConnection()
    assert hasattr(mock_conn, 'calibration'), "MockConnection missing calibration"
    assert hasattr(mock_conn, 'set_calibration_file'), "MockConnection missing set_calibration_file"
    assert hasattr(mock_conn, 'set_calibration_enabled'), "MockConnection missing set_calibration_enabled"
    print("[OK] MockConnection API verified.")

if __name__ == "__main__":
    test_analytical_parameters()
    test_cor_generation_and_loading()
    test_mock_hardware_calibration_switching()
    print("\n=== ALL CALIBRATION SYSTEM TESTS PASSED SUCCESSFULLY! ===")
