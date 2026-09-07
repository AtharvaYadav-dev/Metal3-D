# Metal 3D Printer: Detailed Working & Technical Operations Guide

**Machine Type:** Metal Laser Powder Bed Fusion (LPBF) 3D Printer  
**Audience:** Operators, Engineers, Technicians, and Stakeholders (No programming or code knowledge required)  
**Hardware Setup:** 3 Motorized Mechanical Axes (**Z, U, V**) + Optical Laser Galvo Scanner

---

## Table of Contents
1. [Overall Machine Architecture & Physical Motion Systems](#1-overall-machine-architecture--physical-motion-systems)
2. [Point 1: File Formats for the Galvo Card (From 3D CAD to Laser Beam)](#2-point-1-file-formats-for-the-galvo-card-from-3d-cad-to-laser-beam)
3. [Point 2: Axis Travel Commands (How Motors Move Z, U, and V)](#3-point-2-axis-travel-commands-how-motors-move-z-u-and-v)
4. [Point 3: Travel Distance Setup & Homing Procedure](#4-point-3-travel-distance-setup--homing-procedure)
5. [Point 4: Initial Settings Required Before Any Motion (Startup Safety Sequence)](#5-point-4-initial-settings-required-before-any-motion-startup-safety-sequence)
6. [Step-by-Step Walkthrough of a Complete 1-Layer Print Cycle](#6-step-by-step-walkthrough-of-a-complete-1-layer-print-cycle)
7. [Comprehensive Machine Specifications Matrix](#7-comprehensive-machine-specifications-matrix)

---

## 1. Overall Machine Architecture & Physical Motion Systems

The Metal 3D printer manufactures solid metal components by fusing fine metallic powder using a concentrated laser beam. The machine coordinates **two distinct motion systems** from a single central motion controller card:

```
+-------------------------------------------------------------------------------------------------+
|                                    CENTRAL CONTROLLER CARD                                      |
+-----------------------------------------------+-------------------------------------------------+
                                                |
                +-------------------------------+-------------------------------+
                |                                                               |
    [ OPTICAL LASER SCANNER: GALVO ]                                 [ 3 MECHANICAL MOTOR AXES ]
    - Driven by ultra-fast galvanometer mirrors                      - Driven by industrial servo/stepper motors
    - Steers laser spot on the powder bed                            - Moves physical powder, recoater, & plates
                |                                                               |
        +-------+-------+                                     +-----------------+-----------------+
        |               |                                     |                 |                 |
     X-Mirror        Y-Mirror                              Z-Axis            U-Axis            V-Axis
    (Left-Right)    (Front-Back)                         (Recoater)       (Build Plate)     (Powder Bay)
        |               |                                     |                 |                 |
    Position:       Position:                            Horizontal         Vertical          Vertical
    0 to 65,535     0 to 65,535                           Sweeper           Platform           Feeder
```

### The 3 Physical Motor Axes:
1. **Z-Axis — Recoater Blade (Channel 2):**
   * A rigid horizontal sweeper blade driven by a precision lead screw.
   * **Function:** Sweeps back and forth across the machine (stroke length up to $890.0\text{ mm}$) to spread an ultra-thin, flat, and uniform layer of metal powder across the build plate.
2. **U-Axis — Build Plate Platform (Channel 3):**
   * The heavy-duty vertical elevator platform holding the metal substrate plate where the part is welded and built.
   * **Function:** After every laser melting pass, it moves **downward** by one layer thickness (typically $0.02\text{ to }0.05\text{ mm}$, or $20\text{ to }50\text{ microns}$) to make room for the next fresh powder layer.
3. **V-Axis — Powder Bay / Dosing Bed (Channel 4):**
   * The powder supply reservoir holding fresh metal powder.
   * **Function:** Moves **upward** by a controlled increment (e.g. $+0.02\text{ mm}$) to push fresh powder above bed level so the Recoater Blade can pick it up and spread it.
4. **Optical Galvo Scanner (Channels 0 & 1 Reserved / DB15 Connector):**
   * Contains two orthogonal mirrors mounted on miniature galvanometers.
   * **Function:** Steers the laser beam at speeds over $1,000\text{ mm/second}$ to trace boundaries and melt the metal powder without any heavy mechanical moving parts.

---

## 2. Point 1: File Formats for the Galvo Card (From 3D CAD to Laser Beam)

How does a 3D digital model turn into microscopic laser scanning movements on a bed of metal powder?

### Step A: Input Files Accepted by the Machine
The operator supplies standard industrial files:
* **STL File (`.stl`)**: Standard 3D CAD file where the outer surface of the part is represented by a mesh of thousands of interconnected triangles.
* **DXF File (`.dxf`) & SVG File (`.svg`)**: 2D vector CAD drawings containing exact lines, arcs, circles, and polylines (used for flat marking, 2D test grids, or machine calibration).
* **G-Code File (`.gcode`)**: Numerical control toolpaths containing explicit coordinate move commands and laser power triggers.

---

### Step B: Slicing, Contours, Hatching, and Support Generation
Before any laser movement can take place, the software prepares the geometry:

```
[ 3D CAD Model (STL) ] 
         |
         v
[ Horizontal Slicing at Layer Thickness (e.g. 0.03 mm) ]
         |
         +---> 1. Perimeter Contours (Outer & Inner boundaries for smooth surface)
         |
         +---> 2. Core Hatching (67° rotating back-and-forth zig-zag lines for solid melting)
         |
         +---> 3. Support Anchor Grids (0°/90° cross-hatch to hold part to baseplate)
```

1. **Layer Slicing:** The 3D model is intersected with horizontal planes spaced by the layer thickness ($20\text{ to }50\text{ microns}$).
2. **Perimeter Contours (Border Passes):** The software extracts the boundary outline of each slice and offsets it into 1 or 2 perimeter loops. These are scanned first to give the part a smooth exterior surface finish and tight dimensional accuracy.
3. **Core Hatching (Solid Infill):**
   * To melt the solid interior of the part, the laser sweeps back and forth in high-speed parallel lines (**hatching**).
   * **Line Spacing (Hatch Distance):** The parallel lines are spaced $0.09\text{ mm to }0.13\text{ mm}$ apart, matching the diameter of the laser beam spot ($\approx 70\text{ to }100\text{ microns}$) with a slight overlap to prevent pores.
   * **67.0° Rotation Per Layer:** The angle of the scan lines is rotated by exactly $67^\circ$ on each subsequent layer. This rotation is critical in metal 3D printing because it prevents thermal stresses from accumulating along one direction, eliminating warping and curling.
4. **Anchor Supports:** Underneath overhangs and between the bottom of the part and the build plate, the software generates $0.5\text{ mm}$ cone supports with a $0^\circ/90^\circ$ cross-hatch grid to conduct heat away into the build plate and keep the part securely anchored.

---

### Step C: How the Galvo Card Understands Coordinates (The 16-Bit Grid)
The galvanometer mirrors do not understand millimeters. They are driven by high-precision digital-to-analog converters (DACs) that accept **16-bit unsigned integers from $0\text{ to }65,535$**:

* **Mirror Left / Back Maximum:** Position `0`
* **Mirror Right / Front Maximum:** Position `65,535`
* **Physical Center Origin $[0.0\text{ mm}, 0.0\text{ mm}]$:** Position **`32,767`** (the exact mathematical midpoint).

#### The Millimeter-to-Galvo Conversion Formula:
$$\text{Galvo Position} = 32,767 + \left(\text{Coordinate in Millimeters} \times \frac{65,535}{\text{Optical Field Size in Millimeters}}\right)$$

* **For a $250\text{ mm} \times 250\text{ mm}$ Build Area:**
  $$\text{Resolution} = \frac{65,535}{250} \approx 262.14\text{ digital counts per millimeter}$$
* **Example:**
  * To hit center $(X = 0\text{ mm}, Y = 0\text{ mm})$: Galvo registers receive **`(32767, 32767)`**.
  * To hit coordinate $(X = +50\text{ mm}, Y = +50\text{ mm})$:
    $$\text{Position} = 32,767 + (50 \times 262.14) = 32,767 + 13,107 = \mathbf{45,874}$$

---

### Step D: The Vector Commands Sent to the Galvo Card
The software converts all sliced contours and hatch patterns into a sequence of instructions:
1. **JUMP Command:** Tells the mirrors to pivot rapidly to the start of a line while the **laser is completely turned OFF** (typically moves at $3,000\text{ to }5,000\text{ mm/s}$).
2. **MARK Command:** Tells the mirrors to sweep smoothly along the vector while the **laser is turned ON** at preset power and speed (e.g. $1,000\text{ mm/s}$ at $200\text{ Watts}$).
3. **DELAYS (Corner & Settling Delays):** Microsecond pauses inserted at line ends so mirror inertia settles before the laser switches on or changes direction, preventing rounded corners or burn holes.
4. **Hardware Buffering:** Commands are streamed into an onboard hardware FIFO memory buffer on the controller card. This guarantees that even if the computer operating system hesitates for a millisecond, the laser never pauses unexpectedly over the powder bed (which would vaporize the metal).

---

## 3. Point 2: Axis Travel Commands (How Motors Move Z, U, and V)

Mechanical motion for the Recoater (Z), Build Plate (U), and Powder Bay (V) is executed by electric motor drives.

### How the Controller Drives a Motor:
The motion controller sends high-speed digital electrical signals to each axis driver:
* **PULSE Signal:** A train of rapid electrical on/off square waves. Every individual pulse commands the motor driver to rotate the motor by one microstep.
* **DIRECTION Signal:** A steady voltage level (HIGH vs LOW) that dictates whether the motor turns clockwise or counter-clockwise.

```
Controller Card                       Motor Driver                        Mechanical Lead Screw
  [ Pulse Train ]  ================>   [ YAKO / MS-S3 ]   =============>   [ Rotating Shaft ]
  [ Direction   ]  ================>   [ Drive Unit   ]                    Moves Axis in mm
```

---

### What Every Axis Travel Command Contains:
Whenever an axis is commanded to move, the software sends 6 specific parameters:

1. **Target Axis Identifier:**
   * Axis Index `2` $\rightarrow$ **Z-Axis (Recoater Blade)**
   * Axis Index `3` $\rightarrow$ **U-Axis (Build Plate Platform)**
   * Axis Index `4` $\rightarrow$ **V-Axis (Powder Bay / Feeder)**
2. **Move Mode (Relative vs Absolute):**
   * **Relative Move:** Move by an incremental distance from the current position (e.g. *"lower build plate by $0.02\text{ mm}$"*).
   * **Absolute Move:** Move to an exact coordinate referenced from machine zero (e.g. *"recoater travel to position $240.0\text{ mm}$"*).
3. **Distance Converted to Pulses:** The physical distance in millimeters multiplied by the calibrated steps per millimeter.
4. **Starting Velocity:** A gentle starting pulse rate to overcome mechanical inertia without causing the motor to skip steps or stall.
5. **Maximum Cruising Velocity:** The top pulse rate the motor reaches during steady travel.
6. **Acceleration Ramp Time:** The duration (typically $0.05\text{ to }0.1\text{ seconds}$) over which speed ramps up from start velocity to cruising velocity.

---

### The Motion Profile & Stopping Mechanics:
* **Trapezoidal Motion Profile:** Velocity ramps up gently, cruises at a constant speed, and ramps down smoothly. This prevents sudden mechanical shocks that could disturb the powder bed.
* **Smooth Deceleration Stop:** When stopping at a target or upon an operator pause, the axis decelerates to a stop over $0.05\text{ seconds}$.
* **Emergency Stop (E-Stop):** Immediately cuts pulse generation to all axes simultaneously if a safety interlock trips or an emergency stop button is pressed.
* **Motion Done Verification:** The software continuously monitors the controller's motion status register and confirms the motor has come to a complete standstill before starting laser exposure or moving the next axis.

---

## 4. Point 3: Travel Distance Setup & Homing Procedure

### Part A: Travel Distance Setup (Converting Millimeters to Motor Pulses)
Motors count pulses, but operators program in millimeters. The system uses calibrated conversion rates:

$$\text{Pulses Sent} = \text{Distance in Millimeters} \times \text{Calibrated Steps per Millimeter}$$

| Parameter | Z-Axis (Recoater Blade) | U-Axis (Build Plate) | V-Axis (Powder Bay) |
| :--- | :---: | :---: | :---: |
| **Card Channel Index** | **`2`** | **`3`** | **`4`** |
| **Steps per Millimeter** | **$1280.0\text{ pulses/mm}$** | **$320.0\text{ pulses/mm}$** | **$320.0\text{ pulses/mm}$** |
| **Pulses per 1 mm Move** | $1,280\text{ pulses}$ | $320\text{ pulses}$ | $320\text{ pulses}$ |
| **Single Layer Step ($0.02\text{ mm}$)**| N/A (Travels in sweeps) | $-6.4\text{ pulses}$ (Drops down) | $+6.4\text{ pulses}$ (Rises up) |
| **Travel Direction Polarity** | Inverted in software | Standard | Standard |
| **Allowed Travel Range** | **$0.0\text{ mm to }890.0\text{ mm}$** | **$0.0\text{ mm to }250.0\text{ mm}$** | **$0.0\text{ mm to }250.0\text{ mm}$** |
| **Normal Cruising Speed** | $35,000\text{ pulses/s}$ ($\approx 27.3\text{ mm/s}$) | $10,000\text{ pulses/s}$ ($\approx 31.2\text{ mm/s}$) | $10,000\text{ pulses/s}$ ($\approx 31.2\text{ mm/s}$) |
| **Homing Speed** | $35,000\text{ pulses/s}$ | $3,200\text{ pulses/s}$ ($10.0\text{ mm/s}$) | $3,200\text{ pulses/s}$ ($10.0\text{ mm/s}$) |

#### Software Limit Protection:
To prevent mechanical damage, the software automatically checks every requested move. If a command would drive the Recoater past $890.0\text{ mm}$ or below $0.0\text{ mm}$, the move is automatically blocked.

---

### Part B: The Homing Procedure (Finding True Physical Zero)
When power is first applied, the controller does not know where the mechanical axes are located. **Homing** establishes a repeatable, high-precision physical origin ($0.000\text{ mm}$).

```
[ Axis Moving Towards Home Sensor ] --------> | Inductive Proximity Sensor |
                                                               |
                                            Metal Flag Sensed (Triggered!)
                                                               |
                                            [ Smooth Deceleration Stop ]
                                                               |
                                            [ Back Away +1.0 mm to Clear Sensor ]
                                                               |
                                            [ Reset Internal Counter = 0.000 mm ]
```

#### Step-by-Step Mechanical Homing (Z, U, and V):
Each axis is equipped with an **inductive proximity sensor** (a solid-state metal detector switch) mounted at its home reference point.
1. **Sensor Health Check & Initial Backoff:**
   * The controller reads the sensor state.
   * If an axis is *already* sitting on its sensor, the motor moves in reverse by $+2.0\text{ mm}$ at low speed to clear the sensor flag.
2. **Continuous Homing Move:**
   * The motor initiates a smooth travel stroke toward the sensor:
     * **Recoater (Z):** Moves toward zero at $27.3\text{ mm/s}$.
     * **Build Plate (U):** Moves toward zero at a slow, controlled $10.0\text{ mm/s}$.
     * **Powder Bay (V):** Moves toward zero at a slow, controlled $10.0\text{ mm/s}$.
3. **High-Frequency Sensor Polling:**
   * The controller queries the sensor status every $15\text{ milliseconds}$ (with a safety timeout of $60\text{ seconds}$).
4. **Smooth Deceleration on Detection:**
   * The millisecond metal is detected, the card commands a smooth deceleration stop ($0.05\text{ seconds}$).
5. **Micro-Backoff & Zero Calibration:**
   * The axis gently steps forward by $+1.0\text{ mm}$ at low speed ($1,600\text{ pulses/s}$) to move just outside the sensor's magnetic hysteresis band.
   * The controller sets its internal pulse counter: **"Current position is now exactly $0.000\text{ mm}$."**

#### Galvo Scanner Optical Homing:
* Optical galvanometers have no mechanical limit switches or gears.
* Homing the Galvo is entirely electronic: the controller commands mirror coordinates $(32767, 32767)$. This locks both mirrors in their resting mid-positions, pointing the laser beam at the exact physical center of the build bed.

#### Master Machine Homing Sequence:
When the operator clicks **"Home All"**, the machine executes homing in a safe, logical order:
1. **Home Build Plate (U):** Platform returns to top reference zero ($0.000\text{ mm}$).
2. **Home Powder Bay (V):** Powder reservoir returns to bottom reference zero ($0.000\text{ mm}$).
3. **Home Recoater Blade (Z):** Sweeper blade returns to its parked home station ($0.000\text{ mm}$).
4. **Home Galvo Mirrors:** Electronic centering of the optical scanhead to $(32767, 32767)$.

---

## 5. Point 4: Initial Settings Required Before Any Motion (Startup Safety Sequence)

Before any motor moves or any laser fires, the software executes an automatic 7-step initialization checklist:

```
[ Step 1: Send Security Password (12242) ]
                   |
                   v
[ Step 2: Establish USB Card Handshake & Load Firmware ]
                   |
                   v
[ Step 3: Wait 1.0 sec & Arm Galvo Mirror DAC Channels ]
                   |
                   v
[ Step 4: Configure Motor Output Mode to Pulse/Direction (Mode 0) ]
                   |
                   v
[ Step 5: Disable Floating Z Hard Limit & Clear Driver Alarms ]
                   |
                   v
[ Step 6: Force Laser Interlock to OFF (Pin 0 to LOW) ]
                   |
                   v
[ Step 7: Clear Position Registers to 0.000 mm ]
                   |
                   v
      ===> SYSTEM READY FOR HOMING & OPERATION
```

1. **Security Authentication Code:**
   * The controller card is protected by firmware security. The software must transmit factory password **`12242`** first; otherwise, the card ignores all subsequent commands.
2. **Controller Card Connection & Firmware Loading:**
   * The software verifies that the USB controller card is detected.
   * It confirms that the DSP/FPGA motion firmware files (`4_mcc_GT.bin` and `5_mcc_GT.bin`) are loaded into the card's processor.
3. **Galvo Stabilization Delay & Channel Arming:**
   * Galvanometer analog amplifiers require time for power supply voltages to stabilize.
   * The system waits **$1.0\text{ full second}$**, zeroes out the DAC output channels, and arms the Galvo drive electronics.
4. **Motor Pulse Output Mode Setup:**
   * Configures the motor channels for **Pulse/Direction (Mode 0)** to match the YAKO / MS-S3 servo drives.
5. **Hard Limit & Drive Alarm Overrides:**
   * The machine does not use a physical hard-stop microswitch on the Z-axis (it relies on the inductive home sensor and software bounds). The software explicitly instructs the card to disable hard-limit tripping on Axis 2 so floating electrical noise cannot trigger a false emergency shutdown.
   * Clears any residual driver alarms on axes 2, 3, and 4.
6. **Laser Safety Interlock (Mandatory Default OFF):**
   * The digital output line controlling the laser (DO1 / Pin 0) is **immediately forced to LOW (0 / OFF)** upon connection.
   * This guarantees that the laser can never fire accidentally during power-up or system initialization.
7. **Zero All Position Registers:**
   * Clears internal pulse count registers to zero before any movements begin.

---

## 6. Step-by-Step Walkthrough of a Complete 1-Layer Print Cycle

Once the system is initialized and homed, printing each layer follows this exact physical coordination sequence:

```
                       +-----------------------------------+
                       |   1. RECOATER BLADE HOMED (Z=0)   |
                       +-----------------+-----------------+
                                         |
                                         v
                       +-----------------------------------+
                       | 2. POWDER BAY DOSES UP (+0.02 mm) |
                       +-----------------+-----------------+
                                         |
                                         v
                       +-----------------------------------+
                       | 3. RECOATER SWEEPS TO 240.0 mm    |
                       |    (Spreads flat 20µm powder bed) |
                       +-----------------+-----------------+
                                         |
                                         v
                       +-----------------------------------+
                       | 4. GALVO SCANS & MELTS LAYER      |
                       |    (Contour borders + 67° hatch)  |
                       +-----------------+-----------------+
                                         |
                                         v
                       +-----------------------------------+
                       | 5. BUILD PLATE LOWERS (-0.02 mm)  |
                       |    (Makes room for next layer)    |
                       +-----------------+-----------------+
                                         |
                                         v
                       +-----------------------------------+
                       | 6. RECOATER STROKE TO 760.0 mm    |
                       |    AND RETURNS HOME (0.00 mm)     |
                       +-----------------+-----------------+
                                         |
                                         v
                       [ REPEAT UNTIL 3D PART IS FINISHED ]
```

| Step | Machine Action | Physical Event Inside the Chamber |
| :---: | :--- | :--- |
| **Step 1** | **Home Recoater (Z)** | Recoater blade returns to park position ($Z = 0.00\text{ mm}$), clearing the bed for inspection. |
| **Step 2** | **Dose Powder (V)** | Powder Bay rises by $+0.02\text{ mm}$ ($20\text{ microns}$), pushing a measured volume of fresh powder above bed level. |
| **Step 3** | **Recoater Forward Sweep (Z)** | Recoater moves smoothly to $240.0\text{ mm}$, spreading an even, flat $20\text{ µm}$ layer of powder across the build plate. |
| **Step 4** | **Laser Melting (Galvo)** | Optical Galvo scanner traces perimeter borders and 67° rotated hatch scanlines at $1,000\text{ mm/s}$, solid-melting the layer geometry. |
| **Step 5** | **Lower Build Platform (U)** | Build plate lowers by $-0.02\text{ mm}$ ($20\text{ microns}$) to prepare space for the subsequent layer. |
| **Step 6** | **Recoater Traversal & Return (Z)**| Recoater sweeps forward to $760.0\text{ mm}$ to clear surplus powder into the overflow hopper, then sweeps back to home ($0.00\text{ mm}$). |
| **Step 7** | **Cycle Repeat** | The cycle repeats continuously until all layers are melted and the metal part is fully formed. |

---

## 7. Comprehensive Machine Specifications Matrix

| Feature / Subsystem | Technical Specification | Operational Details |
| :--- | :--- | :--- |
| **Motion Controller Card** | Googol Technology / ProSys GT PROSYS V10 | USB 3.0, 5-Axis DSP/FPGA architecture |
| **Connected Motorized Axes** | **3 Physical Axes:** Z, U, V | Z = Channel 2, U = Channel 3, V = Channel 4 |
| **Recoater Blade (Z-Axis)** | $1280.0\text{ pulses/mm}$ | Travel: $0.0\text{ to }890.0\text{ mm}$; Speed: $27.3\text{ mm/s}$ |
| **Build Plate (U-Axis)** | $320.0\text{ pulses/mm}$ | Travel: $0.0\text{ to }250.0\text{ mm}$; Homing: $10.0\text{ mm/s}$ |
| **Powder Bay (V-Axis)** | $320.0\text{ pulses/mm}$ | Travel: $0.0\text{ to }250.0\text{ mm}$; Homing: $10.0\text{ mm/s}$ |
| **Homing Sensors** | Inductive Proximity Sensors (NPN Normally-Open) | Active-Low ($0$ = Sensed/Triggered, $1$ = Clear) |
| **Optical Scanhead (Galvo)** | 16-bit Dual Galvanometer Mirrors | Resolution: $0\text{ to }65,535$; Center: $(32767, 32767)$ |
| **Scan Speed** | Typical: $900\text{ to }1,400\text{ mm/s}$ | Maximum capability: Up to $1,000,000\text{ points/sec}$ |
| **Laser Interlock Control** | Digital Output DO1 (Pin 0) | $0$ = Laser Disabled (Safe), $1$ = Laser Armed/Active |
| **Layer Thickness Capability** | $0.02\text{ to }0.05\text{ mm}$ ($20\text{ to }50\text{ microns}$) | Precision lead screw controlled via U-Axis |
| **Hatch Rotation Scheme** | $67.0^\circ$ continuous rotation per layer | Minimizes residual thermal stress & prevents part warping |
| **Startup Security Code** | `12242` | Mandatory authentication code for card unlock |
