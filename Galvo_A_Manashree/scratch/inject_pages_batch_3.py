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

def inject_alarm_events(root):
    page = clear_page(root, 'page_alarm_events')
    if page is None: return
    xml = """
<layout class="QVBoxLayout" name="vLayout_alarm_events">
  <!-- TOP ROW -->
  <item>
    <layout class="QHBoxLayout">
      <item>
        <widget class="QGroupBox" name="gb_active_alarms"><property name="title"><string>ACTIVE ALARMS (3)</string></property>
          <layout class="QVBoxLayout">
            <item><widget class="QLabel"><property name="text"><string>&lt;b&gt;OXYGEN LEVEL HIGH&lt;/b&gt;&lt;br&gt;Oxygen level is above limit. [Critical]</string></property></widget></item>
            <item><widget class="QLabel"><property name="text"><string>&lt;b&gt;RECOATER MOTOR OVERLOAD&lt;/b&gt;&lt;br&gt;Recoater motor current exceeds limit. [Major]</string></property></widget></item>
            <item><widget class="QLabel"><property name="text"><string>&lt;b&gt;POWDER LEVEL LOW&lt;/b&gt;&lt;br&gt;Powder level is below warning limit. [Warning]</string></property></widget></item>
            <item>
                <layout class="QHBoxLayout">
                    <item><widget class="QPushButton"><property name="text"><string>Acknowledge All</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Clear All</string></property></widget></item>
                </layout>
            </item>
          </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_alarm_summary"><property name="title"><string>ALARM SUMMARY</string></property>
          <layout class="QGridLayout">
            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>3\nActive</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
            <item row="0" column="1"><widget class="QLabel"><property name="text"><string>2\nUnacknowledged</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>5\nWarnings (24H)</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>0\nAlarms Cleared (24H)</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
          </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_alarm_category"><property name="title"><string>ALARM BY CATEGORY</string></property>
          <layout class="QHBoxLayout">
            <item><widget class="QLabel"><property name="text"><string>[Pie Chart]</string></property></widget></item>
            <item>
              <layout class="QFormLayout">
                <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Environment</string></property></widget></item>
                <item row="0" column="1"><widget class="QLabel"><property name="text"><string>2</string></property></widget></item>
                <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Motion</string></property></widget></item>
                <item row="1" column="1"><widget class="QLabel"><property name="text"><string>2</string></property></widget></item>
                <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Power / Laser</string></property></widget></item>
                <item row="2" column="1"><widget class="QLabel"><property name="text"><string>1</string></property></widget></item>
                <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Safety</string></property></widget></item>
                <item row="3" column="1"><widget class="QLabel"><property name="text"><string>2</string></property></widget></item>
                <item row="4" column="0"><widget class="QLabel"><property name="text"><string>Process</string></property></widget></item>
                <item row="4" column="1"><widget class="QLabel"><property name="text"><string>1</string></property></widget></item>
                <item row="5" column="0"><widget class="QLabel"><property name="text"><string>System</string></property></widget></item>
                <item row="5" column="1"><widget class="QLabel"><property name="text"><string>0</string></property></widget></item>
                <item row="6" column="0"><widget class="QLabel"><property name="text"><string>Total (24H)</string></property></widget></item>
                <item row="6" column="1"><widget class="QLabel"><property name="text"><string>8</string></property></widget></item>
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
        <widget class="QGroupBox" name="gb_alarm_history"><property name="title"><string>ALARM HISTORY</string></property>
          <layout class="QVBoxLayout">
            <item>
                <layout class="QHBoxLayout">
                    <item><spacer><property name="orientation"><enum>Qt::Horizontal</enum></property></spacer></item>
                    <item><widget class="QComboBox"><item><property name="text"><string>All Categories</string></property></item></widget></item>
                    <item><widget class="QComboBox"><item><property name="text"><string>All Severities</string></property></item></widget></item>
                    <item><widget class="QComboBox"><item><property name="text"><string>Last 24 Hours</string></property></item></widget></item>
                </layout>
            </item>
            <item>
                <widget class="QTableWidget">
                    <property name="columnCount"><number>7</number></property>
                    <column><property name="text"><string>TIME</string></property></column>
                    <column><property name="text"><string>DATE</string></property></column>
                    <column><property name="text"><string>ALARM</string></property></column>
                    <column><property name="text"><string>CATEGORY</string></property></column>
                    <column><property name="text"><string>SEVERITY</string></property></column>
                    <column><property name="text"><string>STATUS</string></property></column>
                    <column><property name="text"><string>DURATION</string></property></column>
                </widget>
            </item>
            <item>
                <layout class="QHBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>Showing 1 to 8 of 8 entries</string></property></widget></item>
                    <item><spacer><property name="orientation"><enum>Qt::Horizontal</enum></property></spacer></item>
                    <item><widget class="QPushButton"><property name="text"><string>&lt;</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>1</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>&gt;</string></property></widget></item>
                    <item><spacer><property name="orientation"><enum>Qt::Horizontal</enum></property></spacer></item>
                    <item><widget class="QPushButton"><property name="text"><string>Export History</string></property></widget></item>
                </layout>
            </item>
          </layout>
        </widget>
      </item>
      <item>
        <widget class="QGroupBox" name="gb_alarm_actions"><property name="title"><string>QUICK ACTIONS</string></property>
          <layout class="QVBoxLayout">
            <item><widget class="QPushButton"><property name="text"><string>Acknowledge All</string></property></widget></item>
            <item><widget class="QPushButton"><property name="text"><string>Reset Alarms</string></property></widget></item>
            <item><widget class="QPushButton"><property name="text"><string>Alarm Sound</string></property></widget></item>
            <item><widget class="QPushButton"><property name="text"><string>Test Alarms</string></property></widget></item>
            <item><widget class="QPushButton"><property name="text"><string>Export Alarm Log</string></property></widget></item>
          </layout>
        </widget>
      </item>
    </layout>
  </item>
</layout>
"""
    new_layout = ET.fromstring(xml)
    page.append(new_layout)
    print("Injected alarm/events page")

