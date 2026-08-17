import re

with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace standard UV UI
old_u = """            self.uminusPushButton = QPushButton("U-", self.uvFrame)
            self.uminusPushButton.setObjectName("uminusPushButton")
            self.uplusPushButton = QPushButton("U+", self.uvFrame)
            self.uplusPushButton.setObjectName("uplusPushButton")
            
            u_layout.addWidget(u_label)
            u_layout.addWidget(self.uposLCDNumber)
            u_layout.addWidget(self.uminusPushButton)
            u_layout.addWidget(self.uplusPushButton)"""

new_u = """            self.utravelPushButton = QPushButton("10.0", self.uvFrame)
            self.utravelPushButton.setObjectName("utravelPushButton")
            self.uhomePushButton = QPushButton("Home", self.uvFrame)
            self.uhomePushButton.setObjectName("uhomePushButton")
            self.uminusPushButton = QPushButton("U-", self.uvFrame)
            self.uminusPushButton.setObjectName("uminusPushButton")
            self.uplusPushButton = QPushButton("U+", self.uvFrame)
            self.uplusPushButton.setObjectName("uplusPushButton")
            
            u_layout.addWidget(u_label)
            u_layout.addWidget(self.uposLCDNumber)
            u_layout.addWidget(self.utravelPushButton)
            u_layout.addWidget(self.uhomePushButton)
            u_layout.addWidget(self.uminusPushButton)
            u_layout.addWidget(self.uplusPushButton)"""

content = content.replace(old_u, new_u)

old_v = """            self.vminusPushButton = QPushButton("V-", self.uvFrame)
            self.vminusPushButton.setObjectName("vminusPushButton")
            self.vplusPushButton = QPushButton("V+", self.uvFrame)
            self.vplusPushButton.setObjectName("vplusPushButton")
            
            v_layout.addWidget(v_label)
            v_layout.addWidget(self.vposLCDNumber)
            v_layout.addWidget(self.vminusPushButton)
            v_layout.addWidget(self.vplusPushButton)"""

new_v = """            self.vtravelPushButton = QPushButton("10.0", self.uvFrame)
            self.vtravelPushButton.setObjectName("vtravelPushButton")
            self.vhomePushButton = QPushButton("Home", self.uvFrame)
            self.vhomePushButton.setObjectName("vhomePushButton")
            self.vminusPushButton = QPushButton("V-", self.uvFrame)
            self.vminusPushButton.setObjectName("vminusPushButton")
            self.vplusPushButton = QPushButton("V+", self.uvFrame)
            self.vplusPushButton.setObjectName("vplusPushButton")
            
            v_layout.addWidget(v_label)
            v_layout.addWidget(self.vposLCDNumber)
            v_layout.addWidget(self.vtravelPushButton)
            v_layout.addWidget(self.vhomePushButton)
            v_layout.addWidget(self.vminusPushButton)
            v_layout.addWidget(self.vplusPushButton)"""

content = content.replace(old_v, new_v)

old_map = """            uv_widget_list.append(self.wh.configWidget(self, QPushButton, "vminusPushButton", "clicked", self.jogAction, role="vminus"))
            uv_widget_list.append(self.wh.configWidget(self, QPushButton, "vplusPushButton", "clicked", self.jogAction, role="vplus"))"""

new_map = """            uv_widget_list.append(self.wh.configWidget(self, QPushButton, "vminusPushButton", "clicked", self.jogAction, role="vminus"))
            uv_widget_list.append(self.wh.configWidget(self, QPushButton, "vplusPushButton", "clicked", self.jogAction, role="vplus"))
            uv_widget_list.append(self.wh.configWidget(self, QPushButton, "utravelPushButton", "clicked", self.jogAction, role="utravel_btn"))
            uv_widget_list.append(self.wh.configWidget(self, QPushButton, "uhomePushButton", "clicked", self.jogAction, role="uhome"))
            uv_widget_list.append(self.wh.configWidget(self, QPushButton, "vtravelPushButton", "clicked", self.jogAction, role="vtravel_btn"))
            uv_widget_list.append(self.wh.configWidget(self, QPushButton, "vhomePushButton", "clicked", self.jogAction, role="vhome"))"""

content = content.replace(old_map, new_map)


# Replace galvo UV UI
old_u_g = """            self.uminusPushButton_g = QPushButton("U-", self.uvFrameGalvo)
            self.uminusPushButton_g.setObjectName("uminusPushButton_g")
            self.uplusPushButton_g = QPushButton("U+", self.uvFrameGalvo)
            self.uplusPushButton_g.setObjectName("uplusPushButton_g")
            
            u_layout_g.addWidget(u_label_g)
            u_layout_g.addWidget(self.uposLCDNumber_g)
            u_layout_g.addWidget(self.uminusPushButton_g)
            u_layout_g.addWidget(self.uplusPushButton_g)"""

