import xml.etree.ElementTree as ET
import sys

def inject_dashboard(root):
    # Find page_dashboard
    page = None
    for widget in root.iter('widget'):
        if widget.get('name') == 'page_dashboard':
            page = widget
            break
            
    if page is None:
        print("Could not find page_dashboard")
        return
        
    for child in list(page):
        if child.tag not in ('property', 'attribute'):
            page.remove(child)
            
    xml = """
<layout class="QGridLayout" name="gridLayout_page_dashboard">
  <!-- TOP ROW -->
  <item row="0" column="0">
    <widget class="QGroupBox" name="gb_machine_status"><property name="title"><string>MACHINE STATUS</string></property>
      <layout class="QHBoxLayout">
        <item><widget class="QLabel" name="lbl_status_icon"><property name="text"><string>[Icon]</string></property></widget></item>
        <item><widget class="QLabel" name="lbl_status_text"><property name="text"><string>&lt;b&gt;Ready&lt;/b&gt;&lt;br&gt;All systems normal</string></property></widget></item>
      </layout>
    </widget>
  </item>
  <item row="0" column="1">
    <widget class="QGroupBox" name="gb_build_progress"><property name="title"><string>BUILD PROGRESS</string></property>
      <layout class="QHBoxLayout">
        <item><widget class="QLabel" name="lbl_prog_circle"><property name="text"><string>19%</string></property></widget></item>
        <item>
          <layout class="QFormLayout">
            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Layer</string></property></widget></item>
            <item row="0" column="1"><widget class="QLabel"><property name="text"><string>245 / 1250</string></property></widget></item>
            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Time Elapsed</string></property></widget></item>
            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>01:24:30</string></property></widget></item>
            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Est. Remaining</string></property></widget></item>
            <item row="2" column="1"><widget class="QLabel"><property name="text"><string>05:38:15</string></property></widget></item>
          </layout>
        </item>
      </layout>
    </widget>
  </item>
  <item row="0" column="2">
    <widget class="QGroupBox" name="gb_laser_power_dash"><property name="title"><string>LASER POWER</string></property>
      <layout class="QVBoxLayout">
        <item><widget class="QLabel" name="lbl_laser_gauge"><property name="text"><string>195 W</string></property></widget></item>
        <item><widget class="QLabel"><property name="text"><string>Set: 200 W</string></property></widget></item>
      </layout>
    </widget>
  </item>
  <item row="0" column="3">
    <widget class="QGroupBox" name="gb_chamber_temp_dash"><property name="title"><string>CHAMBER TEMP.</string></property>
      <layout class="QFormLayout">
            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Temp</string></property></widget></item>
            <item row="0" column="1"><widget class="QLabel"><property name="text"><string>&lt;b&gt;32.5 C&lt;/b&gt;</string></property></widget></item>
            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Set</string></property></widget></item>
            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>35 C</string></property></widget></item>
            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Gas/Flow</string></property></widget></item>
            <item row="2" column="1"><widget class="QLabel"><property name="text"><string>Argon 12.5 L/min</string></property></widget></item>
      </layout>
    </widget>
  </item>
  <item row="0" column="4">
    <widget class="QGroupBox" name="gb_oxygen_level_dash"><property name="title"><string>OXYGEN LEVEL</string></property>
      <layout class="QVBoxLayout">
        <item><widget class="QLabel" name="lbl_oxy_gauge"><property name="text"><string>&lt;b&gt;0.05 %&lt;/b&gt;</string></property></widget></item>
        <item><widget class="QLabel"><property name="text"><string>Target: &lt; 0.10%</string></property></widget></item>
      </layout>
    </widget>
  </item>

  <!-- MIDDLE ROW -->
  <item row="1" column="0" colspan="3">
    <widget class="QGroupBox" name="gb_build_preview_dash"><property name="title"><string>BUILD PREVIEW</string></property>
      <layout class="QVBoxLayout">
        <item>
            <layout class="QHBoxLayout">
                <item>
                    <layout class="QVBoxLayout">
                        <item><widget class="QPushButton"><property name="text"><string>Rotate</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Pan</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Zoom</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Top</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Front</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Right</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Reset</string></property></widget></item>
                    </layout>
                </item>
                <item><widget class="QLabel"><property name="text"><string>3D PREVIEW GRAPHIC</string></property><property name="alignment"><set>Qt::AlignCenter</set></property><property name="minimumSize"><size><width>300</width><height>200</height></size></property></widget></item>
                <item><widget class="QSlider"><property name="orientation"><enum>Qt::Vertical</enum></property></widget></item>
            </layout>
        </item>
        <item>
            <layout class="QHBoxLayout">
                <item><widget class="QCheckBox"><property name="text"><string>Show Travels</string></property></widget></item>
                <item><widget class="QCheckBox"><property name="text"><string>Show Layers</string></property></widget></item>
                <item><widget class="QSlider"><property name="orientation"><enum>Qt::Horizontal</enum></property></widget></item>
                <item><widget class="QLabel"><property name="text"><string>Layer: 245</string></property></widget></item>
            </layout>
        </item>
      </layout>
    </widget>
  </item>
  
  <item row="1" column="3">
    <layout class="QVBoxLayout">
        <item>
            <widget class="QGroupBox" name="gb_axis_position"><property name="title"><string>AXIS POSITION (mm)</string></property>
                <layout class="QGridLayout">
                    <item row="0" column="0"><widget class="QLabel"><property name="text"><string>X</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
                    <item row="0" column="1"><widget class="QLabel"><property name="text"><string>Y</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
                    <item row="0" column="2"><widget class="QLabel"><property name="text"><string>Z</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
                    <item row="1" column="0"><widget class="QLineEdit"><property name="text"><string>125.300</string></property></widget></item>
                    <item row="1" column="1"><widget class="QLineEdit"><property name="text"><string>83.450</string></property></widget></item>
                    <item row="1" column="2"><widget class="QLineEdit"><property name="text"><string>45.670</string></property></widget></item>
                    <item row="2" column="0" colspan="2"><widget class="QPushButton"><property name="text"><string>Home All</string></property></widget></item>
                    <item row="2" column="2"><widget class="QPushButton"><property name="text"><string>Go to Zero</string></property></widget></item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_jog_control"><property name="title"><string>JOG CONTROL</string></property>
                <layout class="QVBoxLayout">
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QPushButton"><property name="text"><string>0.1</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>1.0</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>10.0</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>100.0</string></property></widget></item>
                        </layout>
                    </item>
                    <item>
                        <layout class="QGridLayout">
                            <item row="0" column="1"><widget class="QPushButton"><property name="text"><string>+Y</string></property></widget></item>
                            <item row="1" column="0"><widget class="QPushButton"><property name="text"><string>-X</string></property></widget></item>
                            <item row="1" column="1"><widget class="QPushButton"><property name="text"><string>XY</string></property></widget></item>
                            <item row="1" column="2"><widget class="QPushButton"><property name="text"><string>+X</string></property></widget></item>
                            <item row="2" column="1"><widget class="QPushButton"><property name="text"><string>-Y</string></property></widget></item>
                            
                            <item row="0" column="3"><widget class="QPushButton"><property name="text"><string>+Z</string></property></widget></item>
                            <item row="2" column="3"><widget class="QPushButton"><property name="text"><string>-Z</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </widget>
        </item>
    </layout>
  </item>
  
  <item row="1" column="4">
    <layout class="QVBoxLayout">
        <item>
            <widget class="QGroupBox" name="gb_job_control"><property name="title"><string>JOB CONTROL</string></property>
                <layout class="QVBoxLayout">
                    <item><widget class="QPushButton"><property name="text"><string>Start / Resume</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Pause</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Stop</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Abort Job</string></property></widget></item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_layer_control_dash"><property name="title"><string>LAYER CONTROL</string></property>
                <layout class="QVBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>245 / 1250</string></property></widget></item>
                    <item><widget class="QSlider"><property name="orientation"><enum>Qt::Horizontal</enum></property></widget></item>
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QPushButton"><property name="text"><string>-10</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>-1</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>+1</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>+10</string></property></widget></item>
                        </layout>
                    </item>
                    <item><widget class="QPushButton"><property name="text"><string>Go to Layer</string></property></widget></item>
                </layout>
            </widget>
        </item>
    </layout>
  </item>

  <!-- BOTTOM ROW -->
  <item row="2" column="0" colspan="4">
    <widget class="QGroupBox" name="gb_console_log"><property name="title"><string>CONSOLE LOG</string></property>
        <layout class="QVBoxLayout">
            <item><widget class="QTextEdit"><property name="text"><string>[10:46:23] Layer 245 in progress...</string></property></widget></item>
            <item>
                <layout class="QHBoxLayout">
                    <item><spacer><property name="orientation"><enum>Qt::Horizontal</enum></property></spacer></item>
                    <item><widget class="QPushButton"><property name="text"><string>Clear</string></property></widget></item>
                    <item><widget class="QCheckBox"><property name="text"><string>Auto Scroll</string></property></widget></item>
                </layout>
            </item>
        </layout>
    </widget>
  </item>
  
  <item row="2" column="4">
    <widget class="QGroupBox" name="gb_overrides"><property name="title"><string>OVERRIDES</string></property>
        <layout class="QHBoxLayout">
            <item><widget class="QLabel"><property name="text"><string>Laser: 100%</string></property></widget></item>
            <item><widget class="QLabel"><property name="text"><string>Scan: 100%</string></property></widget></item>
            <item><widget class="QLabel"><property name="text"><string>Hatch: 100%</string></property></widget></item>
        </layout>
    </widget>
  </item>

</layout>
"""
    new_layout = ET.fromstring(xml)
    page.append(new_layout)
    print("Injected dashboard page")