def inject_logs(root):
    page = clear_page(root, 'page_logs')
    if page is None: return
    xml = """
<layout class="QHBoxLayout" name="hLayout_logs">
  <item>
    <widget class="QGroupBox" name="gb_system_logs"><property name="title"><string>SYSTEM LOGS</string></property>
        <layout class="QVBoxLayout">
            <item>
                <layout class="QHBoxLayout">
                    <item><widget class="QLineEdit"><property name="placeholderText"><string>Search logs...</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Pause Auto Scroll</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Clear Logs</string></property></widget></item>
                </layout>
            </item>
            <item>
                <widget class="QTableWidget">
                    <property name="columnCount"><number>4</number></property>
                    <column><property name="text"><string>TIME</string></property></column>
                    <column><property name="text"><string>LEVEL</string></property></column>
                    <column><property name="text"><string>SOURCE</string></property></column>
                    <column><property name="text"><string>MESSAGE</string></property></column>
                </widget>
            </item>
            <item>
                <layout class="QHBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>Showing 1 to 15 of 1,248 entries</string></property></widget></item>
                    <item><spacer><property name="orientation"><enum>Qt::Horizontal</enum></property></spacer></item>
                    <item><widget class="QPushButton"><property name="text"><string>&lt;</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>1</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>&gt;</string></property></widget></item>
                </layout>
            </item>
        </layout>
    </widget>
  </item>
  
  <item>
    <layout class="QVBoxLayout">
        <item>
            <widget class="QGroupBox" name="gb_log_filters"><property name="title"><string>LOG FILTERS</string></property>
                <layout class="QFormLayout">
                    <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Log Level</string></property></widget></item>
                    <item row="0" column="1"><widget class="QComboBox"><item><property name="text"><string>All Levels</string></property></item></widget></item>
                    <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Source</string></property></widget></item>
                    <item row="1" column="1"><widget class="QComboBox"><item><property name="text"><string>All Sources</string></property></item></widget></item>
                    <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Time Range</string></property></widget></item>
                    <item row="2" column="1"><widget class="QComboBox"><item><property name="text"><string>Last 24 Hours</string></property></item></widget></item>
                    <item row="3" column="0" colspan="2">
                        <layout class="QHBoxLayout">
                            <item><widget class="QPushButton"><property name="text"><string>Apply Filters</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Reset</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_log_stats"><property name="title"><string>LOG STATISTICS</string></property>
                <layout class="QHBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>[Pie Chart]\n1,248</string></property><property name="alignment"><set>Qt::AlignCenter</set></property></widget></item>
                    <item>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Info</string></property></widget></item>
                            <item row="0" column="1"><widget class="QLabel"><property name="text"><string>972</string></property></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Warning</string></property></widget></item>
                            <item row="1" column="1"><widget class="QLabel"><property name="text"><string>156</string></property></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Error</string></property></widget></item>
                            <item row="2" column="1"><widget class="QLabel"><property name="text"><string>28</string></property></widget></item>
                            <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Debug</string></property></widget></item>
                            <item row="3" column="1"><widget class="QLabel"><property name="text"><string>92</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_export_logs"><property name="title"><string>EXPORT LOGS</string></property>
                <layout class="QVBoxLayout">
                    <item><widget class="QLabel"><property name="text"><string>Export filtered logs to file</string></property></widget></item>
                    <item>
                        <layout class="QHBoxLayout">
                            <item><widget class="QComboBox"><item><property name="text"><string>CSV (.csv)</string></property></item></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Export Logs</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </widget>
        </item>
    </layout>
  </item>
</layout>
"""
    new_layout = ET.fromstring(xml)
    page.append(new_layout)
    print("Injected logs page")

