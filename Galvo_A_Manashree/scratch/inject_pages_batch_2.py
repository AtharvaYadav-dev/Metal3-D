import xml.etree.ElementTree as ET

def clear_page(root, page_name):
    page = None
    for widget in root.iter('widget'):
        if widget.get('name') == page_name:
            page = widget
            break
            
    if page is None:
        print(f"Could not find {page_name}")
        return None
        
    for child in list(page):
        if child.tag not in ('property', 'attribute'):
            page.remove(child)
    return page

def inject_laser_galvo(root):
    page = clear_page(root, 'page_laser_galvo')
    if page is None: return
    
    xml = """
<layout class="QVBoxLayout" name="vLayout_laser_galvo">
  <!-- TOP ROW -->
  <item>
    <layout class="QHBoxLayout">
      <item>
        <widget class="QGroupBox" name="gb_laser_control"><property name="title"><string>LASER CONTROL</string></property>
          <layout class="QHBoxLayout">
            <item>
                <layout class="QVBoxLayout">
                    <item>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Status</string></property></widget></item>
                            <item row="0" column="1"><widget class="QLabel"><property name="text"><string>Enabled</string></property></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Laser State</string></property></widget></item>
                            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>Ready</string></property></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Mode</string></property></widget></item>
                            <item row="2" column="1"><widget class="QLabel"><property name="text"><string>CW</string></property></widget></item>
                        </layout>
                    </item>
                    <item><widget class="QPushButton"><property name="text"><string>Laser Enable</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Laser Disable</string></property></widget></item>
                </layout>
            </item>
            <item>
                <layout class="QVBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>LASER POWER</string></property></widget></item>
                    <item><widget class="QLabel"><property name="text"><string>[Dial Graphic]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>Set Power</string></property></widget></item>
                            <item><widget class="QLineEdit"><property name="text"><string>200</string></property></widget></item>
                            <item><widget class="QLabel"><property name="text"><string>W</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Apply</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </item>
            <item>
                <layout class="QFormLayout">
                    <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Frequency</string></property></widget></item>
                    <item row="0" column="1"><widget class="QLabel"><property name="text"><string>50 kHz</string></property></widget></item>
                    <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Duty Cycle</string></property></widget></item>
                    <item row="1" column="1"><widget class="QLabel"><property name="text"><string>100 %</string></property></widget></item>
                    <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Pulse Width</string></property></widget></item>
                    <item row="2" column="1"><widget class="QLabel"><property name="text"><string>200 ns</string></property></widget></item>
                    <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Beam Diameter</string></property></widget></item>
                    <item row="3" column="1"><widget class="QLabel"><property name="text"><string>70 μm</string></property></widget></item>
                    <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Wavelength</string></property></widget></item>
                    <item row="4" column="1"><widget class="QLabel"><property name="text"><string>1070 nm</string></property></widget></item>
                    <item row="5" column="0"><widget class="QLabel"><property name="text"><string>Laser Hours</string></property></widget></item>
                    <item row="5" column="1"><widget class="QLabel"><property name="text"><string>1245.6 h</string></property></widget></item>
                    <item row="6" column="0"><widget class="QLabel"><property name="text"><string>Laser Temperature</string></property></widget></item>
                    <item row="6" column="1"><widget class="QLabel"><property name="text"><string>25.2 C</string></property></widget></item>
                    <item row="7" column="0"><widget class="QLabel"><property name="text"><string>Driver Temperature</string></property></widget></item>
                    <item row="7" column="1"><widget class="QLabel"><property name="text"><string>31.4 C</string></property></widget></item>
                </layout>
            </item>
          </layout>
        </widget>
      </item>
      
      <item>
        <widget class="QGroupBox" name="gb_galvo_control"><property name="title"><string>GALVO CONTROL</string></property>
          <layout class="QHBoxLayout">
            <item>
                <layout class="QVBoxLayout">
                    <item>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Status</string></property></widget></item>
                            <item row="0" column="1"><widget class="QLabel"><property name="text"><string>Enabled</string></property></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Galvo State</string></property></widget></item>
                            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>Ready</string></property></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Scan Field</string></property></widget></item>
                            <item row="2" column="1"><widget class="QLabel"><property name="text"><string>120 mm</string></property></widget></item>
                        </layout>
                    </item>
                    <item><widget class="QPushButton"><property name="text"><string>Galvo Enable</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Galvo Disable</string></property></widget></item>
                </layout>
            </item>
            <item>
                <layout class="QVBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>GALVO SPEED</string></property></widget></item>
                    <item><widget class="QLabel"><property name="text"><string>[Dial Graphic]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>Set Speed</string></property></widget></item>
                            <item><widget class="QLineEdit"><property name="text"><string>12000</string></property></widget></item>
                            <item><widget class="QLabel"><property name="text"><string>mm/s</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Apply</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </item>
            <item>
                <layout class="QFormLayout">
                    <item row="0" column="0"><widget class="QLabel"><property name="text"><string>X Offset</string></property></widget></item>
                    <item row="0" column="1"><widget class="QLabel"><property name="text"><string>0.000 mm</string></property></widget></item>
                    <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Y Offset</string></property></widget></item>
                    <item row="1" column="1"><widget class="QLabel"><property name="text"><string>0.000 mm</string></property></widget></item>
                    <item row="2" column="0"><widget class="QLabel"><property name="text"><string>X Scale</string></property></widget></item>
                    <item row="2" column="1"><widget class="QLabel"><property name="text"><string>1.000</string></property></widget></item>
                    <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Y Scale</string></property></widget></item>
                    <item row="3" column="1"><widget class="QLabel"><property name="text"><string>1.000</string></property></widget></item>
                    <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Galvo Hours</string></property></widget></item>
                    <item row="4" column="1"><widget class="QLabel"><property name="text"><string>1240.0 h</string></property></widget></item>
                    <item row="5" column="0"><widget class="QLabel"><property name="text"><string>Mirror Temp X</string></property></widget></item>
                    <item row="5" column="1"><widget class="QLabel"><property name="text"><string>27.2 C</string></property></widget></item>
                    <item row="6" column="0"><widget class="QLabel"><property name="text"><string>Mirror Temp Y</string></property></widget></item>
                    <item row="6" column="1"><widget class="QLabel"><property name="text"><string>28.4 C</string></property></widget></item>
                </layout>
            </item>
          </layout>
        </widget>
      </item>
    </layout>
  </item>

  <!-- MIDDLE ROW -->
  <item>
    <layout class="QHBoxLayout">
        <item>
            <widget class="QGroupBox" name="gb_laser_diag"><property name="title"><string>LASER DIAGNOSTICS</string></property>
                <layout class="QHBoxLayout">
                    <item>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Laser Source</string></property></widget></item>
                            <item row="0" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Power Supply</string></property></widget></item>
                            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Water Cooling</string></property></widget></item>
                            <item row="2" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                            <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Interlock Status</string></property></widget></item>
                            <item row="3" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                            <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Emission Status</string></property></widget></item>
                            <item row="4" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                            <item row="5" column="0"><widget class="QLabel"><property name="text"><string>Error Code</string></property></widget></item>
                            <item row="5" column="1"><widget class="QLabel"><property name="text"><string>None</string></property></widget></item>
                        </layout>
                    </item>
                    <item>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>DETAILS</string></property></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Current</string></property></widget></item>
                            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>32.5 A</string></property></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Voltage</string></property></widget></item>
                            <item row="2" column="1"><widget class="QLabel"><property name="text"><string>24.1 V</string></property></widget></item>
                            <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Cooling Flow</string></property></widget></item>
                            <item row="3" column="1"><widget class="QLabel"><property name="text"><string>2.35 L/min</string></property></widget></item>
                            <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Water Temp. In</string></property></widget></item>
                            <item row="4" column="1"><widget class="QLabel"><property name="text"><string>22.1 C</string></property></widget></item>
                            <item row="5" column="0"><widget class="QLabel"><property name="text"><string>Water Temp. Out</string></property></widget></item>
                            <item row="5" column="1"><widget class="QLabel"><property name="text"><string>24.8 C</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_galvo_diag"><property name="title"><string>GALVO DIAGNOSTICS</string></property>
                <layout class="QHBoxLayout">
                    <item>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>X Axis Driver</string></property></widget></item>
                            <item row="0" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Y Axis Driver</string></property></widget></item>
                            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>X Axis Feedback</string></property></widget></item>
                            <item row="2" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                            <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Y Axis Feedback</string></property></widget></item>
                            <item row="3" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                            <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Interlock Status</string></property></widget></item>
                            <item row="4" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                            <item row="5" column="0"><widget class="QLabel"><property name="text"><string>Error Code</string></property></widget></item>
                            <item row="5" column="1"><widget class="QLabel"><property name="text"><string>None</string></property></widget></item>
                        </layout>
                    </item>
                    <item>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>DETAILS</string></property></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>X Position</string></property></widget></item>
                            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>0.000 mm</string></property></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Y Position</string></property></widget></item>
                            <item row="2" column="1"><widget class="QLabel"><property name="text"><string>0.000 mm</string></property></widget></item>
                            <item row="3" column="0"><widget class="QLabel"><property name="text"><string>X Actual Speed</string></property></widget></item>
                            <item row="3" column="1"><widget class="QLabel"><property name="text"><string>0 mm/s</string></property></widget></item>
                            <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Y Actual Speed</string></property></widget></item>
                            <item row="4" column="1"><widget class="QLabel"><property name="text"><string>0 mm/s</string></property></widget></item>
                            <item row="5" column="0"><widget class="QLabel"><property name="text"><string>Tracking Error</string></property></widget></item>
                            <item row="5" column="1"><widget class="QLabel"><property name="text"><string>0.002 mm</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_test_patterns"><property name="title"><string>TEST PATTERNS</string></property>
                <layout class="QGridLayout">
                    <item row="0" column="0"><widget class="QPushButton"><property name="text"><string>Mark Square</string></property></widget></item>
                    <item row="0" column="1"><widget class="QPushButton"><property name="text"><string>Mark Circle</string></property></widget></item>
                    <item row="1" column="0"><widget class="QPushButton"><property name="text"><string>Cross Hair</string></property></widget></item>
                    <item row="1" column="1"><widget class="QPushButton"><property name="text"><string>Spiral</string></property></widget></item>
                    <item row="2" column="0"><widget class="QPushButton"><property name="text"><string>Line Test</string></property></widget></item>
                    <item row="2" column="1"><widget class="QPushButton"><property name="text"><string>Custom Pattern</string></property></widget></item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_pattern_settings"><property name="title"><string>PATTERN SETTINGS</string></property>
                <layout class="QVBoxLayout">
                    <item>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Size</string></property></widget></item>
                            <item row="0" column="1"><widget class="QLineEdit"><property name="text"><string>50</string></property></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Power</string></property></widget></item>
                            <item row="1" column="1"><widget class="QLineEdit"><property name="text"><string>100</string></property></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Speed</string></property></widget></item>
                            <item row="2" column="1"><widget class="QLineEdit"><property name="text"><string>5000</string></property></widget></item>
                            <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Loops</string></property></widget></item>
                            <item row="3" column="1"><widget class="QLineEdit"><property name="text"><string>1</string></property></widget></item>
                        </layout>
                    </item>
                    <item><widget class="QPushButton"><property name="text"><string>Run Pattern</string></property></widget></item>
                </layout>
            </widget>
        </item>
    </layout>
  </item>

  <!-- BOTTOM ROW -->
  <item>
    <widget class="QGroupBox" name="gb_calibration"><property name="title"><string>CALIBRATION</string></property>
        <layout class="QHBoxLayout">
            <item>
                <layout class="QVBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>GALVO FIELD CALIBRATION\nCalibrate the galvo scan field and linearity.</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Start Calibration</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>View Last Result</string></property></widget></item>
                </layout>
            </item>
            <item><widget class="QLabel"><property name="text"><string>[Grid Graphic]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
            <item>
                <layout class="QVBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>DELAY COMPENSATION\nAdjust laser on/off delay for corners.</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Start Calibration</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>View Last Result</string></property></widget></item>
                </layout>
            </item>
            <item><widget class="QLabel"><property name="text"><string>[Plot Graphic]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
            <item>
                <layout class="QVBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>LASER POWER CALIBRATION\nCalibrate actual laser power output.</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Start Calibration</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>View Last Result</string></property></widget></item>
                </layout>
            </item>
            <item><widget class="QLabel"><property name="text"><string>[Curve Graphic]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
            <item>
                <layout class="QVBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>LAST CALIBRATION</string></property></widget></item>
                    <item>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Galvo Field</string></property></widget></item>
                            <item row="0" column="1"><widget class="QLabel"><property name="text"><string>07 Jul 2026 Pass</string></property></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Delay Comp.</string></property></widget></item>
                            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>07 Jul 2026 Pass</string></property></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Laser Power</string></property></widget></item>
                            <item row="2" column="1"><widget class="QLabel"><property name="text"><string>07 Jul 2026 Pass</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </item>
        </layout>
    </widget>
  </item>
</layout>
"""
    new_layout = ET.fromstring(xml)
    page.append(new_layout)
    print("Injected laser/galvo page")