def inject_machine_control(root):
    # Find page_machine_control
    page = None
    for widget in root.iter('widget'):
        if widget.get('name') == 'page_machine_control':
            page = widget
            break
            
    if page is None:
        print("Could not find page_machine_control")
        return
        
    for child in list(page):
        if child.tag not in ('property', 'attribute'):
            page.remove(child)
            
    xml = """
<layout class="QVBoxLayout" name="vLayout_page_mc">
  <!-- TOP ROW -->
  <item>
    <layout class="QHBoxLayout">
        <item>
            <widget class="QGroupBox" name="gb_build_platform"><property name="title"><string>BUILD PLATFORM</string></property>
                <layout class="QVBoxLayout">
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>Position\n125.300 mm</string></property></widget></item>
                            <item><widget class="QLabel"><property name="text"><string>Status\nReady</string></property></widget></item>
                        </layout>
                    </item>
                    <item>
                        <layout class="QHBoxLayout">
                            <item>
                                <layout class="QVBoxLayout">
                                    <item><widget class="QPushButton"><property name="text"><string>Move Up</string></property></widget></item>
                                    <item><widget class="QPushButton"><property name="text"><string>Move Down</string></property></widget></item>
                                    <item><widget class="QPushButton"><property name="text"><string>Home</string></property></widget></item>
                                    <item><widget class="QPushButton"><property name="text"><string>Move To...</string></property></widget></item>
                                </layout>
                            </item>
                            <item><widget class="QLabel"><property name="text"><string>[Graphic]</string></property></widget></item>
                            <item><widget class="QSlider"><property name="orientation"><enum>Qt::Vertical</enum></property></widget></item>
                        </layout>
                    </item>
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>Target (mm)</string></property></widget></item>
                            <item><widget class="QLineEdit"><property name="text"><string>125.300</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Go</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_powder_feed"><property name="title"><string>POWDER FEED</string></property>
                <layout class="QVBoxLayout">
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>Position\n45.670 mm</string></property></widget></item>
                            <item><widget class="QLabel"><property name="text"><string>Status\nReady</string></property></widget></item>
                        </layout>
                    </item>
                    <item>
                        <layout class="QHBoxLayout">
                            <item>
                                <layout class="QVBoxLayout">
                                    <item><widget class="QPushButton"><property name="text"><string>Raise</string></property></widget></item>
                                    <item><widget class="QPushButton"><property name="text"><string>Lower</string></property></widget></item>
                                    <item><widget class="QPushButton"><property name="text"><string>Home</string></property></widget></item>
                                </layout>
                            </item>
                            <item><widget class="QLabel"><property name="text"><string>[Graphic]</string></property></widget></item>
                            <item><widget class="QSlider"><property name="orientation"><enum>Qt::Vertical</enum></property></widget></item>
                        </layout>
                    </item>
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>Target (mm)</string></property></widget></item>
                            <item><widget class="QLineEdit"><property name="text"><string>45.670</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Go</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_recoater"><property name="title"><string>RECOATER</string></property>
                <layout class="QVBoxLayout">
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>Position\n0.00 mm</string></property></widget></item>
                            <item><widget class="QLabel"><property name="text"><string>Status\nReady</string></property></widget></item>
                        </layout>
                    </item>
                    <item><widget class="QLabel"><property name="text"><string>[Recoater Graphic]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QPushButton"><property name="text"><string>Move Left</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Move Right</string></property></widget></item>
                        </layout>
                    </item>
                    <item><widget class="QPushButton"><property name="text"><string>Home Recoater</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Single Spread Cycle</string></property></widget></item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_chamber_door"><property name="title"><string>CHAMBER DOOR</string></property>
                <layout class="QVBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>Status\nClosed &amp; Locked</string></property></widget></item>
                    <item><widget class="QLabel"><property name="text"><string>[Door Graphic]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Unlock</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Open Door</string></property><property name="enabled"><bool>false</bool></property></widget></item>
                </layout>
            </widget>
        </item>
    </layout>
  </item>

  <!-- MIDDLE ROW -->
  <item>
    <layout class="QHBoxLayout">
        <item>
            <widget class="QGroupBox" name="gb_gas_system"><property name="title"><string>GAS SYSTEM</string></property>
                <layout class="QHBoxLayout">
                    <item>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Argon Pressure</string></property></widget></item>
                            <item row="0" column="1"><widget class="QLabel"><property name="text"><string>12.3 bar</string></property></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Argon Flow</string></property></widget></item>
                            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>12.5 L/min</string></property></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Nitrogen Pressure</string></property></widget></item>
                            <item row="2" column="1"><widget class="QLabel"><property name="text"><string>11.8 bar</string></property></widget></item>
                            <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Chamber Pressure</string></property></widget></item>
                            <item row="3" column="1"><widget class="QLabel"><property name="text"><string>-0.02 bar</string></property></widget></item>
                        </layout>
                    </item>
                    <item>
                        <layout class="QVBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>PURGE CONTROL</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Start Purge</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Stop Purge</string></property></widget></item>
                            <item>
                                <layout class="QHBoxLayout">
                                    <item><widget class="QLabel"><property name="text"><string>Auto Purge</string></property></widget></item>
                                    <item><widget class="QCheckBox"><property name="text"><string></string></property><property name="checked"><bool>true</bool></property></widget></item>
                                </layout>
                            </item>
                            <item><widget class="QLabel"><property name="text"><string>Elapsed 00:05:32</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_environment_control"><property name="title"><string>ENVIRONMENT CONTROL</string></property>
                <layout class="QHBoxLayout">
                    <item>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Chamber Temp.</string></property></widget></item>
                            <item row="0" column="1"><widget class="QLabel"><property name="text"><string>32.5 C</string></property></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Set Temperature</string></property></widget></item>
                            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>35.0 C</string></property></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Humidity</string></property></widget></item>
                            <item row="2" column="1"><widget class="QLabel"><property name="text"><string>15.3 %</string></property></widget></item>
                            <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Oxygen Level</string></property></widget></item>
                            <item row="3" column="1"><widget class="QLabel"><property name="text"><string>0.05 %</string></property></widget></item>
                        </layout>
                    </item>
                    <item>
                        <layout class="QVBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>TEMPERATURE CONTROL</string></property></widget></item>
                            <item><widget class="QLabel"><property name="text"><string>Set Temperature (C)</string></property></widget></item>
                            <item>
                                <layout class="QHBoxLayout">
                                    <item><widget class="QLineEdit"><property name="text"><string>35.0</string></property></widget></item>
                                    <item><widget class="QPushButton"><property name="text"><string>Apply</string></property></widget></item>
                                </layout>
                            </item>
                            <item><widget class="QLabel"><property name="text"><string>Heater Status: ON</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_auxiliary_systems"><property name="title"><string>AUXILIARY SYSTEMS</string></property>
                <layout class="QGridLayout">
                    <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Filter Unit</string></property></widget></item>
                    <item row="0" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                    <item row="0" column="2"><widget class="QPushButton"><property name="text"><string>Details</string></property></widget></item>
                    <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Powder Vac System</string></property></widget></item>
                    <item row="1" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                    <item row="1" column="2"><widget class="QPushButton"><property name="text"><string>Details</string></property></widget></item>
                    <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Cooling System</string></property></widget></item>
                    <item row="2" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                    <item row="2" column="2"><widget class="QPushButton"><property name="text"><string>Details</string></property></widget></item>
                    <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Exhaust System</string></property></widget></item>
                    <item row="3" column="1"><widget class="QLabel"><property name="text"><string>OK</string></property></widget></item>
                    <item row="3" column="2"><widget class="QPushButton"><property name="text"><string>Details</string></property></widget></item>
                </layout>
            </widget>
        </item>
    </layout>
  </item>

  <!-- BOTTOM ROW -->
  <item>
    <widget class="QGroupBox" name="gb_quick_actions"><property name="title"><string>QUICK ACTIONS</string></property>
        <layout class="QHBoxLayout">
            <item><widget class="QPushButton"><property name="text"><string>System Home</string></property></widget></item>
            <item><widget class="QPushButton"><property name="text"><string>Safe Position</string></property></widget></item>
            <item><widget class="QPushButton"><property name="text"><string>System Check</string></property></widget></item>
            <item><widget class="QPushButton"><property name="text"><string>Zero All Axes</string></property></widget></item>
            <item><widget class="QPushButton"><property name="text"><string>Unlock All</string></property></widget></item>
            <item><widget class="QPushButton"><property name="text"><string>Refresh Status</string></property></widget></item>
        </layout>
    </widget>
  </item>

</layout>
"""
    new_layout = ET.fromstring(xml)
    page.append(new_layout)
    print("Injected machine control page")

if __name__ == '__main__':
    file_path = 'metal_dashboard.ui'
    tree = ET.parse(file_path)
    root = tree.getroot()
    inject_dashboard(root)
    inject_machine_control(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print("Batch 1 completed!")