def inject_maintenance(root):
    page = clear_page(root, 'page_settings') # As requested, we map Maintenance to settings (index 9)
    if page is None: return
    xml = """
<layout class="QHBoxLayout" name="hLayout_maintenance">
  <item>
    <layout class="QVBoxLayout">
        <item>
            <widget class="QGroupBox" name="gb_maint_tools"><property name="title"><string>MAINTENANCE TOOLS</string></property>
                <layout class="QGridLayout">
                    <item row="0" column="0">
                        <layout class="QVBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>&lt;b&gt;SYSTEM DIAGNOSTICS&lt;/b&gt;</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Run Diagnostics</string></property></widget></item>
                        </layout>
                    </item>
                    <item row="0" column="1">
                        <layout class="QVBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>&lt;b&gt;LUBRICATION REMINDER&lt;/b&gt;</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>View Schedule</string></property></widget></item>
                        </layout>
                    </item>
                    <item row="0" column="2">
                        <layout class="QVBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>&lt;b&gt;CLEANING GUIDE&lt;/b&gt;</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Open Guide</string></property></widget></item>
                        </layout>
                    </item>
                    <item row="0" column="3">
                        <layout class="QVBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>&lt;b&gt;CALIBRATION WIZARD&lt;/b&gt;</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Start Calibration</string></property></widget></item>
                        </layout>
                    </item>
                    <item row="1" column="0">
                        <layout class="QVBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>&lt;b&gt;FIRMWARE UPDATE&lt;/b&gt;</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Check Updates</string></property></widget></item>
                        </layout>
                    </item>
                    <item row="1" column="1">
                        <layout class="QVBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>&lt;b&gt;EXPORT MAINTENANCE LOG&lt;/b&gt;</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Export Logs</string></property></widget></item>
                        </layout>
                    </item>
                    <item row="1" column="2">
                        <layout class="QVBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>&lt;b&gt;FACTORY RESET&lt;/b&gt;</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Factory Reset</string></property></widget></item>
                        </layout>
                    </item>
                    <item row="1" column="3">
                        <layout class="QVBoxLayout">
                            <item><widget class="QLabel"><property name="text"><string>&lt;b&gt;BACKUP / RESTORE&lt;/b&gt;</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Manage Backup</string></property></widget></item>
                        </layout>
                    </item>
                </layout>
            </widget>
        </item>
        <item>
            <layout class="QHBoxLayout">
                <item>
                    <widget class="QGroupBox" name="gb_comp_health"><property name="title"><string>COMPONENT HEALTH</string></property>
                        <layout class="QVBoxLayout">
                            <item>
                                <widget class="QTableWidget">
                                    <property name="columnCount"><number>4</number></property>
                                    <column><property name="text"><string>Component</string></property></column>
                                    <column><property name="text"><string>Status</string></property></column>
                                    <column><property name="text"><string>Health</string></property></column>
                                    <column><property name="text"><string>Last Checked</string></property></column>
                                </widget>
                            </item>
                            <item><widget class="QPushButton"><property name="text"><string>Refresh Health Status</string></property></widget></item>
                        </layout>
                    </widget>
                </item>
                <item>
                    <widget class="QGroupBox" name="gb_maint_schedule"><property name="title"><string>MAINTENANCE SCHEDULE</string></property>
                        <layout class="QVBoxLayout">
                            <item>
                                <widget class="QTableWidget">
                                    <property name="columnCount"><number>5</number></property>
                                    <column><property name="text"><string>Task</string></property></column>
                                    <column><property name="text"><string>Interval</string></property></column>
                                    <column><property name="text"><string>Last Done</string></property></column>
                                    <column><property name="text"><string>Next Due</string></property></column>
                                    <column><property name="text"><string>Status</string></property></column>
                                </widget>
                            </item>
                            <item><widget class="QPushButton"><property name="text"><string>View Full Schedule</string></property></widget></item>
                        </layout>
                    </widget>
                </item>
            </layout>
        </item>
    </layout>
  </item>
  
  <item>
    <layout class="QVBoxLayout">
        <item>
            <widget class="QGroupBox" name="gb_service_info"><property name="title"><string>SERVICE INFORMATION</string></property>
                <layout class="QFormLayout">
                    <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Machine Model</string></property></widget></item>
                    <item row="0" column="1"><widget class="QLabel"><property name="text"><string>M3D-500</string></property></widget></item>
                    <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Serial Number</string></property></widget></item>
                    <item row="1" column="1"><widget class="QLabel"><property name="text"><string>M3D500-2026-00125</string></property></widget></item>
                    <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Service Status</string></property></widget></item>
                    <item row="2" column="1"><widget class="QLabel"><property name="text"><string>Up to Date</string></property></widget></item>
                    <item row="3" column="0" colspan="2"><widget class="QLabel"><property name="text"><string>[!] Next service due in 68 days</string></property></widget></item>
                    <item row="4" column="0" colspan="2"><widget class="QPushButton"><property name="text"><string>View Service Schedule</string></property></widget></item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_maint_notes"><property name="title"><string>MAINTENANCE NOTES</string></property>
                <layout class="QVBoxLayout">
                    <item><widget class="QPushButton"><property name="text"><string>+ Add Note</string></property></widget></item>
                    <item><widget class="QTextEdit"><property name="text"><string>07 Jul 2026 09:15 AM by Operator\nChecked laser optics and cleaned protective window. All systems are working normally.</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>View All Notes</string></property></widget></item>
                </layout>
            </widget>
        </item>
    </layout>
  </item>
</layout>
"""
    new_layout = ET.fromstring(xml)
    page.append(new_layout)
    print("Injected maintenance page")