def inject_motors(root):
    page = clear_page(root, 'page_motors')
    if page is None: return
    
    xml = """
<layout class="QVBoxLayout" name="vLayout_motors">
  <!-- TOP ROW -->
  <item>
    <layout class="QHBoxLayout">
      <item>
        <widget class="QGroupBox" name="gb_motor_build"><property name="title"><string>BUILD PLATFORM MOTOR</string></property>
            <layout class="QVBoxLayout">
                <item>
                    <layout class="QHBoxLayout">
                        <item><widget class="QLabel"><property name="text"><string>[Icon]</string></property></widget></item>
                        <item>
                            <layout class="QFormLayout">
                                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Status</string></property></widget></item>
                                <item row="0" column="1"><widget class="QLabel"><property name="text"><string>Enabled</string></property></widget></item>
                                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Position</string></property></widget></item>
                                <item row="1" column="1"><widget class="QLabel"><property name="text"><string>125.300 mm</string></property></widget></item>
                                <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Velocity</string></property></widget></item>
                                <item row="2" column="1"><widget class="QLabel"><property name="text"><string>2.0 mm/s</string></property></widget></item>
                                <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Current</string></property></widget></item>
                                <item row="3" column="1"><widget class="QLabel"><property name="text"><string>1.25 A</string></property></widget></item>
                                <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Load</string></property></widget></item>
                                <item row="4" column="1"><widget class="QLabel"><property name="text"><string>18 %</string></property></widget></item>
                            </layout>
                        </item>
                    </layout>
                </item>
                <item><widget class="QLabel"><property name="text"><string>Control</string></property></widget></item>
                <item>
                    <layout class="QHBoxLayout">
                        <item><widget class="QPushButton"><property name="text"><string>Home</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Move Up</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Move Down</string></property></widget></item>
                    </layout>
                </item>
                <item><widget class="QLabel"><property name="text"><string>Jog</string></property></widget></item>
                <item>
                    <layout class="QHBoxLayout">
                        <item><widget class="QPushButton"><property name="text"><string>-10</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>-1</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>+1</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>+10</string></property></widget></item>
                    </layout>
                </item>
            </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_motor_powder"><property name="title"><string>POWDER FEED MOTOR</string></property>
            <layout class="QVBoxLayout">
                <item>
                    <layout class="QHBoxLayout">
                        <item><widget class="QLabel"><property name="text"><string>[Icon]</string></property></widget></item>
                        <item>
                            <layout class="QFormLayout">
                                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Status</string></property></widget></item>
                                <item row="0" column="1"><widget class="QLabel"><property name="text"><string>Enabled</string></property></widget></item>
                                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Position</string></property></widget></item>
                                <item row="1" column="1"><widget class="QLabel"><property name="text"><string>45.670 mm</string></property></widget></item>
                                <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Velocity</string></property></widget></item>
                                <item row="2" column="1"><widget class="QLabel"><property name="text"><string>1.5 mm/s</string></property></widget></item>
                                <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Current</string></property></widget></item>
                                <item row="3" column="1"><widget class="QLabel"><property name="text"><string>1.02 A</string></property></widget></item>
                                <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Load</string></property></widget></item>
                                <item row="4" column="1"><widget class="QLabel"><property name="text"><string>16 %</string></property></widget></item>
                            </layout>
                        </item>
                    </layout>
                </item>
                <item><widget class="QLabel"><property name="text"><string>Control</string></property></widget></item>
                <item>
                    <layout class="QHBoxLayout">
                        <item><widget class="QPushButton"><property name="text"><string>Home</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Raise</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Lower</string></property></widget></item>
                    </layout>
                </item>
                <item><widget class="QLabel"><property name="text"><string>Jog</string></property></widget></item>
                <item>
                    <layout class="QHBoxLayout">
                        <item><widget class="QPushButton"><property name="text"><string>-10</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>-1</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>+1</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>+10</string></property></widget></item>
                    </layout>
                </item>
            </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_motor_recoater"><property name="title"><string>RECOATER MOTOR</string></property>
            <layout class="QVBoxLayout">
                <item>
                    <layout class="QHBoxLayout">
                        <item><widget class="QLabel"><property name="text"><string>[Icon]</string></property></widget></item>
                        <item>
                            <layout class="QFormLayout">
                                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Status</string></property></widget></item>
                                <item row="0" column="1"><widget class="QLabel"><property name="text"><string>Enabled</string></property></widget></item>
                                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Position</string></property></widget></item>
                                <item row="1" column="1"><widget class="QLabel"><property name="text"><string>0.000 mm</string></property></widget></item>
                                <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Velocity</string></property></widget></item>
                                <item row="2" column="1"><widget class="QLabel"><property name="text"><string>150.0 mm/s</string></property></widget></item>
                                <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Current</string></property></widget></item>
                                <item row="3" column="1"><widget class="QLabel"><property name="text"><string>1.80 A</string></property></widget></item>
                                <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Load</string></property></widget></item>
                                <item row="4" column="1"><widget class="QLabel"><property name="text"><string>22 %</string></property></widget></item>
                            </layout>
                        </item>
                    </layout>
                </item>
                <item><widget class="QLabel"><property name="text"><string>Control</string></property></widget></item>
                <item>
                    <layout class="QHBoxLayout">
                        <item><widget class="QPushButton"><property name="text"><string>Home</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Left</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Right</string></property></widget></item>
                    </layout>
                </item>
                <item><widget class="QLabel"><property name="text"><string>Jog</string></property></widget></item>
                <item>
                    <layout class="QHBoxLayout">
                        <item><widget class="QPushButton"><property name="text"><string>-10</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>-1</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>+1</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>+10</string></property></widget></item>
                    </layout>
                </item>
            </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_motor_piston"><property name="title"><string>POWDER FEED PISTON MOTOR</string></property>
            <layout class="QVBoxLayout">
                <item>
                    <layout class="QHBoxLayout">
                        <item><widget class="QLabel"><property name="text"><string>[Icon]</string></property></widget></item>
                        <item>
                            <layout class="QFormLayout">
                                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Status</string></property></widget></item>
                                <item row="0" column="1"><widget class="QLabel"><property name="text"><string>Enabled</string></property></widget></item>
                                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Position</string></property></widget></item>
                                <item row="1" column="1"><widget class="QLabel"><property name="text"><string>12.450 mm</string></property></widget></item>
                                <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Velocity</string></property></widget></item>
                                <item row="2" column="1"><widget class="QLabel"><property name="text"><string>2.5 mm/s</string></property></widget></item>
                                <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Current</string></property></widget></item>
                                <item row="3" column="1"><widget class="QLabel"><property name="text"><string>0.85 A</string></property></widget></item>
                                <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Load</string></property></widget></item>
                                <item row="4" column="1"><widget class="QLabel"><property name="text"><string>12 %</string></property></widget></item>
                            </layout>
                        </item>
                    </layout>
                </item>
                <item><widget class="QLabel"><property name="text"><string>Control</string></property></widget></item>
                <item>
                    <layout class="QHBoxLayout">
                        <item><widget class="QPushButton"><property name="text"><string>Home</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Extend</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Retract</string></property></widget></item>
                    </layout>
                </item>
                <item><widget class="QLabel"><property name="text"><string>Jog</string></property></widget></item>
                <item>
                    <layout class="QHBoxLayout">
                        <item><widget class="QPushButton"><property name="text"><string>-10</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>-1</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>+1</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>+10</string></property></widget></item>
                    </layout>
                </item>
            </layout>
        </widget>
      </item>
    </layout>
  </item>

  <!-- MIDDLE ROW -->
  <item>
    <layout class="QHBoxLayout">
        <item>
            <widget class="QGroupBox" name="gb_motors_overview"><property name="title"><string>MOTORS OVERVIEW</string></property>
                <layout class="QVBoxLayout">
                    <item>
                        <widget class="QTableWidget">
                            <property name="columnCount"><number>6</number></property>
                            <column><property name="text"><string>Motor</string></property></column>
                            <column><property name="text"><string>Status</string></property></column>
                            <column><property name="text"><string>Position</string></property></column>
                            <column><property name="text"><string>Velocity</string></property></column>
                            <column><property name="text"><string>Current</string></property></column>
                            <column><property name="text"><string>Load</string></property></column>
                        </widget>
                    </item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_motor_diag"><property name="title"><string>MOTOR DIAGNOSTICS</string></property>
                <layout class="QFormLayout">
                    <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Driver Status</string></property></widget></item>
                    <item row="0" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                    <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Encoder Status</string></property></widget></item>
                    <item row="1" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                    <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Overcurrent</string></property></widget></item>
                    <item row="2" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                    <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Overvoltage</string></property></widget></item>
                    <item row="3" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                    <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Temperature</string></property></widget></item>
                    <item row="4" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                    <item row="5" column="0"><widget class="QLabel"><property name="text"><string>Communication</string></property></widget></item>
                    <item row="5" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                    <item row="6" column="0"><widget class="QLabel"><property name="text"><string>Limit Switch</string></property></widget></item>
                    <item row="6" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_motor_temp"><property name="title"><string>TEMPERATURES</string></property>
                <layout class="QFormLayout">
                    <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Build Motor</string></property></widget></item>
                    <item row="0" column="1"><widget class="QLabel"><property name="text"><string>32.1 C [Bar]</string></property></widget></item>
                    <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Feed Motor</string></property></widget></item>
                    <item row="1" column="1"><widget class="QLabel"><property name="text"><string>30.4 C [Bar]</string></property></widget></item>
                    <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Recoater Motor</string></property></widget></item>
                    <item row="2" column="1"><widget class="QLabel"><property name="text"><string>33.6 C [Bar]</string></property></widget></item>
                    <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Piston Motor</string></property></widget></item>
                    <item row="3" column="1"><widget class="QLabel"><property name="text"><string>28.7 C [Bar]</string></property></widget></item>
                    <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Z Lift Motor</string></property></widget></item>
                    <item row="4" column="1"><widget class="QLabel"><property name="text"><string>31.2 C [Bar]</string></property></widget></item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_motor_actions"><property name="title"><string>ACTIONS</string></property>
                <layout class="QVBoxLayout">
                    <item><widget class="QPushButton"><property name="text"><string>Home All Axes</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Disable All Motors</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Reset All Alarms</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Clear Faults</string></property></widget></item>
                </layout>
            </widget>
        </item>
    </layout>
  </item>

  <!-- BOTTOM ROW -->
  <item>
    <layout class="QHBoxLayout">
        <item>
            <widget class="QGroupBox" name="gb_motor_graph"><property name="title"><string>MOTOR GRAPH</string></property>
                <layout class="QVBoxLayout">
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QPushButton"><property name="text"><string>Position</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Velocity</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Current</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Load</string></property></widget></item>
                            <item><spacer><property name="orientation"><enum>Qt::Horizontal</enum></property></spacer></item>
                        </layout>
                    </item>
                    <item><widget class="QLabel"><property name="text"><string>[Graph Placeholder]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property><property name="minimumHeight"><number>150</number></property></widget></item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_graph_settings"><property name="title"><string>GRAPH SETTINGS</string></property>
                <layout class="QFormLayout">
                    <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Time Range</string></property></widget></item>
                    <item row="0" column="1"><widget class="QComboBox"/></item>
                    <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Auto Refresh</string></property></widget></item>
                    <item row="1" column="1"><widget class="QCheckBox"/></item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_motor_info"><property name="title"><string>MOTOR INFORMATION</string></property>
                <layout class="QFormLayout">
                    <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Total Motors</string></property></widget></item>
                    <item row="0" column="1"><widget class="QLabel"><property name="text"><string>6</string></property></widget></item>
                    <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Enabled Motors</string></property></widget></item>
                    <item row="1" column="1"><widget class="QLabel"><property name="text"><string>5</string></property></widget></item>
                    <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Disabled Motors</string></property></widget></item>
                    <item row="2" column="1"><widget class="QLabel"><property name="text"><string>1</string></property></widget></item>
                    <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Active Alarms</string></property></widget></item>
                    <item row="3" column="1"><widget class="QLabel"><property name="text"><string>0</string></property></widget></item>
                    <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Total Faults</string></property></widget></item>
                    <item row="4" column="1"><widget class="QLabel"><property name="text"><string>0</string></property></widget></item>
                </layout>
            </widget>
        </item>
    </layout>
  </item>
</layout>
"""
    new_layout = ET.fromstring(xml)
    page.append(new_layout)
    print("Injected motors page")

