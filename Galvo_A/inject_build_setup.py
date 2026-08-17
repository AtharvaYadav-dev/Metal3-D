import xml.etree.ElementTree as ET

def inject():
    file_path = 'metal_dashboard.ui'
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Find page_build_setup
    page_build_setup = None
    for widget in root.iter('widget'):
        if widget.get('name') == 'page_build_setup':
            page_build_setup = widget
            break
            
    if page_build_setup is None:
        print("Could not find page_build_setup")
        return
        
    # Remove old layouts/widgets inside it
    to_remove = []
    for child in page_build_setup:
        if child.tag not in ('property', 'attribute'):
            to_remove.append(child)
            
    for child in to_remove:
        page_build_setup.remove(child)
        
    layout_xml = """
<layout class="QGridLayout" name="gridLayout_page2">
  <item row="0" column="0">
    <layout class="QVBoxLayout" name="vLayout_col1">
      <item>
        <widget class="QGroupBox" name="gb_build_files">
          <property name="title"><string>BUILD FILES</string></property>
          <layout class="QVBoxLayout" name="vLayout_build">
            <item>
              <layout class="QHBoxLayout" name="hLayout_build_btns">
                <item><widget class="QPushButton" name="btn_import_build"><property name="text"><string>+ Import Build</string></property></widget></item>
                <item><widget class="QPushButton" name="btn_refresh_build"><property name="text"><string>Refresh</string></property></widget></item>
              </layout>
            </item>
            <item><widget class="QListWidget" name="listWidget_builds"/></item>
          </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_machine_profile">
          <property name="title"><string>MACHINE PROFILE</string></property>
          <layout class="QVBoxLayout" name="vLayout_machine">
            <item><widget class="QComboBox" name="comboBox_machine"/></item>
          </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_material_profile">
          <property name="title"><string>MATERIAL PROFILE</string></property>
          <layout class="QVBoxLayout" name="vLayout_material">
            <item><widget class="QComboBox" name="comboBox_material"/></item>
          </layout>
        </widget>
      </item>
    </layout>
  </item>
  
  <item row="0" column="1">
    <widget class="QGroupBox" name="gb_build_preview">
      <property name="title"><string>BUILD PREVIEW</string></property>
      <layout class="QVBoxLayout" name="vLayout_preview">
        <item>
          <layout class="QHBoxLayout" name="hLayout_preview_toolbar">
            <item><widget class="QPushButton" name="btn_view_iso"><property name="text"><string>ISO</string></property></widget></item>
            <item><widget class="QPushButton" name="btn_view_top"><property name="text"><string>Top</string></property></widget></item>
            <item><widget class="QPushButton" name="btn_view_front"><property name="text"><string>Front</string></property></widget></item>
            <item><spacer><property name="orientation"><enum>Qt::Horizontal</enum></property></spacer></item>
          </layout>
        </item>
        <item><widget class="QLabel" name="lbl_3d_preview_placeholder"><property name="text"><string>3D Preview Placeholder</string></property><property name="alignment"><set>Qt::AlignCenter</set></property><property name="minimumSize"><size><width>400</width><height>300</height></size></property></widget></item>
        <item>
          <layout class="QHBoxLayout" name="hLayout_preview_controls">
            <item><widget class="QPushButton" name="btn_rotate"><property name="text"><string>Rotate</string></property></widget></item>
            <item><widget class="QPushButton" name="btn_pan"><property name="text"><string>Pan</string></property></widget></item>
            <item><widget class="QPushButton" name="btn_zoom"><property name="text"><string>Zoom</string></property></widget></item>
            <item><widget class="QCheckBox" name="chk_section_view"><property name="text"><string>Section View</string></property></widget></item>
          </layout>
        </item>
      </layout>
    </widget>
  </item>
  
  <item row="0" column="2">
    <layout class="QVBoxLayout" name="vLayout_col3">
      <item>
        <widget class="QGroupBox" name="gb_job_info">
          <property name="title"><string>JOB INFORMATION</string></property>
          <layout class="QFormLayout" name="formLayout_job">
            <item row="0" column="0"><widget class="QLabel" name="lbl_job_name"><property name="text"><string>Job Name</string></property></widget></item>
            <item row="0" column="1"><widget class="QLabel" name="val_job_name"><property name="text"><string>gear_sample.gcode</string></property></widget></item>
            <item row="1" column="0"><widget class="QLabel" name="lbl_job_material"><property name="text"><string>Material</string></property></widget></item>
            <item row="1" column="1"><widget class="QLabel" name="val_job_material"><property name="text"><string>SS 316L</string></property></widget></item>
            <item row="2" column="0"><widget class="QLabel" name="lbl_job_thickness"><property name="text"><string>Layer Thickness</string></property></widget></item>
            <item row="2" column="1"><widget class="QLabel" name="val_job_thickness"><property name="text"><string>0.03 mm</string></property></widget></item>
            <item row="3" column="0"><widget class="QLabel" name="lbl_job_layers"><property name="text"><string>Total Layers</string></property></widget></item>
            <item row="3" column="1"><widget class="QLabel" name="val_job_layers"><property name="text"><string>1250</string></property></widget></item>
            <item row="4" column="0"><widget class="QLabel" name="lbl_job_btime"><property name="text"><string>Build Time</string></property></widget></item>
            <item row="4" column="1"><widget class="QLabel" name="val_job_btime"><property name="text"><string>07h 36m</string></property></widget></item>
            <item row="5" column="0"><widget class="QLabel" name="lbl_job_powder"><property name="text"><string>Powder Required</string></property></widget></item>
            <item row="5" column="1"><widget class="QLabel" name="val_job_powder"><property name="text"><string>3.42 kg</string></property></widget></item>
            <item row="6" column="0"><widget class="QLabel" name="lbl_job_parts"><property name="text"><string>Number of Parts</string></property></widget></item>
            <item row="6" column="1"><widget class="QLabel" name="val_job_parts"><property name="text"><string>1</string></property></widget></item>
          </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_validation">
          <property name="title"><string>VALIDATION</string></property>
          <layout class="QFormLayout" name="formLayout_val">
            <item row="0" column="0"><widget class="QLabel" name="lbl_val_vol"><property name="text"><string>Build Volume Check</string></property></widget></item>
            <item row="0" column="1"><widget class="QLabel" name="val_val_vol"><property name="text"><string>Passed</string></property></widget></item>
            <item row="1" column="0"><widget class="QLabel" name="lbl_val_mat"><property name="text"><string>Material Check</string></property></widget></item>
            <item row="1" column="1"><widget class="QLabel" name="val_val_mat"><property name="text"><string>Passed</string></property></widget></item>
            <item row="2" column="0"><widget class="QLabel" name="lbl_val_geo"><property name="text"><string>Geometry Check</string></property></widget></item>
            <item row="2" column="1"><widget class="QLabel" name="val_val_geo"><property name="text"><string>Passed</string></property></widget></item>
            <item row="3" column="0"><widget class="QLabel" name="lbl_val_comp"><property name="text"><string>Machine Compatibility</string></property></widget></item>
            <item row="3" column="1"><widget class="QLabel" name="val_val_comp"><property name="text"><string>Passed</string></property></widget></item>
          </layout>
        </widget>
      </item>
      <item><spacer><property name="orientation"><enum>Qt::Vertical</enum></property></spacer></item>
    </layout>
  </item>
  
  <item row="0" column="3">
    <layout class="QVBoxLayout" name="vLayout_col4">
      <item>
        <widget class="QGroupBox" name="gb_est_stats">
          <property name="title"><string>ESTIMATED STATISTICS</string></property>
          <layout class="QFormLayout" name="formLayout_stats">
            <item row="0" column="0"><widget class="QLabel" name="lbl_stat_time"><property name="text"><string>Build Time</string></property></widget></item>
            <item row="0" column="1"><widget class="QLabel" name="val_stat_time"><property name="text"><string>07h 36m</string></property></widget></item>
            <item row="1" column="0"><widget class="QLabel" name="lbl_stat_scan"><property name="text"><string>Scan Time</string></property></widget></item>
            <item row="1" column="1"><widget class="QLabel" name="val_stat_scan"><property name="text"><string>06h 15m</string></property></widget></item>
            <item row="2" column="0"><widget class="QLabel" name="lbl_stat_jump"><property name="text"><string>Jump Time</string></property></widget></item>
            <item row="2" column="1"><widget class="QLabel" name="val_stat_jump"><property name="text"><string>01h 21m</string></property></widget></item>
            <item row="3" column="0"><widget class="QLabel" name="lbl_stat_layers"><property name="text"><string>Layers</string></property></widget></item>
            <item row="3" column="1"><widget class="QLabel" name="val_stat_layers"><property name="text"><string>1250</string></property></widget></item>
            <item row="4" column="0"><widget class="QLabel" name="lbl_stat_scan_len"><property name="text"><string>Total Scan Length</string></property></widget></item>
            <item row="4" column="1"><widget class="QLabel" name="val_stat_scan_len"><property name="text"><string>1,245.36 m</string></property></widget></item>
            <item row="5" column="0"><widget class="QLabel" name="lbl_stat_jump_len"><property name="text"><string>Total Jump Length</string></property></widget></item>
            <item row="5" column="1"><widget class="QLabel" name="val_stat_jump_len"><property name="text"><string>231.45 m</string></property></widget></item>
            <item row="6" column="0"><widget class="QLabel" name="lbl_stat_powder"><property name="text"><string>Powder Required</string></property></widget></item>
            <item row="6" column="1"><widget class="QLabel" name="val_stat_powder"><property name="text"><string>3.42 kg</string></property></widget></item>
            <item row="7" column="0"><widget class="QLabel" name="lbl_stat_power"><property name="text"><string>Avg. Laser Power</string></property></widget></item>
            <item row="7" column="1"><widget class="QLabel" name="val_stat_power"><property name="text"><string>195 W</string></property></widget></item>
            <item row="8" column="0"><widget class="QLabel" name="lbl_stat_energy"><property name="text"><string>Energy / Layer</string></property></widget></item>
            <item row="8" column="1"><widget class="QLabel" name="val_stat_energy"><property name="text"><string>4.32 kJ</string></property></widget></item>
          </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_actions">
          <property name="title"><string>ACTIONS</string></property>
          <layout class="QVBoxLayout" name="vLayout_actions">
            <item><widget class="QPushButton" name="btn_verify_build"><property name="text"><string>Verify Build</string></property></widget></item>
            <item><widget class="QPushButton" name="btn_send_queue"><property name="text"><string>Send to Queue</string></property></widget></item>
            <item><widget class="QPushButton" name="btn_prepare_machine"><property name="text"><string>Prepare Machine</string></property></widget></item>
          </layout>
        </widget>
      </item>
      <item><spacer><property name="orientation"><enum>Qt::Vertical</enum></property></spacer></item>
    </layout>
  </item>
  
  <item row="1" column="0" colspan="3">
    <widget class="QGroupBox" name="gb_build_queue">
      <property name="title"><string>BUILD QUEUE</string></property>
      <layout class="QVBoxLayout" name="vLayout_queue">
        <item>
            <widget class="QTableWidget" name="tableWidget_queue">
                <property name="columnCount"><number>6</number></property>
                <column><property name="text"><string>#</string></property></column>
                <column><property name="text"><string>Job Name</string></property></column>
                <column><property name="text"><string>Material</string></property></column>
                <column><property name="text"><string>Layers</string></property></column>
                <column><property name="text"><string>Estimated Time</string></property></column>
                <column><property name="text"><string>Status</string></property></column>
            </widget>
        </item>
      </layout>
    </widget>
  </item>
  
  <item row="1" column="3">
    <widget class="QGroupBox" name="gb_build_notes">
      <property name="title"><string>BUILD NOTES</string></property>
      <layout class="QVBoxLayout" name="vLayout_notes">
        <item><widget class="QTextEdit" name="txt_build_notes"><property name="placeholderText"><string>Add notes about this build...</string></property></widget></item>
        <item><widget class="QPushButton" name="btn_save_notes"><property name="text"><string>Save Notes</string></property></widget></item>
      </layout>
    </widget>
  </item>
</layout>
"""
    new_layout = ET.fromstring(layout_xml)
    page_build_setup.append(new_layout)
    
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print("Successfully injected build setup page into metal_dashboard.ui")

if __name__ == '__main__':
    inject()