def inject_settings(root):
    page = clear_page(root, 'page_settings_2') # As requested, we map Settings to settings_2 (index 10)
    if page is None: return
    xml = """
<layout class="QHBoxLayout" name="hLayout_settings">
  <item>
    <widget class="QTabWidget">
        <widget class="QWidget" name="tab_general"><attribute name="title"><string>GENERAL</string></attribute>
            <layout class="QGridLayout">
                <item row="0" column="0">
                    <widget class="QGroupBox" name="gb_general_settings"><property name="title"><string>GENERAL SETTINGS</string></property>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Language</string></property></widget></item>
                            <item row="0" column="1"><widget class="QComboBox"><item><property name="text"><string>English</string></property></item></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Theme</string></property></widget></item>
                            <item row="1" column="1"><widget class="QComboBox"><item><property name="text"><string>Dark</string></property></item></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Distance Units</string></property></widget></item>
                            <item row="2" column="1"><widget class="QComboBox"><item><property name="text"><string>mm</string></property></item></widget></item>
                            <item row="3" column="0"><widget class="QLabel"><property name="text"><string>Temperature Units</string></property></widget></item>
                            <item row="3" column="1"><widget class="QComboBox"><item><property name="text"><string>C</string></property></item></widget></item>
                        </layout>
                    </widget>
                </item>
                <item row="0" column="1">
                    <widget class="QGroupBox" name="gb_display_settings"><property name="title"><string>DISPLAY SETTINGS</string></property>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Refresh Interval</string></property></widget></item>
                            <item row="0" column="1"><widget class="QComboBox"><item><property name="text"><string>500 ms</string></property></item></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Graph Time Range</string></property></widget></item>
                            <item row="1" column="1"><widget class="QComboBox"><item><property name="text"><string>3 Minutes</string></property></item></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Show Grid in Graph</string></property></widget></item>
                            <item row="2" column="1"><widget class="QCheckBox"/></item>
                        </layout>
                    </widget>
                </item>
                <item row="0" column="2">
                    <widget class="QGroupBox" name="gb_notif_settings"><property name="title"><string>NOTIFICATION SETTINGS</string></property>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Alarm Notifications</string></property></widget></item>
                            <item row="0" column="1"><widget class="QCheckBox"/></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Sound Alerts</string></property></widget></item>
                            <item row="1" column="1"><widget class="QCheckBox"/></item>
                            <item row="2" column="0" colspan="2"><widget class="QPushButton"><property name="text"><string>Test Notification</string></property></widget></item>
                        </layout>
                    </widget>
                </item>
                <item row="1" column="0">
                    <widget class="QGroupBox" name="gb_alarm_thresholds"><property name="title"><string>ALARM THRESHOLDS</string></property>
                        <layout class="QVBoxLayout">
                            <item>
                                <widget class="QTableWidget">
                                    <property name="columnCount"><number>3</number></property>
                                    <column><property name="text"><string>Parameter</string></property></column>
                                    <column><property name="text"><string>Warning</string></property></column>
                                    <column><property name="text"><string>Critical</string></property></column>
                                </widget>
                            </item>
                            <item><widget class="QPushButton"><property name="text"><string>Save Thresholds</string></property></widget></item>
                        </layout>
                    </widget>
                </item>
                <item row="1" column="1">
                    <widget class="QGroupBox" name="gb_file_settings"><property name="title"><string>FILE SETTINGS</string></property>
                        <layout class="QFormLayout">
                            <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Default G-code</string></property></widget></item>
                            <item row="0" column="1"><widget class="QLineEdit"><property name="text"><string>D:\Metal3D\Gcode</string></property></widget></item>
                            <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Default Export</string></property></widget></item>
                            <item row="1" column="1"><widget class="QLineEdit"><property name="text"><string>D:\Metal3D\Exports</string></property></widget></item>
                            <item row="2" column="0"><widget class="QLabel"><property name="text"><string>Enable Auto Save</string></property></widget></item>
                            <item row="2" column="1"><widget class="QCheckBox"/></item>
                        </layout>
                    </widget>
                </item>
                <item row="1" column="2">
                    <widget class="QGroupBox" name="gb_data_backup"><property name="title"><string>DATA &amp; BACKUP</string></property>
                        <layout class="QVBoxLayout">
                            <item><widget class="QPushButton"><property name="text"><string>Backup Now</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Restore</string></property></widget></item>
                            <item><widget class="QPushButton"><property name="text"><string>Reset</string></property></widget></item>
                        </layout>
                    </widget>
                </item>
            </layout>
        </widget>
    </widget>
  </item>
  
  <item>
    <layout class="QVBoxLayout">
        <item>
            <widget class="QGroupBox" name="gb_sys_info"><property name="title"><string>SYSTEM INFORMATION</string></property>
                <layout class="QFormLayout">
                    <item row="0" column="0"><widget class="QLabel"><property name="text"><string>Software Version</string></property></widget></item>
                    <item row="0" column="1"><widget class="QLabel"><property name="text"><string>2.4.1</string></property></widget></item>
                    <item row="1" column="0"><widget class="QLabel"><property name="text"><string>Build Number</string></property></widget></item>
                    <item row="1" column="1"><widget class="QLabel"><property name="text"><string>20260707.1</string></property></widget></item>
                    <item row="2" column="0"><widget class="QLabel"><property name="text"><string>UI Framework</string></property></widget></item>
                    <item row="2" column="1"><widget class="QLabel"><property name="text"><string>Qt 6.6.2</string></property></widget></item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_data_mgmt"><property name="title"><string>DATA MANAGEMENT</string></property>
                <layout class="QVBoxLayout">
                    <item><widget class="QPushButton"><property name="text"><string>Export Report</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Clear Data</string></property></widget></item>
                </layout>
            </widget>
        </item>
        <item>
            <widget class="QGroupBox" name="gb_quick_settings"><property name="title"><string>QUICK SETTINGS</string></property>
                <layout class="QVBoxLayout">
                    <item><widget class="QPushButton"><property name="text"><string>Communication Ports</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>Bloodhound Access</string></property></widget></item>
                    <item><widget class="QPushButton"><property name="text"><string>License Information</string></property></widget></item>
                </layout>
            </widget>
        </item>
    </layout>
  </item>
</layout>
"""
    new_layout = ET.fromstring(xml)
    page.append(new_layout)
    print("Injected settings page")

if __name__ == '__main__':
    file_path = 'metal_dashboard.ui'
    tree = ET.parse(file_path)
    root = tree.getroot()
    inject_alarm_events(root)
    inject_logs(root)
    inject_maintenance(root)
    inject_settings(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print("Batch 3 completed!")
