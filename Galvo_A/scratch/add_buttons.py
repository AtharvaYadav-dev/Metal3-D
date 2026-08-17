with open("metal_dashboard.ui", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("name=\"sliderRow\"")
if idx != -1:
    end_item = text.find("</layout>\n                 </item>", idx)
    if end_item != -1:
        end_pos = end_item + len("</layout>\n                 </item>")
        xml = """
                 <item>
                  <layout class="QHBoxLayout" name="processControlRow">
                   <property name="spacing">
                    <number>12</number>
                   </property>
                   <item>
                    <widget class="QPushButton" name="btn_start_process">
                     <property name="minimumSize">
                      <size>
                       <width>0</width>
                       <height>42</height>
                      </size>
                     </property>
                     <property name="styleSheet">
                      <string notr="true">QPushButton { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #10b981, stop:1 #059669); color: #ffffff; font-weight: bold; font-size: 13px; font-family: sans-serif; border: 1px solid #047857; border-radius: 6px; padding: 6px 12px; } QPushButton:hover { background: #10b981; } QPushButton:pressed { background: #047857; }</string>
                     </property>
                     <property name="text">
                      <string>START PROCESS</string>
                     </property>
                    </widget>
                   </item>
                   <item>
                    <widget class="QPushButton" name="btn_pause_process">
                     <property name="minimumSize">
                      <size>
                       <width>0</width>
                       <height>42</height>
                      </size>
                     </property>
                     <property name="styleSheet">
                      <string notr="true">QPushButton { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f59e0b, stop:1 #d97706); color: #ffffff; font-weight: bold; font-size: 13px; font-family: sans-serif; border: 1px solid #b45309; border-radius: 6px; padding: 6px 12px; } QPushButton:hover { background: #f59e0b; } QPushButton:pressed { background: #b45309; }</string>
                     </property>
                     <property name="text">
                      <string>PAUSE PROCESS</string>
                     </property>
                    </widget>
                   </item>
                   <item>
                    <widget class="QPushButton" name="btn_stop_process">
                     <property name="minimumSize">
                      <size>
                       <width>0</width>
                       <height>42</height>
                      </size>
                     </property>
                     <property name="styleSheet">
                      <string notr="true">QPushButton { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ef4444, stop:1 #dc2626); color: #ffffff; font-weight: bold; font-size: 13px; font-family: sans-serif; border: 1px solid #b91c1c; border-radius: 6px; padding: 6px 12px; } QPushButton:hover { background: #ef4444; } QPushButton:pressed { background: #b91c1c; }</string>
                     </property>
                     <property name="text">
                      <string>STOP PROCESS</string>
                     </property>
                    </widget>
                   </item>
                  </layout>
                 </item>"""
        new_text = text[:end_pos] + xml + text[end_pos:]
        with open("metal_dashboard.ui", "w", encoding="utf-8") as f:
            f.write(new_text)
        print("[PASS] Added 3 process control buttons to metal_dashboard.ui!")
