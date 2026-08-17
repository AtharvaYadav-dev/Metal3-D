import xml.etree.ElementTree as ET

def inject():
    file_path = 'metal_dashboard.ui'
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Find page_gcode
    page_gcode = None
    for widget in root.iter('widget'):
        if widget.get('name') == 'page_gcode':
            page_gcode = widget
            break
            
    if page_gcode is None:
        print("Could not find page_gcode")
        return
        
    # Remove old layouts/widgets inside it
    to_remove = []
    for child in page_gcode:
        if child.tag not in ('property', 'attribute'):
            to_remove.append(child)
            
    for child in to_remove:
        page_gcode.remove(child)
        
    layout_xml = """
<layout class="QGridLayout" name="gridLayout_page3">
  <item row="0" column="0">
    <layout class="QVBoxLayout" name="vLayout_c1_p3">
      <item>
        <widget class="QGroupBox" name="gb_layer_controls">
          <property name="title"><string>LAYER CONTROLS</string></property>
          <layout class="QVBoxLayout" name="vLayout_layer_controls">
            <item>
              <layout class="QHBoxLayout" name="hLayout_layer_status">
                <item><widget class="QLabel" name="lbl_layer_text"><property name="text"><string>Layer</string></property></widget></item>
                <item><widget class="QLabel" name="lbl_layer_val"><property name="text"><string>245 / 1250</string></property><property name="alignment"><set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set></property></widget></item>
              </layout>
            </item>
            <item><widget class="QSlider" name="slider_layer"><property name="orientation"><enum>Qt::Horizontal</enum></property></widget></item>
            <item>
              <layout class="QHBoxLayout" name="hLayout_layer_btns">
                <item><widget class="QPushButton" name="btn_layer_first"><property name="text"><string>|&lt;</string></property></widget></item>
                <item><widget class="QPushButton" name="btn_layer_prev"><property name="text"><string>&lt;</string></property></widget></item>
                <item><widget class="QPushButton" name="btn_layer_next"><property name="text"><string>&gt;</string></property></widget></item>
                <item><widget class="QPushButton" name="btn_layer_last"><property name="text"><string>&gt;|</string></property></widget></item>
              </layout>
            </item>
            <item><widget class="QPushButton" name="btn_jump_layer"><property name="text"><string>Jump to Layer</string></property></widget></item>
            <item>
              <layout class="QHBoxLayout" name="hLayout_range_status">
                <item><widget class="QLabel" name="lbl_range_text"><property name="text"><string>Layer Range</string></property></widget></item>
                <item><widget class="QLabel" name="lbl_range_val"><property name="text"><string>1 - 1250</string></property><property name="alignment"><set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set></property></widget></item>
              </layout>
            </item>
            <item><widget class="QSlider" name="slider_layer_range"><property name="orientation"><enum>Qt::Horizontal</enum></property></widget></item>
          </layout>
        </widget>
      </item>
      
      <item>
        <widget class="QGroupBox" name="gb_display_options">
          <property name="title"><string>DISPLAY OPTIONS</string></property>
          <layout class="QVBoxLayout" name="vLayout_display_options">
            <item><widget class="QCheckBox" name="chk_show_contours"><property name="text"><string>Show Contours</string></property><property name="checked"><bool>true</bool></property></widget></item>
            <item><widget class="QCheckBox" name="chk_show_hatch"><property name="text"><string>Show Hatch</string></property><property name="checked"><bool>true</bool></property></widget></item>
            <item><widget class="QCheckBox" name="chk_show_supports"><property name="text"><string>Show Supports</string></property><property name="checked"><bool>true</bool></property></widget></item>
            <item><widget class="QCheckBox" name="chk_show_jump"><property name="text"><string>Show Jump Moves</string></property><property name="checked"><bool>true</bool></property></widget></item>
            <item><widget class="QCheckBox" name="chk_show_scan_dir"><property name="text"><string>Show Scan Direction</string></property><property name="checked"><bool>true</bool></property></widget></item>
            <item><widget class="QCheckBox" name="chk_only_current"><property name="text"><string>Only Current Layer</string></property></widget></item>
          </layout>
        </widget>
      </item>
      
      <item>
        <widget class="QGroupBox" name="gb_view_mode">
          <property name="title"><string>VIEW MODE</string></property>
          <layout class="QHBoxLayout" name="hLayout_view_mode">
            <item><widget class="QPushButton" name="btn_view_2d"><property name="text"><string>2D</string></property></widget></item>
            <item><widget class="QPushButton" name="btn_view_3d"><property name="text"><string>3D</string></property></widget></item>
            <item><widget class="QPushButton" name="btn_view_25d"><property name="text"><string>2.5D</string></property></widget></item>
          </layout>
        </widget>
      </item>
      
      <item>
        <widget class="QGroupBox" name="gb_layer_info">
          <property name="title"><string>LAYER INFORMATION</string></property>
          <layout class="QFormLayout" name="formLayout_layer_info">
            <item row="0" column="0"><widget class="QLabel" name="lbl_linfo_thick"><property name="text"><string>Layer Thickness</string></property></widget></item>
            <item row="0" column="1"><widget class="QLabel" name="val_linfo_thick"><property name="text"><string>0.03 mm</string></property></widget></item>
            <item row="1" column="0"><widget class="QLabel" name="lbl_linfo_ltime"><property name="text"><string>Layer Time</string></property></widget></item>
            <item row="1" column="1"><widget class="QLabel" name="val_linfo_ltime"><property name="text"><string>12.45 s</string></property></widget></item>
            <item row="2" column="0"><widget class="QLabel" name="lbl_linfo_stime"><property name="text"><string>Scan Time</string></property></widget></item>
            <item row="2" column="1"><widget class="QLabel" name="val_linfo_stime"><property name="text"><string>10.32 s</string></property></widget></item>
            <item row="3" column="0"><widget class="QLabel" name="lbl_linfo_jtime"><property name="text"><string>Jump Time</string></property></widget></item>
            <item row="3" column="1"><widget class="QLabel" name="val_linfo_jtime"><property name="text"><string>2.13 s</string></property></widget></item>
            <item row="4" column="0"><widget class="QLabel" name="lbl_linfo_hlen"><property name="text"><string>Hatch Length</string></property></widget></item>
            <item row="4" column="1"><widget class="QLabel" name="val_linfo_hlen"><property name="text"><string>125.43 m</string></property></widget></item>
            <item row="5" column="0"><widget class="QLabel" name="lbl_linfo_jlen"><property name="text"><string>Jump Length</string></property></widget></item>
            <item row="5" column="1"><widget class="QLabel" name="val_linfo_jlen"><property name="text"><string>18.27 m</string></property></widget></item>
            <item row="6" column="0"><widget class="QLabel" name="lbl_linfo_energy"><property name="text"><string>Energy / Layer</string></property></widget></item>
            <item row="6" column="1"><widget class="QLabel" name="val_linfo_energy"><property name="text"><string>4.32 kJ</string></property></widget></item>
          </layout>
        </widget>
      </item>
      <item><spacer><property name="orientation"><enum>Qt::Vertical</enum></property></spacer></item>
    </layout>
  </item>
  
  <item row="0" column="1">
    <layout class="QVBoxLayout" name="vLayout_c2_p3">
      <item>
        <widget class="QGraphicsView" name="graphicsView_layer">
            <property name="minimumSize"><size><width>400</width><height>400</height></size></property>
        </widget>
      </item>
      <item>
        <widget class="QWidget" name="widget_layer_coords">
          <layout class="QHBoxLayout" name="hLayout_coords">
            <item><widget class="QLabel" name="lbl_coord_x"><property name="text"><string>X: 45.230 mm\nMin: -90.000\nMax: 90.000</string></property></widget></item>
            <item><widget class="QLabel" name="lbl_coord_y"><property name="text"><string>Y: 67.890 mm\nMin: -90.000\nMax: 90.000</string></property></widget></item>
            <item><widget class="QLabel" name="lbl_coord_z"><property name="text"><string>Z: 7.320 mm\nMin: 0.000\nMax: 37.500</string></property></widget></item>
            <item><widget class="QLabel" name="lbl_coord_zoom"><property name="text"><string>Zoom: 2.36x\nSpeed: 2500 mm/s\nPower: 195 W</string></property></widget></item>
          </layout>
        </widget>
      </item>
    </layout>
  </item>
  
  <item row="0" column="2">
    <layout class="QVBoxLayout" name="vLayout_c3_p3">
      <item>
        <widget class="QGroupBox" name="gb_layer_thumbnails">
          <property name="title"><string>LAYER THUMBNAILS</string></property>
          <layout class="QHBoxLayout" name="hLayout_thumbnails">
            <item><widget class="QPushButton" name="btn_thumb_prev"><property name="text"><string>&lt;</string></property><property name="maximumWidth"><number>30</number></property></widget></item>
            <item><widget class="QLabel" name="lbl_thumb_1"><property name="text"><string>243</string></property><property name="alignment"><set>Qt::AlignCenter</set></property><property name="minimumHeight"><number>60</number></property></widget></item>
            <item><widget class="QLabel" name="lbl_thumb_2"><property name="text"><string>244</string></property><property name="alignment"><set>Qt::AlignCenter</set></property><property name="minimumHeight"><number>60</number></property></widget></item>
            <item><widget class="QLabel" name="lbl_thumb_3"><property name="text"><string>245</string></property><property name="alignment"><set>Qt::AlignCenter</set></property><property name="minimumHeight"><number>60</number></property></widget></item>
            <item><widget class="QLabel" name="lbl_thumb_4"><property name="text"><string>246</string></property><property name="alignment"><set>Qt::AlignCenter</set></property><property name="minimumHeight"><number>60</number></property></widget></item>
            <item><widget class="QLabel" name="lbl_thumb_5"><property name="text"><string>247</string></property><property name="alignment"><set>Qt::AlignCenter</set></property><property name="minimumHeight"><number>60</number></property></widget></item>
            <item><widget class="QPushButton" name="btn_thumb_next"><property name="text"><string>&gt;</string></property><property name="maximumWidth"><number>30</number></property></widget></item>
          </layout>
        </widget>
      </item>
      
      <item>
        <widget class="QGroupBox" name="gb_scan_strategy">
          <property name="title"><string>SCAN STRATEGY</string></property>
          <layout class="QHBoxLayout" name="hLayout_scan_strategy">
            <item>
              <layout class="QFormLayout" name="formLayout_scan_strategy">
                <item row="0" column="0"><widget class="QLabel" name="lbl_strat_type"><property name="text"><string>Strategy</string></property></widget></item>
                <item row="0" column="1"><widget class="QLabel" name="val_strat_type"><property name="text"><string>Island Scan</string></property></widget></item>
                <item row="1" column="0"><widget class="QLabel" name="lbl_strat_rot"><property name="text"><string>Rotation Angle</string></property></widget></item>
                <item row="1" column="1"><widget class="QLabel" name="val_strat_rot"><property name="text"><string>67°</string></property></widget></item>
                <item row="2" column="0"><widget class="QLabel" name="lbl_strat_hatch"><property name="text"><string>Hatch Spacing</string></property></widget></item>
                <item row="2" column="1"><widget class="QLabel" name="val_strat_hatch"><property name="text"><string>0.10 mm</string></property></widget></item>
                <item row="3" column="0"><widget class="QLabel" name="lbl_strat_hatch_angle"><property name="text"><string>Hatch Angle</string></property></widget></item>
                <item row="3" column="1"><widget class="QLabel" name="val_strat_hatch_angle"><property name="text"><string>67°</string></property></widget></item>
                <item row="4" column="0"><widget class="QLabel" name="lbl_strat_island"><property name="text"><string>Island Size</string></property></widget></item>
                <item row="4" column="1"><widget class="QLabel" name="val_strat_island"><property name="text"><string>5.00 mm</string></property></widget></item>
                <item row="5" column="0"><widget class="QLabel" name="lbl_strat_border"><property name="text"><string>Border Offset</string></property></widget></item>
                <item row="5" column="1"><widget class="QLabel" name="val_strat_border"><property name="text"><string>0.05 mm</string></property></widget></item>
                <item row="6" column="0"><widget class="QLabel" name="lbl_strat_contour"><property name="text"><string>Contour Offset</string></property></widget></item>
                <item row="6" column="1"><widget class="QLabel" name="val_strat_contour"><property name="text"><string>0.02 mm</string></property></widget></item>
              </layout>
            </item>
            <item>
              <widget class="QLabel" name="lbl_strat_img_placeholder">
                <property name="text"><string>Strategy\nImage</string></property>
                <property name="alignment"><set>Qt::AlignCenter</set></property>
                <property name="minimumWidth"><number>120</number></property>
              </widget>
            </item>
          </layout>
        </widget>
      </item>
      
      <item>
        <widget class="QGroupBox" name="gb_layer_statistics">
          <property name="title"><string>LAYER STATISTICS</string></property>
          <layout class="QHBoxLayout" name="hLayout_layer_stats">
            <item>
              <widget class="QLabel" name="lbl_stats_pie_placeholder">
                <property name="text"><string>Pie Chart</string></property>
                <property name="alignment"><set>Qt::AlignCenter</set></property>
              </widget>
            </item>
            <item>
              <layout class="QFormLayout" name="formLayout_layer_stats">
                <item row="0" column="0"><widget class="QLabel" name="lbl_stat_contour"><property name="text"><string>Contour</string></property></widget></item>
                <item row="0" column="1"><widget class="QLabel" name="val_stat_contour"><property name="text"><string>12.45 m (6.2%)</string></property></widget></item>
                <item row="1" column="0"><widget class="QLabel" name="lbl_stat_hatch"><property name="text"><string>Hatch</string></property></widget></item>
                <item row="1" column="1"><widget class="QLabel" name="val_stat_hatch"><property name="text"><string>125.43 m (62.7%)</string></property></widget></item>
                <item row="2" column="0"><widget class="QLabel" name="lbl_stat_supp"><property name="text"><string>Supports</string></property></widget></item>
                <item row="2" column="1"><widget class="QLabel" name="val_stat_supp"><property name="text"><string>32.18 m (16.1%)</string></property></widget></item>
                <item row="3" column="0"><widget class="QLabel" name="lbl_stat_jump"><property name="text"><string>Jump Moves</string></property></widget></item>
                <item row="3" column="1"><widget class="QLabel" name="val_stat_jump"><property name="text"><string>30.27 m (15.0%)</string></property></widget></item>
                <item row="4" column="0"><widget class="QLabel" name="lbl_stat_total"><property name="text"><string>Total</string></property></widget></item>
                <item row="4" column="1"><widget class="QLabel" name="val_stat_total"><property name="text"><string>200.33 m</string></property></widget></item>
              </layout>
            </item>
          </layout>
        </widget>
      </item>
      
      <item>
        <widget class="QGroupBox" name="gb_layer_actions">
          <property name="title"><string>ACTIONS</string></property>
          <layout class="QGridLayout" name="gridLayout_layer_actions">
            <item row="0" column="0"><widget class="QPushButton" name="btn_act_export_img"><property name="text"><string>Export Layer Image</string></property></widget></item>
            <item row="0" column="1"><widget class="QPushButton" name="btn_act_export_data"><property name="text"><string>Export Layer Data</string></property></widget></item>
            <item row="1" column="0"><widget class="QPushButton" name="btn_act_simulate"><property name="text"><string>Simulate From Here</string></property></widget></item>
            <item row="1" column="1"><widget class="QPushButton" name="btn_act_clear"><property name="text"><string>Clear Selection</string></property></widget></item>
          </layout>
        </widget>
      </item>
      
      <item><spacer><property name="orientation"><enum>Qt::Vertical</enum></property></spacer></item>
    </layout>
  </item>
</layout>
"""
    new_layout = ET.fromstring(layout_xml)
    page_gcode.append(new_layout)
    
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print("Successfully injected layer viewer page into metal_dashboard.ui")

if __name__ == '__main__':
    inject()
