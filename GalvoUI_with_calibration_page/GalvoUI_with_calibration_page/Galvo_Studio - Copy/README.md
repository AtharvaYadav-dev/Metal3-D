# Galvo Studio - Development Roadmap

This software serves as the **Hardware Abstraction Layer** and **Motion Simulator** for the Galvo system. It is specifically designed to support an asynchronous remote and office workflow.

## Project Structure

```text
Galvo_Studio/
│
├── core/
│   ├── dll_wrapper.py        # Hardware abstraction layer + Mocking + Logging
│   ├── motion_planner.py     # Buffer queue system (Generate -> Preview -> Send)
│   ├── svg_parser.py         # SVG to mm to galvo coordinate parsing
│   └── coordinate_mapper.py  # mm -> 65535 mapping
│
├── ui/
│   ├── main_window.py        # Main user interface
│   └── preview_widget.py     # PySide6 + QGraphicsView simulation
│
├── machine/
│   ├── galvo_controller.py   # Higher-level controller connecting DLL & Planner
│   └── stepper_controller.py # Controller for auxiliary axes
│
└── main.py                   # Application Entry Point
```

## Setup & Run

1. **Install Dependencies:**
   ```bash
   pip install PySide6 svgpathtools
   ```

2. **Run the Application:**
   ```bash
   python main.py
   ```

## Remote / Office Workflow

### For Remote Developers
You can work entirely without hardware:
1. `HARDWARE_CONNECTED` is set to `False` by default in `core/dll_wrapper.py`.
2. The application simulates the hardware initialization and execution.
3. Every executed command is logged to `logs/galvo_log_YYYY-MM-DD.txt`.

### For Office Testers
1. Change `HARDWARE_CONNECTED = True` in `core/dll_wrapper.py`.
2. Ensure the actual `gt5motion_GT.dll` is available.
3. Run `main.py` and execute tests.
4. If testing encounters issues, zip the `logs/` folder and send it back to the developer.

## Testing Priority for Office Team

When the office team runs the software, they should test these steps in order:
1. **TEST 1 (Initialize Card):** Just running the app should print "INIT_CARD result=..."
2. **TEST 2 (Move galvo center):** Generate Test Pattern -> Execute Buffer. Watch if it goes to center.
3. **TEST 3 (Move square pattern):** The test pattern draws a square.
4. **TEST 4 (Buffer execution):** Test large SVGs for continuous movement.
5. **TEST 5 (Laser ON/OFF):** Observe physical laser marking during the square pattern test.
