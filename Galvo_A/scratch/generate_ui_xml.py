import os

def generate_metal_dashboard_ui():
    style_path = os.path.join(os.path.dirname(__file__), "..", "style.qss")
    ui_path = os.path.join(os.path.dirname(__file__), "..", "metal_dashboard.ui")

    with open(style_path, "r", encoding="utf-8") as f:
        css = f.read()

    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1380</width>
    <height>850</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Specialize Products Private Limited - Metal 3D Printer</string>
  </property>
  <property name="styleSheet">
   <string><![CDATA[
{css}
   ]]></string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="mainLayout">
    <property name="spacing">
     <number>0</number>
    </property>
    <property name="leftMargin">
     <number>0</number>
    </property>
    <property name="topMargin">
     <number>0</number>
    </property>
    <property name="rightMargin">
     <number>0</number>
    </property>
    <property name="bottomMargin">
     <number>0</number>
    </property>
    <item>
     <!-- TOP HEADER BAR -->
     <widget class="QFrame" name="topNavFrame">
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>60</height>
       </size>
      </property>
      <property name="maximumSize">
       <size>
        <width>16777215</width>
        <height>60</height>
       </size>
      </property>
      <layout class="QHBoxLayout" name="headerLayout">
       <property name="leftMargin">
        <number>16</number>
       </property>
       <property name="topMargin">
        <number>8</number>
       </property>
       <property name="rightMargin">
        <number>16</number>
       </property>
       <property name="bottomMargin">
        <number>8</number>
       </property>
       <item>
        <widget class="QLabel" name="logoLabel">
         <property name="minimumSize">
          <size>
           <width>38</width>
           <height>38</height>
          </size>
         </property>
         <property name="text">
          <string/>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QWidget" name="brandWidget" native="true">
         <layout class="QVBoxLayout" name="brandLayout">
          <property name="spacing">
           <number>2</number>
          </property>
          <property name="leftMargin">
           <number>0</number>
          </property>
          <property name="topMargin">
           <number>0</number>
          </property>
          <property name="rightMargin">
           <number>0</number>
          </property>
          <property name="bottomMargin">
           <number>0</number>
          </property>
          <item>
           <widget class="QLabel" name="titleLabel">
            <property name="font">
             <font>
              <family>Inter</family>
              <pointsize>13</pointsize>
              <bold>true</bold>
             </font>
            </property>
            <property name="styleSheet">
             <string notr="true">color: #b8c4ff; letter-spacing: 0.5px;</string>
            </property>
            <property name="text">
             <string>SPECIALIZE PRODUCTS PRIVATE LIMITED</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLabel" name="subtitleLabel">
            <property name="font">
             <font>
              <family>JetBrains Mono</family>
              <pointsize>9</pointsize>
             </font>
            </property>
            <property name="styleSheet">
             <string notr="true">color: #8e909f;</string>
            </property>
            <property name="text">
             <string>Metal 3D Printer</string>
            </property>
           </widget>
          </item>
         </layout>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="lblStatusBadge">
         <property name="font">
          <font>
           <family>JetBrains Mono</family>
           <pointsize>10</pointsize>
           <bold>true</bold>
          </font>
         </property>
         <property name="styleSheet">
          <string notr="true">background-color: rgba(16,185,129,0.15); color: #10b981; border: 1px solid #10b981; padding: 4px 10px;</string>
         </property>
         <property name="text">
          <string>READY / SIMULATION MODE</string>
         </property>
        </widget>
       </item>
       <item>
        <spacer name="headerSpacer">
         <property name="orientation">
          <enum>Qt::Horizontal</enum>
         </property>
         <property name="sizeHint" stdset="0">
          <size>
           <width>40</width>
           <height>20</height>
          </size>
         </property>
        </spacer>
       </item>
       <item>
        <widget class="QFrame" name="telemetryFrame">
         <layout class="QHBoxLayout" name="telemetryLayout">
          <property name="spacing">
           <number>16</number>
          </property>
          <property name="leftMargin">
           <number>0</number>
          </property>
          <property name="topMargin">
           <number>0</number>
          </property>
          <property name="rightMargin">
           <number>0</number>
          </property>
          <property name="bottomMargin">
           <number>0</number>
          </property>
          <item>
           <widget class="QLabel" name="lblChamberP">
            <property name="font">
             <font>
              <family>JetBrains Mono</family>
              <pointsize>10</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Chamber P: 1013 mbar</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLabel" name="lblO2">
            <property name="font">
             <font>
              <family>JetBrains Mono</family>
              <pointsize>10</pointsize>
             </font>
            </property>
            <property name="text">
             <string>O2: 0.04%</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLabel" name="lblBedTemp">
            <property name="font">
             <font>
              <family>JetBrains Mono</family>
              <pointsize>10</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Bed Temp: 65°C</string>
            </property>
           </widget>
          </item>
         </layout>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="btnEmergencyStop">
         <property name="font">
          <font>
           <family>Inter</family>
           <pointsize>11</pointsize>
           <bold>true</bold>
          </font>
         </property>
         <property name="styleSheet">
          <string notr="true">background-color: #ef4444; color: white; border: 1px solid #ffb4ab; padding: 8px 16px;</string>
         </property>
         <property name="text">
          <string>EMERGENCY STOP</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
    <item>
     <!-- BODY CONTAINER -->
     <widget class="QWidget" name="bodyContainer" native="true">
      <layout class="QHBoxLayout" name="bodyLayout">
       <property name="spacing">
        <number>0</number>
       </property>
       <property name="leftMargin">
        <number>0</number>
       </property>
       <property name="topMargin">
        <number>0</number>
       </property>
       <property name="rightMargin">
        <number>0</number>
       </property>
       <property name="bottomMargin">
        <number>0</number>
       </property>
       <item>
        <!-- LEFT SIDEBAR -->
        <widget class="QFrame" name="sidebarFrame">
         <property name="minimumSize">
          <size>
           <width>220</width>
           <height>0</height>
          </size>
         </property>
         <property name="maximumSize">
          <size>
           <width>220</width>
           <height>16777215</height>
          </size>
         </property>
         <layout class="QVBoxLayout" name="sidebarLayout">
          <property name="spacing">
           <number>8</number>
          </property>
          <property name="leftMargin">
           <number>12</number>
          </property>
          <property name="topMargin">
           <number>16</number>
          </property>
          <property name="rightMargin">
           <number>12</number>
          </property>
          <property name="bottomMargin">
           <number>16</number>
          </property>
          <item>
           <widget class="QLabel" name="lblNavHeader">
            <property name="font">
             <font>
              <family>Inter</family>
              <pointsize>10</pointsize>
              <bold>true</bold>
             </font>
            </property>
            <property name="styleSheet">
             <string notr="true">color: #8e909f; letter-spacing: 1px; margin-bottom: 8px;</string>
            </property>
            <property name="text">
             <string>NAVIGATION</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="btnDashboard">
            <property name="text">
             <string>📊  Dashboard</string>
            </property>
            <property name="checkable">
             <bool>true</bool>
            </property>
            <property name="checked">
             <bool>true</bool>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="btnMachineControl">
            <property name="text">
             <string>⚙️  Motion Control</string>
            </property>
            <property name="checkable">
             <bool>true</bool>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="btnBuildSetup">
            <property name="text">
             <string>📁  Files &amp; Slicing</string>
            </property>
            <property name="checkable">
             <bool>true</bool>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="btnSettings">
            <property name="text">
             <string>🔧  System Settings</string>
            </property>
            <property name="checkable">
             <bool>true</bool>
            </property>
           </widget>
          </item>
          <item>
           <spacer name="sidebarSpacer">
            <property name="orientation">
             <enum>Qt::Vertical</enum>
            </property>
            <property name="sizeHint" stdset="0">
             <size>
              <width>20</width>
              <height>40</height>
             </size>
            </property>
           </spacer>
          </item>
         </layout>
        </widget>
       </item>
       <item>
        <!-- STACKED WIDGET PAGES -->
        <widget class="QStackedWidget" name="stackedWidget">
         <property name="currentIndex">
          <number>0</number>
         </property>
         <!-- PAGE 0: DASHBOARD -->
         <widget class="QWidget" name="page_dashboard">
          <layout class="QVBoxLayout" name="dashboardLayout">
           <property name="spacing">
            <number>16</number>
           </property>
           <property name="leftMargin">
            <number>16</number>
           </property>
           <property name="topMargin">
            <number>16</number>
           </property>
           <property name="rightMargin">
            <number>16</number>
           </property>
           <property name="bottomMargin">
            <number>16</number>
           </property>
           <item>
            <!-- COLUMNS CONTAINER -->
            <widget class="QWidget" name="columnsWidget" native="true">
             <layout class="QHBoxLayout" name="columnsLayout">
              <property name="spacing">
               <number>16</number>
              </property>
              <property name="leftMargin">
               <number>0</number>
              </property>
              <property name="topMargin">
               <number>0</number>
              </property>
              <property name="rightMargin">
               <number>0</number>
              </property>
              <property name="bottomMargin">
               <number>0</number>
              </property>
              <item>
               <!-- LEFT COLUMN: ACTIVE JOB -->
               <widget class="QGroupBox" name="gb_active_job">
                <property name="title">
                 <string>ACTIVE JOB &amp; CALCULATIONS</string>
                </property>
                <layout class="QVBoxLayout" name="activeJobLayout">
                 <property name="spacing">
                  <number>8</number>
                 </property>
                 <item>
                  <layout class="QHBoxLayout" name="fileRow">
                   <item>
                    <widget class="QLabel" name="lbl_active_file">
                     <property name="font">
                      <font>
                       <family>JetBrains Mono</family>
                       <pointsize>10</pointsize>
                       <bold>true</bold>
                      </font>
                     </property>
                     <property name="styleSheet">
                      <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px;</string>
                     </property>
                     <property name="text">
                      <string>demo_cube.stl</string>
                     </property>
                    </widget>
                   </item>
                   <item>
                    <widget class="QPushButton" name="btn_import_build">
                     <property name="styleSheet">
                      <string notr="true">background-color: #ec6a06; color: white; border: 1px solid #ffb690; font-weight: bold;</string>
                     </property>
                     <property name="text">
                      <string>IMPORT FILE</string>
                     </property>
                    </widget>
                   </item>
                  </layout>
                 </item>
                 <item>
                  <layout class="QGridLayout" name="calcGrid">
                   <property name="spacing">
                    <number>6</number>
                   </property>
                   <item row="0" column="0">
                    <widget class="QLabel" name="lbl_calc_dims">
                     <property name="styleSheet">
                      <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 5px; font-family: 'JetBrains Mono';</string>
                     </property>
                     <property name="text">
                      <string>Part Dims: 50.0 x 50.0 x 25.0 mm</string>
                     </property>
                    </widget>
                   </item>
                   <item row="0" column="1">
                    <widget class="QLabel" name="lbl_calc_layers">
                     <property name="styleSheet">
                      <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 5px; font-family: 'JetBrains Mono';</string>
                     </property>
                     <property name="text">
                      <string>Total Layers: 500 Layers</string>
                     </property>
                    </widget>
                   </item>
                   <item row="1" column="0">
                    <widget class="QLabel" name="lbl_calc_dose">
                     <property name="styleSheet">
                      <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 5px; font-family: 'JetBrains Mono';</string>
                     </property>
                     <property name="text">
                      <string>Powder Dose (+U): 0.075 mm</string>
                     </property>
                    </widget>
                   </item>
                   <item row="1" column="1">
                    <widget class="QLabel" name="lbl_calc_vol">
                     <property name="styleSheet">
                      <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 5px; font-family: 'JetBrains Mono';</string>
                     </property>
                     <property name="text">
                      <string>Powder Vol: 234.38 cm³</string>
                     </property>
                    </widget>
                   </item>
                   <item row="2" column="0">
                    <widget class="QLabel" name="lbl_calc_vectors">
                     <property name="styleSheet">
                      <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 5px; font-family: 'JetBrains Mono';</string>
                     </property>
                     <property name="text">
                      <string>Vectors: 12,500 Commands</string>
                     </property>
                    </widget>
                   </item>
                   <item row="2" column="1">
                    <widget class="QLabel" name="lbl_calc_time">
                     <property name="styleSheet">
                      <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 5px; font-family: 'JetBrains Mono';</string>
                     </property>
                     <property name="text">
                      <string>Est. Time: 01:14:30</string>
                     </property>
                    </widget>
                   </item>
                  </layout>
                 </item>
                 <item>
                  <widget class="QProgressBar" name="progressBar">
                   <property name="value">
                    <number>0</number>
                   </property>
                  </widget>
                 </item>
                 <item>
                  <widget class="QPushButton" name="btn_act_simulate">
                   <property name="minimumSize">
                    <size>
                     <width>0</width>
                     <height>38</height>
                    </size>
                   </property>
                   <property name="font">
                    <font>
                     <family>Inter</family>
                     <pointsize>12</pointsize>
                     <bold>true</bold>
                    </font>
                   </property>
                   <property name="styleSheet">
                    <string notr="true">background-color: #ec6a06; color: white; border: 1px solid #ffb690; font-weight: bold;</string>
                   </property>
                   <property name="text">
                    <string>🚀  START BUILD SIMULATION</string>
                   </property>
                  </widget>
                 </item>
                </layout>
               </widget>
              </item>
              <item>
               <!-- MIDDLE COLUMN: 3D PREVIEW -->
               <widget class="QGroupBox" name="gb_build_preview_dash">
                <property name="title">
                 <string>3D PART SLICER &amp; PREVIEW</string>
                </property>
                <layout class="QVBoxLayout" name="previewLayout">
                 <property name="spacing">
                  <number>8</number>
                 </property>
                 <item>
                  <layout class="QHBoxLayout" name="camBar">
                   <item>
                    <widget class="QPushButton" name="btn_view_iso">
                     <property name="text">
                      <string>Iso</string>
                     </property>
                    </widget>
                   </item>
                   <item>
                    <widget class="QPushButton" name="btn_view_top">
                     <property name="text">
                      <string>Top</string>
                     </property>
                    </widget>
                   </item>
                   <item>
                    <widget class="QPushButton" name="btn_view_front">
                     <property name="text">
                      <string>Front</string>
                     </property>
                    </widget>
                   </item>
                   <item>
                    <widget class="QPushButton" name="btn_rotate">
                     <property name="text">
                      <string>Rot</string>
                     </property>
                    </widget>
                   </item>
                   <item>
                    <widget class="QPushButton" name="btn_pan">
                     <property name="text">
                      <string>Pan</string>
                     </property>
                    </widget>
                   </item>
                   <item>
                    <widget class="QPushButton" name="btn_zoom">
                     <property name="text">
                      <string>Zoom</string>
                     </property>
                    </widget>
                   </item>
                  </layout>
                 </item>
                 <item>
                  <widget class="QLabel" name="lbl_3d_preview_placeholder">
                   <property name="styleSheet">
                    <string notr="true">background-color: #0d0e14; border: 1px solid #444653;</string>
                   </property>
                   <property name="text">
                    <string>3D PREVIEW GRAPHIC</string>
                   </property>
                   <property name="alignment">
                    <set>Qt::AlignCenter</set>
                   </property>
                  </widget>
                 </item>
                 <item>
                  <layout class="QHBoxLayout" name="sliderRow">
                   <item>
                    <widget class="QLabel" name="lblSlice">
                     <property name="text">
                      <string>Layer Cut:</string>
                     </property>
                    </widget>
                   </item>
                   <item>
                    <widget class="QSlider" name="slider_layer">
                     <property name="orientation">
                      <enum>Qt::Horizontal</enum>
                     </property>
                    </widget>
                   </item>
                   <item>
                    <widget class="QCheckBox" name="chk_section_view">
                     <property name="text">
                      <string>Section Cut</string>
                     </property>
                    </widget>
                   </item>
                  </layout>
                 </item>
                </layout>
               </widget>
              </item>
              <item>
               <!-- RIGHT COLUMN: TELEMETRY -->
               <widget class="QGroupBox" name="gb_telemetry">
                <property name="title">
                 <string>HARDWARE TELEMETRY</string>
                </property>
                <layout class="QVBoxLayout" name="telemetryColLayout">
                 <property name="spacing">
                  <number>10</number>
                 </property>
                 <item>
                  <widget class="QLabel" name="lbl_laser_gauge">
                   <property name="text">
                    <string>LASER POWER</string>
                   </property>
                   <property name="alignment">
                    <set>Qt::AlignCenter</set>
                   </property>
                  </widget>
                 </item>
                 <item>
                  <widget class="QLabel" name="lbl_oxy_gauge">
                   <property name="text">
                    <string>O2 LEVEL</string>
                   </property>
                   <property name="alignment">
                    <set>Qt::AlignCenter</set>
                   </property>
                  </widget>
                 </item>
                 <item>
                  <widget class="QLabel" name="lblAxisHeader">
                   <property name="text">
                    <string>AXIS POSITIONS (mm):</string>
                   </property>
                  </widget>
                 </item>
                 <item>
                  <widget class="QLabel" name="lbl_dash_u">
                   <property name="font">
                    <font>
                     <family>JetBrains Mono</family>
                     <pointsize>10</pointsize>
                     <bold>true</bold>
                    </font>
                   </property>
                   <property name="styleSheet">
                    <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px;</string>
                   </property>
                   <property name="text">
                    <string>Powder Bay (U): +0.000 mm</string>
                   </property>
                  </widget>
                 </item>
                 <item>
                  <widget class="QLabel" name="lbl_dash_v">
                   <property name="font">
                    <font>
                     <family>JetBrains Mono</family>
                     <pointsize>10</pointsize>
                     <bold>true</bold>
                    </font>
                   </property>
                   <property name="styleSheet">
                    <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px;</string>
                   </property>
                   <property name="text">
                    <string>Build Plate (V): +0.000 mm</string>
                   </property>
                  </widget>
                 </item>
                 <item>
                  <widget class="QLabel" name="lbl_dash_z">
                   <property name="font">
                    <font>
                     <family>JetBrains Mono</family>
                     <pointsize>10</pointsize>
                     <bold>true</bold>
                    </font>
                   </property>
                   <property name="styleSheet">
                    <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px;</string>
                   </property>
                   <property name="text">
                    <string>Recoater Blade (Z): +0.000 mm</string>
                   </property>
                  </widget>
                 </item>
                </layout>
               </widget>
              </item>
             </layout>
            </widget>
           </item>
           <item>
            <!-- BOTTOM TERMINAL LOG -->
            <widget class="QGroupBox" name="gb_console_log">
             <property name="title">
              <string>SYSTEM TERMINAL &amp; EXPOSURE LOG</string>
             </property>
             <layout class="QVBoxLayout" name="logLayout">
              <item>
               <widget class="QTextEdit" name="textEdit">
                <property name="maximumSize">
                 <size>
                  <width>16777215</width>
                  <height>140</height>
                 </size>
                </property>
                <property name="readOnly">
                 <bool>true</bool>
                </property>
               </widget>
              </item>
              <item>
               <layout class="QHBoxLayout" name="logBtnRow">
                <item>
                 <widget class="QCheckBox" name="checkBox">
                  <property name="text">
                   <string>Auto-Scroll</string>
                  </property>
                  <property name="checked">
                   <bool>true</bool>
                  </property>
                 </widget>
                </item>
                <item>
                 <spacer name="logSpacer">
                  <property name="orientation">
                   <enum>Qt::Horizontal</enum>
                  </property>
                  <property name="sizeHint" stdset="0">
                   <size>
                    <width>40</width>
                    <height>20</height>
                   </size>
                  </property>
                 </spacer>
                </item>
                <item>
                 <widget class="QPushButton" name="pushButton">
                  <property name="text">
                   <string>Clear Console Log</string>
                  </property>
                 </widget>
                </item>
               </layout>
              </item>
             </layout>
            </widget>
           </item>
          </layout>
         </widget>
         <!-- PAGE 1: MOTION CONTROL -->
         <widget class="QWidget" name="page_machine_control">
          <layout class="QVBoxLayout" name="motionLayout">
           <property name="spacing">
            <number>16</number>
           </property>
           <property name="leftMargin">
            <number>16</number>
           </property>
           <property name="topMargin">
            <number>16</number>
           </property>
           <property name="rightMargin">
            <number>16</number>
           </property>
           <property name="bottomMargin">
            <number>16</number>
           </property>
           <item>
            <widget class="QLabel" name="lblMotionTitle">
             <property name="font">
              <font>
               <family>Inter</family>
               <pointsize>14</pointsize>
               <bold>true</bold>
              </font>
             </property>
             <property name="styleSheet">
              <string notr="true">color: #b8c4ff;</string>
             </property>
             <property name="text">
              <string>MOTION CONTROL &amp; MANUAL AXIS JOGGING</string>
             </property>
            </widget>
           </item>
           <item>
            <layout class="QHBoxLayout" name="cardsLayout">
             <property name="spacing">
              <number>16</number>
             </property>
             <item>
              <!-- POWDER BAY -->
              <widget class="QGroupBox" name="gb_powder_bay">
               <property name="title">
                <string>POWDER BAY (FEEDER - U AXIS)</string>
               </property>
               <layout class="QVBoxLayout" name="uLayout">
                <property name="spacing">
                 <number>10</number>
                </property>
                <item>
                 <widget class="QLabel" name="uposlcddisplay">
                  <property name="font">
                   <font>
                    <family>JetBrains Mono</family>
                    <pointsize>16</pointsize>
                    <bold>true</bold>
                   </font>
                  </property>
                  <property name="styleSheet">
                   <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 10px;</string>
                  </property>
                  <property name="text">
                   <string>+0.000 mm</string>
                  </property>
                  <property name="alignment">
                   <set>Qt::AlignCenter</set>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="upluspushButton">
                  <property name="text">
                   <string>+U (Supply Powder UP)</string>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="uminuspushButton">
                  <property name="text">
                   <string>-U (Supply Powder DOWN)</string>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="btnhomeU">
                  <property name="text">
                   <string>Home Powder Bay (U)</string>
                  </property>
                 </widget>
                </item>
               </layout>
              </widget>
             </item>
             <item>
              <!-- BUILD PLATE -->
              <widget class="QGroupBox" name="gb_build_plate">
               <property name="title">
                <string>BUILD PLATE (PLATFORM - V AXIS)</string>
               </property>
               <layout class="QVBoxLayout" name="vLayout">
                <property name="spacing">
                 <number>10</number>
                </property>
                <item>
                 <widget class="QLabel" name="vposlcddisplay">
                  <property name="font">
                   <font>
                    <family>JetBrains Mono</family>
                    <pointsize>16</pointsize>
                    <bold>true</bold>
                   </font>
                  </property>
                  <property name="styleSheet">
                   <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 10px;</string>
                  </property>
                  <property name="text">
                   <string>+0.000 mm</string>
                  </property>
                  <property name="alignment">
                   <set>Qt::AlignCenter</set>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="vpluspushButton">
                  <property name="text">
                   <string>+V (Platform UP)</string>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="vminuspushButton">
                  <property name="text">
                   <string>-V (Platform DOWN)</string>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="btnhomeV">
                  <property name="text">
                   <string>Home Build Plate (V)</string>
                  </property>
                 </widget>
                </item>
               </layout>
              </widget>
             </item>
             <item>
              <!-- RECOATER -->
              <widget class="QGroupBox" name="gb_recoater">
               <property name="title">
                <string>RECOATER BLADE (DOSING - Z AXIS)</string>
               </property>
               <layout class="QVBoxLayout" name="zLayout">
                <property name="spacing">
                 <number>10</number>
                </property>
                <item>
                 <widget class="QLabel" name="zposlcddisplay">
                  <property name="font">
                   <font>
                    <family>JetBrains Mono</family>
                    <pointsize>16</pointsize>
                    <bold>true</bold>
                   </font>
                  </property>
                  <property name="styleSheet">
                   <string notr="true">color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 10px;</string>
                  </property>
                  <property name="text">
                   <string>+0.000 mm</string>
                  </property>
                  <property name="alignment">
                   <set>Qt::AlignCenter</set>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="zpluspushButton">
                  <property name="text">
                   <string>+Z (Recoater RIGHT)</string>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="zminuspushButton">
                  <property name="text">
                   <string>-Z (Recoater LEFT)</string>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="btnrecoaterSweep">
                  <property name="styleSheet">
                   <string notr="true">background-color: #1e40af; color: white; border: 1px solid #b8c4ff;</string>
                  </property>
                  <property name="text">
                   <string>Full Sweep Cycle (300mm)</string>
                  </property>
                 </widget>
                </item>
               </layout>
              </widget>
             </item>
            </layout>
           </item>
           <item>
            <!-- JOG STEP TRAVEL -->
            <widget class="QGroupBox" name="gb_travel_step">
             <property name="title">
              <string>JOG STEP TRAVEL DISTANCE (mm)</string>
             </property>
             <layout class="QHBoxLayout" name="stepLayout">
              <property name="spacing">
               <number>10</number>
              </property>
              <item>
               <widget class="QPushButton" name="travelpushButton_1">
                <property name="text">
                 <string>0.01 mm</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="travelpushButton_2">
                <property name="text">
                 <string>0.1 mm</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="travelpushButton_3">
                <property name="text">
                 <string>1.0 mm</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="travelpushButton_4">
                <property name="text">
                 <string>5.0 mm</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="travelpushButton_5">
                <property name="text">
                 <string>10.0 mm</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="travelpushButton_6">
                <property name="text">
                 <string>50.0 mm</string>
                </property>
               </widget>
              </item>
             </layout>
            </widget>
           </item>
           <item>
            <!-- MASTER CONTROLS -->
            <widget class="QGroupBox" name="gb_master_controls">
             <property name="title">
              <string>SYSTEM MASTER CONTROLS</string>
             </property>
             <layout class="QHBoxLayout" name="masterLayout">
              <property name="spacing">
               <number>16</number>
              </property>
              <item>
               <widget class="QPushButton" name="allhomepushButton">
                <property name="text">
                 <string>🏠  HOME ALL AXES (U, V, Z)</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="galvohomepushButton">
                <property name="text">
                 <string>🎯  GALVO SCANNER HOME</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="btn_master_estop">
                <property name="styleSheet">
                 <string notr="true">background-color: #ef4444; color: white; border: 1px solid #ffb4ab;</string>
                </property>
                <property name="text">
                 <string>🚨  EMERGENCY STOP</string>
                </property>
               </widget>
              </item>
             </layout>
            </widget>
           </item>
          </layout>
         </widget>
         <!-- PAGE 2: FILES & SLICING -->
         <widget class="QWidget" name="page_build_setup">
          <layout class="QVBoxLayout" name="filesLayout">
           <item>
            <widget class="QLabel" name="graphicsView_layer">
             <property name="styleSheet">
              <string notr="true">background-color: #0d0e14; border: 1px solid #444653;</string>
             </property>
             <property name="text">
              <string>2D GALVO PREVIEW PLACEHOLDER</string>
             </property>
             <property name="alignment">
              <set>Qt::AlignCenter</set>
             </property>
            </widget>
           </item>
          </layout>
         </widget>
         <!-- PAGE 3: SETTINGS -->
         <widget class="QWidget" name="page_settings">
          <layout class="QVBoxLayout" name="settingsLayout">
           <item>
            <widget class="QLabel" name="lblSettings">
             <property name="text">
              <string>SYSTEM SETTINGS PLACEHOLDER</string>
             </property>
            </widget>
           </item>
          </layout>
         </widget>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
</ui>
"""

    with open(ui_path, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print("Successfully generated clean modern Qt XML metal_dashboard.ui file!")

if __name__ == "__main__":
    generate_metal_dashboard_ui()