new_u_g = """            self.utravelPushButton_g = QPushButton("10.0", self.uvFrameGalvo)
            self.utravelPushButton_g.setObjectName("utravelPushButton_g")
            self.uhomePushButton_g = QPushButton("Home", self.uvFrameGalvo)
            self.uhomePushButton_g.setObjectName("uhomePushButton_g")
            self.uminusPushButton_g = QPushButton("U-", self.uvFrameGalvo)
            self.uminusPushButton_g.setObjectName("uminusPushButton_g")
            self.uplusPushButton_g = QPushButton("U+", self.uvFrameGalvo)
            self.uplusPushButton_g.setObjectName("uplusPushButton_g")
            
            u_layout_g.addWidget(u_label_g)
            u_layout_g.addWidget(self.uposLCDNumber_g)
            u_layout_g.addWidget(self.utravelPushButton_g)
            u_layout_g.addWidget(self.uhomePushButton_g)
            u_layout_g.addWidget(self.uminusPushButton_g)
            u_layout_g.addWidget(self.uplusPushButton_g)"""

content = content.replace(old_u_g, new_u_g)

old_v_g = """            self.vminusPushButton_g = QPushButton("V-", self.uvFrameGalvo)
            self.vminusPushButton_g.setObjectName("vminusPushButton_g")
            self.vplusPushButton_g = QPushButton("V+", self.uvFrameGalvo)
            self.vplusPushButton_g.setObjectName("vplusPushButton_g")
            
            v_layout_g.addWidget(v_label_g)
            v_layout_g.addWidget(self.vposLCDNumber_g)
            v_layout_g.addWidget(self.vminusPushButton_g)
            v_layout_g.addWidget(self.vplusPushButton_g)"""

new_v_g = """            self.vtravelPushButton_g = QPushButton("10.0", self.uvFrameGalvo)
            self.vtravelPushButton_g.setObjectName("vtravelPushButton_g")
            self.vhomePushButton_g = QPushButton("Home", self.uvFrameGalvo)
            self.vhomePushButton_g.setObjectName("vhomePushButton_g")
            self.vminusPushButton_g = QPushButton("V-", self.uvFrameGalvo)
            self.vminusPushButton_g.setObjectName("vminusPushButton_g")
            self.vplusPushButton_g = QPushButton("V+", self.uvFrameGalvo)
            self.vplusPushButton_g.setObjectName("vplusPushButton_g")
            
            v_layout_g.addWidget(v_label_g)
            v_layout_g.addWidget(self.vposLCDNumber_g)
            v_layout_g.addWidget(self.vtravelPushButton_g)
            v_layout_g.addWidget(self.vhomePushButton_g)
            v_layout_g.addWidget(self.vminusPushButton_g)
            v_layout_g.addWidget(self.vplusPushButton_g)"""

content = content.replace(old_v_g, new_v_g)

old_map_g = """            uv_widget_list_g.append(self.wh.configWidget(self, QPushButton, "vminusPushButton_g", "clicked", self.jogGalvoAction, role="vminusgalvo"))
            uv_widget_list_g.append(self.wh.configWidget(self, QPushButton, "vplusPushButton_g", "clicked", self.jogGalvoAction, role="vplusgalvo"))"""

new_map_g = """            uv_widget_list_g.append(self.wh.configWidget(self, QPushButton, "vminusPushButton_g", "clicked", self.jogGalvoAction, role="vminusgalvo"))
            uv_widget_list_g.append(self.wh.configWidget(self, QPushButton, "vplusPushButton_g", "clicked", self.jogGalvoAction, role="vplusgalvo"))
            uv_widget_list_g.append(self.wh.configWidget(self, QPushButton, "utravelPushButton_g", "clicked", self.jogGalvoAction, role="utravelgalvo"))
            uv_widget_list_g.append(self.wh.configWidget(self, QPushButton, "uhomePushButton_g", "clicked", self.jogGalvoAction, role="uhomegalvo"))
            uv_widget_list_g.append(self.wh.configWidget(self, QPushButton, "vtravelPushButton_g", "clicked", self.jogGalvoAction, role="vtravelgalvo"))
            uv_widget_list_g.append(self.wh.configWidget(self, QPushButton, "vhomePushButton_g", "clicked", self.jogGalvoAction, role="vhomegalvo"))"""

content = content.replace(old_map_g, new_map_g)

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Replaced successfully")
