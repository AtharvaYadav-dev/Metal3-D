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
<layout class="QVBoxLayout" name="vLayout_page_dashboard" stretch="1,5,1">
  <!-- TOP ROW -->
  <item>
    <layout class="QHBoxLayout" name="hLayout_top">
      <item>
        <widget class="QGroupBox" name="gb_machine_status"><property name="title"><string>MACHINE STATUS</string></property>
          <layout class="QHBoxLayout">
            <item><widget class="QLabel" name="lbl_status_icon"><property name="text"><string>[Icon]</string></property></widget></item>
            <item><widget class="QLabel" name="lbl_status_text"><property name="text"><string>&lt;b&gt;Ready&lt;/b&gt;&lt;br&gt;All systems normal</string></property></widget></item>
          </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_build_progress"><property name="title"><string>BUILD PROGRESS</string></property>
          <layout class="QHBoxLayout">
            <item><widget class="QLabel" name="lbl_prog_circle"><property name="text"><string>[Dial Graphic]</string></property></widget></item>
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
      <item>
        <widget class="QGroupBox" name="gb_laser_power_dash"><property name="title"><string>LASER POWER</string></property>
          <layout class="QVBoxLayout">
            <item><widget class="QLabel" name="lbl_laser_gauge"><property name="text"><string>[Dial Graphic]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
          </layout>
        </widget>
      </item>
      <item>
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
      <item>
        <widget class="QGroupBox" name="gb_oxygen_level_dash"><property name="title"><string>OXYGEN LEVEL</string></property>
          <layout class="QVBoxLayout">
            <item><widget class="QLabel" name="lbl_oxy_gauge"><property name="text"><string>[Dial Graphic]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
          </layout>
        </widget>
      </item>
    </layout>
  </item>

  <!-- MIDDLE ROW -->
  <item>
    <layout class="QHBoxLayout" name="hLayout_middle" stretch="2,1,1">
      <item>
        <widget class="QGroupBox" name="gb_build_preview_dash"><property name="title"><string>BUILD PREVIEW</string></property>
          <layout class="QHBoxLayout">
            <item>
                <layout class="QVBoxLayout">
                    <item><widget class="QPushButton"><property name="text"><string>Rot</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Pan</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Zoom</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Top</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Frt</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Rgt</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Rst</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                    <item><spacer><property name="orientation"><enum>Qt::Vertical</enum></property></spacer></item>
                </layout>
            </item>
            <item>
                <layout class="QVBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>3D PREVIEW GRAPHIC</string></property><property name="alignment"><set>Qt::AlignCenter</set></property><property name="sizePolicy"><sizepolicy hsizetype="Expanding" vsizetype="Expanding"><horstretch>0</horstretch><verstretch>0</verstretch></sizepolicy></property></widget></item>
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QCheckBox"><property name="text"><string>Show Travels</string></property></widget></item>
                            <item><widget class="QCheckBox"><property name="text"><string>Show Layers</string></property></widget></item>
                            <item><widget class="QSlider"><property name="orientation"><enum>Qt::Horizontal</enum></property></widget></item>
                            <item><widget class="QLabel"><property name="text"><string>Layer: 245</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </item>
            <item>
                <widget class="QSlider"><property name="orientation"><enum>Qt::Vertical</enum></property></widget>
            </item>
          </layout>
        </widget>
      </item>
      
      <item>
        <layout class="QVBoxLayout">
            <item>
                <widget class="QGroupBox" name="gb_axis_position"><property name="title"><string>AXIS POSITION (mm)</string></property>
                    <layout class="QGridLayout">
                        <item row="0" column="0"><widget class="QLabel"><property name="text"><string>&lt;font color='#3B82F6'&gt;X&lt;/font&gt;</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
                        <item row="0" column="1"><widget class="QLabel"><property name="text"><string>&lt;font color='#10B981'&gt;Y&lt;/font&gt;</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
                        <item row="0" column="2"><widget class="QLabel"><property name="text"><string>&lt;font color='#F59E0B'&gt;Z&lt;/font&gt;</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
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
                                <item><widget class="QPushButton"><property name="text"><string>1.0</string></property><property name="styleSheet"><string>background-color:#2563EB;</string></property></widget></item>
                                <item><widget class="QPushButton"><property name="text"><string>10.0</string></property></widget></item>
                                <item><widget class="QPushButton"><property name="text"><string>100.0</string></property></widget></item>
                            </layout>
                        </item>
                        <item>
                            <layout class="QHBoxLayout">
                                <item>
                                    <layout class="QGridLayout">
                                        <item row="0" column="1"><widget class="QPushButton"><property name="text"><string>+Y</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                                        <item row="1" column="0"><widget class="QPushButton"><property name="text"><string>-X</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                                        <item row="1" column="1"><widget class="QPushButton"><property name="text"><string>XY</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                                        <item row="1" column="2"><widget class="QPushButton"><property name="text"><string>+X</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                                        <item row="2" column="1"><widget class="QPushButton"><property name="text"><string>-Y</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                                    </layout>
                                </item>
                                <item>
                                    <layout class="QVBoxLayout">
                                        <item><widget class="QPushButton"><property name="text"><string>+Z</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                                        <item><spacer><property name="orientation"><enum>Qt::Vertical</enum></property></spacer></item>
                                        <item><widget class="QPushButton"><property name="text"><string>-Z</string></property><property name="maximumSize"><size><width>45</width><height>30</height></size></property></widget></item>
                                    </layout>
                                </item>
                            </layout>
                        </item>
                    </layout>
                </widget>
            </item>
        </layout>
      </item>
      
      <item>
        <layout class="QVBoxLayout">
            <item>
                <widget class="QGroupBox" name="gb_job_control"><property name="title"><string>JOB CONTROL</string></property>
                    <layout class="QVBoxLayout">
                        <item><widget class="QPushButton"><property name="text"><string>Start / Resume</string></property><property name="styleSheet"><string>background-color:#2563EB; font-weight:bold;</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Pause</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Stop</string></property></widget></item>
                        <item><widget class="QPushButton"><property name="text"><string>Abort Job</string></property></widget></item>
                    </layout>
                </widget>
            </item>
            <item>
                <widget class="QGroupBox" name="gb_layer_control_dash"><property name="title"><string>LAYER CONTROL</string></property>
                    <layout class="QVBoxLayout">
                        <item>
                            <layout class="QHBoxLayout">
                                <item><spacer><property name="orientation"><enum>Qt::Horizontal</enum></property></spacer></item>
                                <item><widget class="QLabel"><property name="text"><string>245 / 1250</string></property></widget></item>
                            </layout>
                        </item>
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
    </layout>
  </item>

  <!-- BOTTOM ROW -->
  <item>
    <layout class="QHBoxLayout" name="hLayout_bottom" stretch="4,1">
      <item>
        <widget class="QGroupBox" name="gb_console_log"><property name="title"><string>CONSOLE LOG</string></property>
            <layout class="QVBoxLayout">
                <item><widget class="QTextEdit"><property name="text"><string>&lt;font color='#10B981'&gt;[10:42:11] System initialized&lt;/font&gt;&lt;br&gt;&lt;font color='#10B981'&gt;[10:42:13] Connection established on COM5&lt;/font&gt;&lt;br&gt;&lt;font color='#3B82F6'&gt;[10:42:15] File loaded: gear_sample.gcode&lt;/font&gt;&lt;br&gt;&lt;font color='#10B981'&gt;[10:42:17] Build job ready&lt;/font&gt;&lt;br&gt;&lt;font color='#10B981'&gt;[10:42:20] Build started&lt;/font&gt;&lt;br&gt;&lt;font color='#3B82F6'&gt;[10:43:33] Layer 100 completed&lt;/font&gt;&lt;br&gt;&lt;font color='#F59E0B'&gt;[10:46:23] Layer 245 in progress&lt;/font&gt;</string></property></widget></item>
                <item>
                    <layout class="QHBoxLayout">
                        <item><spacer><property name="orientation"><enum>Qt::Horizontal</enum></property></spacer></item>
                        <item><widget class="QPushButton"><property name="text"><string>Clear</string></property><property name="maximumSize"><size><width>60</width><height>30</height></size></property></widget></item>
                        <item><widget class="QCheckBox"><property name="text"><string>Auto Scroll</string></property><property name="checked"><bool>true</bool></property></widget></item>
                    </layout>
                </item>
            </layout>
        </widget>
      </item>
      
      <item>
        <widget class="QGroupBox" name="gb_overrides"><property name="title"><string>OVERRIDES</string></property>
            <layout class="QHBoxLayout">
                <item><widget class="QLabel" name="lbl_override_laser"><property name="text"><string>[Dial Graphic]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
                <item><widget class="QLabel" name="lbl_override_scan"><property name="text"><string>[Dial Graphic]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
                <item><widget class="QLabel" name="lbl_override_hatch"><property name="text"><string>[Dial Graphic]</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
            </layout>
        </widget>
      </item>
    </layout>
  </item>
</layout>
"""
    new_layout = ET.fromstring(xml)
    page.append(new_layout)
    print("Injected PERFECT dashboard page")

if __name__ == '__main__':
    file_path = 'metal_dashboard.ui'
    tree = ET.parse(file_path)
    root = tree.getroot()
    inject_dashboard(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print("Rebuild completed!")