def inject_sensors(root):
    page = clear_page(root, 'page_sensors')
    if page is None: return
    
    xml = """
<layout class="QVBoxLayout" name="vLayout_sensors">
  <!-- TOP ROW -->
  <item>
    <layout class="QHBoxLayout">
      <item>
        <widget class="QGroupBox" name="gb_env"><property name="title"><string>ENVIRONMENT</string></property>
            <layout class="QFormLayout">
                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Chamber Temperature</string></property></widget></item>
                <item row="0" column="1"><widget class="QLabel"><property name="text"><string>32.5 C</string></property></widget></item>
                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Set Temperature</string></property></widget></item>
                <item row="1" column="1"><widget class="QLabel"><property name="text"><string>35.0 C</string></property></widget></item>
                <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Humidity</string></property></widget></item>
                <item row="2" column="1"><widget class="QLabel"><property name="text"><string>15.3 %</string></property></widget></item>
                <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Oxygen Level</string></property></widget></item>
                <item row="3" column="1"><widget class="QLabel"><property name="text"><string>0.05 %</string></property></widget></item>
                <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Pressure</string></property></widget></item>
                <item row="4" column="1"><widget class="QLabel"><property name="text"><string>-0.02 bar</string></property></widget></item>
                <item row="5" column="0"><widget class="QLabel"><property name="text"><string>Atmospheric Pressure</string></property></widget></item>
                <item row="5" column="1"><widget class="QLabel"><property name="text"><string>1.02 bar</string></property></widget></item>
            </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_gas"><property name="title"><string>GAS SYSTEM</string></property>
            <layout class="QFormLayout">
                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Argon Pressure</string></property></widget></item>
                <item row="0" column="1"><widget class="QLabel"><property name="text"><string>12.3 bar</string></property></widget></item>
                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Argon Flow</string></property></widget></item>
                <item row="1" column="1"><widget class="QLabel"><property name="text"><string>12.5 L/min</string></property></widget></item>
                <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Nitrogen Pressure</string></property></widget></item>
                <item row="2" column="1"><widget class="QLabel"><property name="text"><string>11.8 bar</string></property></widget></item>
                <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Gas Inlet Pressure</string></property></widget></item>
                <item row="3" column="1"><widget class="QLabel"><property name="text"><string>12.1 bar</string></property></widget></item>
                <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Gas Outlet Pressure</string></property></widget></item>
                <item row="4" column="1"><widget class="QLabel"><property name="text"><string>11.9 bar</string></property></widget></item>
                <item row="5" column="0"><widget class="QLabel"><property name="text"><string>Gas Purity (O2)</string></property></widget></item>
                <item row="5" column="1"><widget class="QLabel"><property name="text"><string>0.05 %</string></property></widget></item>
            </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_powder"><property name="title"><string>POWDER SYSTEM</string></property>
            <layout class="QFormLayout">
                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Powder Level</string></property></widget></item>
                <item row="0" column="1"><widget class="QLabel"><property name="text"><string>78 % [Bar]</string></property></widget></item>
                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Overflow Sensor</string></property></widget></item>
                <item row="1" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Hopper Level Sensor</string></property></widget></item>
                <item row="2" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Feed Piston Upper Limit</string></property></widget></item>
                <item row="3" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Feed Piston Lower Limit</string></property></widget></item>
                <item row="4" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
            </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_door"><property name="title"><string>CHAMBER DOOR</string></property>
            <layout class="QFormLayout">
                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Door Status</string></property></widget></item>
                <item row="0" column="1"><widget class="QLabel"><property name="text"><string>Closed &amp; Locked</string></property></widget></item>
                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Door Lock</string></property></widget></item>
                <item row="1" column="1"><widget class="QLabel"><property name="text"><string>Locked</string></property></widget></item>
                <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Safety Interlock</string></property></widget></item>
                <item row="2" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Door Seal Pressure</string></property></widget></item>
                <item row="3" column="1"><widget class="QLabel"><property name="text"><string>-0.01 bar</string></property></widget></item>
            </layout>
        </widget>
      </item>
    </layout>
  </item>

  <!-- MIDDLE ROW -->
  <item>
    <layout class="QHBoxLayout">
      <item>
        <widget class="QGroupBox" name="gb_safety"><property name="title"><string>SAFETY SYSTEMS</string></property>
            <layout class="QFormLayout">
                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Emergency Stop</string></property></widget></item>
                <item row="0" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Safety PLC</string></property></widget></item>
                <item row="1" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Laser Safety Interlock</string></property></widget></item>
                <item row="2" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Door Interlock</string></property></widget></item>
                <item row="3" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Gas Pressure Switch</string></property></widget></item>
                <item row="4" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="5" column="0"><widget class="QLabel"><property name="text"><string>Over Temp Switch</string></property></widget></item>
                <item row="5" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="6" column="0"><widget class="QLabel"><property name="text"><string>Smoke Detector</string></property></widget></item>
                <item row="6" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="7" column="0"><widget class="QLabel"><property name="text"><string>Fire Suppression</string></property></widget></item>
                <item row="7" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="8" column="0"><widget class="QLabel"><property name="text"><string>Power Supply Status</string></property></widget></item>
                <item row="8" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                <item row="9" column="0"><widget class="QLabel"><property name="text"><string>Ground Fault</string></property></widget></item>
                <item row="9" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
            </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_temps"><property name="title"><string>TEMPERATURES</string></property>
            <layout class="QGridLayout">
                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Laser Head Temp.\n25.2 C</string></property></widget></item>
                <item row="0" column="1"><widget class="QLabel"><property name="text"><string>Chiller Inlet Temp.\n22.1 C</string></property></widget></item>
                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Galvo Driver Temp.\n27.2 C</string></property></widget></item>
                <item row="1" column="1"><widget class="QLabel"><property name="text"><string>Chiller Outlet Temp.\n24.8 C</string></property></widget></item>
                <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Power Supply Temp.\n31.4 C</string></property></widget></item>
                <item row="2" column="1"><widget class="QLabel"><property name="text"><string>Powder Bed Temp.\n32.5 C</string></property></widget></item>
                <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Control Cabinet Temp.\n30.1 C</string></property></widget></item>
                <item row="3" column="1"><widget class="QLabel"><property name="text"><string>Recoater Motor Temp.\n33.6 C</string></property></widget></item>
            </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_misc"><property name="title"><string>MISCELLANEOUS</string></property>
            <layout class="QFormLayout">
                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>UPS Status</string></property></widget></item>
                <item row="0" column="1"><widget class="QLabel"><property name="text"><string>Normal</string></property></widget></item>
                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Main Power</string></property></widget></item>
                <item row="1" column="1"><widget class="QLabel"><property name="text"><string>ON</string></property></widget></item>
                <item row="2" column="0"><widget class="QLabel"><property name="text"><string>24V Power Supply</string></property></widget></item>
                <item row="2" column="1"><widget class="QLabel"><property name="text"><string>24.1 V</string></property></widget></item>
                <item row="3" column="0"><widget class="QLabel"><property name="text"><string>5V Power Supply</string></property></widget></item>
                <item row="3" column="1"><widget class="QLabel"><property name="text"><string>5.02 V</string></property></widget></item>
                <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Battery Voltage</string></property></widget></item>
                <item row="4" column="1"><widget class="QLabel"><property name="text"><string>25.6 V</string></property></widget></item>
                <item row="5" column="0"><widget class="QLabel"><property name="text"><string>Air Pressure</string></property></widget></item>
                <item row="5" column="1"><widget class="QLabel"><property name="text"><string>6.5 bar</string></property></widget></item>
                <item row="6" column="0"><widget class="QLabel"><property name="text"><string>Water Flow (Chiller)</string></property></widget></item>
                <item row="6" column="1"><widget class="QLabel"><property name="text"><string>2.35 L/min</string></property></widget></item>
                <item row="7" column="0"><widget class="QLabel"><property name="text"><string>Filter Diff. Pressure</string></property></widget></item>
                <item row="7" column="1"><widget class="QLabel"><property name="text"><string>78 Pa</string></property></widget></item>
            </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_sensor_overview"><property name="title"><string>SENSOR STATUS OVERVIEW</string></property>
            <layout class="QHBoxLayout">
                <item><widget class="QLabel"><property name="text"><string>[Pie Chart]</string></property></widget></item>
                <item>
                    <layout class="QFormLayout">
                        <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Normal</string></property></widget></item>
                        <item row="0" column="1"><widget class="QLabel"><property name="text"><string>42</string></property></widget></item>
                        <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Warning</string></property></widget></item>
                        <item row="1" column="1"><widget class="QLabel"><property name="text"><string>2</string></property></widget></item>
                        <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Fault</string></property></widget></item>
                        <item row="2" column="1"><widget class="QLabel"><property name="text"><string>1</string></property></widget></item>
                        <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Total Sensors</string></property></widget></item>
                        <item row="3" column="1"><widget class="QLabel"><property name="text"><string>45</string></property></widget></item>
                    </layout>
                </item>
            </layout>
        </widget>
      </item>
    </layout>
  </item>

  <!-- BOTTOM ROW -->
  <item>
    <layout class="QHBoxLayout">
      <item>
        <widget class="QGroupBox" name="gb_history"><property name="title"><string>SENSOR HISTORY (Last 1 Hour)</string></property>
            <layout class="QVBoxLayout">
                <item><widget class="QLabel"><property name="text"><string>[Line Chart]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property><property name="minimumHeight"><number>120</number></property></widget></item>
            </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_filter"><property name="title"><string>SENSOR FILTER</string></property>
            <layout class="QFormLayout">
                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Category</string></property></widget></item>
                <item row="0" column="1"><widget class="QComboBox"/></item>
                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Status</string></property></widget></item>
                <item row="1" column="1"><widget class="QComboBox"/></item>
                <item row="2" column="0" colspan="2"><widget class="QPushButton"><property name="text"><string>Reset Filters</string></property></widget></item>
            </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_calibration_sensors"><property name="title"><string>SENSOR CALIBRATION</string></property>
            <layout class="QVBoxLayout">
                <item>
                    <widget class="QTableWidget">
                        <property name="columnCount"><number>4</number></property>
                        <column><property name="text"><string>Sensor</string></property></column>
                        <column><property name="text"><string>Last Calibrated</string></property></column>
                        <column><property name="text"><string>Next Due</string></property></column>
                        <column><property name="text"><string>Status</string></property></column>
                    </widget>
                </item>
                <item><widget class="QPushButton"><property name="text"><string>View All Calibration</string></property></widget></item>
            </layout>
        </widget>
      </item>
    </layout>
  </item>
</layout>
"""
    new_layout = ET.fromstring(xml)
    page.append(new_layout)
    print("Injected sensors page")

if __name__ == '__main__':
    file_path = 'metal_dashboard.ui'
    tree = ET.parse(file_path)
    root = tree.getroot()
    inject_laser_galvo(root)
    inject_motors(root)
    inject_sensors(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print("Batch 2 completed!")
