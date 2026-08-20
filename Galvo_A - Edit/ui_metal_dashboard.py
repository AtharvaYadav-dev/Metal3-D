# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'metal_dashboardmweykC.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1527, 843)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(4)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(2, 2, 2, 2)
        self.sidebarFrame = QFrame(self.centralwidget)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setMaximumSize(QSize(240, 16777215))
        self.verticalLayout = QVBoxLayout(self.sidebarFrame)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logoLabel = QLabel(self.sidebarFrame)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(0, 80))
        self.logoLabel.setTextFormat(Qt.TextFormat.RichText)
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.logoLabel)

        self.btnDashboard = QPushButton(self.sidebarFrame)
        self.btnDashboard.setObjectName(u"btnDashboard")
        self.btnDashboard.setMinimumSize(QSize(0, 20))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        self.btnDashboard.setFont(font)
        self.btnDashboard.setCheckable(True)
        self.btnDashboard.setChecked(True)

        self.verticalLayout.addWidget(self.btnDashboard)

        self.btnBuildSetup = QPushButton(self.sidebarFrame)
        self.btnBuildSetup.setObjectName(u"btnBuildSetup")
        self.btnBuildSetup.setMinimumSize(QSize(0, 20))
        self.btnBuildSetup.setFont(font)
        self.btnBuildSetup.setCheckable(True)
        self.btnBuildSetup.setChecked(False)

        self.verticalLayout.addWidget(self.btnBuildSetup)

        self.btnGCode = QPushButton(self.sidebarFrame)
        self.btnGCode.setObjectName(u"btnGCode")
        self.btnGCode.setMinimumSize(QSize(0, 20))
        self.btnGCode.setFont(font)
        self.btnGCode.setCheckable(True)
        self.btnGCode.setChecked(False)

        self.verticalLayout.addWidget(self.btnGCode)

        self.btnMachineControl = QPushButton(self.sidebarFrame)
        self.btnMachineControl.setObjectName(u"btnMachineControl")
        self.btnMachineControl.setMinimumSize(QSize(0, 20))
        self.btnMachineControl.setFont(font)
        self.btnMachineControl.setCheckable(True)
        self.btnMachineControl.setChecked(False)

        self.verticalLayout.addWidget(self.btnMachineControl)

        self.btnLaserGalvo = QPushButton(self.sidebarFrame)
        self.btnLaserGalvo.setObjectName(u"btnLaserGalvo")
        self.btnLaserGalvo.setMinimumSize(QSize(0, 20))
        self.btnLaserGalvo.setFont(font)
        self.btnLaserGalvo.setCheckable(True)
        self.btnLaserGalvo.setChecked(False)

        self.verticalLayout.addWidget(self.btnLaserGalvo)

        self.btnMotors = QPushButton(self.sidebarFrame)
        self.btnMotors.setObjectName(u"btnMotors")
        self.btnMotors.setMinimumSize(QSize(0, 20))
        self.btnMotors.setFont(font)
        self.btnMotors.setCheckable(True)
        self.btnMotors.setChecked(False)

        self.verticalLayout.addWidget(self.btnMotors)

        self.btnSensors = QPushButton(self.sidebarFrame)
        self.btnSensors.setObjectName(u"btnSensors")
        self.btnSensors.setMinimumSize(QSize(0, 20))
        self.btnSensors.setFont(font)
        self.btnSensors.setCheckable(True)
        self.btnSensors.setChecked(False)

        self.verticalLayout.addWidget(self.btnSensors)

        self.btnAlarmEvents = QPushButton(self.sidebarFrame)
        self.btnAlarmEvents.setObjectName(u"btnAlarmEvents")
        self.btnAlarmEvents.setMinimumSize(QSize(0, 20))
        self.btnAlarmEvents.setFont(font)
        self.btnAlarmEvents.setCheckable(True)
        self.btnAlarmEvents.setChecked(False)

        self.verticalLayout.addWidget(self.btnAlarmEvents)

        self.btnLogs = QPushButton(self.sidebarFrame)
        self.btnLogs.setObjectName(u"btnLogs")
        self.btnLogs.setMinimumSize(QSize(0, 20))
        self.btnLogs.setFont(font)
        self.btnLogs.setCheckable(True)
        self.btnLogs.setChecked(False)

        self.verticalLayout.addWidget(self.btnLogs)

        self.btnSettings = QPushButton(self.sidebarFrame)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setMinimumSize(QSize(0, 20))
        self.btnSettings.setFont(font)
        self.btnSettings.setCheckable(True)
        self.btnSettings.setChecked(False)

        self.verticalLayout.addWidget(self.btnSettings)

        self.btnSettings_2 = QPushButton(self.sidebarFrame)
        self.btnSettings_2.setObjectName(u"btnSettings_2")
        self.btnSettings_2.setMinimumSize(QSize(0, 20))
        self.btnSettings_2.setFont(font)
        self.btnSettings_2.setCheckable(True)
        self.btnSettings_2.setChecked(False)

        self.verticalLayout.addWidget(self.btnSettings_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnEmergencyStop = QPushButton(self.sidebarFrame)
        self.btnEmergencyStop.setObjectName(u"btnEmergencyStop")
        self.btnEmergencyStop.setMinimumSize(QSize(0, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.btnEmergencyStop.setFont(font1)

        self.verticalLayout.addWidget(self.btnEmergencyStop)


        self.mainLayout.addWidget(self.sidebarFrame)

        self.rightAreaLayout = QVBoxLayout()
        self.rightAreaLayout.setSpacing(4)
        self.rightAreaLayout.setObjectName(u"rightAreaLayout")
        self.topbarFrame = QFrame(self.centralwidget)
        self.topbarFrame.setObjectName(u"topbarFrame")
        self.topbarFrame.setMaximumSize(QSize(16777215, 70))
        self.topbarLayout = QHBoxLayout(self.topbarFrame)
        self.topbarLayout.setSpacing(4)
        self.topbarLayout.setObjectName(u"topbarLayout")
        self.topbarLayout.setContentsMargins(2, -1, 2, -1)
        self.lblConnectionStatus = QLabel(self.topbarFrame)
        self.lblConnectionStatus.setObjectName(u"lblConnectionStatus")

        self.topbarLayout.addWidget(self.lblConnectionStatus)

        self.comboPort = QComboBox(self.topbarFrame)
        self.comboPort.addItem("")
        self.comboPort.setObjectName(u"comboPort")
        self.comboPort.setMinimumSize(QSize(100, 35))

        self.topbarLayout.addWidget(self.comboPort)

        self.btnDisconnect = QPushButton(self.topbarFrame)
        self.btnDisconnect.setObjectName(u"btnDisconnect")
        self.btnDisconnect.setMinimumSize(QSize(100, 20))

        self.topbarLayout.addWidget(self.btnDisconnect)

        self.topbarSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.topbarLayout.addItem(self.topbarSpacer1)

        self.lblJobInfo = QLabel(self.topbarFrame)
        self.lblJobInfo.setObjectName(u"lblJobInfo")

        self.topbarLayout.addWidget(self.lblJobInfo)

        self.topbarSpacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.topbarLayout.addItem(self.topbarSpacer2)

        self.comboUser = QComboBox(self.topbarFrame)
        self.comboUser.addItem("")
        self.comboUser.setObjectName(u"comboUser")
        self.comboUser.setMinimumSize(QSize(150, 35))

        self.topbarLayout.addWidget(self.comboUser)


        self.rightAreaLayout.addWidget(self.topbarFrame)

        self.statusBarFrame = QFrame(self.centralwidget)
        self.statusBarFrame.setObjectName(u"statusBarFrame")
        self.statusBarFrame.setMaximumSize(QSize(16777215, 50))
        self.statusLayout = QHBoxLayout(self.statusBarFrame)
        self.statusLayout.setSpacing(4)
        self.statusLayout.setObjectName(u"statusLayout")
        self.label = QLabel(self.statusBarFrame)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.TextFormat.RichText)

        self.statusLayout.addWidget(self.label)

        self.label1 = QLabel(self.statusBarFrame)
        self.label1.setObjectName(u"label1")
        self.label1.setTextFormat(Qt.TextFormat.RichText)

        self.statusLayout.addWidget(self.label1)

        self.label2 = QLabel(self.statusBarFrame)
        self.label2.setObjectName(u"label2")
        self.label2.setTextFormat(Qt.TextFormat.RichText)

        self.statusLayout.addWidget(self.label2)

        self.label3 = QLabel(self.statusBarFrame)
        self.label3.setObjectName(u"label3")
        self.label3.setTextFormat(Qt.TextFormat.RichText)

        self.statusLayout.addWidget(self.label3)

        self.label4 = QLabel(self.statusBarFrame)
        self.label4.setObjectName(u"label4")
        self.label4.setTextFormat(Qt.TextFormat.RichText)

        self.statusLayout.addWidget(self.label4)

        self.label5 = QLabel(self.statusBarFrame)
        self.label5.setObjectName(u"label5")
        self.label5.setTextFormat(Qt.TextFormat.RichText)

        self.statusLayout.addWidget(self.label5)

        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.statusLayout.addItem(self.spacerItem)

        self.label6 = QLabel(self.statusBarFrame)
        self.label6.setObjectName(u"label6")
        self.label6.setTextFormat(Qt.TextFormat.RichText)
        self.label6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.statusLayout.addWidget(self.label6)


        self.rightAreaLayout.addWidget(self.statusBarFrame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.vLayout_page_dashboard = QVBoxLayout(self.page_dashboard)
        self.vLayout_page_dashboard.setObjectName(u"vLayout_page_dashboard")
        self.hLayout_top = QHBoxLayout()
        self.hLayout_top.setObjectName(u"hLayout_top")
        self.gb_machine_status = QGroupBox(self.page_dashboard)
        self.gb_machine_status.setObjectName(u"gb_machine_status")
        self.hboxLayout = QHBoxLayout(self.gb_machine_status)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.lbl_status_icon = QLabel(self.gb_machine_status)
        self.lbl_status_icon.setObjectName(u"lbl_status_icon")

        self.hboxLayout.addWidget(self.lbl_status_icon)

        self.lbl_status_text = QLabel(self.gb_machine_status)
        self.lbl_status_text.setObjectName(u"lbl_status_text")

        self.hboxLayout.addWidget(self.lbl_status_text)


        self.hLayout_top.addWidget(self.gb_machine_status)

        self.gb_build_progress = QGroupBox(self.page_dashboard)
        self.gb_build_progress.setObjectName(u"gb_build_progress")
        self.hboxLayout1 = QHBoxLayout(self.gb_build_progress)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.lbl_prog_circle = QLabel(self.gb_build_progress)
        self.lbl_prog_circle.setObjectName(u"lbl_prog_circle")

        self.hboxLayout1.addWidget(self.lbl_prog_circle)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label7 = QLabel(self.gb_build_progress)
        self.label7.setObjectName(u"label7")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label7)

        self.label8 = QLabel(self.gb_build_progress)
        self.label8.setObjectName(u"label8")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label8)

        self.label9 = QLabel(self.gb_build_progress)
        self.label9.setObjectName(u"label9")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label9)

        self.label10 = QLabel(self.gb_build_progress)
        self.label10.setObjectName(u"label10")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label10)

        self.label11 = QLabel(self.gb_build_progress)
        self.label11.setObjectName(u"label11")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label11)

        self.label12 = QLabel(self.gb_build_progress)
        self.label12.setObjectName(u"label12")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label12)


        self.hboxLayout1.addLayout(self.formLayout)


        self.hLayout_top.addWidget(self.gb_build_progress)

        self.gb_laser_power_dash = QGroupBox(self.page_dashboard)
        self.gb_laser_power_dash.setObjectName(u"gb_laser_power_dash")
        self.vboxLayout = QVBoxLayout(self.gb_laser_power_dash)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.lbl_laser_gauge = QLabel(self.gb_laser_power_dash)
        self.lbl_laser_gauge.setObjectName(u"lbl_laser_gauge")
        self.lbl_laser_gauge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.lbl_laser_gauge)


        self.hLayout_top.addWidget(self.gb_laser_power_dash)

        self.gb_chamber_temp_dash = QGroupBox(self.page_dashboard)
        self.gb_chamber_temp_dash.setObjectName(u"gb_chamber_temp_dash")
        self.formLayout1 = QFormLayout(self.gb_chamber_temp_dash)
        self.formLayout1.setObjectName(u"formLayout1")
        self.label13 = QLabel(self.gb_chamber_temp_dash)
        self.label13.setObjectName(u"label13")

        self.formLayout1.setWidget(0, QFormLayout.LabelRole, self.label13)

        self.label14 = QLabel(self.gb_chamber_temp_dash)
        self.label14.setObjectName(u"label14")

        self.formLayout1.setWidget(0, QFormLayout.FieldRole, self.label14)

        self.label15 = QLabel(self.gb_chamber_temp_dash)
        self.label15.setObjectName(u"label15")

        self.formLayout1.setWidget(1, QFormLayout.LabelRole, self.label15)

        self.label16 = QLabel(self.gb_chamber_temp_dash)
        self.label16.setObjectName(u"label16")

        self.formLayout1.setWidget(1, QFormLayout.FieldRole, self.label16)

        self.label17 = QLabel(self.gb_chamber_temp_dash)
        self.label17.setObjectName(u"label17")

        self.formLayout1.setWidget(2, QFormLayout.LabelRole, self.label17)

        self.label18 = QLabel(self.gb_chamber_temp_dash)
        self.label18.setObjectName(u"label18")

        self.formLayout1.setWidget(2, QFormLayout.FieldRole, self.label18)


        self.hLayout_top.addWidget(self.gb_chamber_temp_dash)

        self.gb_oxygen_level_dash = QGroupBox(self.page_dashboard)
        self.gb_oxygen_level_dash.setObjectName(u"gb_oxygen_level_dash")
        self.vboxLayout1 = QVBoxLayout(self.gb_oxygen_level_dash)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.lbl_oxy_gauge = QLabel(self.gb_oxygen_level_dash)
        self.lbl_oxy_gauge.setObjectName(u"lbl_oxy_gauge")
        self.lbl_oxy_gauge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout1.addWidget(self.lbl_oxy_gauge)


        self.hLayout_top.addWidget(self.gb_oxygen_level_dash)


        self.vLayout_page_dashboard.addLayout(self.hLayout_top)

        self.hLayout_middle = QHBoxLayout()
        self.hLayout_middle.setObjectName(u"hLayout_middle")
        self.gb_build_preview_dash = QGroupBox(self.page_dashboard)
        self.gb_build_preview_dash.setObjectName(u"gb_build_preview_dash")
        self.hboxLayout2 = QHBoxLayout(self.gb_build_preview_dash)
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.vboxLayout2 = QVBoxLayout()
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.pushButton = QPushButton(self.gb_build_preview_dash)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(45, 30))

        self.vboxLayout2.addWidget(self.pushButton)

        self.pushButton1 = QPushButton(self.gb_build_preview_dash)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setMaximumSize(QSize(45, 30))

        self.vboxLayout2.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton(self.gb_build_preview_dash)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setMaximumSize(QSize(45, 30))

        self.vboxLayout2.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton(self.gb_build_preview_dash)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setMaximumSize(QSize(45, 30))

        self.vboxLayout2.addWidget(self.pushButton3)

        self.pushButton4 = QPushButton(self.gb_build_preview_dash)
        self.pushButton4.setObjectName(u"pushButton4")
        self.pushButton4.setMaximumSize(QSize(45, 30))

        self.vboxLayout2.addWidget(self.pushButton4)

        self.pushButton5 = QPushButton(self.gb_build_preview_dash)
        self.pushButton5.setObjectName(u"pushButton5")
        self.pushButton5.setMaximumSize(QSize(45, 30))

        self.vboxLayout2.addWidget(self.pushButton5)

        self.pushButton6 = QPushButton(self.gb_build_preview_dash)
        self.pushButton6.setObjectName(u"pushButton6")
        self.pushButton6.setMaximumSize(QSize(45, 30))

        self.vboxLayout2.addWidget(self.pushButton6)

        self.spacerItem1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout2.addItem(self.spacerItem1)


        self.hboxLayout2.addLayout(self.vboxLayout2)

        self.vboxLayout3 = QVBoxLayout()
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.label19 = QLabel(self.gb_build_preview_dash)
        self.label19.setObjectName(u"label19")
        sizePolicy.setHeightForWidth(self.label19.sizePolicy().hasHeightForWidth())
        self.label19.setSizePolicy(sizePolicy)
        self.label19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout3.addWidget(self.label19)

        self.hboxLayout3 = QHBoxLayout()
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.checkBox = QCheckBox(self.gb_build_preview_dash)
        self.checkBox.setObjectName(u"checkBox")

        self.hboxLayout3.addWidget(self.checkBox)

        self.checkBox1 = QCheckBox(self.gb_build_preview_dash)
        self.checkBox1.setObjectName(u"checkBox1")

        self.hboxLayout3.addWidget(self.checkBox1)

        self.slider = QSlider(self.gb_build_preview_dash)
        self.slider.setObjectName(u"slider")
        self.slider.setOrientation(Qt.Orientation.Horizontal)

        self.hboxLayout3.addWidget(self.slider)

        self.label20 = QLabel(self.gb_build_preview_dash)
        self.label20.setObjectName(u"label20")

        self.hboxLayout3.addWidget(self.label20)


        self.vboxLayout3.addLayout(self.hboxLayout3)


        self.hboxLayout2.addLayout(self.vboxLayout3)

        self.slider1 = QSlider(self.gb_build_preview_dash)
        self.slider1.setObjectName(u"slider1")
        self.slider1.setOrientation(Qt.Orientation.Vertical)

        self.hboxLayout2.addWidget(self.slider1)


        self.hLayout_middle.addWidget(self.gb_build_preview_dash)

        self.vboxLayout4 = QVBoxLayout()
        self.vboxLayout4.setObjectName(u"vboxLayout4")
        self.gb_axis_position = QGroupBox(self.page_dashboard)
        self.gb_axis_position.setObjectName(u"gb_axis_position")
        self.gridLayout = QGridLayout(self.gb_axis_position)
        self.gridLayout.setObjectName(u"gridLayout")
        self.uposlcddisplay = QLineEdit(self.gb_axis_position)
        self.uposlcddisplay.setObjectName(u"uposlcddisplay")

        self.gridLayout.addWidget(self.uposlcddisplay, 1, 0, 1, 1)

        self.zposlcddisplay = QLineEdit(self.gb_axis_position)
        self.zposlcddisplay.setObjectName(u"zposlcddisplay")

        self.gridLayout.addWidget(self.zposlcddisplay, 1, 2, 1, 1)

        self.galvohomepushButton = QPushButton(self.gb_axis_position)
        self.galvohomepushButton.setObjectName(u"galvohomepushButton")

        self.gridLayout.addWidget(self.galvohomepushButton, 2, 2, 1, 1)

        self.vposlcddisplay = QLineEdit(self.gb_axis_position)
        self.vposlcddisplay.setObjectName(u"vposlcddisplay")

        self.gridLayout.addWidget(self.vposlcddisplay, 1, 1, 1, 1)

        self.allhomepushButton = QPushButton(self.gb_axis_position)
        self.allhomepushButton.setObjectName(u"allhomepushButton")

        self.gridLayout.addWidget(self.allhomepushButton, 2, 0, 1, 2)

        self.label21 = QLabel(self.gb_axis_position)
        self.label21.setObjectName(u"label21")
        self.label21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label21, 0, 0, 1, 1)

        self.label22 = QLabel(self.gb_axis_position)
        self.label22.setObjectName(u"label22")
        self.label22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label22, 0, 2, 1, 1)

        self.label23 = QLabel(self.gb_axis_position)
        self.label23.setObjectName(u"label23")
        self.label23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label23, 0, 1, 1, 1)


        self.vboxLayout4.addWidget(self.gb_axis_position)

        self.gb_jog_control = QGroupBox(self.page_dashboard)
        self.gb_jog_control.setObjectName(u"gb_jog_control")
        self.vboxLayout5 = QVBoxLayout(self.gb_jog_control)
        self.vboxLayout5.setObjectName(u"vboxLayout5")
        self.hboxLayout4 = QHBoxLayout()
        self.hboxLayout4.setObjectName(u"hboxLayout4")
        self.travelpushButton_1 = QPushButton(self.gb_jog_control)
        self.travelpushButton_1.setObjectName(u"travelpushButton_1")

        self.hboxLayout4.addWidget(self.travelpushButton_1)

        self.travelpushButton_2 = QPushButton(self.gb_jog_control)
        self.travelpushButton_2.setObjectName(u"travelpushButton_2")

        self.hboxLayout4.addWidget(self.travelpushButton_2)

        self.travelpushButton_3 = QPushButton(self.gb_jog_control)
        self.travelpushButton_3.setObjectName(u"travelpushButton_3")

        self.hboxLayout4.addWidget(self.travelpushButton_3)

        self.travelpushButton_4 = QPushButton(self.gb_jog_control)
        self.travelpushButton_4.setObjectName(u"travelpushButton_4")

        self.hboxLayout4.addWidget(self.travelpushButton_4)

        self.travelpushButton_5 = QPushButton(self.gb_jog_control)
        self.travelpushButton_5.setObjectName(u"travelpushButton_5")

        self.hboxLayout4.addWidget(self.travelpushButton_5)


        self.vboxLayout5.addLayout(self.hboxLayout4)

        self.hboxLayout5 = QHBoxLayout()
        self.hboxLayout5.setObjectName(u"hboxLayout5")
        self.gridLayout1 = QGridLayout()
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.upluspushButton = QPushButton(self.gb_jog_control)
        self.upluspushButton.setObjectName(u"upluspushButton")
        self.upluspushButton.setMaximumSize(QSize(45, 30))

        self.gridLayout1.addWidget(self.upluspushButton, 0, 1, 1, 1)

        self.vminuspushButton = QPushButton(self.gb_jog_control)
        self.vminuspushButton.setObjectName(u"vminuspushButton")
        self.vminuspushButton.setMaximumSize(QSize(45, 30))

        self.gridLayout1.addWidget(self.vminuspushButton, 1, 0, 1, 1)

        self.pushButton7 = QPushButton(self.gb_jog_control)
        self.pushButton7.setObjectName(u"pushButton7")
        self.pushButton7.setMaximumSize(QSize(45, 30))

        self.gridLayout1.addWidget(self.pushButton7, 1, 1, 1, 1)

        self.vpluspushButton = QPushButton(self.gb_jog_control)
        self.vpluspushButton.setObjectName(u"vpluspushButton")
        self.vpluspushButton.setMaximumSize(QSize(45, 30))

        self.gridLayout1.addWidget(self.vpluspushButton, 1, 2, 1, 1)

        self.uminuspushButton = QPushButton(self.gb_jog_control)
        self.uminuspushButton.setObjectName(u"uminuspushButton")
        self.uminuspushButton.setMaximumSize(QSize(45, 30))

        self.gridLayout1.addWidget(self.uminuspushButton, 2, 1, 1, 1)


        self.hboxLayout5.addLayout(self.gridLayout1)

        self.vboxLayout6 = QVBoxLayout()
        self.vboxLayout6.setObjectName(u"vboxLayout6")
        self.zpluspushButton = QPushButton(self.gb_jog_control)
        self.zpluspushButton.setObjectName(u"zpluspushButton")
        self.zpluspushButton.setMaximumSize(QSize(45, 30))

        self.vboxLayout6.addWidget(self.zpluspushButton)

        self.spacerItem2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout6.addItem(self.spacerItem2)

        self.zminuspushButton = QPushButton(self.gb_jog_control)
        self.zminuspushButton.setObjectName(u"zminuspushButton")
        self.zminuspushButton.setMaximumSize(QSize(45, 30))

        self.vboxLayout6.addWidget(self.zminuspushButton)


        self.hboxLayout5.addLayout(self.vboxLayout6)

        self.hboxLayout5.setStretch(0, 4)
        self.hboxLayout5.setStretch(1, 2)

        self.vboxLayout5.addLayout(self.hboxLayout5)


        self.vboxLayout4.addWidget(self.gb_jog_control)


        self.hLayout_middle.addLayout(self.vboxLayout4)

        self.vboxLayout7 = QVBoxLayout()
        self.vboxLayout7.setObjectName(u"vboxLayout7")
        self.gb_job_control = QGroupBox(self.page_dashboard)
        self.gb_job_control.setObjectName(u"gb_job_control")
        self.vboxLayout8 = QVBoxLayout(self.gb_job_control)
        self.vboxLayout8.setObjectName(u"vboxLayout8")
        self.pushButton8 = QPushButton(self.gb_job_control)
        self.pushButton8.setObjectName(u"pushButton8")

        self.vboxLayout8.addWidget(self.pushButton8)

        self.pushButton9 = QPushButton(self.gb_job_control)
        self.pushButton9.setObjectName(u"pushButton9")

        self.vboxLayout8.addWidget(self.pushButton9)

        self.pushButton10 = QPushButton(self.gb_job_control)
        self.pushButton10.setObjectName(u"pushButton10")

        self.vboxLayout8.addWidget(self.pushButton10)

        self.pushButton11 = QPushButton(self.gb_job_control)
        self.pushButton11.setObjectName(u"pushButton11")

        self.vboxLayout8.addWidget(self.pushButton11)


        self.vboxLayout7.addWidget(self.gb_job_control)

        self.gb_layer_control_dash = QGroupBox(self.page_dashboard)
        self.gb_layer_control_dash.setObjectName(u"gb_layer_control_dash")
        self.vboxLayout9 = QVBoxLayout(self.gb_layer_control_dash)
        self.vboxLayout9.setObjectName(u"vboxLayout9")
        self.hboxLayout6 = QHBoxLayout()
        self.hboxLayout6.setObjectName(u"hboxLayout6")
        self.spacerItem3 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout6.addItem(self.spacerItem3)

        self.label24 = QLabel(self.gb_layer_control_dash)
        self.label24.setObjectName(u"label24")

        self.hboxLayout6.addWidget(self.label24)


        self.vboxLayout9.addLayout(self.hboxLayout6)

        self.slider2 = QSlider(self.gb_layer_control_dash)
        self.slider2.setObjectName(u"slider2")
        self.slider2.setOrientation(Qt.Orientation.Horizontal)

        self.vboxLayout9.addWidget(self.slider2)

        self.hboxLayout7 = QHBoxLayout()
        self.hboxLayout7.setObjectName(u"hboxLayout7")
        self.pushButton12 = QPushButton(self.gb_layer_control_dash)
        self.pushButton12.setObjectName(u"pushButton12")

        self.hboxLayout7.addWidget(self.pushButton12)

        self.pushButton13 = QPushButton(self.gb_layer_control_dash)
        self.pushButton13.setObjectName(u"pushButton13")

        self.hboxLayout7.addWidget(self.pushButton13)

        self.pushButton14 = QPushButton(self.gb_layer_control_dash)
        self.pushButton14.setObjectName(u"pushButton14")

        self.hboxLayout7.addWidget(self.pushButton14)

        self.pushButton15 = QPushButton(self.gb_layer_control_dash)
        self.pushButton15.setObjectName(u"pushButton15")

        self.hboxLayout7.addWidget(self.pushButton15)


        self.vboxLayout9.addLayout(self.hboxLayout7)

        self.pushButton16 = QPushButton(self.gb_layer_control_dash)
        self.pushButton16.setObjectName(u"pushButton16")

        self.vboxLayout9.addWidget(self.pushButton16)


        self.vboxLayout7.addWidget(self.gb_layer_control_dash)


        self.hLayout_middle.addLayout(self.vboxLayout7)

        self.hLayout_middle.setStretch(0, 2)
        self.hLayout_middle.setStretch(1, 1)
        self.hLayout_middle.setStretch(2, 1)

        self.vLayout_page_dashboard.addLayout(self.hLayout_middle)

        self.hLayout_bottom = QHBoxLayout()
        self.hLayout_bottom.setObjectName(u"hLayout_bottom")
        self.gb_console_log = QGroupBox(self.page_dashboard)
        self.gb_console_log.setObjectName(u"gb_console_log")
        self.vboxLayout10 = QVBoxLayout(self.gb_console_log)
        self.vboxLayout10.setObjectName(u"vboxLayout10")
        self.textEdit = QTextEdit(self.gb_console_log)
        self.textEdit.setObjectName(u"textEdit")

        self.vboxLayout10.addWidget(self.textEdit)

        self.hboxLayout8 = QHBoxLayout()
        self.hboxLayout8.setObjectName(u"hboxLayout8")
        self.spacerItem4 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout8.addItem(self.spacerItem4)

        self.pushButton17 = QPushButton(self.gb_console_log)
        self.pushButton17.setObjectName(u"pushButton17")
        self.pushButton17.setMaximumSize(QSize(60, 30))

        self.hboxLayout8.addWidget(self.pushButton17)

        self.checkBox2 = QCheckBox(self.gb_console_log)
        self.checkBox2.setObjectName(u"checkBox2")
        self.checkBox2.setChecked(True)

        self.hboxLayout8.addWidget(self.checkBox2)


        self.vboxLayout10.addLayout(self.hboxLayout8)


        self.hLayout_bottom.addWidget(self.gb_console_log)

        self.gb_overrides = QGroupBox(self.page_dashboard)
        self.gb_overrides.setObjectName(u"gb_overrides")
        self.hboxLayout9 = QHBoxLayout(self.gb_overrides)
        self.hboxLayout9.setObjectName(u"hboxLayout9")
        self.lbl_override_laser = QLabel(self.gb_overrides)
        self.lbl_override_laser.setObjectName(u"lbl_override_laser")
        self.lbl_override_laser.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hboxLayout9.addWidget(self.lbl_override_laser)

        self.lbl_override_scan = QLabel(self.gb_overrides)
        self.lbl_override_scan.setObjectName(u"lbl_override_scan")
        self.lbl_override_scan.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hboxLayout9.addWidget(self.lbl_override_scan)

        self.lbl_override_hatch = QLabel(self.gb_overrides)
        self.lbl_override_hatch.setObjectName(u"lbl_override_hatch")
        self.lbl_override_hatch.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hboxLayout9.addWidget(self.lbl_override_hatch)


        self.hLayout_bottom.addWidget(self.gb_overrides)

        self.hLayout_bottom.setStretch(0, 4)
        self.hLayout_bottom.setStretch(1, 1)

        self.vLayout_page_dashboard.addLayout(self.hLayout_bottom)

        self.vLayout_page_dashboard.setStretch(0, 1)
        self.vLayout_page_dashboard.setStretch(1, 5)
        self.vLayout_page_dashboard.setStretch(2, 1)
        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_build_setup = QWidget()
        self.page_build_setup.setObjectName(u"page_build_setup")
        self.gridLayout_page2 = QGridLayout(self.page_build_setup)
        self.gridLayout_page2.setSpacing(4)
        self.gridLayout_page2.setObjectName(u"gridLayout_page2")
        self.vLayout_col1 = QVBoxLayout()
        self.vLayout_col1.setSpacing(4)
        self.vLayout_col1.setObjectName(u"vLayout_col1")
        self.gb_build_files = QGroupBox(self.page_build_setup)
        self.gb_build_files.setObjectName(u"gb_build_files")
        sizePolicy.setHeightForWidth(self.gb_build_files.sizePolicy().hasHeightForWidth())
        self.gb_build_files.setSizePolicy(sizePolicy)
        self.vLayout_build = QVBoxLayout(self.gb_build_files)
        self.vLayout_build.setSpacing(4)
        self.vLayout_build.setObjectName(u"vLayout_build")
        self.hLayout_build_btns = QHBoxLayout()
        self.hLayout_build_btns.setSpacing(4)
        self.hLayout_build_btns.setObjectName(u"hLayout_build_btns")
        self.btn_import_build = QPushButton(self.gb_build_files)
        self.btn_import_build.setObjectName(u"btn_import_build")
        self.btn_import_build.setMinimumSize(QSize(0, 20))

        self.hLayout_build_btns.addWidget(self.btn_import_build)

        self.btn_refresh_build = QPushButton(self.gb_build_files)
        self.btn_refresh_build.setObjectName(u"btn_refresh_build")
        self.btn_refresh_build.setMinimumSize(QSize(0, 20))

        self.hLayout_build_btns.addWidget(self.btn_refresh_build)


        self.vLayout_build.addLayout(self.hLayout_build_btns)

        self.listWidget_builds = QListWidget(self.gb_build_files)
        self.listWidget_builds.setObjectName(u"listWidget_builds")

        self.vLayout_build.addWidget(self.listWidget_builds)


        self.vLayout_col1.addWidget(self.gb_build_files)

        self.gb_machine_profile = QGroupBox(self.page_build_setup)
        self.gb_machine_profile.setObjectName(u"gb_machine_profile")
        sizePolicy.setHeightForWidth(self.gb_machine_profile.sizePolicy().hasHeightForWidth())
        self.gb_machine_profile.setSizePolicy(sizePolicy)
        self.vLayout_machine = QVBoxLayout(self.gb_machine_profile)
        self.vLayout_machine.setSpacing(4)
        self.vLayout_machine.setObjectName(u"vLayout_machine")
        self.comboBox_machine = QComboBox(self.gb_machine_profile)
        self.comboBox_machine.setObjectName(u"comboBox_machine")

        self.vLayout_machine.addWidget(self.comboBox_machine)


        self.vLayout_col1.addWidget(self.gb_machine_profile)

        self.gb_material_profile = QGroupBox(self.page_build_setup)
        self.gb_material_profile.setObjectName(u"gb_material_profile")
        sizePolicy.setHeightForWidth(self.gb_material_profile.sizePolicy().hasHeightForWidth())
        self.gb_material_profile.setSizePolicy(sizePolicy)
        self.vLayout_material = QVBoxLayout(self.gb_material_profile)
        self.vLayout_material.setSpacing(4)
        self.vLayout_material.setObjectName(u"vLayout_material")
        self.comboBox_material = QComboBox(self.gb_material_profile)
        self.comboBox_material.setObjectName(u"comboBox_material")

        self.vLayout_material.addWidget(self.comboBox_material)


        self.vLayout_col1.addWidget(self.gb_material_profile)


        self.gridLayout_page2.addLayout(self.vLayout_col1, 0, 0, 1, 1)

        self.gb_build_preview = QGroupBox(self.page_build_setup)
        self.gb_build_preview.setObjectName(u"gb_build_preview")
        sizePolicy.setHeightForWidth(self.gb_build_preview.sizePolicy().hasHeightForWidth())
        self.gb_build_preview.setSizePolicy(sizePolicy)
        self.vLayout_preview = QVBoxLayout(self.gb_build_preview)
        self.vLayout_preview.setSpacing(4)
        self.vLayout_preview.setObjectName(u"vLayout_preview")
        self.hLayout_preview_toolbar = QHBoxLayout()
        self.hLayout_preview_toolbar.setSpacing(4)
        self.hLayout_preview_toolbar.setObjectName(u"hLayout_preview_toolbar")
        self.btn_view_iso = QPushButton(self.gb_build_preview)
        self.btn_view_iso.setObjectName(u"btn_view_iso")
        self.btn_view_iso.setMinimumSize(QSize(0, 20))

        self.hLayout_preview_toolbar.addWidget(self.btn_view_iso)

        self.btn_view_top = QPushButton(self.gb_build_preview)
        self.btn_view_top.setObjectName(u"btn_view_top")
        self.btn_view_top.setMinimumSize(QSize(0, 20))

        self.hLayout_preview_toolbar.addWidget(self.btn_view_top)

        self.btn_view_front = QPushButton(self.gb_build_preview)
        self.btn_view_front.setObjectName(u"btn_view_front")
        self.btn_view_front.setMinimumSize(QSize(0, 20))

        self.hLayout_preview_toolbar.addWidget(self.btn_view_front)

        self.spacerItem5 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_preview_toolbar.addItem(self.spacerItem5)


        self.vLayout_preview.addLayout(self.hLayout_preview_toolbar)

        self.lbl_3d_preview_placeholder = QLabel(self.gb_build_preview)
        self.lbl_3d_preview_placeholder.setObjectName(u"lbl_3d_preview_placeholder")
        self.lbl_3d_preview_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vLayout_preview.addWidget(self.lbl_3d_preview_placeholder)

        self.hLayout_preview_controls = QHBoxLayout()
        self.hLayout_preview_controls.setSpacing(4)
        self.hLayout_preview_controls.setObjectName(u"hLayout_preview_controls")
        self.btn_rotate = QPushButton(self.gb_build_preview)
        self.btn_rotate.setObjectName(u"btn_rotate")
        self.btn_rotate.setMinimumSize(QSize(0, 20))

        self.hLayout_preview_controls.addWidget(self.btn_rotate)

        self.btn_pan = QPushButton(self.gb_build_preview)
        self.btn_pan.setObjectName(u"btn_pan")
        self.btn_pan.setMinimumSize(QSize(0, 20))

        self.hLayout_preview_controls.addWidget(self.btn_pan)

        self.btn_zoom = QPushButton(self.gb_build_preview)
        self.btn_zoom.setObjectName(u"btn_zoom")
        self.btn_zoom.setMinimumSize(QSize(0, 20))

        self.hLayout_preview_controls.addWidget(self.btn_zoom)

        self.chk_section_view = QCheckBox(self.gb_build_preview)
        self.chk_section_view.setObjectName(u"chk_section_view")

        self.hLayout_preview_controls.addWidget(self.chk_section_view)


        self.vLayout_preview.addLayout(self.hLayout_preview_controls)


        self.gridLayout_page2.addWidget(self.gb_build_preview, 0, 1, 1, 1)

        self.vLayout_col3 = QVBoxLayout()
        self.vLayout_col3.setSpacing(4)
        self.vLayout_col3.setObjectName(u"vLayout_col3")
        self.gb_job_info = QGroupBox(self.page_build_setup)
        self.gb_job_info.setObjectName(u"gb_job_info")
        sizePolicy.setHeightForWidth(self.gb_job_info.sizePolicy().hasHeightForWidth())
        self.gb_job_info.setSizePolicy(sizePolicy)
        self.formLayout_job = QFormLayout(self.gb_job_info)
        self.formLayout_job.setObjectName(u"formLayout_job")
        self.formLayout_job.setHorizontalSpacing(4)
        self.formLayout_job.setVerticalSpacing(4)
        self.lbl_job_name = QLabel(self.gb_job_info)
        self.lbl_job_name.setObjectName(u"lbl_job_name")

        self.formLayout_job.setWidget(0, QFormLayout.LabelRole, self.lbl_job_name)

        self.val_job_name = QLabel(self.gb_job_info)
        self.val_job_name.setObjectName(u"val_job_name")

        self.formLayout_job.setWidget(0, QFormLayout.FieldRole, self.val_job_name)

        self.lbl_job_material = QLabel(self.gb_job_info)
        self.lbl_job_material.setObjectName(u"lbl_job_material")

        self.formLayout_job.setWidget(1, QFormLayout.LabelRole, self.lbl_job_material)

        self.val_job_material = QLabel(self.gb_job_info)
        self.val_job_material.setObjectName(u"val_job_material")

        self.formLayout_job.setWidget(1, QFormLayout.FieldRole, self.val_job_material)

        self.lbl_job_thickness = QLabel(self.gb_job_info)
        self.lbl_job_thickness.setObjectName(u"lbl_job_thickness")

        self.formLayout_job.setWidget(2, QFormLayout.LabelRole, self.lbl_job_thickness)

        self.val_job_thickness = QLabel(self.gb_job_info)
        self.val_job_thickness.setObjectName(u"val_job_thickness")

        self.formLayout_job.setWidget(2, QFormLayout.FieldRole, self.val_job_thickness)

        self.lbl_job_layers = QLabel(self.gb_job_info)
        self.lbl_job_layers.setObjectName(u"lbl_job_layers")

        self.formLayout_job.setWidget(3, QFormLayout.LabelRole, self.lbl_job_layers)

        self.val_job_layers = QLabel(self.gb_job_info)
        self.val_job_layers.setObjectName(u"val_job_layers")

        self.formLayout_job.setWidget(3, QFormLayout.FieldRole, self.val_job_layers)

        self.lbl_job_btime = QLabel(self.gb_job_info)
        self.lbl_job_btime.setObjectName(u"lbl_job_btime")

        self.formLayout_job.setWidget(4, QFormLayout.LabelRole, self.lbl_job_btime)

        self.val_job_btime = QLabel(self.gb_job_info)
        self.val_job_btime.setObjectName(u"val_job_btime")

        self.formLayout_job.setWidget(4, QFormLayout.FieldRole, self.val_job_btime)

        self.lbl_job_powder = QLabel(self.gb_job_info)
        self.lbl_job_powder.setObjectName(u"lbl_job_powder")

        self.formLayout_job.setWidget(5, QFormLayout.LabelRole, self.lbl_job_powder)

        self.val_job_powder = QLabel(self.gb_job_info)
        self.val_job_powder.setObjectName(u"val_job_powder")

        self.formLayout_job.setWidget(5, QFormLayout.FieldRole, self.val_job_powder)

        self.lbl_job_parts = QLabel(self.gb_job_info)
        self.lbl_job_parts.setObjectName(u"lbl_job_parts")

        self.formLayout_job.setWidget(6, QFormLayout.LabelRole, self.lbl_job_parts)

        self.val_job_parts = QLabel(self.gb_job_info)
        self.val_job_parts.setObjectName(u"val_job_parts")

        self.formLayout_job.setWidget(6, QFormLayout.FieldRole, self.val_job_parts)


        self.vLayout_col3.addWidget(self.gb_job_info)

        self.gb_validation = QGroupBox(self.page_build_setup)
        self.gb_validation.setObjectName(u"gb_validation")
        sizePolicy.setHeightForWidth(self.gb_validation.sizePolicy().hasHeightForWidth())
        self.gb_validation.setSizePolicy(sizePolicy)
        self.formLayout_val = QFormLayout(self.gb_validation)
        self.formLayout_val.setObjectName(u"formLayout_val")
        self.formLayout_val.setHorizontalSpacing(4)
        self.formLayout_val.setVerticalSpacing(4)
        self.lbl_val_vol = QLabel(self.gb_validation)
        self.lbl_val_vol.setObjectName(u"lbl_val_vol")

        self.formLayout_val.setWidget(0, QFormLayout.LabelRole, self.lbl_val_vol)

        self.val_val_vol = QLabel(self.gb_validation)
        self.val_val_vol.setObjectName(u"val_val_vol")

        self.formLayout_val.setWidget(0, QFormLayout.FieldRole, self.val_val_vol)

        self.lbl_val_mat = QLabel(self.gb_validation)
        self.lbl_val_mat.setObjectName(u"lbl_val_mat")

        self.formLayout_val.setWidget(1, QFormLayout.LabelRole, self.lbl_val_mat)

        self.val_val_mat = QLabel(self.gb_validation)
        self.val_val_mat.setObjectName(u"val_val_mat")

        self.formLayout_val.setWidget(1, QFormLayout.FieldRole, self.val_val_mat)

        self.lbl_val_geo = QLabel(self.gb_validation)
        self.lbl_val_geo.setObjectName(u"lbl_val_geo")

        self.formLayout_val.setWidget(2, QFormLayout.LabelRole, self.lbl_val_geo)

        self.val_val_geo = QLabel(self.gb_validation)
        self.val_val_geo.setObjectName(u"val_val_geo")

        self.formLayout_val.setWidget(2, QFormLayout.FieldRole, self.val_val_geo)

        self.lbl_val_comp = QLabel(self.gb_validation)
        self.lbl_val_comp.setObjectName(u"lbl_val_comp")

        self.formLayout_val.setWidget(3, QFormLayout.LabelRole, self.lbl_val_comp)

        self.val_val_comp = QLabel(self.gb_validation)
        self.val_val_comp.setObjectName(u"val_val_comp")

        self.formLayout_val.setWidget(3, QFormLayout.FieldRole, self.val_val_comp)


        self.vLayout_col3.addWidget(self.gb_validation)

        self.spacerItem6 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vLayout_col3.addItem(self.spacerItem6)


        self.gridLayout_page2.addLayout(self.vLayout_col3, 0, 2, 1, 1)

        self.vLayout_col4 = QVBoxLayout()
        self.vLayout_col4.setSpacing(4)
        self.vLayout_col4.setObjectName(u"vLayout_col4")
        self.gb_est_stats = QGroupBox(self.page_build_setup)
        self.gb_est_stats.setObjectName(u"gb_est_stats")
        sizePolicy.setHeightForWidth(self.gb_est_stats.sizePolicy().hasHeightForWidth())
        self.gb_est_stats.setSizePolicy(sizePolicy)
        self.formLayout_stats = QFormLayout(self.gb_est_stats)
        self.formLayout_stats.setObjectName(u"formLayout_stats")
        self.formLayout_stats.setHorizontalSpacing(4)
        self.formLayout_stats.setVerticalSpacing(4)
        self.lbl_stat_time = QLabel(self.gb_est_stats)
        self.lbl_stat_time.setObjectName(u"lbl_stat_time")

        self.formLayout_stats.setWidget(0, QFormLayout.LabelRole, self.lbl_stat_time)

        self.val_stat_time = QLabel(self.gb_est_stats)
        self.val_stat_time.setObjectName(u"val_stat_time")

        self.formLayout_stats.setWidget(0, QFormLayout.FieldRole, self.val_stat_time)

        self.lbl_stat_scan = QLabel(self.gb_est_stats)
        self.lbl_stat_scan.setObjectName(u"lbl_stat_scan")

        self.formLayout_stats.setWidget(1, QFormLayout.LabelRole, self.lbl_stat_scan)

        self.val_stat_scan = QLabel(self.gb_est_stats)
        self.val_stat_scan.setObjectName(u"val_stat_scan")

        self.formLayout_stats.setWidget(1, QFormLayout.FieldRole, self.val_stat_scan)

        self.lbl_stat_jump = QLabel(self.gb_est_stats)
        self.lbl_stat_jump.setObjectName(u"lbl_stat_jump")

        self.formLayout_stats.setWidget(2, QFormLayout.LabelRole, self.lbl_stat_jump)

        self.val_stat_jump = QLabel(self.gb_est_stats)
        self.val_stat_jump.setObjectName(u"val_stat_jump")

        self.formLayout_stats.setWidget(2, QFormLayout.FieldRole, self.val_stat_jump)

        self.lbl_stat_layers = QLabel(self.gb_est_stats)
        self.lbl_stat_layers.setObjectName(u"lbl_stat_layers")

        self.formLayout_stats.setWidget(3, QFormLayout.LabelRole, self.lbl_stat_layers)

        self.val_stat_layers = QLabel(self.gb_est_stats)
        self.val_stat_layers.setObjectName(u"val_stat_layers")

        self.formLayout_stats.setWidget(3, QFormLayout.FieldRole, self.val_stat_layers)

        self.lbl_stat_scan_len = QLabel(self.gb_est_stats)
        self.lbl_stat_scan_len.setObjectName(u"lbl_stat_scan_len")

        self.formLayout_stats.setWidget(4, QFormLayout.LabelRole, self.lbl_stat_scan_len)

        self.val_stat_scan_len = QLabel(self.gb_est_stats)
        self.val_stat_scan_len.setObjectName(u"val_stat_scan_len")

        self.formLayout_stats.setWidget(4, QFormLayout.FieldRole, self.val_stat_scan_len)

        self.lbl_stat_jump_len = QLabel(self.gb_est_stats)
        self.lbl_stat_jump_len.setObjectName(u"lbl_stat_jump_len")

        self.formLayout_stats.setWidget(5, QFormLayout.LabelRole, self.lbl_stat_jump_len)

        self.val_stat_jump_len = QLabel(self.gb_est_stats)
        self.val_stat_jump_len.setObjectName(u"val_stat_jump_len")

        self.formLayout_stats.setWidget(5, QFormLayout.FieldRole, self.val_stat_jump_len)

        self.lbl_stat_powder = QLabel(self.gb_est_stats)
        self.lbl_stat_powder.setObjectName(u"lbl_stat_powder")

        self.formLayout_stats.setWidget(6, QFormLayout.LabelRole, self.lbl_stat_powder)

        self.val_stat_powder = QLabel(self.gb_est_stats)
        self.val_stat_powder.setObjectName(u"val_stat_powder")

        self.formLayout_stats.setWidget(6, QFormLayout.FieldRole, self.val_stat_powder)

        self.lbl_stat_power = QLabel(self.gb_est_stats)
        self.lbl_stat_power.setObjectName(u"lbl_stat_power")

        self.formLayout_stats.setWidget(7, QFormLayout.LabelRole, self.lbl_stat_power)

        self.val_stat_power = QLabel(self.gb_est_stats)
        self.val_stat_power.setObjectName(u"val_stat_power")

        self.formLayout_stats.setWidget(7, QFormLayout.FieldRole, self.val_stat_power)

        self.lbl_stat_energy = QLabel(self.gb_est_stats)
        self.lbl_stat_energy.setObjectName(u"lbl_stat_energy")

        self.formLayout_stats.setWidget(8, QFormLayout.LabelRole, self.lbl_stat_energy)

        self.val_stat_energy = QLabel(self.gb_est_stats)
        self.val_stat_energy.setObjectName(u"val_stat_energy")

        self.formLayout_stats.setWidget(8, QFormLayout.FieldRole, self.val_stat_energy)


        self.vLayout_col4.addWidget(self.gb_est_stats)

        self.gb_actions = QGroupBox(self.page_build_setup)
        self.gb_actions.setObjectName(u"gb_actions")
        sizePolicy.setHeightForWidth(self.gb_actions.sizePolicy().hasHeightForWidth())
        self.gb_actions.setSizePolicy(sizePolicy)
        self.vLayout_actions = QVBoxLayout(self.gb_actions)
        self.vLayout_actions.setSpacing(4)
        self.vLayout_actions.setObjectName(u"vLayout_actions")
        self.btn_verify_build = QPushButton(self.gb_actions)
        self.btn_verify_build.setObjectName(u"btn_verify_build")
        self.btn_verify_build.setMinimumSize(QSize(0, 20))

        self.vLayout_actions.addWidget(self.btn_verify_build)

        self.btn_send_queue = QPushButton(self.gb_actions)
        self.btn_send_queue.setObjectName(u"btn_send_queue")
        self.btn_send_queue.setMinimumSize(QSize(0, 20))

        self.vLayout_actions.addWidget(self.btn_send_queue)

        self.btn_prepare_machine = QPushButton(self.gb_actions)
        self.btn_prepare_machine.setObjectName(u"btn_prepare_machine")
        self.btn_prepare_machine.setMinimumSize(QSize(0, 20))

        self.vLayout_actions.addWidget(self.btn_prepare_machine)


        self.vLayout_col4.addWidget(self.gb_actions)

        self.spacerItem7 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vLayout_col4.addItem(self.spacerItem7)


        self.gridLayout_page2.addLayout(self.vLayout_col4, 0, 3, 1, 1)

        self.gb_build_queue = QGroupBox(self.page_build_setup)
        self.gb_build_queue.setObjectName(u"gb_build_queue")
        sizePolicy.setHeightForWidth(self.gb_build_queue.sizePolicy().hasHeightForWidth())
        self.gb_build_queue.setSizePolicy(sizePolicy)
        self.vLayout_queue = QVBoxLayout(self.gb_build_queue)
        self.vLayout_queue.setSpacing(4)
        self.vLayout_queue.setObjectName(u"vLayout_queue")
        self.tableWidget_queue = QTableWidget(self.gb_build_queue)
        if (self.tableWidget_queue.columnCount() < 6):
            self.tableWidget_queue.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_queue.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_queue.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_queue.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_queue.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_queue.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_queue.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_queue.setObjectName(u"tableWidget_queue")
        sizePolicy.setHeightForWidth(self.tableWidget_queue.sizePolicy().hasHeightForWidth())
        self.tableWidget_queue.setSizePolicy(sizePolicy)
        self.tableWidget_queue.setColumnCount(6)

        self.vLayout_queue.addWidget(self.tableWidget_queue)


        self.gridLayout_page2.addWidget(self.gb_build_queue, 1, 0, 1, 3)

        self.gb_build_notes = QGroupBox(self.page_build_setup)
        self.gb_build_notes.setObjectName(u"gb_build_notes")
        sizePolicy.setHeightForWidth(self.gb_build_notes.sizePolicy().hasHeightForWidth())
        self.gb_build_notes.setSizePolicy(sizePolicy)
        self.vLayout_notes = QVBoxLayout(self.gb_build_notes)
        self.vLayout_notes.setSpacing(4)
        self.vLayout_notes.setObjectName(u"vLayout_notes")
        self.txt_build_notes = QTextEdit(self.gb_build_notes)
        self.txt_build_notes.setObjectName(u"txt_build_notes")
        sizePolicy.setHeightForWidth(self.txt_build_notes.sizePolicy().hasHeightForWidth())
        self.txt_build_notes.setSizePolicy(sizePolicy)

        self.vLayout_notes.addWidget(self.txt_build_notes)

        self.btn_save_notes = QPushButton(self.gb_build_notes)
        self.btn_save_notes.setObjectName(u"btn_save_notes")
        self.btn_save_notes.setMinimumSize(QSize(0, 20))

        self.vLayout_notes.addWidget(self.btn_save_notes)


        self.gridLayout_page2.addWidget(self.gb_build_notes, 1, 3, 1, 1)

        self.gridLayout_page2.setRowStretch(0, 6)
        self.gridLayout_page2.setRowStretch(1, 3)
        self.gridLayout_page2.setColumnStretch(0, 3)
        self.gridLayout_page2.setColumnStretch(1, 6)
        self.gridLayout_page2.setColumnStretch(2, 2)
        self.gridLayout_page2.setColumnStretch(3, 2)
        self.stackedWidget.addWidget(self.page_build_setup)
        self.page_gcode = QWidget()
        self.page_gcode.setObjectName(u"page_gcode")
        self.gridLayout_page3 = QGridLayout(self.page_gcode)
        self.gridLayout_page3.setSpacing(4)
        self.gridLayout_page3.setObjectName(u"gridLayout_page3")
        self.vLayout_c1_p3 = QVBoxLayout()
        self.vLayout_c1_p3.setSpacing(4)
        self.vLayout_c1_p3.setObjectName(u"vLayout_c1_p3")
        self.gb_layer_controls = QGroupBox(self.page_gcode)
        self.gb_layer_controls.setObjectName(u"gb_layer_controls")
        sizePolicy.setHeightForWidth(self.gb_layer_controls.sizePolicy().hasHeightForWidth())
        self.gb_layer_controls.setSizePolicy(sizePolicy)
        self.vLayout_layer_controls = QVBoxLayout(self.gb_layer_controls)
        self.vLayout_layer_controls.setSpacing(4)
        self.vLayout_layer_controls.setObjectName(u"vLayout_layer_controls")
        self.hLayout_layer_status = QHBoxLayout()
        self.hLayout_layer_status.setSpacing(4)
        self.hLayout_layer_status.setObjectName(u"hLayout_layer_status")
        self.lbl_layer_text = QLabel(self.gb_layer_controls)
        self.lbl_layer_text.setObjectName(u"lbl_layer_text")

        self.hLayout_layer_status.addWidget(self.lbl_layer_text)

        self.lbl_layer_val = QLabel(self.gb_layer_controls)
        self.lbl_layer_val.setObjectName(u"lbl_layer_val")
        self.lbl_layer_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.hLayout_layer_status.addWidget(self.lbl_layer_val)


        self.vLayout_layer_controls.addLayout(self.hLayout_layer_status)

        self.slider_layer = QSlider(self.gb_layer_controls)
        self.slider_layer.setObjectName(u"slider_layer")
        self.slider_layer.setOrientation(Qt.Orientation.Horizontal)

        self.vLayout_layer_controls.addWidget(self.slider_layer)

        self.hLayout_layer_btns = QHBoxLayout()
        self.hLayout_layer_btns.setSpacing(4)
        self.hLayout_layer_btns.setObjectName(u"hLayout_layer_btns")
        self.btn_layer_first = QPushButton(self.gb_layer_controls)
        self.btn_layer_first.setObjectName(u"btn_layer_first")
        self.btn_layer_first.setMinimumSize(QSize(0, 20))

        self.hLayout_layer_btns.addWidget(self.btn_layer_first)

        self.btn_layer_prev = QPushButton(self.gb_layer_controls)
        self.btn_layer_prev.setObjectName(u"btn_layer_prev")
        self.btn_layer_prev.setMinimumSize(QSize(0, 20))

        self.hLayout_layer_btns.addWidget(self.btn_layer_prev)

        self.btn_layer_next = QPushButton(self.gb_layer_controls)
        self.btn_layer_next.setObjectName(u"btn_layer_next")
        self.btn_layer_next.setMinimumSize(QSize(0, 20))

        self.hLayout_layer_btns.addWidget(self.btn_layer_next)

        self.btn_layer_last = QPushButton(self.gb_layer_controls)
        self.btn_layer_last.setObjectName(u"btn_layer_last")
        self.btn_layer_last.setMinimumSize(QSize(0, 20))

        self.hLayout_layer_btns.addWidget(self.btn_layer_last)


        self.vLayout_layer_controls.addLayout(self.hLayout_layer_btns)

        self.btn_jump_layer = QPushButton(self.gb_layer_controls)
        self.btn_jump_layer.setObjectName(u"btn_jump_layer")
        self.btn_jump_layer.setMinimumSize(QSize(0, 20))

        self.vLayout_layer_controls.addWidget(self.btn_jump_layer)

        self.hLayout_range_status = QHBoxLayout()
        self.hLayout_range_status.setSpacing(4)
        self.hLayout_range_status.setObjectName(u"hLayout_range_status")
        self.lbl_range_text = QLabel(self.gb_layer_controls)
        self.lbl_range_text.setObjectName(u"lbl_range_text")

        self.hLayout_range_status.addWidget(self.lbl_range_text)

        self.lbl_range_val = QLabel(self.gb_layer_controls)
        self.lbl_range_val.setObjectName(u"lbl_range_val")
        self.lbl_range_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.hLayout_range_status.addWidget(self.lbl_range_val)


        self.vLayout_layer_controls.addLayout(self.hLayout_range_status)

        self.slider_layer_range = QSlider(self.gb_layer_controls)
        self.slider_layer_range.setObjectName(u"slider_layer_range")
        self.slider_layer_range.setOrientation(Qt.Orientation.Horizontal)

        self.vLayout_layer_controls.addWidget(self.slider_layer_range)


        self.vLayout_c1_p3.addWidget(self.gb_layer_controls)

        self.gb_display_options = QGroupBox(self.page_gcode)
        self.gb_display_options.setObjectName(u"gb_display_options")
        sizePolicy.setHeightForWidth(self.gb_display_options.sizePolicy().hasHeightForWidth())
        self.gb_display_options.setSizePolicy(sizePolicy)
        self.vLayout_display_options = QVBoxLayout(self.gb_display_options)
        self.vLayout_display_options.setSpacing(4)
        self.vLayout_display_options.setObjectName(u"vLayout_display_options")
        self.chk_show_contours = QCheckBox(self.gb_display_options)
        self.chk_show_contours.setObjectName(u"chk_show_contours")
        self.chk_show_contours.setChecked(True)

        self.vLayout_display_options.addWidget(self.chk_show_contours)

        self.chk_show_hatch = QCheckBox(self.gb_display_options)
        self.chk_show_hatch.setObjectName(u"chk_show_hatch")
        self.chk_show_hatch.setChecked(True)

        self.vLayout_display_options.addWidget(self.chk_show_hatch)

        self.chk_show_supports = QCheckBox(self.gb_display_options)
        self.chk_show_supports.setObjectName(u"chk_show_supports")
        self.chk_show_supports.setChecked(True)

        self.vLayout_display_options.addWidget(self.chk_show_supports)

        self.chk_show_jump = QCheckBox(self.gb_display_options)
        self.chk_show_jump.setObjectName(u"chk_show_jump")
        self.chk_show_jump.setChecked(True)

        self.vLayout_display_options.addWidget(self.chk_show_jump)

        self.chk_show_scan_dir = QCheckBox(self.gb_display_options)
        self.chk_show_scan_dir.setObjectName(u"chk_show_scan_dir")
        self.chk_show_scan_dir.setChecked(True)

        self.vLayout_display_options.addWidget(self.chk_show_scan_dir)

        self.chk_only_current = QCheckBox(self.gb_display_options)
        self.chk_only_current.setObjectName(u"chk_only_current")

        self.vLayout_display_options.addWidget(self.chk_only_current)


        self.vLayout_c1_p3.addWidget(self.gb_display_options)

        self.gb_view_mode = QGroupBox(self.page_gcode)
        self.gb_view_mode.setObjectName(u"gb_view_mode")
        sizePolicy.setHeightForWidth(self.gb_view_mode.sizePolicy().hasHeightForWidth())
        self.gb_view_mode.setSizePolicy(sizePolicy)
        self.hLayout_view_mode = QHBoxLayout(self.gb_view_mode)
        self.hLayout_view_mode.setSpacing(4)
        self.hLayout_view_mode.setObjectName(u"hLayout_view_mode")
        self.btn_view_2d = QPushButton(self.gb_view_mode)
        self.btn_view_2d.setObjectName(u"btn_view_2d")
        self.btn_view_2d.setMinimumSize(QSize(0, 20))

        self.hLayout_view_mode.addWidget(self.btn_view_2d)

        self.btn_view_3d = QPushButton(self.gb_view_mode)
        self.btn_view_3d.setObjectName(u"btn_view_3d")
        self.btn_view_3d.setMinimumSize(QSize(0, 20))

        self.hLayout_view_mode.addWidget(self.btn_view_3d)

        self.btn_view_25d = QPushButton(self.gb_view_mode)
        self.btn_view_25d.setObjectName(u"btn_view_25d")
        self.btn_view_25d.setMinimumSize(QSize(0, 20))

        self.hLayout_view_mode.addWidget(self.btn_view_25d)


        self.vLayout_c1_p3.addWidget(self.gb_view_mode)

        self.gb_layer_info = QGroupBox(self.page_gcode)
        self.gb_layer_info.setObjectName(u"gb_layer_info")
        sizePolicy.setHeightForWidth(self.gb_layer_info.sizePolicy().hasHeightForWidth())
        self.gb_layer_info.setSizePolicy(sizePolicy)
        self.formLayout_layer_info = QFormLayout(self.gb_layer_info)
        self.formLayout_layer_info.setObjectName(u"formLayout_layer_info")
        self.formLayout_layer_info.setHorizontalSpacing(4)
        self.formLayout_layer_info.setVerticalSpacing(4)
        self.lbl_linfo_thick = QLabel(self.gb_layer_info)
        self.lbl_linfo_thick.setObjectName(u"lbl_linfo_thick")

        self.formLayout_layer_info.setWidget(0, QFormLayout.LabelRole, self.lbl_linfo_thick)

        self.val_linfo_thick = QLabel(self.gb_layer_info)
        self.val_linfo_thick.setObjectName(u"val_linfo_thick")

        self.formLayout_layer_info.setWidget(0, QFormLayout.FieldRole, self.val_linfo_thick)

        self.lbl_linfo_ltime = QLabel(self.gb_layer_info)
        self.lbl_linfo_ltime.setObjectName(u"lbl_linfo_ltime")

        self.formLayout_layer_info.setWidget(1, QFormLayout.LabelRole, self.lbl_linfo_ltime)

        self.val_linfo_ltime = QLabel(self.gb_layer_info)
        self.val_linfo_ltime.setObjectName(u"val_linfo_ltime")

        self.formLayout_layer_info.setWidget(1, QFormLayout.FieldRole, self.val_linfo_ltime)

        self.lbl_linfo_stime = QLabel(self.gb_layer_info)
        self.lbl_linfo_stime.setObjectName(u"lbl_linfo_stime")

        self.formLayout_layer_info.setWidget(2, QFormLayout.LabelRole, self.lbl_linfo_stime)

        self.val_linfo_stime = QLabel(self.gb_layer_info)
        self.val_linfo_stime.setObjectName(u"val_linfo_stime")

        self.formLayout_layer_info.setWidget(2, QFormLayout.FieldRole, self.val_linfo_stime)

        self.lbl_linfo_jtime = QLabel(self.gb_layer_info)
        self.lbl_linfo_jtime.setObjectName(u"lbl_linfo_jtime")

        self.formLayout_layer_info.setWidget(3, QFormLayout.LabelRole, self.lbl_linfo_jtime)

        self.val_linfo_jtime = QLabel(self.gb_layer_info)
        self.val_linfo_jtime.setObjectName(u"val_linfo_jtime")

        self.formLayout_layer_info.setWidget(3, QFormLayout.FieldRole, self.val_linfo_jtime)

        self.lbl_linfo_hlen = QLabel(self.gb_layer_info)
        self.lbl_linfo_hlen.setObjectName(u"lbl_linfo_hlen")

        self.formLayout_layer_info.setWidget(4, QFormLayout.LabelRole, self.lbl_linfo_hlen)

        self.val_linfo_hlen = QLabel(self.gb_layer_info)
        self.val_linfo_hlen.setObjectName(u"val_linfo_hlen")

        self.formLayout_layer_info.setWidget(4, QFormLayout.FieldRole, self.val_linfo_hlen)

        self.lbl_linfo_jlen = QLabel(self.gb_layer_info)
        self.lbl_linfo_jlen.setObjectName(u"lbl_linfo_jlen")

        self.formLayout_layer_info.setWidget(5, QFormLayout.LabelRole, self.lbl_linfo_jlen)

        self.val_linfo_jlen = QLabel(self.gb_layer_info)
        self.val_linfo_jlen.setObjectName(u"val_linfo_jlen")

        self.formLayout_layer_info.setWidget(5, QFormLayout.FieldRole, self.val_linfo_jlen)

        self.lbl_linfo_energy = QLabel(self.gb_layer_info)
        self.lbl_linfo_energy.setObjectName(u"lbl_linfo_energy")

        self.formLayout_layer_info.setWidget(6, QFormLayout.LabelRole, self.lbl_linfo_energy)

        self.val_linfo_energy = QLabel(self.gb_layer_info)
        self.val_linfo_energy.setObjectName(u"val_linfo_energy")

        self.formLayout_layer_info.setWidget(6, QFormLayout.FieldRole, self.val_linfo_energy)


        self.vLayout_c1_p3.addWidget(self.gb_layer_info)

        self.spacerItem8 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vLayout_c1_p3.addItem(self.spacerItem8)


        self.gridLayout_page3.addLayout(self.vLayout_c1_p3, 0, 0, 1, 1)

        self.vLayout_c2_p3 = QVBoxLayout()
        self.vLayout_c2_p3.setSpacing(4)
        self.vLayout_c2_p3.setObjectName(u"vLayout_c2_p3")
        self.graphicsView_layer = QGraphicsView(self.page_gcode)
        self.graphicsView_layer.setObjectName(u"graphicsView_layer")
        sizePolicy.setHeightForWidth(self.graphicsView_layer.sizePolicy().hasHeightForWidth())
        self.graphicsView_layer.setSizePolicy(sizePolicy)

        self.vLayout_c2_p3.addWidget(self.graphicsView_layer)

        self.hLayout_coords = QHBoxLayout()
        self.hLayout_coords.setSpacing(4)
        self.hLayout_coords.setObjectName(u"hLayout_coords")
        self.lbl_coord_x = QLabel(self.page_gcode)
        self.lbl_coord_x.setObjectName(u"lbl_coord_x")

        self.hLayout_coords.addWidget(self.lbl_coord_x)

        self.lbl_coord_y = QLabel(self.page_gcode)
        self.lbl_coord_y.setObjectName(u"lbl_coord_y")

        self.hLayout_coords.addWidget(self.lbl_coord_y)

        self.lbl_coord_z = QLabel(self.page_gcode)
        self.lbl_coord_z.setObjectName(u"lbl_coord_z")

        self.hLayout_coords.addWidget(self.lbl_coord_z)

        self.lbl_coord_zoom = QLabel(self.page_gcode)
        self.lbl_coord_zoom.setObjectName(u"lbl_coord_zoom")

        self.hLayout_coords.addWidget(self.lbl_coord_zoom)


        self.vLayout_c2_p3.addLayout(self.hLayout_coords)


        self.gridLayout_page3.addLayout(self.vLayout_c2_p3, 0, 1, 1, 1)

        self.vLayout_c3_p3 = QVBoxLayout()
        self.vLayout_c3_p3.setSpacing(4)
        self.vLayout_c3_p3.setObjectName(u"vLayout_c3_p3")
        self.gb_layer_thumbnails = QGroupBox(self.page_gcode)
        self.gb_layer_thumbnails.setObjectName(u"gb_layer_thumbnails")
        sizePolicy.setHeightForWidth(self.gb_layer_thumbnails.sizePolicy().hasHeightForWidth())
        self.gb_layer_thumbnails.setSizePolicy(sizePolicy)
        self.hLayout_thumbnails = QHBoxLayout(self.gb_layer_thumbnails)
        self.hLayout_thumbnails.setSpacing(4)
        self.hLayout_thumbnails.setObjectName(u"hLayout_thumbnails")
        self.btn_thumb_prev = QPushButton(self.gb_layer_thumbnails)
        self.btn_thumb_prev.setObjectName(u"btn_thumb_prev")
        self.btn_thumb_prev.setMinimumSize(QSize(0, 20))

        self.hLayout_thumbnails.addWidget(self.btn_thumb_prev)

        self.lbl_thumb_1 = QLabel(self.gb_layer_thumbnails)
        self.lbl_thumb_1.setObjectName(u"lbl_thumb_1")
        self.lbl_thumb_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hLayout_thumbnails.addWidget(self.lbl_thumb_1)

        self.lbl_thumb_2 = QLabel(self.gb_layer_thumbnails)
        self.lbl_thumb_2.setObjectName(u"lbl_thumb_2")
        self.lbl_thumb_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hLayout_thumbnails.addWidget(self.lbl_thumb_2)

        self.lbl_thumb_3 = QLabel(self.gb_layer_thumbnails)
        self.lbl_thumb_3.setObjectName(u"lbl_thumb_3")
        self.lbl_thumb_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hLayout_thumbnails.addWidget(self.lbl_thumb_3)

        self.lbl_thumb_4 = QLabel(self.gb_layer_thumbnails)
        self.lbl_thumb_4.setObjectName(u"lbl_thumb_4")
        self.lbl_thumb_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hLayout_thumbnails.addWidget(self.lbl_thumb_4)

        self.lbl_thumb_5 = QLabel(self.gb_layer_thumbnails)
        self.lbl_thumb_5.setObjectName(u"lbl_thumb_5")
        self.lbl_thumb_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hLayout_thumbnails.addWidget(self.lbl_thumb_5)

        self.btn_thumb_next = QPushButton(self.gb_layer_thumbnails)
        self.btn_thumb_next.setObjectName(u"btn_thumb_next")
        self.btn_thumb_next.setMinimumSize(QSize(0, 20))

        self.hLayout_thumbnails.addWidget(self.btn_thumb_next)


        self.vLayout_c3_p3.addWidget(self.gb_layer_thumbnails)

        self.gb_scan_strategy = QGroupBox(self.page_gcode)
        self.gb_scan_strategy.setObjectName(u"gb_scan_strategy")
        sizePolicy.setHeightForWidth(self.gb_scan_strategy.sizePolicy().hasHeightForWidth())
        self.gb_scan_strategy.setSizePolicy(sizePolicy)
        self.hLayout_scan_strategy = QHBoxLayout(self.gb_scan_strategy)
        self.hLayout_scan_strategy.setSpacing(4)
        self.hLayout_scan_strategy.setObjectName(u"hLayout_scan_strategy")
        self.formLayout_scan_strategy = QFormLayout()
        self.formLayout_scan_strategy.setObjectName(u"formLayout_scan_strategy")
        self.formLayout_scan_strategy.setHorizontalSpacing(4)
        self.formLayout_scan_strategy.setVerticalSpacing(4)
        self.lbl_strat_type = QLabel(self.gb_scan_strategy)
        self.lbl_strat_type.setObjectName(u"lbl_strat_type")

        self.formLayout_scan_strategy.setWidget(0, QFormLayout.LabelRole, self.lbl_strat_type)

        self.val_strat_type = QLabel(self.gb_scan_strategy)
        self.val_strat_type.setObjectName(u"val_strat_type")

        self.formLayout_scan_strategy.setWidget(0, QFormLayout.FieldRole, self.val_strat_type)

        self.lbl_strat_rot = QLabel(self.gb_scan_strategy)
        self.lbl_strat_rot.setObjectName(u"lbl_strat_rot")

        self.formLayout_scan_strategy.setWidget(1, QFormLayout.LabelRole, self.lbl_strat_rot)

        self.val_strat_rot = QLabel(self.gb_scan_strategy)
        self.val_strat_rot.setObjectName(u"val_strat_rot")

        self.formLayout_scan_strategy.setWidget(1, QFormLayout.FieldRole, self.val_strat_rot)

        self.lbl_strat_hatch = QLabel(self.gb_scan_strategy)
        self.lbl_strat_hatch.setObjectName(u"lbl_strat_hatch")

        self.formLayout_scan_strategy.setWidget(2, QFormLayout.LabelRole, self.lbl_strat_hatch)

        self.val_strat_hatch = QLabel(self.gb_scan_strategy)
        self.val_strat_hatch.setObjectName(u"val_strat_hatch")

        self.formLayout_scan_strategy.setWidget(2, QFormLayout.FieldRole, self.val_strat_hatch)

        self.lbl_strat_hatch_angle = QLabel(self.gb_scan_strategy)
        self.lbl_strat_hatch_angle.setObjectName(u"lbl_strat_hatch_angle")

        self.formLayout_scan_strategy.setWidget(3, QFormLayout.LabelRole, self.lbl_strat_hatch_angle)

        self.val_strat_hatch_angle = QLabel(self.gb_scan_strategy)
        self.val_strat_hatch_angle.setObjectName(u"val_strat_hatch_angle")

        self.formLayout_scan_strategy.setWidget(3, QFormLayout.FieldRole, self.val_strat_hatch_angle)

        self.lbl_strat_island = QLabel(self.gb_scan_strategy)
        self.lbl_strat_island.setObjectName(u"lbl_strat_island")

        self.formLayout_scan_strategy.setWidget(4, QFormLayout.LabelRole, self.lbl_strat_island)

        self.val_strat_island = QLabel(self.gb_scan_strategy)
        self.val_strat_island.setObjectName(u"val_strat_island")

        self.formLayout_scan_strategy.setWidget(4, QFormLayout.FieldRole, self.val_strat_island)

        self.lbl_strat_border = QLabel(self.gb_scan_strategy)
        self.lbl_strat_border.setObjectName(u"lbl_strat_border")

        self.formLayout_scan_strategy.setWidget(5, QFormLayout.LabelRole, self.lbl_strat_border)

        self.val_strat_border = QLabel(self.gb_scan_strategy)
        self.val_strat_border.setObjectName(u"val_strat_border")

        self.formLayout_scan_strategy.setWidget(5, QFormLayout.FieldRole, self.val_strat_border)

        self.lbl_strat_contour = QLabel(self.gb_scan_strategy)
        self.lbl_strat_contour.setObjectName(u"lbl_strat_contour")

        self.formLayout_scan_strategy.setWidget(6, QFormLayout.LabelRole, self.lbl_strat_contour)

        self.val_strat_contour = QLabel(self.gb_scan_strategy)
        self.val_strat_contour.setObjectName(u"val_strat_contour")

        self.formLayout_scan_strategy.setWidget(6, QFormLayout.FieldRole, self.val_strat_contour)


        self.hLayout_scan_strategy.addLayout(self.formLayout_scan_strategy)

        self.lbl_strat_img_placeholder = QLabel(self.gb_scan_strategy)
        self.lbl_strat_img_placeholder.setObjectName(u"lbl_strat_img_placeholder")
        self.lbl_strat_img_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hLayout_scan_strategy.addWidget(self.lbl_strat_img_placeholder)


        self.vLayout_c3_p3.addWidget(self.gb_scan_strategy)

        self.gb_layer_statistics = QGroupBox(self.page_gcode)
        self.gb_layer_statistics.setObjectName(u"gb_layer_statistics")
        sizePolicy.setHeightForWidth(self.gb_layer_statistics.sizePolicy().hasHeightForWidth())
        self.gb_layer_statistics.setSizePolicy(sizePolicy)
        self.hLayout_layer_stats = QHBoxLayout(self.gb_layer_statistics)
        self.hLayout_layer_stats.setSpacing(4)
        self.hLayout_layer_stats.setObjectName(u"hLayout_layer_stats")
        self.lbl_stats_pie_placeholder = QLabel(self.gb_layer_statistics)
        self.lbl_stats_pie_placeholder.setObjectName(u"lbl_stats_pie_placeholder")
        self.lbl_stats_pie_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hLayout_layer_stats.addWidget(self.lbl_stats_pie_placeholder)

        self.formLayout_layer_stats = QFormLayout()
        self.formLayout_layer_stats.setObjectName(u"formLayout_layer_stats")
        self.formLayout_layer_stats.setHorizontalSpacing(4)
        self.formLayout_layer_stats.setVerticalSpacing(4)
        self.lbl_stat_contour = QLabel(self.gb_layer_statistics)
        self.lbl_stat_contour.setObjectName(u"lbl_stat_contour")

        self.formLayout_layer_stats.setWidget(0, QFormLayout.LabelRole, self.lbl_stat_contour)

        self.val_stat_contour = QLabel(self.gb_layer_statistics)
        self.val_stat_contour.setObjectName(u"val_stat_contour")

        self.formLayout_layer_stats.setWidget(0, QFormLayout.FieldRole, self.val_stat_contour)

        self.lbl_stat_hatch = QLabel(self.gb_layer_statistics)
        self.lbl_stat_hatch.setObjectName(u"lbl_stat_hatch")

        self.formLayout_layer_stats.setWidget(1, QFormLayout.LabelRole, self.lbl_stat_hatch)

        self.val_stat_hatch = QLabel(self.gb_layer_statistics)
        self.val_stat_hatch.setObjectName(u"val_stat_hatch")

        self.formLayout_layer_stats.setWidget(1, QFormLayout.FieldRole, self.val_stat_hatch)

        self.lbl_stat_supp = QLabel(self.gb_layer_statistics)
        self.lbl_stat_supp.setObjectName(u"lbl_stat_supp")

        self.formLayout_layer_stats.setWidget(2, QFormLayout.LabelRole, self.lbl_stat_supp)

        self.val_stat_supp = QLabel(self.gb_layer_statistics)
        self.val_stat_supp.setObjectName(u"val_stat_supp")

        self.formLayout_layer_stats.setWidget(2, QFormLayout.FieldRole, self.val_stat_supp)

        self.lbl_stat_jump1 = QLabel(self.gb_layer_statistics)
        self.lbl_stat_jump1.setObjectName(u"lbl_stat_jump1")

        self.formLayout_layer_stats.setWidget(3, QFormLayout.LabelRole, self.lbl_stat_jump1)

        self.val_stat_jump1 = QLabel(self.gb_layer_statistics)
        self.val_stat_jump1.setObjectName(u"val_stat_jump1")

        self.formLayout_layer_stats.setWidget(3, QFormLayout.FieldRole, self.val_stat_jump1)

        self.lbl_stat_total = QLabel(self.gb_layer_statistics)
        self.lbl_stat_total.setObjectName(u"lbl_stat_total")

        self.formLayout_layer_stats.setWidget(4, QFormLayout.LabelRole, self.lbl_stat_total)

        self.val_stat_total = QLabel(self.gb_layer_statistics)
        self.val_stat_total.setObjectName(u"val_stat_total")

        self.formLayout_layer_stats.setWidget(4, QFormLayout.FieldRole, self.val_stat_total)


        self.hLayout_layer_stats.addLayout(self.formLayout_layer_stats)


        self.vLayout_c3_p3.addWidget(self.gb_layer_statistics)

        self.gb_layer_actions = QGroupBox(self.page_gcode)
        self.gb_layer_actions.setObjectName(u"gb_layer_actions")
        sizePolicy.setHeightForWidth(self.gb_layer_actions.sizePolicy().hasHeightForWidth())
        self.gb_layer_actions.setSizePolicy(sizePolicy)
        self.gridLayout_layer_actions = QGridLayout(self.gb_layer_actions)
        self.gridLayout_layer_actions.setSpacing(4)
        self.gridLayout_layer_actions.setObjectName(u"gridLayout_layer_actions")
        self.btn_act_export_img = QPushButton(self.gb_layer_actions)
        self.btn_act_export_img.setObjectName(u"btn_act_export_img")
        self.btn_act_export_img.setMinimumSize(QSize(0, 20))

        self.gridLayout_layer_actions.addWidget(self.btn_act_export_img, 0, 0, 1, 1)

        self.btn_act_export_data = QPushButton(self.gb_layer_actions)
        self.btn_act_export_data.setObjectName(u"btn_act_export_data")
        self.btn_act_export_data.setMinimumSize(QSize(0, 20))

        self.gridLayout_layer_actions.addWidget(self.btn_act_export_data, 0, 1, 1, 1)

        self.btn_act_simulate = QPushButton(self.gb_layer_actions)
        self.btn_act_simulate.setObjectName(u"btn_act_simulate")
        self.btn_act_simulate.setMinimumSize(QSize(0, 20))

        self.gridLayout_layer_actions.addWidget(self.btn_act_simulate, 1, 0, 1, 1)

        self.btn_act_clear = QPushButton(self.gb_layer_actions)
        self.btn_act_clear.setObjectName(u"btn_act_clear")
        self.btn_act_clear.setMinimumSize(QSize(0, 20))

        self.gridLayout_layer_actions.addWidget(self.btn_act_clear, 1, 1, 1, 1)


        self.vLayout_c3_p3.addWidget(self.gb_layer_actions)

        self.spacerItem9 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vLayout_c3_p3.addItem(self.spacerItem9)


        self.gridLayout_page3.addLayout(self.vLayout_c3_p3, 0, 2, 1, 1)

        self.gridLayout_page3.setColumnStretch(0, 2)
        self.gridLayout_page3.setColumnStretch(1, 6)
        self.gridLayout_page3.setColumnStretch(2, 3)
        self.stackedWidget.addWidget(self.page_gcode)
        self.page_machine_control = QWidget()
        self.page_machine_control.setObjectName(u"page_machine_control")
        self.vLayout_page_mc = QVBoxLayout(self.page_machine_control)
        self.vLayout_page_mc.setSpacing(4)
        self.vLayout_page_mc.setObjectName(u"vLayout_page_mc")
        self.hboxLayout10 = QHBoxLayout()
        self.hboxLayout10.setSpacing(4)
        self.hboxLayout10.setObjectName(u"hboxLayout10")
        self.gb_build_platform = QGroupBox(self.page_machine_control)
        self.gb_build_platform.setObjectName(u"gb_build_platform")
        sizePolicy.setHeightForWidth(self.gb_build_platform.sizePolicy().hasHeightForWidth())
        self.gb_build_platform.setSizePolicy(sizePolicy)
        self.vboxLayout11 = QVBoxLayout(self.gb_build_platform)
        self.vboxLayout11.setSpacing(4)
        self.vboxLayout11.setObjectName(u"vboxLayout11")
        self.hboxLayout11 = QHBoxLayout()
        self.hboxLayout11.setSpacing(4)
        self.hboxLayout11.setObjectName(u"hboxLayout11")
        self.label25 = QLabel(self.gb_build_platform)
        self.label25.setObjectName(u"label25")

        self.hboxLayout11.addWidget(self.label25)

        self.label26 = QLabel(self.gb_build_platform)
        self.label26.setObjectName(u"label26")

        self.hboxLayout11.addWidget(self.label26)


        self.vboxLayout11.addLayout(self.hboxLayout11)

        self.hboxLayout12 = QHBoxLayout()
        self.hboxLayout12.setSpacing(4)
        self.hboxLayout12.setObjectName(u"hboxLayout12")
        self.vboxLayout12 = QVBoxLayout()
        self.vboxLayout12.setSpacing(4)
        self.vboxLayout12.setObjectName(u"vboxLayout12")
        self.pushButton18 = QPushButton(self.gb_build_platform)
        self.pushButton18.setObjectName(u"pushButton18")
        self.pushButton18.setMinimumSize(QSize(0, 20))

        self.vboxLayout12.addWidget(self.pushButton18)

        self.pushButton19 = QPushButton(self.gb_build_platform)
        self.pushButton19.setObjectName(u"pushButton19")
        self.pushButton19.setMinimumSize(QSize(0, 20))

        self.vboxLayout12.addWidget(self.pushButton19)

        self.pushButton20 = QPushButton(self.gb_build_platform)
        self.pushButton20.setObjectName(u"pushButton20")
        self.pushButton20.setMinimumSize(QSize(0, 20))

        self.vboxLayout12.addWidget(self.pushButton20)

        self.pushButton21 = QPushButton(self.gb_build_platform)
        self.pushButton21.setObjectName(u"pushButton21")
        self.pushButton21.setMinimumSize(QSize(0, 20))

        self.vboxLayout12.addWidget(self.pushButton21)


        self.hboxLayout12.addLayout(self.vboxLayout12)

        self.label27 = QLabel(self.gb_build_platform)
        self.label27.setObjectName(u"label27")

        self.hboxLayout12.addWidget(self.label27)

        self.slider3 = QSlider(self.gb_build_platform)
        self.slider3.setObjectName(u"slider3")
        self.slider3.setOrientation(Qt.Orientation.Vertical)

        self.hboxLayout12.addWidget(self.slider3)


        self.vboxLayout11.addLayout(self.hboxLayout12)

        self.hboxLayout13 = QHBoxLayout()
        self.hboxLayout13.setSpacing(4)
        self.hboxLayout13.setObjectName(u"hboxLayout13")
        self.label28 = QLabel(self.gb_build_platform)
        self.label28.setObjectName(u"label28")

        self.hboxLayout13.addWidget(self.label28)

        self.lineEdit = QLineEdit(self.gb_build_platform)
        self.lineEdit.setObjectName(u"lineEdit")

        self.hboxLayout13.addWidget(self.lineEdit)

        self.pushButton22 = QPushButton(self.gb_build_platform)
        self.pushButton22.setObjectName(u"pushButton22")
        self.pushButton22.setMinimumSize(QSize(0, 20))

        self.hboxLayout13.addWidget(self.pushButton22)


        self.vboxLayout11.addLayout(self.hboxLayout13)


        self.hboxLayout10.addWidget(self.gb_build_platform)

        self.gb_powder_feed = QGroupBox(self.page_machine_control)
        self.gb_powder_feed.setObjectName(u"gb_powder_feed")
        sizePolicy.setHeightForWidth(self.gb_powder_feed.sizePolicy().hasHeightForWidth())
        self.gb_powder_feed.setSizePolicy(sizePolicy)
        self.vboxLayout13 = QVBoxLayout(self.gb_powder_feed)
        self.vboxLayout13.setSpacing(4)
        self.vboxLayout13.setObjectName(u"vboxLayout13")
        self.hboxLayout14 = QHBoxLayout()
        self.hboxLayout14.setSpacing(4)
        self.hboxLayout14.setObjectName(u"hboxLayout14")
        self.label29 = QLabel(self.gb_powder_feed)
        self.label29.setObjectName(u"label29")

        self.hboxLayout14.addWidget(self.label29)

        self.label30 = QLabel(self.gb_powder_feed)
        self.label30.setObjectName(u"label30")

        self.hboxLayout14.addWidget(self.label30)


        self.vboxLayout13.addLayout(self.hboxLayout14)

        self.hboxLayout15 = QHBoxLayout()
        self.hboxLayout15.setSpacing(4)
        self.hboxLayout15.setObjectName(u"hboxLayout15")
        self.vboxLayout14 = QVBoxLayout()
        self.vboxLayout14.setSpacing(4)
        self.vboxLayout14.setObjectName(u"vboxLayout14")
        self.pushButton23 = QPushButton(self.gb_powder_feed)
        self.pushButton23.setObjectName(u"pushButton23")
        self.pushButton23.setMinimumSize(QSize(0, 20))

        self.vboxLayout14.addWidget(self.pushButton23)

        self.pushButton24 = QPushButton(self.gb_powder_feed)
        self.pushButton24.setObjectName(u"pushButton24")
        self.pushButton24.setMinimumSize(QSize(0, 20))

        self.vboxLayout14.addWidget(self.pushButton24)

        self.pushButton25 = QPushButton(self.gb_powder_feed)
        self.pushButton25.setObjectName(u"pushButton25")
        self.pushButton25.setMinimumSize(QSize(0, 20))

        self.vboxLayout14.addWidget(self.pushButton25)


        self.hboxLayout15.addLayout(self.vboxLayout14)

        self.label31 = QLabel(self.gb_powder_feed)
        self.label31.setObjectName(u"label31")

        self.hboxLayout15.addWidget(self.label31)

        self.slider4 = QSlider(self.gb_powder_feed)
        self.slider4.setObjectName(u"slider4")
        self.slider4.setOrientation(Qt.Orientation.Vertical)

        self.hboxLayout15.addWidget(self.slider4)


        self.vboxLayout13.addLayout(self.hboxLayout15)

        self.hboxLayout16 = QHBoxLayout()
        self.hboxLayout16.setSpacing(4)
        self.hboxLayout16.setObjectName(u"hboxLayout16")
        self.label32 = QLabel(self.gb_powder_feed)
        self.label32.setObjectName(u"label32")

        self.hboxLayout16.addWidget(self.label32)

        self.lineEdit1 = QLineEdit(self.gb_powder_feed)
        self.lineEdit1.setObjectName(u"lineEdit1")

        self.hboxLayout16.addWidget(self.lineEdit1)

        self.pushButton26 = QPushButton(self.gb_powder_feed)
        self.pushButton26.setObjectName(u"pushButton26")
        self.pushButton26.setMinimumSize(QSize(0, 20))

        self.hboxLayout16.addWidget(self.pushButton26)


        self.vboxLayout13.addLayout(self.hboxLayout16)


        self.hboxLayout10.addWidget(self.gb_powder_feed)

        self.gb_recoater = QGroupBox(self.page_machine_control)
        self.gb_recoater.setObjectName(u"gb_recoater")
        sizePolicy.setHeightForWidth(self.gb_recoater.sizePolicy().hasHeightForWidth())
        self.gb_recoater.setSizePolicy(sizePolicy)
        self.vboxLayout15 = QVBoxLayout(self.gb_recoater)
        self.vboxLayout15.setSpacing(4)
        self.vboxLayout15.setObjectName(u"vboxLayout15")
        self.hboxLayout17 = QHBoxLayout()
        self.hboxLayout17.setSpacing(4)
        self.hboxLayout17.setObjectName(u"hboxLayout17")
        self.label33 = QLabel(self.gb_recoater)
        self.label33.setObjectName(u"label33")

        self.hboxLayout17.addWidget(self.label33)

        self.label34 = QLabel(self.gb_recoater)
        self.label34.setObjectName(u"label34")

        self.hboxLayout17.addWidget(self.label34)


        self.vboxLayout15.addLayout(self.hboxLayout17)

        self.label35 = QLabel(self.gb_recoater)
        self.label35.setObjectName(u"label35")
        self.label35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout15.addWidget(self.label35)

        self.hboxLayout18 = QHBoxLayout()
        self.hboxLayout18.setSpacing(4)
        self.hboxLayout18.setObjectName(u"hboxLayout18")
        self.pushButton27 = QPushButton(self.gb_recoater)
        self.pushButton27.setObjectName(u"pushButton27")
        self.pushButton27.setMinimumSize(QSize(0, 20))

        self.hboxLayout18.addWidget(self.pushButton27)

        self.pushButton28 = QPushButton(self.gb_recoater)
        self.pushButton28.setObjectName(u"pushButton28")
        self.pushButton28.setMinimumSize(QSize(0, 20))

        self.hboxLayout18.addWidget(self.pushButton28)


        self.vboxLayout15.addLayout(self.hboxLayout18)

        self.pushButton29 = QPushButton(self.gb_recoater)
        self.pushButton29.setObjectName(u"pushButton29")
        self.pushButton29.setMinimumSize(QSize(0, 20))

        self.vboxLayout15.addWidget(self.pushButton29)

        self.pushButton30 = QPushButton(self.gb_recoater)
        self.pushButton30.setObjectName(u"pushButton30")
        self.pushButton30.setMinimumSize(QSize(0, 20))

        self.vboxLayout15.addWidget(self.pushButton30)


        self.hboxLayout10.addWidget(self.gb_recoater)

        self.gb_chamber_door = QGroupBox(self.page_machine_control)
        self.gb_chamber_door.setObjectName(u"gb_chamber_door")
        sizePolicy.setHeightForWidth(self.gb_chamber_door.sizePolicy().hasHeightForWidth())
        self.gb_chamber_door.setSizePolicy(sizePolicy)
        self.vboxLayout16 = QVBoxLayout(self.gb_chamber_door)
        self.vboxLayout16.setSpacing(4)
        self.vboxLayout16.setObjectName(u"vboxLayout16")
        self.label36 = QLabel(self.gb_chamber_door)
        self.label36.setObjectName(u"label36")

        self.vboxLayout16.addWidget(self.label36)

        self.label37 = QLabel(self.gb_chamber_door)
        self.label37.setObjectName(u"label37")
        self.label37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout16.addWidget(self.label37)

        self.pushButton31 = QPushButton(self.gb_chamber_door)
        self.pushButton31.setObjectName(u"pushButton31")
        self.pushButton31.setMinimumSize(QSize(0, 20))

        self.vboxLayout16.addWidget(self.pushButton31)

        self.pushButton32 = QPushButton(self.gb_chamber_door)
        self.pushButton32.setObjectName(u"pushButton32")
        self.pushButton32.setEnabled(False)
        self.pushButton32.setMinimumSize(QSize(0, 20))

        self.vboxLayout16.addWidget(self.pushButton32)


        self.hboxLayout10.addWidget(self.gb_chamber_door)


        self.vLayout_page_mc.addLayout(self.hboxLayout10)

        self.hboxLayout19 = QHBoxLayout()
        self.hboxLayout19.setSpacing(4)
        self.hboxLayout19.setObjectName(u"hboxLayout19")
        self.gb_gas_system = QGroupBox(self.page_machine_control)
        self.gb_gas_system.setObjectName(u"gb_gas_system")
        sizePolicy.setHeightForWidth(self.gb_gas_system.sizePolicy().hasHeightForWidth())
        self.gb_gas_system.setSizePolicy(sizePolicy)
        self.hboxLayout20 = QHBoxLayout(self.gb_gas_system)
        self.hboxLayout20.setSpacing(4)
        self.hboxLayout20.setObjectName(u"hboxLayout20")
        self.formLayout2 = QFormLayout()
        self.formLayout2.setObjectName(u"formLayout2")
        self.formLayout2.setHorizontalSpacing(4)
        self.formLayout2.setVerticalSpacing(4)
        self.label38 = QLabel(self.gb_gas_system)
        self.label38.setObjectName(u"label38")

        self.formLayout2.setWidget(0, QFormLayout.LabelRole, self.label38)

        self.label39 = QLabel(self.gb_gas_system)
        self.label39.setObjectName(u"label39")

        self.formLayout2.setWidget(0, QFormLayout.FieldRole, self.label39)

        self.label40 = QLabel(self.gb_gas_system)
        self.label40.setObjectName(u"label40")

        self.formLayout2.setWidget(1, QFormLayout.LabelRole, self.label40)

        self.label41 = QLabel(self.gb_gas_system)
        self.label41.setObjectName(u"label41")

        self.formLayout2.setWidget(1, QFormLayout.FieldRole, self.label41)

        self.label42 = QLabel(self.gb_gas_system)
        self.label42.setObjectName(u"label42")

        self.formLayout2.setWidget(2, QFormLayout.LabelRole, self.label42)

        self.label43 = QLabel(self.gb_gas_system)
        self.label43.setObjectName(u"label43")

        self.formLayout2.setWidget(2, QFormLayout.FieldRole, self.label43)

        self.label44 = QLabel(self.gb_gas_system)
        self.label44.setObjectName(u"label44")

        self.formLayout2.setWidget(3, QFormLayout.LabelRole, self.label44)

        self.label45 = QLabel(self.gb_gas_system)
        self.label45.setObjectName(u"label45")

        self.formLayout2.setWidget(3, QFormLayout.FieldRole, self.label45)


        self.hboxLayout20.addLayout(self.formLayout2)

        self.vboxLayout17 = QVBoxLayout()
        self.vboxLayout17.setSpacing(4)
        self.vboxLayout17.setObjectName(u"vboxLayout17")
        self.label46 = QLabel(self.gb_gas_system)
        self.label46.setObjectName(u"label46")

        self.vboxLayout17.addWidget(self.label46)

        self.pushButton33 = QPushButton(self.gb_gas_system)
        self.pushButton33.setObjectName(u"pushButton33")
        self.pushButton33.setMinimumSize(QSize(0, 20))

        self.vboxLayout17.addWidget(self.pushButton33)

        self.pushButton34 = QPushButton(self.gb_gas_system)
        self.pushButton34.setObjectName(u"pushButton34")
        self.pushButton34.setMinimumSize(QSize(0, 20))

        self.vboxLayout17.addWidget(self.pushButton34)

        self.hboxLayout21 = QHBoxLayout()
        self.hboxLayout21.setSpacing(4)
        self.hboxLayout21.setObjectName(u"hboxLayout21")
        self.label47 = QLabel(self.gb_gas_system)
        self.label47.setObjectName(u"label47")

        self.hboxLayout21.addWidget(self.label47)

        self.checkBox3 = QCheckBox(self.gb_gas_system)
        self.checkBox3.setObjectName(u"checkBox3")
        self.checkBox3.setChecked(True)

        self.hboxLayout21.addWidget(self.checkBox3)


        self.vboxLayout17.addLayout(self.hboxLayout21)

        self.label48 = QLabel(self.gb_gas_system)
        self.label48.setObjectName(u"label48")

        self.vboxLayout17.addWidget(self.label48)


        self.hboxLayout20.addLayout(self.vboxLayout17)


        self.hboxLayout19.addWidget(self.gb_gas_system)

        self.gb_environment_control = QGroupBox(self.page_machine_control)
        self.gb_environment_control.setObjectName(u"gb_environment_control")
        sizePolicy.setHeightForWidth(self.gb_environment_control.sizePolicy().hasHeightForWidth())
        self.gb_environment_control.setSizePolicy(sizePolicy)
        self.hboxLayout22 = QHBoxLayout(self.gb_environment_control)
        self.hboxLayout22.setSpacing(4)
        self.hboxLayout22.setObjectName(u"hboxLayout22")
        self.formLayout3 = QFormLayout()
        self.formLayout3.setObjectName(u"formLayout3")
        self.formLayout3.setHorizontalSpacing(4)
        self.formLayout3.setVerticalSpacing(4)
        self.label49 = QLabel(self.gb_environment_control)
        self.label49.setObjectName(u"label49")

        self.formLayout3.setWidget(0, QFormLayout.LabelRole, self.label49)

        self.label50 = QLabel(self.gb_environment_control)
        self.label50.setObjectName(u"label50")

        self.formLayout3.setWidget(0, QFormLayout.FieldRole, self.label50)

        self.label51 = QLabel(self.gb_environment_control)
        self.label51.setObjectName(u"label51")

        self.formLayout3.setWidget(1, QFormLayout.LabelRole, self.label51)

        self.label52 = QLabel(self.gb_environment_control)
        self.label52.setObjectName(u"label52")

        self.formLayout3.setWidget(1, QFormLayout.FieldRole, self.label52)

        self.label53 = QLabel(self.gb_environment_control)
        self.label53.setObjectName(u"label53")

        self.formLayout3.setWidget(2, QFormLayout.LabelRole, self.label53)

        self.label54 = QLabel(self.gb_environment_control)
        self.label54.setObjectName(u"label54")

        self.formLayout3.setWidget(2, QFormLayout.FieldRole, self.label54)

        self.label55 = QLabel(self.gb_environment_control)
        self.label55.setObjectName(u"label55")

        self.formLayout3.setWidget(3, QFormLayout.LabelRole, self.label55)

        self.label56 = QLabel(self.gb_environment_control)
        self.label56.setObjectName(u"label56")

        self.formLayout3.setWidget(3, QFormLayout.FieldRole, self.label56)


        self.hboxLayout22.addLayout(self.formLayout3)

        self.vboxLayout18 = QVBoxLayout()
        self.vboxLayout18.setSpacing(4)
        self.vboxLayout18.setObjectName(u"vboxLayout18")
        self.label57 = QLabel(self.gb_environment_control)
        self.label57.setObjectName(u"label57")

        self.vboxLayout18.addWidget(self.label57)

        self.label58 = QLabel(self.gb_environment_control)
        self.label58.setObjectName(u"label58")

        self.vboxLayout18.addWidget(self.label58)

        self.hboxLayout23 = QHBoxLayout()
        self.hboxLayout23.setSpacing(4)
        self.hboxLayout23.setObjectName(u"hboxLayout23")
        self.lineEdit2 = QLineEdit(self.gb_environment_control)
        self.lineEdit2.setObjectName(u"lineEdit2")

        self.hboxLayout23.addWidget(self.lineEdit2)

        self.pushButton35 = QPushButton(self.gb_environment_control)
        self.pushButton35.setObjectName(u"pushButton35")
        self.pushButton35.setMinimumSize(QSize(0, 20))

        self.hboxLayout23.addWidget(self.pushButton35)


        self.vboxLayout18.addLayout(self.hboxLayout23)

        self.label59 = QLabel(self.gb_environment_control)
        self.label59.setObjectName(u"label59")

        self.vboxLayout18.addWidget(self.label59)


        self.hboxLayout22.addLayout(self.vboxLayout18)


        self.hboxLayout19.addWidget(self.gb_environment_control)

        self.gb_auxiliary_systems = QGroupBox(self.page_machine_control)
        self.gb_auxiliary_systems.setObjectName(u"gb_auxiliary_systems")
        sizePolicy.setHeightForWidth(self.gb_auxiliary_systems.sizePolicy().hasHeightForWidth())
        self.gb_auxiliary_systems.setSizePolicy(sizePolicy)
        self.gridLayout2 = QGridLayout(self.gb_auxiliary_systems)
        self.gridLayout2.setSpacing(4)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.label60 = QLabel(self.gb_auxiliary_systems)
        self.label60.setObjectName(u"label60")

        self.gridLayout2.addWidget(self.label60, 0, 0, 1, 1)

        self.label61 = QLabel(self.gb_auxiliary_systems)
        self.label61.setObjectName(u"label61")

        self.gridLayout2.addWidget(self.label61, 0, 1, 1, 1)

        self.pushButton36 = QPushButton(self.gb_auxiliary_systems)
        self.pushButton36.setObjectName(u"pushButton36")
        self.pushButton36.setMinimumSize(QSize(0, 20))

        self.gridLayout2.addWidget(self.pushButton36, 0, 2, 1, 1)

        self.label62 = QLabel(self.gb_auxiliary_systems)
        self.label62.setObjectName(u"label62")

        self.gridLayout2.addWidget(self.label62, 1, 0, 1, 1)

        self.label63 = QLabel(self.gb_auxiliary_systems)
        self.label63.setObjectName(u"label63")

        self.gridLayout2.addWidget(self.label63, 1, 1, 1, 1)

        self.pushButton37 = QPushButton(self.gb_auxiliary_systems)
        self.pushButton37.setObjectName(u"pushButton37")
        self.pushButton37.setMinimumSize(QSize(0, 20))

        self.gridLayout2.addWidget(self.pushButton37, 1, 2, 1, 1)

        self.label64 = QLabel(self.gb_auxiliary_systems)
        self.label64.setObjectName(u"label64")

        self.gridLayout2.addWidget(self.label64, 2, 0, 1, 1)

        self.label65 = QLabel(self.gb_auxiliary_systems)
        self.label65.setObjectName(u"label65")

        self.gridLayout2.addWidget(self.label65, 2, 1, 1, 1)

        self.pushButton38 = QPushButton(self.gb_auxiliary_systems)
        self.pushButton38.setObjectName(u"pushButton38")
        self.pushButton38.setMinimumSize(QSize(0, 20))

        self.gridLayout2.addWidget(self.pushButton38, 2, 2, 1, 1)

        self.label66 = QLabel(self.gb_auxiliary_systems)
        self.label66.setObjectName(u"label66")

        self.gridLayout2.addWidget(self.label66, 3, 0, 1, 1)

        self.label67 = QLabel(self.gb_auxiliary_systems)
        self.label67.setObjectName(u"label67")

        self.gridLayout2.addWidget(self.label67, 3, 1, 1, 1)

        self.pushButton39 = QPushButton(self.gb_auxiliary_systems)
        self.pushButton39.setObjectName(u"pushButton39")
        self.pushButton39.setMinimumSize(QSize(0, 20))

        self.gridLayout2.addWidget(self.pushButton39, 3, 2, 1, 1)


        self.hboxLayout19.addWidget(self.gb_auxiliary_systems)


        self.vLayout_page_mc.addLayout(self.hboxLayout19)

        self.gb_quick_actions = QGroupBox(self.page_machine_control)
        self.gb_quick_actions.setObjectName(u"gb_quick_actions")
        sizePolicy.setHeightForWidth(self.gb_quick_actions.sizePolicy().hasHeightForWidth())
        self.gb_quick_actions.setSizePolicy(sizePolicy)
        self.hboxLayout24 = QHBoxLayout(self.gb_quick_actions)
        self.hboxLayout24.setSpacing(4)
        self.hboxLayout24.setObjectName(u"hboxLayout24")
        self.pushButton40 = QPushButton(self.gb_quick_actions)
        self.pushButton40.setObjectName(u"pushButton40")
        self.pushButton40.setMinimumSize(QSize(0, 20))

        self.hboxLayout24.addWidget(self.pushButton40)

        self.pushButton41 = QPushButton(self.gb_quick_actions)
        self.pushButton41.setObjectName(u"pushButton41")
        self.pushButton41.setMinimumSize(QSize(0, 20))

        self.hboxLayout24.addWidget(self.pushButton41)

        self.pushButton42 = QPushButton(self.gb_quick_actions)
        self.pushButton42.setObjectName(u"pushButton42")
        self.pushButton42.setMinimumSize(QSize(0, 20))

        self.hboxLayout24.addWidget(self.pushButton42)

        self.pushButton43 = QPushButton(self.gb_quick_actions)
        self.pushButton43.setObjectName(u"pushButton43")
        self.pushButton43.setMinimumSize(QSize(0, 20))

        self.hboxLayout24.addWidget(self.pushButton43)

        self.pushButton44 = QPushButton(self.gb_quick_actions)
        self.pushButton44.setObjectName(u"pushButton44")
        self.pushButton44.setMinimumSize(QSize(0, 20))

        self.hboxLayout24.addWidget(self.pushButton44)

        self.pushButton45 = QPushButton(self.gb_quick_actions)
        self.pushButton45.setObjectName(u"pushButton45")
        self.pushButton45.setMinimumSize(QSize(0, 20))

        self.hboxLayout24.addWidget(self.pushButton45)


        self.vLayout_page_mc.addWidget(self.gb_quick_actions)

        self.vLayout_page_mc.setStretch(0, 3)
        self.vLayout_page_mc.setStretch(1, 2)
        self.vLayout_page_mc.setStretch(2, 1)
        self.stackedWidget.addWidget(self.page_machine_control)
        self.page_laser_galvo = QWidget()
        self.page_laser_galvo.setObjectName(u"page_laser_galvo")
        self.vLayout_laser_galvo = QVBoxLayout(self.page_laser_galvo)
        self.vLayout_laser_galvo.setSpacing(4)
        self.vLayout_laser_galvo.setObjectName(u"vLayout_laser_galvo")
        self.hboxLayout25 = QHBoxLayout()
        self.hboxLayout25.setSpacing(4)
        self.hboxLayout25.setObjectName(u"hboxLayout25")
        self.gb_laser_control = QGroupBox(self.page_laser_galvo)
        self.gb_laser_control.setObjectName(u"gb_laser_control")
        sizePolicy.setHeightForWidth(self.gb_laser_control.sizePolicy().hasHeightForWidth())
        self.gb_laser_control.setSizePolicy(sizePolicy)
        self.hboxLayout26 = QHBoxLayout(self.gb_laser_control)
        self.hboxLayout26.setSpacing(4)
        self.hboxLayout26.setObjectName(u"hboxLayout26")
        self.vboxLayout19 = QVBoxLayout()
        self.vboxLayout19.setSpacing(4)
        self.vboxLayout19.setObjectName(u"vboxLayout19")
        self.formLayout4 = QFormLayout()
        self.formLayout4.setObjectName(u"formLayout4")
        self.formLayout4.setHorizontalSpacing(4)
        self.formLayout4.setVerticalSpacing(4)
        self.label68 = QLabel(self.gb_laser_control)
        self.label68.setObjectName(u"label68")

        self.formLayout4.setWidget(0, QFormLayout.LabelRole, self.label68)

        self.label69 = QLabel(self.gb_laser_control)
        self.label69.setObjectName(u"label69")

        self.formLayout4.setWidget(0, QFormLayout.FieldRole, self.label69)

        self.label70 = QLabel(self.gb_laser_control)
        self.label70.setObjectName(u"label70")

        self.formLayout4.setWidget(1, QFormLayout.LabelRole, self.label70)

        self.label71 = QLabel(self.gb_laser_control)
        self.label71.setObjectName(u"label71")

        self.formLayout4.setWidget(1, QFormLayout.FieldRole, self.label71)

        self.label72 = QLabel(self.gb_laser_control)
        self.label72.setObjectName(u"label72")

        self.formLayout4.setWidget(2, QFormLayout.LabelRole, self.label72)

        self.label73 = QLabel(self.gb_laser_control)
        self.label73.setObjectName(u"label73")

        self.formLayout4.setWidget(2, QFormLayout.FieldRole, self.label73)


        self.vboxLayout19.addLayout(self.formLayout4)

        self.pushButton46 = QPushButton(self.gb_laser_control)
        self.pushButton46.setObjectName(u"pushButton46")
        self.pushButton46.setMinimumSize(QSize(0, 20))

        self.vboxLayout19.addWidget(self.pushButton46)

        self.pushButton47 = QPushButton(self.gb_laser_control)
        self.pushButton47.setObjectName(u"pushButton47")
        self.pushButton47.setMinimumSize(QSize(0, 20))

        self.vboxLayout19.addWidget(self.pushButton47)


        self.hboxLayout26.addLayout(self.vboxLayout19)

        self.vboxLayout20 = QVBoxLayout()
        self.vboxLayout20.setSpacing(4)
        self.vboxLayout20.setObjectName(u"vboxLayout20")
        self.label74 = QLabel(self.gb_laser_control)
        self.label74.setObjectName(u"label74")

        self.vboxLayout20.addWidget(self.label74)

        self.label75 = QLabel(self.gb_laser_control)
        self.label75.setObjectName(u"label75")
        self.label75.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout20.addWidget(self.label75)

        self.hboxLayout27 = QHBoxLayout()
        self.hboxLayout27.setSpacing(4)
        self.hboxLayout27.setObjectName(u"hboxLayout27")
        self.label76 = QLabel(self.gb_laser_control)
        self.label76.setObjectName(u"label76")

        self.hboxLayout27.addWidget(self.label76)

        self.lineEdit3 = QLineEdit(self.gb_laser_control)
        self.lineEdit3.setObjectName(u"lineEdit3")

        self.hboxLayout27.addWidget(self.lineEdit3)

        self.label77 = QLabel(self.gb_laser_control)
        self.label77.setObjectName(u"label77")

        self.hboxLayout27.addWidget(self.label77)

        self.pushButton48 = QPushButton(self.gb_laser_control)
        self.pushButton48.setObjectName(u"pushButton48")
        self.pushButton48.setMinimumSize(QSize(0, 20))

        self.hboxLayout27.addWidget(self.pushButton48)


        self.vboxLayout20.addLayout(self.hboxLayout27)


        self.hboxLayout26.addLayout(self.vboxLayout20)

        self.formLayout5 = QFormLayout()
        self.formLayout5.setObjectName(u"formLayout5")
        self.formLayout5.setHorizontalSpacing(4)
        self.formLayout5.setVerticalSpacing(4)
        self.label78 = QLabel(self.gb_laser_control)
        self.label78.setObjectName(u"label78")

        self.formLayout5.setWidget(0, QFormLayout.LabelRole, self.label78)

        self.label79 = QLabel(self.gb_laser_control)
        self.label79.setObjectName(u"label79")

        self.formLayout5.setWidget(0, QFormLayout.FieldRole, self.label79)

        self.label80 = QLabel(self.gb_laser_control)
        self.label80.setObjectName(u"label80")

        self.formLayout5.setWidget(1, QFormLayout.LabelRole, self.label80)

        self.label81 = QLabel(self.gb_laser_control)
        self.label81.setObjectName(u"label81")

        self.formLayout5.setWidget(1, QFormLayout.FieldRole, self.label81)

        self.label82 = QLabel(self.gb_laser_control)
        self.label82.setObjectName(u"label82")

        self.formLayout5.setWidget(2, QFormLayout.LabelRole, self.label82)

        self.label83 = QLabel(self.gb_laser_control)
        self.label83.setObjectName(u"label83")

        self.formLayout5.setWidget(2, QFormLayout.FieldRole, self.label83)

        self.label84 = QLabel(self.gb_laser_control)
        self.label84.setObjectName(u"label84")

        self.formLayout5.setWidget(3, QFormLayout.LabelRole, self.label84)

        self.label85 = QLabel(self.gb_laser_control)
        self.label85.setObjectName(u"label85")

        self.formLayout5.setWidget(3, QFormLayout.FieldRole, self.label85)

        self.label86 = QLabel(self.gb_laser_control)
        self.label86.setObjectName(u"label86")

        self.formLayout5.setWidget(4, QFormLayout.LabelRole, self.label86)

        self.label87 = QLabel(self.gb_laser_control)
        self.label87.setObjectName(u"label87")

        self.formLayout5.setWidget(4, QFormLayout.FieldRole, self.label87)

        self.label88 = QLabel(self.gb_laser_control)
        self.label88.setObjectName(u"label88")

        self.formLayout5.setWidget(5, QFormLayout.LabelRole, self.label88)

        self.label89 = QLabel(self.gb_laser_control)
        self.label89.setObjectName(u"label89")

        self.formLayout5.setWidget(5, QFormLayout.FieldRole, self.label89)

        self.label90 = QLabel(self.gb_laser_control)
        self.label90.setObjectName(u"label90")

        self.formLayout5.setWidget(6, QFormLayout.LabelRole, self.label90)

        self.label91 = QLabel(self.gb_laser_control)
        self.label91.setObjectName(u"label91")

        self.formLayout5.setWidget(6, QFormLayout.FieldRole, self.label91)

        self.label92 = QLabel(self.gb_laser_control)
        self.label92.setObjectName(u"label92")

        self.formLayout5.setWidget(7, QFormLayout.LabelRole, self.label92)

        self.label93 = QLabel(self.gb_laser_control)
        self.label93.setObjectName(u"label93")

        self.formLayout5.setWidget(7, QFormLayout.FieldRole, self.label93)


        self.hboxLayout26.addLayout(self.formLayout5)


        self.hboxLayout25.addWidget(self.gb_laser_control)

        self.gb_galvo_control = QGroupBox(self.page_laser_galvo)
        self.gb_galvo_control.setObjectName(u"gb_galvo_control")
        sizePolicy.setHeightForWidth(self.gb_galvo_control.sizePolicy().hasHeightForWidth())
        self.gb_galvo_control.setSizePolicy(sizePolicy)
        self.hboxLayout28 = QHBoxLayout(self.gb_galvo_control)
        self.hboxLayout28.setSpacing(4)
        self.hboxLayout28.setObjectName(u"hboxLayout28")
        self.vboxLayout21 = QVBoxLayout()
        self.vboxLayout21.setSpacing(4)
        self.vboxLayout21.setObjectName(u"vboxLayout21")
        self.formLayout6 = QFormLayout()
        self.formLayout6.setObjectName(u"formLayout6")
        self.formLayout6.setHorizontalSpacing(4)
        self.formLayout6.setVerticalSpacing(4)
        self.label94 = QLabel(self.gb_galvo_control)
        self.label94.setObjectName(u"label94")

        self.formLayout6.setWidget(0, QFormLayout.LabelRole, self.label94)

        self.label95 = QLabel(self.gb_galvo_control)
        self.label95.setObjectName(u"label95")

        self.formLayout6.setWidget(0, QFormLayout.FieldRole, self.label95)

        self.label96 = QLabel(self.gb_galvo_control)
        self.label96.setObjectName(u"label96")

        self.formLayout6.setWidget(1, QFormLayout.LabelRole, self.label96)

        self.label97 = QLabel(self.gb_galvo_control)
        self.label97.setObjectName(u"label97")

        self.formLayout6.setWidget(1, QFormLayout.FieldRole, self.label97)

        self.label98 = QLabel(self.gb_galvo_control)
        self.label98.setObjectName(u"label98")

        self.formLayout6.setWidget(2, QFormLayout.LabelRole, self.label98)

        self.label99 = QLabel(self.gb_galvo_control)
        self.label99.setObjectName(u"label99")

        self.formLayout6.setWidget(2, QFormLayout.FieldRole, self.label99)


        self.vboxLayout21.addLayout(self.formLayout6)

        self.pushButton49 = QPushButton(self.gb_galvo_control)
        self.pushButton49.setObjectName(u"pushButton49")
        self.pushButton49.setMinimumSize(QSize(0, 20))

        self.vboxLayout21.addWidget(self.pushButton49)

        self.pushButton50 = QPushButton(self.gb_galvo_control)
        self.pushButton50.setObjectName(u"pushButton50")
        self.pushButton50.setMinimumSize(QSize(0, 20))

        self.vboxLayout21.addWidget(self.pushButton50)


        self.hboxLayout28.addLayout(self.vboxLayout21)

        self.vboxLayout22 = QVBoxLayout()
        self.vboxLayout22.setSpacing(4)
        self.vboxLayout22.setObjectName(u"vboxLayout22")
        self.label100 = QLabel(self.gb_galvo_control)
        self.label100.setObjectName(u"label100")

        self.vboxLayout22.addWidget(self.label100)

        self.label101 = QLabel(self.gb_galvo_control)
        self.label101.setObjectName(u"label101")
        self.label101.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout22.addWidget(self.label101)

        self.hboxLayout29 = QHBoxLayout()
        self.hboxLayout29.setSpacing(4)
        self.hboxLayout29.setObjectName(u"hboxLayout29")
        self.label102 = QLabel(self.gb_galvo_control)
        self.label102.setObjectName(u"label102")

        self.hboxLayout29.addWidget(self.label102)

        self.lineEdit4 = QLineEdit(self.gb_galvo_control)
        self.lineEdit4.setObjectName(u"lineEdit4")

        self.hboxLayout29.addWidget(self.lineEdit4)

        self.label103 = QLabel(self.gb_galvo_control)
        self.label103.setObjectName(u"label103")

        self.hboxLayout29.addWidget(self.label103)

        self.pushButton51 = QPushButton(self.gb_galvo_control)
        self.pushButton51.setObjectName(u"pushButton51")
        self.pushButton51.setMinimumSize(QSize(0, 20))

        self.hboxLayout29.addWidget(self.pushButton51)


        self.vboxLayout22.addLayout(self.hboxLayout29)


        self.hboxLayout28.addLayout(self.vboxLayout22)

        self.formLayout7 = QFormLayout()
        self.formLayout7.setObjectName(u"formLayout7")
        self.formLayout7.setHorizontalSpacing(4)
        self.formLayout7.setVerticalSpacing(4)
        self.label104 = QLabel(self.gb_galvo_control)
        self.label104.setObjectName(u"label104")

        self.formLayout7.setWidget(0, QFormLayout.LabelRole, self.label104)

        self.label105 = QLabel(self.gb_galvo_control)
        self.label105.setObjectName(u"label105")

        self.formLayout7.setWidget(0, QFormLayout.FieldRole, self.label105)

        self.label106 = QLabel(self.gb_galvo_control)
        self.label106.setObjectName(u"label106")

        self.formLayout7.setWidget(1, QFormLayout.LabelRole, self.label106)

        self.label107 = QLabel(self.gb_galvo_control)
        self.label107.setObjectName(u"label107")

        self.formLayout7.setWidget(1, QFormLayout.FieldRole, self.label107)

        self.label108 = QLabel(self.gb_galvo_control)
        self.label108.setObjectName(u"label108")

        self.formLayout7.setWidget(2, QFormLayout.LabelRole, self.label108)

        self.label109 = QLabel(self.gb_galvo_control)
        self.label109.setObjectName(u"label109")

        self.formLayout7.setWidget(2, QFormLayout.FieldRole, self.label109)

        self.label110 = QLabel(self.gb_galvo_control)
        self.label110.setObjectName(u"label110")

        self.formLayout7.setWidget(3, QFormLayout.LabelRole, self.label110)

        self.label111 = QLabel(self.gb_galvo_control)
        self.label111.setObjectName(u"label111")

        self.formLayout7.setWidget(3, QFormLayout.FieldRole, self.label111)

        self.label112 = QLabel(self.gb_galvo_control)
        self.label112.setObjectName(u"label112")

        self.formLayout7.setWidget(4, QFormLayout.LabelRole, self.label112)

        self.label113 = QLabel(self.gb_galvo_control)
        self.label113.setObjectName(u"label113")

        self.formLayout7.setWidget(4, QFormLayout.FieldRole, self.label113)

        self.label114 = QLabel(self.gb_galvo_control)
        self.label114.setObjectName(u"label114")

        self.formLayout7.setWidget(5, QFormLayout.LabelRole, self.label114)

        self.label115 = QLabel(self.gb_galvo_control)
        self.label115.setObjectName(u"label115")

        self.formLayout7.setWidget(5, QFormLayout.FieldRole, self.label115)

        self.label116 = QLabel(self.gb_galvo_control)
        self.label116.setObjectName(u"label116")

        self.formLayout7.setWidget(6, QFormLayout.LabelRole, self.label116)

        self.label117 = QLabel(self.gb_galvo_control)
        self.label117.setObjectName(u"label117")

        self.formLayout7.setWidget(6, QFormLayout.FieldRole, self.label117)


        self.hboxLayout28.addLayout(self.formLayout7)


        self.hboxLayout25.addWidget(self.gb_galvo_control)


        self.vLayout_laser_galvo.addLayout(self.hboxLayout25)

        self.hboxLayout30 = QHBoxLayout()
        self.hboxLayout30.setSpacing(4)
        self.hboxLayout30.setObjectName(u"hboxLayout30")
        self.gb_laser_diag = QGroupBox(self.page_laser_galvo)
        self.gb_laser_diag.setObjectName(u"gb_laser_diag")
        sizePolicy.setHeightForWidth(self.gb_laser_diag.sizePolicy().hasHeightForWidth())
        self.gb_laser_diag.setSizePolicy(sizePolicy)
        self.hboxLayout31 = QHBoxLayout(self.gb_laser_diag)
        self.hboxLayout31.setSpacing(4)
        self.hboxLayout31.setObjectName(u"hboxLayout31")
        self.formLayout8 = QFormLayout()
        self.formLayout8.setObjectName(u"formLayout8")
        self.formLayout8.setHorizontalSpacing(4)
        self.formLayout8.setVerticalSpacing(4)
        self.label118 = QLabel(self.gb_laser_diag)
        self.label118.setObjectName(u"label118")

        self.formLayout8.setWidget(0, QFormLayout.LabelRole, self.label118)

        self.label119 = QLabel(self.gb_laser_diag)
        self.label119.setObjectName(u"label119")

        self.formLayout8.setWidget(0, QFormLayout.FieldRole, self.label119)

        self.label160 = QLabel(self.gb_laser_diag)
        self.label160.setObjectName(u"label160")

        self.formLayout8.setWidget(1, QFormLayout.LabelRole, self.label160)

        self.label121 = QLabel(self.gb_laser_diag)
        self.label121.setObjectName(u"label121")

        self.formLayout8.setWidget(1, QFormLayout.FieldRole, self.label121)

        self.label122 = QLabel(self.gb_laser_diag)
        self.label122.setObjectName(u"label122")

        self.formLayout8.setWidget(2, QFormLayout.LabelRole, self.label122)

        self.label123 = QLabel(self.gb_laser_diag)
        self.label123.setObjectName(u"label123")

        self.formLayout8.setWidget(2, QFormLayout.FieldRole, self.label123)

        self.label124 = QLabel(self.gb_laser_diag)
        self.label124.setObjectName(u"label124")

        self.formLayout8.setWidget(3, QFormLayout.LabelRole, self.label124)

        self.label125 = QLabel(self.gb_laser_diag)
        self.label125.setObjectName(u"label125")

        self.formLayout8.setWidget(3, QFormLayout.FieldRole, self.label125)

        self.label126 = QLabel(self.gb_laser_diag)
        self.label126.setObjectName(u"label126")

        self.formLayout8.setWidget(4, QFormLayout.LabelRole, self.label126)

        self.label127 = QLabel(self.gb_laser_diag)
        self.label127.setObjectName(u"label127")

        self.formLayout8.setWidget(4, QFormLayout.FieldRole, self.label127)

        self.label128 = QLabel(self.gb_laser_diag)
        self.label128.setObjectName(u"label128")

        self.formLayout8.setWidget(5, QFormLayout.LabelRole, self.label128)

        self.label129 = QLabel(self.gb_laser_diag)
        self.label129.setObjectName(u"label129")

        self.formLayout8.setWidget(5, QFormLayout.FieldRole, self.label129)


        self.hboxLayout31.addLayout(self.formLayout8)

        self.formLayout9 = QFormLayout()
        self.formLayout9.setObjectName(u"formLayout9")
        self.formLayout9.setHorizontalSpacing(4)
        self.formLayout9.setVerticalSpacing(4)
        self.label130 = QLabel(self.gb_laser_diag)
        self.label130.setObjectName(u"label130")

        self.formLayout9.setWidget(0, QFormLayout.LabelRole, self.label130)

        self.label131 = QLabel(self.gb_laser_diag)
        self.label131.setObjectName(u"label131")

        self.formLayout9.setWidget(1, QFormLayout.LabelRole, self.label131)

        self.label132 = QLabel(self.gb_laser_diag)
        self.label132.setObjectName(u"label132")

        self.formLayout9.setWidget(1, QFormLayout.FieldRole, self.label132)

        self.label133 = QLabel(self.gb_laser_diag)
        self.label133.setObjectName(u"label133")

        self.formLayout9.setWidget(2, QFormLayout.LabelRole, self.label133)

        self.label134 = QLabel(self.gb_laser_diag)
        self.label134.setObjectName(u"label134")

        self.formLayout9.setWidget(2, QFormLayout.FieldRole, self.label134)

        self.label135 = QLabel(self.gb_laser_diag)
        self.label135.setObjectName(u"label135")

        self.formLayout9.setWidget(3, QFormLayout.LabelRole, self.label135)

        self.label136 = QLabel(self.gb_laser_diag)
        self.label136.setObjectName(u"label136")

        self.formLayout9.setWidget(3, QFormLayout.FieldRole, self.label136)

        self.label137 = QLabel(self.gb_laser_diag)
        self.label137.setObjectName(u"label137")

        self.formLayout9.setWidget(4, QFormLayout.LabelRole, self.label137)

        self.label138 = QLabel(self.gb_laser_diag)
        self.label138.setObjectName(u"label138")

        self.formLayout9.setWidget(4, QFormLayout.FieldRole, self.label138)

        self.label139 = QLabel(self.gb_laser_diag)
        self.label139.setObjectName(u"label139")

        self.formLayout9.setWidget(5, QFormLayout.LabelRole, self.label139)

        self.label140 = QLabel(self.gb_laser_diag)
        self.label140.setObjectName(u"label140")

        self.formLayout9.setWidget(5, QFormLayout.FieldRole, self.label140)


        self.hboxLayout31.addLayout(self.formLayout9)


        self.hboxLayout30.addWidget(self.gb_laser_diag)

        self.gb_galvo_diag = QGroupBox(self.page_laser_galvo)
        self.gb_galvo_diag.setObjectName(u"gb_galvo_diag")
        sizePolicy.setHeightForWidth(self.gb_galvo_diag.sizePolicy().hasHeightForWidth())
        self.gb_galvo_diag.setSizePolicy(sizePolicy)
        self.hboxLayout32 = QHBoxLayout(self.gb_galvo_diag)
        self.hboxLayout32.setSpacing(4)
        self.hboxLayout32.setObjectName(u"hboxLayout32")
        self.formLayout10 = QFormLayout()
        self.formLayout10.setObjectName(u"formLayout10")
        self.formLayout10.setHorizontalSpacing(4)
        self.formLayout10.setVerticalSpacing(4)
        self.label141 = QLabel(self.gb_galvo_diag)
        self.label141.setObjectName(u"label141")

        self.formLayout10.setWidget(0, QFormLayout.LabelRole, self.label141)

        self.label142 = QLabel(self.gb_galvo_diag)
        self.label142.setObjectName(u"label142")

        self.formLayout10.setWidget(0, QFormLayout.FieldRole, self.label142)

        self.label143 = QLabel(self.gb_galvo_diag)
        self.label143.setObjectName(u"label143")

        self.formLayout10.setWidget(1, QFormLayout.LabelRole, self.label143)

        self.label144 = QLabel(self.gb_galvo_diag)
        self.label144.setObjectName(u"label144")

        self.formLayout10.setWidget(1, QFormLayout.FieldRole, self.label144)

        self.label145 = QLabel(self.gb_galvo_diag)
        self.label145.setObjectName(u"label145")

        self.formLayout10.setWidget(2, QFormLayout.LabelRole, self.label145)

        self.label146 = QLabel(self.gb_galvo_diag)
        self.label146.setObjectName(u"label146")

        self.formLayout10.setWidget(2, QFormLayout.FieldRole, self.label146)

        self.label147 = QLabel(self.gb_galvo_diag)
        self.label147.setObjectName(u"label147")

        self.formLayout10.setWidget(3, QFormLayout.LabelRole, self.label147)

        self.label148 = QLabel(self.gb_galvo_diag)
        self.label148.setObjectName(u"label148")

        self.formLayout10.setWidget(3, QFormLayout.FieldRole, self.label148)

        self.label149 = QLabel(self.gb_galvo_diag)
        self.label149.setObjectName(u"label149")

        self.formLayout10.setWidget(4, QFormLayout.LabelRole, self.label149)

        self.label150 = QLabel(self.gb_galvo_diag)
        self.label150.setObjectName(u"label150")

        self.formLayout10.setWidget(4, QFormLayout.FieldRole, self.label150)

        self.label151 = QLabel(self.gb_galvo_diag)
        self.label151.setObjectName(u"label151")

        self.formLayout10.setWidget(5, QFormLayout.LabelRole, self.label151)

        self.label152 = QLabel(self.gb_galvo_diag)
        self.label152.setObjectName(u"label152")

        self.formLayout10.setWidget(5, QFormLayout.FieldRole, self.label152)


        self.hboxLayout32.addLayout(self.formLayout10)

        self.formLayout11 = QFormLayout()
        self.formLayout11.setObjectName(u"formLayout11")
        self.formLayout11.setHorizontalSpacing(4)
        self.formLayout11.setVerticalSpacing(4)
        self.label153 = QLabel(self.gb_galvo_diag)
        self.label153.setObjectName(u"label153")

        self.formLayout11.setWidget(0, QFormLayout.LabelRole, self.label153)

        self.label154 = QLabel(self.gb_galvo_diag)
        self.label154.setObjectName(u"label154")

        self.formLayout11.setWidget(1, QFormLayout.LabelRole, self.label154)

        self.label155 = QLabel(self.gb_galvo_diag)
        self.label155.setObjectName(u"label155")

        self.formLayout11.setWidget(1, QFormLayout.FieldRole, self.label155)

        self.label156 = QLabel(self.gb_galvo_diag)
        self.label156.setObjectName(u"label156")

        self.formLayout11.setWidget(2, QFormLayout.LabelRole, self.label156)

        self.label157 = QLabel(self.gb_galvo_diag)
        self.label157.setObjectName(u"label157")

        self.formLayout11.setWidget(2, QFormLayout.FieldRole, self.label157)

        self.label158 = QLabel(self.gb_galvo_diag)
        self.label158.setObjectName(u"label158")

        self.formLayout11.setWidget(3, QFormLayout.LabelRole, self.label158)

        self.label159 = QLabel(self.gb_galvo_diag)
        self.label159.setObjectName(u"label159")

        self.formLayout11.setWidget(3, QFormLayout.FieldRole, self.label159)

        self.label160 = QLabel(self.gb_galvo_diag)
        self.label160.setObjectName(u"label160")

        self.formLayout11.setWidget(4, QFormLayout.LabelRole, self.label160)

        self.label161 = QLabel(self.gb_galvo_diag)
        self.label161.setObjectName(u"label161")

        self.formLayout11.setWidget(4, QFormLayout.FieldRole, self.label161)

        self.label162 = QLabel(self.gb_galvo_diag)
        self.label162.setObjectName(u"label162")

        self.formLayout11.setWidget(5, QFormLayout.LabelRole, self.label162)

        self.label163 = QLabel(self.gb_galvo_diag)
        self.label163.setObjectName(u"label163")

        self.formLayout11.setWidget(5, QFormLayout.FieldRole, self.label163)


        self.hboxLayout32.addLayout(self.formLayout11)


        self.hboxLayout30.addWidget(self.gb_galvo_diag)

        self.gb_test_patterns = QGroupBox(self.page_laser_galvo)
        self.gb_test_patterns.setObjectName(u"gb_test_patterns")
        sizePolicy.setHeightForWidth(self.gb_test_patterns.sizePolicy().hasHeightForWidth())
        self.gb_test_patterns.setSizePolicy(sizePolicy)
        self.gridLayout3 = QGridLayout(self.gb_test_patterns)
        self.gridLayout3.setSpacing(4)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.pushButton52 = QPushButton(self.gb_test_patterns)
        self.pushButton52.setObjectName(u"pushButton52")
        self.pushButton52.setMinimumSize(QSize(0, 20))

        self.gridLayout3.addWidget(self.pushButton52, 0, 0, 1, 1)

        self.pushButton53 = QPushButton(self.gb_test_patterns)
        self.pushButton53.setObjectName(u"pushButton53")
        self.pushButton53.setMinimumSize(QSize(0, 20))

        self.gridLayout3.addWidget(self.pushButton53, 0, 1, 1, 1)

        self.pushButton54 = QPushButton(self.gb_test_patterns)
        self.pushButton54.setObjectName(u"pushButton54")
        self.pushButton54.setMinimumSize(QSize(0, 20))

        self.gridLayout3.addWidget(self.pushButton54, 1, 0, 1, 1)

        self.pushButton55 = QPushButton(self.gb_test_patterns)
        self.pushButton55.setObjectName(u"pushButton55")
        self.pushButton55.setMinimumSize(QSize(0, 20))

        self.gridLayout3.addWidget(self.pushButton55, 1, 1, 1, 1)

        self.pushButton56 = QPushButton(self.gb_test_patterns)
        self.pushButton56.setObjectName(u"pushButton56")
        self.pushButton56.setMinimumSize(QSize(0, 20))

        self.gridLayout3.addWidget(self.pushButton56, 2, 0, 1, 1)

        self.pushButton57 = QPushButton(self.gb_test_patterns)
        self.pushButton57.setObjectName(u"pushButton57")
        self.pushButton57.setMinimumSize(QSize(0, 20))

        self.gridLayout3.addWidget(self.pushButton57, 2, 1, 1, 1)


        self.hboxLayout30.addWidget(self.gb_test_patterns)

        self.gb_pattern_settings = QGroupBox(self.page_laser_galvo)
        self.gb_pattern_settings.setObjectName(u"gb_pattern_settings")
        sizePolicy.setHeightForWidth(self.gb_pattern_settings.sizePolicy().hasHeightForWidth())
        self.gb_pattern_settings.setSizePolicy(sizePolicy)
        self.vboxLayout23 = QVBoxLayout(self.gb_pattern_settings)
        self.vboxLayout23.setSpacing(4)
        self.vboxLayout23.setObjectName(u"vboxLayout23")
        self.formLayout12 = QFormLayout()
        self.formLayout12.setObjectName(u"formLayout12")
        self.formLayout12.setHorizontalSpacing(4)
        self.formLayout12.setVerticalSpacing(4)
        self.label164 = QLabel(self.gb_pattern_settings)
        self.label164.setObjectName(u"label164")

        self.formLayout12.setWidget(0, QFormLayout.LabelRole, self.label164)

        self.lineEdit5 = QLineEdit(self.gb_pattern_settings)
        self.lineEdit5.setObjectName(u"lineEdit5")

        self.formLayout12.setWidget(0, QFormLayout.FieldRole, self.lineEdit5)

        self.label165 = QLabel(self.gb_pattern_settings)
        self.label165.setObjectName(u"label165")

        self.formLayout12.setWidget(1, QFormLayout.LabelRole, self.label165)

        self.lineEdit6 = QLineEdit(self.gb_pattern_settings)
        self.lineEdit6.setObjectName(u"lineEdit6")

        self.formLayout12.setWidget(1, QFormLayout.FieldRole, self.lineEdit6)

        self.label166 = QLabel(self.gb_pattern_settings)
        self.label166.setObjectName(u"label166")

        self.formLayout12.setWidget(2, QFormLayout.LabelRole, self.label166)

        self.lineEdit7 = QLineEdit(self.gb_pattern_settings)
        self.lineEdit7.setObjectName(u"lineEdit7")

        self.formLayout12.setWidget(2, QFormLayout.FieldRole, self.lineEdit7)

        self.label167 = QLabel(self.gb_pattern_settings)
        self.label167.setObjectName(u"label167")

        self.formLayout12.setWidget(3, QFormLayout.LabelRole, self.label167)

        self.lineEdit8 = QLineEdit(self.gb_pattern_settings)
        self.lineEdit8.setObjectName(u"lineEdit8")

        self.formLayout12.setWidget(3, QFormLayout.FieldRole, self.lineEdit8)


        self.vboxLayout23.addLayout(self.formLayout12)

        self.pushButton58 = QPushButton(self.gb_pattern_settings)
        self.pushButton58.setObjectName(u"pushButton58")
        self.pushButton58.setMinimumSize(QSize(0, 20))

        self.vboxLayout23.addWidget(self.pushButton58)


        self.hboxLayout30.addWidget(self.gb_pattern_settings)


        self.vLayout_laser_galvo.addLayout(self.hboxLayout30)

        self.gb_calibration = QGroupBox(self.page_laser_galvo)
        self.gb_calibration.setObjectName(u"gb_calibration")
        sizePolicy.setHeightForWidth(self.gb_calibration.sizePolicy().hasHeightForWidth())
        self.gb_calibration.setSizePolicy(sizePolicy)
        self.hboxLayout33 = QHBoxLayout(self.gb_calibration)
        self.hboxLayout33.setSpacing(4)
        self.hboxLayout33.setObjectName(u"hboxLayout33")
        self.vboxLayout24 = QVBoxLayout()
        self.vboxLayout24.setSpacing(4)
        self.vboxLayout24.setObjectName(u"vboxLayout24")
        self.label168 = QLabel(self.gb_calibration)
        self.label168.setObjectName(u"label168")

        self.vboxLayout24.addWidget(self.label168)

        self.pushButton59 = QPushButton(self.gb_calibration)
        self.pushButton59.setObjectName(u"pushButton59")
        self.pushButton59.setMinimumSize(QSize(0, 20))

        self.vboxLayout24.addWidget(self.pushButton59)

        self.pushButton60 = QPushButton(self.gb_calibration)
        self.pushButton60.setObjectName(u"pushButton60")
        self.pushButton60.setMinimumSize(QSize(0, 20))

        self.vboxLayout24.addWidget(self.pushButton60)


        self.hboxLayout33.addLayout(self.vboxLayout24)

        self.label169 = QLabel(self.gb_calibration)
        self.label169.setObjectName(u"label169")
        self.label169.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hboxLayout33.addWidget(self.label169)

        self.vboxLayout25 = QVBoxLayout()
        self.vboxLayout25.setSpacing(4)
        self.vboxLayout25.setObjectName(u"vboxLayout25")
        self.label170 = QLabel(self.gb_calibration)
        self.label170.setObjectName(u"label170")

        self.vboxLayout25.addWidget(self.label170)

        self.pushButton61 = QPushButton(self.gb_calibration)
        self.pushButton61.setObjectName(u"pushButton61")
        self.pushButton61.setMinimumSize(QSize(0, 20))

        self.vboxLayout25.addWidget(self.pushButton61)

        self.pushButton62 = QPushButton(self.gb_calibration)
        self.pushButton62.setObjectName(u"pushButton62")
        self.pushButton62.setMinimumSize(QSize(0, 20))

        self.vboxLayout25.addWidget(self.pushButton62)


        self.hboxLayout33.addLayout(self.vboxLayout25)

        self.label171 = QLabel(self.gb_calibration)
        self.label171.setObjectName(u"label171")
        self.label171.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hboxLayout33.addWidget(self.label171)

        self.vboxLayout26 = QVBoxLayout()
        self.vboxLayout26.setSpacing(4)
        self.vboxLayout26.setObjectName(u"vboxLayout26")
        self.label172 = QLabel(self.gb_calibration)
        self.label172.setObjectName(u"label172")

        self.vboxLayout26.addWidget(self.label172)

        self.pushButton63 = QPushButton(self.gb_calibration)
        self.pushButton63.setObjectName(u"pushButton63")
        self.pushButton63.setMinimumSize(QSize(0, 20))

        self.vboxLayout26.addWidget(self.pushButton63)

        self.pushButton64 = QPushButton(self.gb_calibration)
        self.pushButton64.setObjectName(u"pushButton64")
        self.pushButton64.setMinimumSize(QSize(0, 20))

        self.vboxLayout26.addWidget(self.pushButton64)


        self.hboxLayout33.addLayout(self.vboxLayout26)

        self.label173 = QLabel(self.gb_calibration)
        self.label173.setObjectName(u"label173")
        self.label173.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hboxLayout33.addWidget(self.label173)

        self.vboxLayout27 = QVBoxLayout()
        self.vboxLayout27.setSpacing(4)
        self.vboxLayout27.setObjectName(u"vboxLayout27")
        self.label174 = QLabel(self.gb_calibration)
        self.label174.setObjectName(u"label174")

        self.vboxLayout27.addWidget(self.label174)

        self.formLayout13 = QFormLayout()
        self.formLayout13.setObjectName(u"formLayout13")
        self.formLayout13.setHorizontalSpacing(4)
        self.formLayout13.setVerticalSpacing(4)
        self.label175 = QLabel(self.gb_calibration)
        self.label175.setObjectName(u"label175")

        self.formLayout13.setWidget(0, QFormLayout.LabelRole, self.label175)

        self.label176 = QLabel(self.gb_calibration)
        self.label176.setObjectName(u"label176")

        self.formLayout13.setWidget(0, QFormLayout.FieldRole, self.label176)

        self.label177 = QLabel(self.gb_calibration)
        self.label177.setObjectName(u"label177")

        self.formLayout13.setWidget(1, QFormLayout.LabelRole, self.label177)

        self.label178 = QLabel(self.gb_calibration)
        self.label178.setObjectName(u"label178")

        self.formLayout13.setWidget(1, QFormLayout.FieldRole, self.label178)

        self.label179 = QLabel(self.gb_calibration)
        self.label179.setObjectName(u"label179")

        self.formLayout13.setWidget(2, QFormLayout.LabelRole, self.label179)

        self.label180 = QLabel(self.gb_calibration)
        self.label180.setObjectName(u"label180")

        self.formLayout13.setWidget(2, QFormLayout.FieldRole, self.label180)


        self.vboxLayout27.addLayout(self.formLayout13)


        self.hboxLayout33.addLayout(self.vboxLayout27)


        self.vLayout_laser_galvo.addWidget(self.gb_calibration)

        self.stackedWidget.addWidget(self.page_laser_galvo)
        self.page_motors = QWidget()
        self.page_motors.setObjectName(u"page_motors")
        self.vLayout_motors = QVBoxLayout(self.page_motors)
        self.vLayout_motors.setSpacing(4)
        self.vLayout_motors.setObjectName(u"vLayout_motors")
        self.hboxLayout34 = QHBoxLayout()
        self.hboxLayout34.setSpacing(4)
        self.hboxLayout34.setObjectName(u"hboxLayout34")
        self.gb_motor_build = QGroupBox(self.page_motors)
        self.gb_motor_build.setObjectName(u"gb_motor_build")
        sizePolicy.setHeightForWidth(self.gb_motor_build.sizePolicy().hasHeightForWidth())
        self.gb_motor_build.setSizePolicy(sizePolicy)
        self.vboxLayout28 = QVBoxLayout(self.gb_motor_build)
        self.vboxLayout28.setSpacing(4)
        self.vboxLayout28.setObjectName(u"vboxLayout28")
        self.hboxLayout35 = QHBoxLayout()
        self.hboxLayout35.setSpacing(4)
        self.hboxLayout35.setObjectName(u"hboxLayout35")
        self.label181 = QLabel(self.gb_motor_build)
        self.label181.setObjectName(u"label181")

        self.hboxLayout35.addWidget(self.label181)

        self.formLayout14 = QFormLayout()
        self.formLayout14.setObjectName(u"formLayout14")
        self.formLayout14.setHorizontalSpacing(4)
        self.formLayout14.setVerticalSpacing(4)
        self.label182 = QLabel(self.gb_motor_build)
        self.label182.setObjectName(u"label182")

        self.formLayout14.setWidget(0, QFormLayout.LabelRole, self.label182)

        self.label183 = QLabel(self.gb_motor_build)
        self.label183.setObjectName(u"label183")

        self.formLayout14.setWidget(0, QFormLayout.FieldRole, self.label183)

        self.label184 = QLabel(self.gb_motor_build)
        self.label184.setObjectName(u"label184")

        self.formLayout14.setWidget(1, QFormLayout.LabelRole, self.label184)

        self.label185 = QLabel(self.gb_motor_build)
        self.label185.setObjectName(u"label185")

        self.formLayout14.setWidget(1, QFormLayout.FieldRole, self.label185)

        self.label186 = QLabel(self.gb_motor_build)
        self.label186.setObjectName(u"label186")

        self.formLayout14.setWidget(2, QFormLayout.LabelRole, self.label186)

        self.label187 = QLabel(self.gb_motor_build)
        self.label187.setObjectName(u"label187")

        self.formLayout14.setWidget(2, QFormLayout.FieldRole, self.label187)

        self.label188 = QLabel(self.gb_motor_build)
        self.label188.setObjectName(u"label188")

        self.formLayout14.setWidget(3, QFormLayout.LabelRole, self.label188)

        self.label189 = QLabel(self.gb_motor_build)
        self.label189.setObjectName(u"label189")

        self.formLayout14.setWidget(3, QFormLayout.FieldRole, self.label189)

        self.label190 = QLabel(self.gb_motor_build)
        self.label190.setObjectName(u"label190")

        self.formLayout14.setWidget(4, QFormLayout.LabelRole, self.label190)

        self.label191 = QLabel(self.gb_motor_build)
        self.label191.setObjectName(u"label191")

        self.formLayout14.setWidget(4, QFormLayout.FieldRole, self.label191)


        self.hboxLayout35.addLayout(self.formLayout14)


        self.vboxLayout28.addLayout(self.hboxLayout35)

        self.label192 = QLabel(self.gb_motor_build)
        self.label192.setObjectName(u"label192")

        self.vboxLayout28.addWidget(self.label192)

        self.hboxLayout36 = QHBoxLayout()
        self.hboxLayout36.setSpacing(4)
        self.hboxLayout36.setObjectName(u"hboxLayout36")
        self.pushButton65 = QPushButton(self.gb_motor_build)
        self.pushButton65.setObjectName(u"pushButton65")
        self.pushButton65.setMinimumSize(QSize(0, 20))

        self.hboxLayout36.addWidget(self.pushButton65)

        self.pushButton66 = QPushButton(self.gb_motor_build)
        self.pushButton66.setObjectName(u"pushButton66")
        self.pushButton66.setMinimumSize(QSize(0, 20))

        self.hboxLayout36.addWidget(self.pushButton66)

        self.pushButton67 = QPushButton(self.gb_motor_build)
        self.pushButton67.setObjectName(u"pushButton67")
        self.pushButton67.setMinimumSize(QSize(0, 20))

        self.hboxLayout36.addWidget(self.pushButton67)


        self.vboxLayout28.addLayout(self.hboxLayout36)

        self.label193 = QLabel(self.gb_motor_build)
        self.label193.setObjectName(u"label193")

        self.vboxLayout28.addWidget(self.label193)

        self.hboxLayout37 = QHBoxLayout()
        self.hboxLayout37.setSpacing(4)
        self.hboxLayout37.setObjectName(u"hboxLayout37")
        self.pushButton68 = QPushButton(self.gb_motor_build)
        self.pushButton68.setObjectName(u"pushButton68")
        self.pushButton68.setMinimumSize(QSize(0, 20))

        self.hboxLayout37.addWidget(self.pushButton68)

        self.pushButton69 = QPushButton(self.gb_motor_build)
        self.pushButton69.setObjectName(u"pushButton69")
        self.pushButton69.setMinimumSize(QSize(0, 20))

        self.hboxLayout37.addWidget(self.pushButton69)

        self.pushButton70 = QPushButton(self.gb_motor_build)
        self.pushButton70.setObjectName(u"pushButton70")
        self.pushButton70.setMinimumSize(QSize(0, 20))

        self.hboxLayout37.addWidget(self.pushButton70)

        self.pushButton71 = QPushButton(self.gb_motor_build)
        self.pushButton71.setObjectName(u"pushButton71")
        self.pushButton71.setMinimumSize(QSize(0, 20))

        self.hboxLayout37.addWidget(self.pushButton71)


        self.vboxLayout28.addLayout(self.hboxLayout37)


        self.hboxLayout34.addWidget(self.gb_motor_build)

        self.gb_motor_powder = QGroupBox(self.page_motors)
        self.gb_motor_powder.setObjectName(u"gb_motor_powder")
        sizePolicy.setHeightForWidth(self.gb_motor_powder.sizePolicy().hasHeightForWidth())
        self.gb_motor_powder.setSizePolicy(sizePolicy)
        self.vboxLayout29 = QVBoxLayout(self.gb_motor_powder)
        self.vboxLayout29.setSpacing(4)
        self.vboxLayout29.setObjectName(u"vboxLayout29")
        self.hboxLayout38 = QHBoxLayout()
        self.hboxLayout38.setSpacing(4)
        self.hboxLayout38.setObjectName(u"hboxLayout38")
        self.label194 = QLabel(self.gb_motor_powder)
        self.label194.setObjectName(u"label194")

        self.hboxLayout38.addWidget(self.label194)

        self.formLayout15 = QFormLayout()
        self.formLayout15.setObjectName(u"formLayout15")
        self.formLayout15.setHorizontalSpacing(4)
        self.formLayout15.setVerticalSpacing(4)
        self.label195 = QLabel(self.gb_motor_powder)
        self.label195.setObjectName(u"label195")

        self.formLayout15.setWidget(0, QFormLayout.LabelRole, self.label195)

        self.label196 = QLabel(self.gb_motor_powder)
        self.label196.setObjectName(u"label196")

        self.formLayout15.setWidget(0, QFormLayout.FieldRole, self.label196)

        self.label197 = QLabel(self.gb_motor_powder)
        self.label197.setObjectName(u"label197")

        self.formLayout15.setWidget(1, QFormLayout.LabelRole, self.label197)

        self.label198 = QLabel(self.gb_motor_powder)
        self.label198.setObjectName(u"label198")

        self.formLayout15.setWidget(1, QFormLayout.FieldRole, self.label198)

        self.label199 = QLabel(self.gb_motor_powder)
        self.label199.setObjectName(u"label199")

        self.formLayout15.setWidget(2, QFormLayout.LabelRole, self.label199)

        self.label200 = QLabel(self.gb_motor_powder)
        self.label200.setObjectName(u"label200")

        self.formLayout15.setWidget(2, QFormLayout.FieldRole, self.label200)

        self.label201 = QLabel(self.gb_motor_powder)
        self.label201.setObjectName(u"label201")

        self.formLayout15.setWidget(3, QFormLayout.LabelRole, self.label201)

        self.label202 = QLabel(self.gb_motor_powder)
        self.label202.setObjectName(u"label202")

        self.formLayout15.setWidget(3, QFormLayout.FieldRole, self.label202)

        self.label203 = QLabel(self.gb_motor_powder)
        self.label203.setObjectName(u"label203")

        self.formLayout15.setWidget(4, QFormLayout.LabelRole, self.label203)

        self.label204 = QLabel(self.gb_motor_powder)
        self.label204.setObjectName(u"label204")

        self.formLayout15.setWidget(4, QFormLayout.FieldRole, self.label204)


        self.hboxLayout38.addLayout(self.formLayout15)


        self.vboxLayout29.addLayout(self.hboxLayout38)

        self.label205 = QLabel(self.gb_motor_powder)
        self.label205.setObjectName(u"label205")

        self.vboxLayout29.addWidget(self.label205)

        self.hboxLayout39 = QHBoxLayout()
        self.hboxLayout39.setSpacing(4)
        self.hboxLayout39.setObjectName(u"hboxLayout39")
        self.pushButton72 = QPushButton(self.gb_motor_powder)
        self.pushButton72.setObjectName(u"pushButton72")
        self.pushButton72.setMinimumSize(QSize(0, 20))

        self.hboxLayout39.addWidget(self.pushButton72)

        self.pushButton73 = QPushButton(self.gb_motor_powder)
        self.pushButton73.setObjectName(u"pushButton73")
        self.pushButton73.setMinimumSize(QSize(0, 20))

        self.hboxLayout39.addWidget(self.pushButton73)

        self.pushButton74 = QPushButton(self.gb_motor_powder)
        self.pushButton74.setObjectName(u"pushButton74")
        self.pushButton74.setMinimumSize(QSize(0, 20))

        self.hboxLayout39.addWidget(self.pushButton74)


        self.vboxLayout29.addLayout(self.hboxLayout39)

        self.label206 = QLabel(self.gb_motor_powder)
        self.label206.setObjectName(u"label206")

        self.vboxLayout29.addWidget(self.label206)

        self.hboxLayout40 = QHBoxLayout()
        self.hboxLayout40.setSpacing(4)
        self.hboxLayout40.setObjectName(u"hboxLayout40")
        self.pushButton75 = QPushButton(self.gb_motor_powder)
        self.pushButton75.setObjectName(u"pushButton75")
        self.pushButton75.setMinimumSize(QSize(0, 20))

        self.hboxLayout40.addWidget(self.pushButton75)

        self.pushButton76 = QPushButton(self.gb_motor_powder)
        self.pushButton76.setObjectName(u"pushButton76")
        self.pushButton76.setMinimumSize(QSize(0, 20))

        self.hboxLayout40.addWidget(self.pushButton76)

        self.pushButton77 = QPushButton(self.gb_motor_powder)
        self.pushButton77.setObjectName(u"pushButton77")
        self.pushButton77.setMinimumSize(QSize(0, 20))

        self.hboxLayout40.addWidget(self.pushButton77)

        self.pushButton78 = QPushButton(self.gb_motor_powder)
        self.pushButton78.setObjectName(u"pushButton78")
        self.pushButton78.setMinimumSize(QSize(0, 20))

        self.hboxLayout40.addWidget(self.pushButton78)


        self.vboxLayout29.addLayout(self.hboxLayout40)


        self.hboxLayout34.addWidget(self.gb_motor_powder)

        self.gb_motor_recoater = QGroupBox(self.page_motors)
        self.gb_motor_recoater.setObjectName(u"gb_motor_recoater")
        sizePolicy.setHeightForWidth(self.gb_motor_recoater.sizePolicy().hasHeightForWidth())
        self.gb_motor_recoater.setSizePolicy(sizePolicy)
        self.vboxLayout30 = QVBoxLayout(self.gb_motor_recoater)
        self.vboxLayout30.setSpacing(4)
        self.vboxLayout30.setObjectName(u"vboxLayout30")
        self.hboxLayout41 = QHBoxLayout()
        self.hboxLayout41.setSpacing(4)
        self.hboxLayout41.setObjectName(u"hboxLayout41")
        self.label207 = QLabel(self.gb_motor_recoater)
        self.label207.setObjectName(u"label207")

        self.hboxLayout41.addWidget(self.label207)

        self.formLayout16 = QFormLayout()
        self.formLayout16.setObjectName(u"formLayout16")
        self.formLayout16.setHorizontalSpacing(4)
        self.formLayout16.setVerticalSpacing(4)
        self.label208 = QLabel(self.gb_motor_recoater)
        self.label208.setObjectName(u"label208")

        self.formLayout16.setWidget(0, QFormLayout.LabelRole, self.label208)

        self.label209 = QLabel(self.gb_motor_recoater)
        self.label209.setObjectName(u"label209")

        self.formLayout16.setWidget(0, QFormLayout.FieldRole, self.label209)

        self.label210 = QLabel(self.gb_motor_recoater)
        self.label210.setObjectName(u"label210")

        self.formLayout16.setWidget(1, QFormLayout.LabelRole, self.label210)

        self.label211 = QLabel(self.gb_motor_recoater)
        self.label211.setObjectName(u"label211")

        self.formLayout16.setWidget(1, QFormLayout.FieldRole, self.label211)

        self.label212 = QLabel(self.gb_motor_recoater)
        self.label212.setObjectName(u"label212")

        self.formLayout16.setWidget(2, QFormLayout.LabelRole, self.label212)

        self.label213 = QLabel(self.gb_motor_recoater)
        self.label213.setObjectName(u"label213")

        self.formLayout16.setWidget(2, QFormLayout.FieldRole, self.label213)

        self.label214 = QLabel(self.gb_motor_recoater)
        self.label214.setObjectName(u"label214")

        self.formLayout16.setWidget(3, QFormLayout.LabelRole, self.label214)

        self.label215 = QLabel(self.gb_motor_recoater)
        self.label215.setObjectName(u"label215")

        self.formLayout16.setWidget(3, QFormLayout.FieldRole, self.label215)

        self.label216 = QLabel(self.gb_motor_recoater)
        self.label216.setObjectName(u"label216")

        self.formLayout16.setWidget(4, QFormLayout.LabelRole, self.label216)

        self.label217 = QLabel(self.gb_motor_recoater)
        self.label217.setObjectName(u"label217")

        self.formLayout16.setWidget(4, QFormLayout.FieldRole, self.label217)


        self.hboxLayout41.addLayout(self.formLayout16)


        self.vboxLayout30.addLayout(self.hboxLayout41)

        self.label218 = QLabel(self.gb_motor_recoater)
        self.label218.setObjectName(u"label218")

        self.vboxLayout30.addWidget(self.label218)

        self.hboxLayout42 = QHBoxLayout()
        self.hboxLayout42.setSpacing(4)
        self.hboxLayout42.setObjectName(u"hboxLayout42")
        self.pushButton79 = QPushButton(self.gb_motor_recoater)
        self.pushButton79.setObjectName(u"pushButton79")
        self.pushButton79.setMinimumSize(QSize(0, 20))

        self.hboxLayout42.addWidget(self.pushButton79)

        self.pushButton80 = QPushButton(self.gb_motor_recoater)
        self.pushButton80.setObjectName(u"pushButton80")
        self.pushButton80.setMinimumSize(QSize(0, 20))

        self.hboxLayout42.addWidget(self.pushButton80)

        self.pushButton81 = QPushButton(self.gb_motor_recoater)
        self.pushButton81.setObjectName(u"pushButton81")
        self.pushButton81.setMinimumSize(QSize(0, 20))

        self.hboxLayout42.addWidget(self.pushButton81)


        self.vboxLayout30.addLayout(self.hboxLayout42)

        self.label219 = QLabel(self.gb_motor_recoater)
        self.label219.setObjectName(u"label219")

        self.vboxLayout30.addWidget(self.label219)

        self.hboxLayout43 = QHBoxLayout()
        self.hboxLayout43.setSpacing(4)
        self.hboxLayout43.setObjectName(u"hboxLayout43")
        self.pushButton82 = QPushButton(self.gb_motor_recoater)
        self.pushButton82.setObjectName(u"pushButton82")
        self.pushButton82.setMinimumSize(QSize(0, 20))

        self.hboxLayout43.addWidget(self.pushButton82)

        self.pushButton83 = QPushButton(self.gb_motor_recoater)
        self.pushButton83.setObjectName(u"pushButton83")
        self.pushButton83.setMinimumSize(QSize(0, 20))

        self.hboxLayout43.addWidget(self.pushButton83)

        self.pushButton84 = QPushButton(self.gb_motor_recoater)
        self.pushButton84.setObjectName(u"pushButton84")
        self.pushButton84.setMinimumSize(QSize(0, 20))

        self.hboxLayout43.addWidget(self.pushButton84)

        self.pushButton85 = QPushButton(self.gb_motor_recoater)
        self.pushButton85.setObjectName(u"pushButton85")
        self.pushButton85.setMinimumSize(QSize(0, 20))

        self.hboxLayout43.addWidget(self.pushButton85)


        self.vboxLayout30.addLayout(self.hboxLayout43)


        self.hboxLayout34.addWidget(self.gb_motor_recoater)

        self.gb_motor_piston = QGroupBox(self.page_motors)
        self.gb_motor_piston.setObjectName(u"gb_motor_piston")
        sizePolicy.setHeightForWidth(self.gb_motor_piston.sizePolicy().hasHeightForWidth())
        self.gb_motor_piston.setSizePolicy(sizePolicy)
        self.vboxLayout31 = QVBoxLayout(self.gb_motor_piston)
        self.vboxLayout31.setSpacing(4)
        self.vboxLayout31.setObjectName(u"vboxLayout31")
        self.hboxLayout44 = QHBoxLayout()
        self.hboxLayout44.setSpacing(4)
        self.hboxLayout44.setObjectName(u"hboxLayout44")
        self.label220 = QLabel(self.gb_motor_piston)
        self.label220.setObjectName(u"label220")

        self.hboxLayout44.addWidget(self.label220)

        self.formLayout17 = QFormLayout()
        self.formLayout17.setObjectName(u"formLayout17")
        self.formLayout17.setHorizontalSpacing(4)
        self.formLayout17.setVerticalSpacing(4)
        self.label221 = QLabel(self.gb_motor_piston)
        self.label221.setObjectName(u"label221")

        self.formLayout17.setWidget(0, QFormLayout.LabelRole, self.label221)

        self.label222 = QLabel(self.gb_motor_piston)
        self.label222.setObjectName(u"label222")

        self.formLayout17.setWidget(0, QFormLayout.FieldRole, self.label222)

        self.label223 = QLabel(self.gb_motor_piston)
        self.label223.setObjectName(u"label223")

        self.formLayout17.setWidget(1, QFormLayout.LabelRole, self.label223)

        self.label224 = QLabel(self.gb_motor_piston)
        self.label224.setObjectName(u"label224")

        self.formLayout17.setWidget(1, QFormLayout.FieldRole, self.label224)

        self.label225 = QLabel(self.gb_motor_piston)
        self.label225.setObjectName(u"label225")

        self.formLayout17.setWidget(2, QFormLayout.LabelRole, self.label225)

        self.label226 = QLabel(self.gb_motor_piston)
        self.label226.setObjectName(u"label226")

        self.formLayout17.setWidget(2, QFormLayout.FieldRole, self.label226)

        self.label227 = QLabel(self.gb_motor_piston)
        self.label227.setObjectName(u"label227")

        self.formLayout17.setWidget(3, QFormLayout.LabelRole, self.label227)

        self.label228 = QLabel(self.gb_motor_piston)
        self.label228.setObjectName(u"label228")

        self.formLayout17.setWidget(3, QFormLayout.FieldRole, self.label228)

        self.label229 = QLabel(self.gb_motor_piston)
        self.label229.setObjectName(u"label229")

        self.formLayout17.setWidget(4, QFormLayout.LabelRole, self.label229)

        self.label230 = QLabel(self.gb_motor_piston)
        self.label230.setObjectName(u"label230")

        self.formLayout17.setWidget(4, QFormLayout.FieldRole, self.label230)


        self.hboxLayout44.addLayout(self.formLayout17)


        self.vboxLayout31.addLayout(self.hboxLayout44)

        self.label231 = QLabel(self.gb_motor_piston)
        self.label231.setObjectName(u"label231")

        self.vboxLayout31.addWidget(self.label231)

        self.hboxLayout45 = QHBoxLayout()
        self.hboxLayout45.setSpacing(4)
        self.hboxLayout45.setObjectName(u"hboxLayout45")
        self.pushButton86 = QPushButton(self.gb_motor_piston)
        self.pushButton86.setObjectName(u"pushButton86")
        self.pushButton86.setMinimumSize(QSize(0, 20))

        self.hboxLayout45.addWidget(self.pushButton86)

        self.pushButton87 = QPushButton(self.gb_motor_piston)
        self.pushButton87.setObjectName(u"pushButton87")
        self.pushButton87.setMinimumSize(QSize(0, 20))

        self.hboxLayout45.addWidget(self.pushButton87)

        self.pushButton88 = QPushButton(self.gb_motor_piston)
        self.pushButton88.setObjectName(u"pushButton88")
        self.pushButton88.setMinimumSize(QSize(0, 20))

        self.hboxLayout45.addWidget(self.pushButton88)


        self.vboxLayout31.addLayout(self.hboxLayout45)

        self.label232 = QLabel(self.gb_motor_piston)
        self.label232.setObjectName(u"label232")

        self.vboxLayout31.addWidget(self.label232)

        self.hboxLayout46 = QHBoxLayout()
        self.hboxLayout46.setSpacing(4)
        self.hboxLayout46.setObjectName(u"hboxLayout46")
        self.pushButton89 = QPushButton(self.gb_motor_piston)
        self.pushButton89.setObjectName(u"pushButton89")
        self.pushButton89.setMinimumSize(QSize(0, 20))

        self.hboxLayout46.addWidget(self.pushButton89)

        self.pushButton90 = QPushButton(self.gb_motor_piston)
        self.pushButton90.setObjectName(u"pushButton90")
        self.pushButton90.setMinimumSize(QSize(0, 20))

        self.hboxLayout46.addWidget(self.pushButton90)

        self.pushButton91 = QPushButton(self.gb_motor_piston)
        self.pushButton91.setObjectName(u"pushButton91")
        self.pushButton91.setMinimumSize(QSize(0, 20))

        self.hboxLayout46.addWidget(self.pushButton91)

        self.pushButton92 = QPushButton(self.gb_motor_piston)
        self.pushButton92.setObjectName(u"pushButton92")
        self.pushButton92.setMinimumSize(QSize(0, 20))

        self.hboxLayout46.addWidget(self.pushButton92)


        self.vboxLayout31.addLayout(self.hboxLayout46)


        self.hboxLayout34.addWidget(self.gb_motor_piston)


        self.vLayout_motors.addLayout(self.hboxLayout34)

        self.hboxLayout47 = QHBoxLayout()
        self.hboxLayout47.setSpacing(4)
        self.hboxLayout47.setObjectName(u"hboxLayout47")
        self.gb_motors_overview = QGroupBox(self.page_motors)
        self.gb_motors_overview.setObjectName(u"gb_motors_overview")
        sizePolicy.setHeightForWidth(self.gb_motors_overview.sizePolicy().hasHeightForWidth())
        self.gb_motors_overview.setSizePolicy(sizePolicy)
        self.vboxLayout32 = QVBoxLayout(self.gb_motors_overview)
        self.vboxLayout32.setSpacing(4)
        self.vboxLayout32.setObjectName(u"vboxLayout32")
        self.tableWidget = QTableWidget(self.gb_motors_overview)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setColumnCount(6)

        self.vboxLayout32.addWidget(self.tableWidget)


        self.hboxLayout47.addWidget(self.gb_motors_overview)

        self.gb_motor_diag = QGroupBox(self.page_motors)
        self.gb_motor_diag.setObjectName(u"gb_motor_diag")
        sizePolicy.setHeightForWidth(self.gb_motor_diag.sizePolicy().hasHeightForWidth())
        self.gb_motor_diag.setSizePolicy(sizePolicy)
        self.formLayout18 = QFormLayout(self.gb_motor_diag)
        self.formLayout18.setObjectName(u"formLayout18")
        self.formLayout18.setHorizontalSpacing(4)
        self.formLayout18.setVerticalSpacing(4)
        self.label233 = QLabel(self.gb_motor_diag)
        self.label233.setObjectName(u"label233")

        self.formLayout18.setWidget(0, QFormLayout.LabelRole, self.label233)

        self.label234 = QLabel(self.gb_motor_diag)
        self.label234.setObjectName(u"label234")

        self.formLayout18.setWidget(0, QFormLayout.FieldRole, self.label234)

        self.label235 = QLabel(self.gb_motor_diag)
        self.label235.setObjectName(u"label235")

        self.formLayout18.setWidget(1, QFormLayout.LabelRole, self.label235)

        self.label236 = QLabel(self.gb_motor_diag)
        self.label236.setObjectName(u"label236")

        self.formLayout18.setWidget(1, QFormLayout.FieldRole, self.label236)

        self.label237 = QLabel(self.gb_motor_diag)
        self.label237.setObjectName(u"label237")

        self.formLayout18.setWidget(2, QFormLayout.LabelRole, self.label237)

        self.label238 = QLabel(self.gb_motor_diag)
        self.label238.setObjectName(u"label238")

        self.formLayout18.setWidget(2, QFormLayout.FieldRole, self.label238)

        self.label239 = QLabel(self.gb_motor_diag)
        self.label239.setObjectName(u"label239")

        self.formLayout18.setWidget(3, QFormLayout.LabelRole, self.label239)

        self.label240 = QLabel(self.gb_motor_diag)
        self.label240.setObjectName(u"label240")

        self.formLayout18.setWidget(3, QFormLayout.FieldRole, self.label240)

        self.label241 = QLabel(self.gb_motor_diag)
        self.label241.setObjectName(u"label241")

        self.formLayout18.setWidget(4, QFormLayout.LabelRole, self.label241)

        self.label242 = QLabel(self.gb_motor_diag)
        self.label242.setObjectName(u"label242")

        self.formLayout18.setWidget(4, QFormLayout.FieldRole, self.label242)

        self.label243 = QLabel(self.gb_motor_diag)
        self.label243.setObjectName(u"label243")

        self.formLayout18.setWidget(5, QFormLayout.LabelRole, self.label243)

        self.label244 = QLabel(self.gb_motor_diag)
        self.label244.setObjectName(u"label244")

        self.formLayout18.setWidget(5, QFormLayout.FieldRole, self.label244)

        self.label245 = QLabel(self.gb_motor_diag)
        self.label245.setObjectName(u"label245")

        self.formLayout18.setWidget(6, QFormLayout.LabelRole, self.label245)

        self.label246 = QLabel(self.gb_motor_diag)
        self.label246.setObjectName(u"label246")

        self.formLayout18.setWidget(6, QFormLayout.FieldRole, self.label246)


        self.hboxLayout47.addWidget(self.gb_motor_diag)

        self.gb_motor_temp = QGroupBox(self.page_motors)
        self.gb_motor_temp.setObjectName(u"gb_motor_temp")
        sizePolicy.setHeightForWidth(self.gb_motor_temp.sizePolicy().hasHeightForWidth())
        self.gb_motor_temp.setSizePolicy(sizePolicy)
        self.formLayout19 = QFormLayout(self.gb_motor_temp)
        self.formLayout19.setObjectName(u"formLayout19")
        self.formLayout19.setHorizontalSpacing(4)
        self.formLayout19.setVerticalSpacing(4)
        self.label247 = QLabel(self.gb_motor_temp)
        self.label247.setObjectName(u"label247")

        self.formLayout19.setWidget(0, QFormLayout.LabelRole, self.label247)

        self.label248 = QLabel(self.gb_motor_temp)
        self.label248.setObjectName(u"label248")

        self.formLayout19.setWidget(0, QFormLayout.FieldRole, self.label248)

        self.label249 = QLabel(self.gb_motor_temp)
        self.label249.setObjectName(u"label249")

        self.formLayout19.setWidget(1, QFormLayout.LabelRole, self.label249)

        self.label250 = QLabel(self.gb_motor_temp)
        self.label250.setObjectName(u"label250")

        self.formLayout19.setWidget(1, QFormLayout.FieldRole, self.label250)

        self.label251 = QLabel(self.gb_motor_temp)
        self.label251.setObjectName(u"label251")

        self.formLayout19.setWidget(2, QFormLayout.LabelRole, self.label251)

        self.label252 = QLabel(self.gb_motor_temp)
        self.label252.setObjectName(u"label252")

        self.formLayout19.setWidget(2, QFormLayout.FieldRole, self.label252)

        self.label253 = QLabel(self.gb_motor_temp)
        self.label253.setObjectName(u"label253")

        self.formLayout19.setWidget(3, QFormLayout.LabelRole, self.label253)

        self.label254 = QLabel(self.gb_motor_temp)
        self.label254.setObjectName(u"label254")

        self.formLayout19.setWidget(3, QFormLayout.FieldRole, self.label254)

        self.label255 = QLabel(self.gb_motor_temp)
        self.label255.setObjectName(u"label255")

        self.formLayout19.setWidget(4, QFormLayout.LabelRole, self.label255)

        self.label256 = QLabel(self.gb_motor_temp)
        self.label256.setObjectName(u"label256")

        self.formLayout19.setWidget(4, QFormLayout.FieldRole, self.label256)


        self.hboxLayout47.addWidget(self.gb_motor_temp)

        self.gb_motor_actions = QGroupBox(self.page_motors)
        self.gb_motor_actions.setObjectName(u"gb_motor_actions")
        sizePolicy.setHeightForWidth(self.gb_motor_actions.sizePolicy().hasHeightForWidth())
        self.gb_motor_actions.setSizePolicy(sizePolicy)
        self.vboxLayout33 = QVBoxLayout(self.gb_motor_actions)
        self.vboxLayout33.setSpacing(4)
        self.vboxLayout33.setObjectName(u"vboxLayout33")
        self.pushButton93 = QPushButton(self.gb_motor_actions)
        self.pushButton93.setObjectName(u"pushButton93")
        self.pushButton93.setMinimumSize(QSize(0, 20))

        self.vboxLayout33.addWidget(self.pushButton93)

        self.pushButton94 = QPushButton(self.gb_motor_actions)
        self.pushButton94.setObjectName(u"pushButton94")
        self.pushButton94.setMinimumSize(QSize(0, 20))

        self.vboxLayout33.addWidget(self.pushButton94)

        self.pushButton95 = QPushButton(self.gb_motor_actions)
        self.pushButton95.setObjectName(u"pushButton95")
        self.pushButton95.setMinimumSize(QSize(0, 20))

        self.vboxLayout33.addWidget(self.pushButton95)

        self.pushButton96 = QPushButton(self.gb_motor_actions)
        self.pushButton96.setObjectName(u"pushButton96")
        self.pushButton96.setMinimumSize(QSize(0, 20))

        self.vboxLayout33.addWidget(self.pushButton96)


        self.hboxLayout47.addWidget(self.gb_motor_actions)


        self.vLayout_motors.addLayout(self.hboxLayout47)

        self.hboxLayout48 = QHBoxLayout()
        self.hboxLayout48.setSpacing(4)
        self.hboxLayout48.setObjectName(u"hboxLayout48")
        self.gb_motor_graph = QGroupBox(self.page_motors)
        self.gb_motor_graph.setObjectName(u"gb_motor_graph")
        sizePolicy.setHeightForWidth(self.gb_motor_graph.sizePolicy().hasHeightForWidth())
        self.gb_motor_graph.setSizePolicy(sizePolicy)
        self.vboxLayout34 = QVBoxLayout(self.gb_motor_graph)
        self.vboxLayout34.setSpacing(4)
        self.vboxLayout34.setObjectName(u"vboxLayout34")
        self.hboxLayout49 = QHBoxLayout()
        self.hboxLayout49.setSpacing(4)
        self.hboxLayout49.setObjectName(u"hboxLayout49")
        self.pushButton97 = QPushButton(self.gb_motor_graph)
        self.pushButton97.setObjectName(u"pushButton97")
        self.pushButton97.setMinimumSize(QSize(0, 20))

        self.hboxLayout49.addWidget(self.pushButton97)

        self.pushButton98 = QPushButton(self.gb_motor_graph)
        self.pushButton98.setObjectName(u"pushButton98")
        self.pushButton98.setMinimumSize(QSize(0, 20))

        self.hboxLayout49.addWidget(self.pushButton98)

        self.pushButton99 = QPushButton(self.gb_motor_graph)
        self.pushButton99.setObjectName(u"pushButton99")
        self.pushButton99.setMinimumSize(QSize(0, 20))

        self.hboxLayout49.addWidget(self.pushButton99)

        self.pushButton100 = QPushButton(self.gb_motor_graph)
        self.pushButton100.setObjectName(u"pushButton100")
        self.pushButton100.setMinimumSize(QSize(0, 20))

        self.hboxLayout49.addWidget(self.pushButton100)

        self.spacerItem10 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout49.addItem(self.spacerItem10)


        self.vboxLayout34.addLayout(self.hboxLayout49)

        self.label257 = QLabel(self.gb_motor_graph)
        self.label257.setObjectName(u"label257")
        self.label257.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout34.addWidget(self.label257)


        self.hboxLayout48.addWidget(self.gb_motor_graph)

        self.gb_graph_settings = QGroupBox(self.page_motors)
        self.gb_graph_settings.setObjectName(u"gb_graph_settings")
        sizePolicy.setHeightForWidth(self.gb_graph_settings.sizePolicy().hasHeightForWidth())
        self.gb_graph_settings.setSizePolicy(sizePolicy)
        self.formLayout20 = QFormLayout(self.gb_graph_settings)
        self.formLayout20.setObjectName(u"formLayout20")
        self.formLayout20.setHorizontalSpacing(4)
        self.formLayout20.setVerticalSpacing(4)
        self.label258 = QLabel(self.gb_graph_settings)
        self.label258.setObjectName(u"label258")

        self.formLayout20.setWidget(0, QFormLayout.LabelRole, self.label258)

        self.comboBox = QComboBox(self.gb_graph_settings)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout20.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.label259 = QLabel(self.gb_graph_settings)
        self.label259.setObjectName(u"label259")

        self.formLayout20.setWidget(1, QFormLayout.LabelRole, self.label259)

        self.checkBox4 = QCheckBox(self.gb_graph_settings)
        self.checkBox4.setObjectName(u"checkBox4")

        self.formLayout20.setWidget(1, QFormLayout.FieldRole, self.checkBox4)


        self.hboxLayout48.addWidget(self.gb_graph_settings)

        self.gb_motor_info = QGroupBox(self.page_motors)
        self.gb_motor_info.setObjectName(u"gb_motor_info")
        sizePolicy.setHeightForWidth(self.gb_motor_info.sizePolicy().hasHeightForWidth())
        self.gb_motor_info.setSizePolicy(sizePolicy)
        self.formLayout21 = QFormLayout(self.gb_motor_info)
        self.formLayout21.setObjectName(u"formLayout21")
        self.formLayout21.setHorizontalSpacing(4)
        self.formLayout21.setVerticalSpacing(4)
        self.label260 = QLabel(self.gb_motor_info)
        self.label260.setObjectName(u"label260")

        self.formLayout21.setWidget(0, QFormLayout.LabelRole, self.label260)

        self.label261 = QLabel(self.gb_motor_info)
        self.label261.setObjectName(u"label261")

        self.formLayout21.setWidget(0, QFormLayout.FieldRole, self.label261)

        self.label262 = QLabel(self.gb_motor_info)
        self.label262.setObjectName(u"label262")

        self.formLayout21.setWidget(1, QFormLayout.LabelRole, self.label262)

        self.label263 = QLabel(self.gb_motor_info)
        self.label263.setObjectName(u"label263")

        self.formLayout21.setWidget(1, QFormLayout.FieldRole, self.label263)

        self.label264 = QLabel(self.gb_motor_info)
        self.label264.setObjectName(u"label264")

        self.formLayout21.setWidget(2, QFormLayout.LabelRole, self.label264)

        self.label265 = QLabel(self.gb_motor_info)
        self.label265.setObjectName(u"label265")

        self.formLayout21.setWidget(2, QFormLayout.FieldRole, self.label265)

        self.label266 = QLabel(self.gb_motor_info)
        self.label266.setObjectName(u"label266")

        self.formLayout21.setWidget(3, QFormLayout.LabelRole, self.label266)

        self.label267 = QLabel(self.gb_motor_info)
        self.label267.setObjectName(u"label267")

        self.formLayout21.setWidget(3, QFormLayout.FieldRole, self.label267)

        self.label268 = QLabel(self.gb_motor_info)
        self.label268.setObjectName(u"label268")

        self.formLayout21.setWidget(4, QFormLayout.LabelRole, self.label268)

        self.label269 = QLabel(self.gb_motor_info)
        self.label269.setObjectName(u"label269")

        self.formLayout21.setWidget(4, QFormLayout.FieldRole, self.label269)


        self.hboxLayout48.addWidget(self.gb_motor_info)


        self.vLayout_motors.addLayout(self.hboxLayout48)

        self.stackedWidget.addWidget(self.page_motors)
        self.page_sensors = QWidget()
        self.page_sensors.setObjectName(u"page_sensors")
        self.vLayout_sensors = QVBoxLayout(self.page_sensors)
        self.vLayout_sensors.setSpacing(4)
        self.vLayout_sensors.setObjectName(u"vLayout_sensors")
        self.hboxLayout50 = QHBoxLayout()
        self.hboxLayout50.setSpacing(4)
        self.hboxLayout50.setObjectName(u"hboxLayout50")
        self.gb_env = QGroupBox(self.page_sensors)
        self.gb_env.setObjectName(u"gb_env")
        sizePolicy.setHeightForWidth(self.gb_env.sizePolicy().hasHeightForWidth())
        self.gb_env.setSizePolicy(sizePolicy)
        self.formLayout22 = QFormLayout(self.gb_env)
        self.formLayout22.setObjectName(u"formLayout22")
        self.formLayout22.setHorizontalSpacing(4)
        self.formLayout22.setVerticalSpacing(4)
        self.label270 = QLabel(self.gb_env)
        self.label270.setObjectName(u"label270")

        self.formLayout22.setWidget(0, QFormLayout.LabelRole, self.label270)

        self.label271 = QLabel(self.gb_env)
        self.label271.setObjectName(u"label271")

        self.formLayout22.setWidget(0, QFormLayout.FieldRole, self.label271)

        self.label272 = QLabel(self.gb_env)
        self.label272.setObjectName(u"label272")

        self.formLayout22.setWidget(1, QFormLayout.LabelRole, self.label272)

        self.label273 = QLabel(self.gb_env)
        self.label273.setObjectName(u"label273")

        self.formLayout22.setWidget(1, QFormLayout.FieldRole, self.label273)

        self.label274 = QLabel(self.gb_env)
        self.label274.setObjectName(u"label274")

        self.formLayout22.setWidget(2, QFormLayout.LabelRole, self.label274)

        self.label275 = QLabel(self.gb_env)
        self.label275.setObjectName(u"label275")

        self.formLayout22.setWidget(2, QFormLayout.FieldRole, self.label275)

        self.label276 = QLabel(self.gb_env)
        self.label276.setObjectName(u"label276")

        self.formLayout22.setWidget(3, QFormLayout.LabelRole, self.label276)

        self.label277 = QLabel(self.gb_env)
        self.label277.setObjectName(u"label277")

        self.formLayout22.setWidget(3, QFormLayout.FieldRole, self.label277)

        self.label278 = QLabel(self.gb_env)
        self.label278.setObjectName(u"label278")

        self.formLayout22.setWidget(4, QFormLayout.LabelRole, self.label278)

        self.label279 = QLabel(self.gb_env)
        self.label279.setObjectName(u"label279")

        self.formLayout22.setWidget(4, QFormLayout.FieldRole, self.label279)

        self.label280 = QLabel(self.gb_env)
        self.label280.setObjectName(u"label280")

        self.formLayout22.setWidget(5, QFormLayout.LabelRole, self.label280)

        self.label281 = QLabel(self.gb_env)
        self.label281.setObjectName(u"label281")

        self.formLayout22.setWidget(5, QFormLayout.FieldRole, self.label281)


        self.hboxLayout50.addWidget(self.gb_env)

        self.gb_gas = QGroupBox(self.page_sensors)
        self.gb_gas.setObjectName(u"gb_gas")
        sizePolicy.setHeightForWidth(self.gb_gas.sizePolicy().hasHeightForWidth())
        self.gb_gas.setSizePolicy(sizePolicy)
        self.formLayout23 = QFormLayout(self.gb_gas)
        self.formLayout23.setObjectName(u"formLayout23")
        self.formLayout23.setHorizontalSpacing(4)
        self.formLayout23.setVerticalSpacing(4)
        self.label282 = QLabel(self.gb_gas)
        self.label282.setObjectName(u"label282")

        self.formLayout23.setWidget(0, QFormLayout.LabelRole, self.label282)

        self.label283 = QLabel(self.gb_gas)
        self.label283.setObjectName(u"label283")

        self.formLayout23.setWidget(0, QFormLayout.FieldRole, self.label283)

        self.label284 = QLabel(self.gb_gas)
        self.label284.setObjectName(u"label284")

        self.formLayout23.setWidget(1, QFormLayout.LabelRole, self.label284)

        self.label285 = QLabel(self.gb_gas)
        self.label285.setObjectName(u"label285")

        self.formLayout23.setWidget(1, QFormLayout.FieldRole, self.label285)

        self.label286 = QLabel(self.gb_gas)
        self.label286.setObjectName(u"label286")

        self.formLayout23.setWidget(2, QFormLayout.LabelRole, self.label286)

        self.label287 = QLabel(self.gb_gas)
        self.label287.setObjectName(u"label287")

        self.formLayout23.setWidget(2, QFormLayout.FieldRole, self.label287)

        self.label288 = QLabel(self.gb_gas)
        self.label288.setObjectName(u"label288")

        self.formLayout23.setWidget(3, QFormLayout.LabelRole, self.label288)

        self.label289 = QLabel(self.gb_gas)
        self.label289.setObjectName(u"label289")

        self.formLayout23.setWidget(3, QFormLayout.FieldRole, self.label289)

        self.label290 = QLabel(self.gb_gas)
        self.label290.setObjectName(u"label290")

        self.formLayout23.setWidget(4, QFormLayout.LabelRole, self.label290)

        self.label291 = QLabel(self.gb_gas)
        self.label291.setObjectName(u"label291")

        self.formLayout23.setWidget(4, QFormLayout.FieldRole, self.label291)

        self.label292 = QLabel(self.gb_gas)
        self.label292.setObjectName(u"label292")

        self.formLayout23.setWidget(5, QFormLayout.LabelRole, self.label292)

        self.label293 = QLabel(self.gb_gas)
        self.label293.setObjectName(u"label293")

        self.formLayout23.setWidget(5, QFormLayout.FieldRole, self.label293)


        self.hboxLayout50.addWidget(self.gb_gas)

        self.gb_powder = QGroupBox(self.page_sensors)
        self.gb_powder.setObjectName(u"gb_powder")
        sizePolicy.setHeightForWidth(self.gb_powder.sizePolicy().hasHeightForWidth())
        self.gb_powder.setSizePolicy(sizePolicy)
        self.formLayout24 = QFormLayout(self.gb_powder)
        self.formLayout24.setObjectName(u"formLayout24")
        self.formLayout24.setHorizontalSpacing(4)
        self.formLayout24.setVerticalSpacing(4)
        self.label294 = QLabel(self.gb_powder)
        self.label294.setObjectName(u"label294")

        self.formLayout24.setWidget(0, QFormLayout.LabelRole, self.label294)

        self.label295 = QLabel(self.gb_powder)
        self.label295.setObjectName(u"label295")

        self.formLayout24.setWidget(0, QFormLayout.FieldRole, self.label295)

        self.label296 = QLabel(self.gb_powder)
        self.label296.setObjectName(u"label296")

        self.formLayout24.setWidget(1, QFormLayout.LabelRole, self.label296)

        self.label297 = QLabel(self.gb_powder)
        self.label297.setObjectName(u"label297")

        self.formLayout24.setWidget(1, QFormLayout.FieldRole, self.label297)

        self.label298 = QLabel(self.gb_powder)
        self.label298.setObjectName(u"label298")

        self.formLayout24.setWidget(2, QFormLayout.LabelRole, self.label298)

        self.label299 = QLabel(self.gb_powder)
        self.label299.setObjectName(u"label299")

        self.formLayout24.setWidget(2, QFormLayout.FieldRole, self.label299)

        self.label300 = QLabel(self.gb_powder)
        self.label300.setObjectName(u"label300")

        self.formLayout24.setWidget(3, QFormLayout.LabelRole, self.label300)

        self.label301 = QLabel(self.gb_powder)
        self.label301.setObjectName(u"label301")

        self.formLayout24.setWidget(3, QFormLayout.FieldRole, self.label301)

        self.label302 = QLabel(self.gb_powder)
        self.label302.setObjectName(u"label302")

        self.formLayout24.setWidget(4, QFormLayout.LabelRole, self.label302)

        self.label303 = QLabel(self.gb_powder)
        self.label303.setObjectName(u"label303")

        self.formLayout24.setWidget(4, QFormLayout.FieldRole, self.label303)


        self.hboxLayout50.addWidget(self.gb_powder)

        self.gb_door = QGroupBox(self.page_sensors)
        self.gb_door.setObjectName(u"gb_door")
        sizePolicy.setHeightForWidth(self.gb_door.sizePolicy().hasHeightForWidth())
        self.gb_door.setSizePolicy(sizePolicy)
        self.formLayout25 = QFormLayout(self.gb_door)
        self.formLayout25.setObjectName(u"formLayout25")
        self.formLayout25.setHorizontalSpacing(4)
        self.formLayout25.setVerticalSpacing(4)
        self.label304 = QLabel(self.gb_door)
        self.label304.setObjectName(u"label304")

        self.formLayout25.setWidget(0, QFormLayout.LabelRole, self.label304)

        self.label305 = QLabel(self.gb_door)
        self.label305.setObjectName(u"label305")

        self.formLayout25.setWidget(0, QFormLayout.FieldRole, self.label305)

        self.label306 = QLabel(self.gb_door)
        self.label306.setObjectName(u"label306")

        self.formLayout25.setWidget(1, QFormLayout.LabelRole, self.label306)

        self.label307 = QLabel(self.gb_door)
        self.label307.setObjectName(u"label307")

        self.formLayout25.setWidget(1, QFormLayout.FieldRole, self.label307)

        self.label308 = QLabel(self.gb_door)
        self.label308.setObjectName(u"label308")

        self.formLayout25.setWidget(2, QFormLayout.LabelRole, self.label308)

        self.label309 = QLabel(self.gb_door)
        self.label309.setObjectName(u"label309")

        self.formLayout25.setWidget(2, QFormLayout.FieldRole, self.label309)

        self.label310 = QLabel(self.gb_door)
        self.label310.setObjectName(u"label310")

        self.formLayout25.setWidget(3, QFormLayout.LabelRole, self.label310)

        self.label311 = QLabel(self.gb_door)
        self.label311.setObjectName(u"label311")

        self.formLayout25.setWidget(3, QFormLayout.FieldRole, self.label311)


        self.hboxLayout50.addWidget(self.gb_door)


        self.vLayout_sensors.addLayout(self.hboxLayout50)

        self.hboxLayout51 = QHBoxLayout()
        self.hboxLayout51.setSpacing(4)
        self.hboxLayout51.setObjectName(u"hboxLayout51")
        self.gb_safety = QGroupBox(self.page_sensors)
        self.gb_safety.setObjectName(u"gb_safety")
        sizePolicy.setHeightForWidth(self.gb_safety.sizePolicy().hasHeightForWidth())
        self.gb_safety.setSizePolicy(sizePolicy)
        self.formLayout26 = QFormLayout(self.gb_safety)
        self.formLayout26.setObjectName(u"formLayout26")
        self.formLayout26.setHorizontalSpacing(4)
        self.formLayout26.setVerticalSpacing(4)
        self.label312 = QLabel(self.gb_safety)
        self.label312.setObjectName(u"label312")

        self.formLayout26.setWidget(0, QFormLayout.LabelRole, self.label312)

        self.label313 = QLabel(self.gb_safety)
        self.label313.setObjectName(u"label313")

        self.formLayout26.setWidget(0, QFormLayout.FieldRole, self.label313)

        self.label314 = QLabel(self.gb_safety)
        self.label314.setObjectName(u"label314")

        self.formLayout26.setWidget(1, QFormLayout.LabelRole, self.label314)

        self.label315 = QLabel(self.gb_safety)
        self.label315.setObjectName(u"label315")

        self.formLayout26.setWidget(1, QFormLayout.FieldRole, self.label315)

        self.label316 = QLabel(self.gb_safety)
        self.label316.setObjectName(u"label316")

        self.formLayout26.setWidget(2, QFormLayout.LabelRole, self.label316)

        self.label317 = QLabel(self.gb_safety)
        self.label317.setObjectName(u"label317")

        self.formLayout26.setWidget(2, QFormLayout.FieldRole, self.label317)

        self.label318 = QLabel(self.gb_safety)
        self.label318.setObjectName(u"label318")

        self.formLayout26.setWidget(3, QFormLayout.LabelRole, self.label318)

        self.label319 = QLabel(self.gb_safety)
        self.label319.setObjectName(u"label319")

        self.formLayout26.setWidget(3, QFormLayout.FieldRole, self.label319)

        self.label320 = QLabel(self.gb_safety)
        self.label320.setObjectName(u"label320")

        self.formLayout26.setWidget(4, QFormLayout.LabelRole, self.label320)

        self.label321 = QLabel(self.gb_safety)
        self.label321.setObjectName(u"label321")

        self.formLayout26.setWidget(4, QFormLayout.FieldRole, self.label321)

        self.label322 = QLabel(self.gb_safety)
        self.label322.setObjectName(u"label322")

        self.formLayout26.setWidget(5, QFormLayout.LabelRole, self.label322)

        self.label323 = QLabel(self.gb_safety)
        self.label323.setObjectName(u"label323")

        self.formLayout26.setWidget(5, QFormLayout.FieldRole, self.label323)

        self.label324 = QLabel(self.gb_safety)
        self.label324.setObjectName(u"label324")

        self.formLayout26.setWidget(6, QFormLayout.LabelRole, self.label324)

        self.label325 = QLabel(self.gb_safety)
        self.label325.setObjectName(u"label325")

        self.formLayout26.setWidget(6, QFormLayout.FieldRole, self.label325)

        self.label326 = QLabel(self.gb_safety)
        self.label326.setObjectName(u"label326")

        self.formLayout26.setWidget(7, QFormLayout.LabelRole, self.label326)

        self.label327 = QLabel(self.gb_safety)
        self.label327.setObjectName(u"label327")

        self.formLayout26.setWidget(7, QFormLayout.FieldRole, self.label327)

        self.label328 = QLabel(self.gb_safety)
        self.label328.setObjectName(u"label328")

        self.formLayout26.setWidget(8, QFormLayout.LabelRole, self.label328)

        self.label329 = QLabel(self.gb_safety)
        self.label329.setObjectName(u"label329")

        self.formLayout26.setWidget(8, QFormLayout.FieldRole, self.label329)

        self.label330 = QLabel(self.gb_safety)
        self.label330.setObjectName(u"label330")

        self.formLayout26.setWidget(9, QFormLayout.LabelRole, self.label330)

        self.label331 = QLabel(self.gb_safety)
        self.label331.setObjectName(u"label331")

        self.formLayout26.setWidget(9, QFormLayout.FieldRole, self.label331)


        self.hboxLayout51.addWidget(self.gb_safety)

        self.gb_temps = QGroupBox(self.page_sensors)
        self.gb_temps.setObjectName(u"gb_temps")
        sizePolicy.setHeightForWidth(self.gb_temps.sizePolicy().hasHeightForWidth())
        self.gb_temps.setSizePolicy(sizePolicy)
        self.gridLayout4 = QGridLayout(self.gb_temps)
        self.gridLayout4.setSpacing(4)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.label332 = QLabel(self.gb_temps)
        self.label332.setObjectName(u"label332")

        self.gridLayout4.addWidget(self.label332, 0, 0, 1, 1)

        self.label333 = QLabel(self.gb_temps)
        self.label333.setObjectName(u"label333")

        self.gridLayout4.addWidget(self.label333, 0, 1, 1, 1)

        self.label334 = QLabel(self.gb_temps)
        self.label334.setObjectName(u"label334")

        self.gridLayout4.addWidget(self.label334, 1, 0, 1, 1)

        self.label335 = QLabel(self.gb_temps)
        self.label335.setObjectName(u"label335")

        self.gridLayout4.addWidget(self.label335, 1, 1, 1, 1)

        self.label336 = QLabel(self.gb_temps)
        self.label336.setObjectName(u"label336")

        self.gridLayout4.addWidget(self.label336, 2, 0, 1, 1)

        self.label337 = QLabel(self.gb_temps)
        self.label337.setObjectName(u"label337")

        self.gridLayout4.addWidget(self.label337, 2, 1, 1, 1)

        self.label338 = QLabel(self.gb_temps)
        self.label338.setObjectName(u"label338")

        self.gridLayout4.addWidget(self.label338, 3, 0, 1, 1)

        self.label339 = QLabel(self.gb_temps)
        self.label339.setObjectName(u"label339")

        self.gridLayout4.addWidget(self.label339, 3, 1, 1, 1)


        self.hboxLayout51.addWidget(self.gb_temps)

        self.gb_misc = QGroupBox(self.page_sensors)
        self.gb_misc.setObjectName(u"gb_misc")
        sizePolicy.setHeightForWidth(self.gb_misc.sizePolicy().hasHeightForWidth())
        self.gb_misc.setSizePolicy(sizePolicy)
        self.formLayout27 = QFormLayout(self.gb_misc)
        self.formLayout27.setObjectName(u"formLayout27")
        self.formLayout27.setHorizontalSpacing(4)
        self.formLayout27.setVerticalSpacing(4)
        self.label340 = QLabel(self.gb_misc)
        self.label340.setObjectName(u"label340")

        self.formLayout27.setWidget(0, QFormLayout.LabelRole, self.label340)

        self.label341 = QLabel(self.gb_misc)
        self.label341.setObjectName(u"label341")

        self.formLayout27.setWidget(0, QFormLayout.FieldRole, self.label341)

        self.label342 = QLabel(self.gb_misc)
        self.label342.setObjectName(u"label342")

        self.formLayout27.setWidget(1, QFormLayout.LabelRole, self.label342)

        self.label343 = QLabel(self.gb_misc)
        self.label343.setObjectName(u"label343")

        self.formLayout27.setWidget(1, QFormLayout.FieldRole, self.label343)

        self.label344 = QLabel(self.gb_misc)
        self.label344.setObjectName(u"label344")

        self.formLayout27.setWidget(2, QFormLayout.LabelRole, self.label344)

        self.label345 = QLabel(self.gb_misc)
        self.label345.setObjectName(u"label345")

        self.formLayout27.setWidget(2, QFormLayout.FieldRole, self.label345)

        self.label346 = QLabel(self.gb_misc)
        self.label346.setObjectName(u"label346")

        self.formLayout27.setWidget(3, QFormLayout.LabelRole, self.label346)

        self.label347 = QLabel(self.gb_misc)
        self.label347.setObjectName(u"label347")

        self.formLayout27.setWidget(3, QFormLayout.FieldRole, self.label347)

        self.label348 = QLabel(self.gb_misc)
        self.label348.setObjectName(u"label348")

        self.formLayout27.setWidget(4, QFormLayout.LabelRole, self.label348)

        self.label349 = QLabel(self.gb_misc)
        self.label349.setObjectName(u"label349")

        self.formLayout27.setWidget(4, QFormLayout.FieldRole, self.label349)

        self.label350 = QLabel(self.gb_misc)
        self.label350.setObjectName(u"label350")

        self.formLayout27.setWidget(5, QFormLayout.LabelRole, self.label350)

        self.label351 = QLabel(self.gb_misc)
        self.label351.setObjectName(u"label351")

        self.formLayout27.setWidget(5, QFormLayout.FieldRole, self.label351)

        self.label352 = QLabel(self.gb_misc)
        self.label352.setObjectName(u"label352")

        self.formLayout27.setWidget(6, QFormLayout.LabelRole, self.label352)

        self.label353 = QLabel(self.gb_misc)
        self.label353.setObjectName(u"label353")

        self.formLayout27.setWidget(6, QFormLayout.FieldRole, self.label353)

        self.label354 = QLabel(self.gb_misc)
        self.label354.setObjectName(u"label354")

        self.formLayout27.setWidget(7, QFormLayout.LabelRole, self.label354)

        self.label355 = QLabel(self.gb_misc)
        self.label355.setObjectName(u"label355")

        self.formLayout27.setWidget(7, QFormLayout.FieldRole, self.label355)


        self.hboxLayout51.addWidget(self.gb_misc)

        self.gb_sensor_overview = QGroupBox(self.page_sensors)
        self.gb_sensor_overview.setObjectName(u"gb_sensor_overview")
        sizePolicy.setHeightForWidth(self.gb_sensor_overview.sizePolicy().hasHeightForWidth())
        self.gb_sensor_overview.setSizePolicy(sizePolicy)
        self.hboxLayout52 = QHBoxLayout(self.gb_sensor_overview)
        self.hboxLayout52.setSpacing(4)
        self.hboxLayout52.setObjectName(u"hboxLayout52")
        self.label356 = QLabel(self.gb_sensor_overview)
        self.label356.setObjectName(u"label356")

        self.hboxLayout52.addWidget(self.label356)

        self.formLayout28 = QFormLayout()
        self.formLayout28.setObjectName(u"formLayout28")
        self.formLayout28.setHorizontalSpacing(4)
        self.formLayout28.setVerticalSpacing(4)
        self.label357 = QLabel(self.gb_sensor_overview)
        self.label357.setObjectName(u"label357")

        self.formLayout28.setWidget(0, QFormLayout.LabelRole, self.label357)

        self.label358 = QLabel(self.gb_sensor_overview)
        self.label358.setObjectName(u"label358")

        self.formLayout28.setWidget(0, QFormLayout.FieldRole, self.label358)

        self.label359 = QLabel(self.gb_sensor_overview)
        self.label359.setObjectName(u"label359")

        self.formLayout28.setWidget(1, QFormLayout.LabelRole, self.label359)

        self.label360 = QLabel(self.gb_sensor_overview)
        self.label360.setObjectName(u"label360")

        self.formLayout28.setWidget(1, QFormLayout.FieldRole, self.label360)

        self.label361 = QLabel(self.gb_sensor_overview)
        self.label361.setObjectName(u"label361")

        self.formLayout28.setWidget(2, QFormLayout.LabelRole, self.label361)

        self.label362 = QLabel(self.gb_sensor_overview)
        self.label362.setObjectName(u"label362")

        self.formLayout28.setWidget(2, QFormLayout.FieldRole, self.label362)

        self.label363 = QLabel(self.gb_sensor_overview)
        self.label363.setObjectName(u"label363")

        self.formLayout28.setWidget(3, QFormLayout.LabelRole, self.label363)

        self.label364 = QLabel(self.gb_sensor_overview)
        self.label364.setObjectName(u"label364")

        self.formLayout28.setWidget(3, QFormLayout.FieldRole, self.label364)


        self.hboxLayout52.addLayout(self.formLayout28)


        self.hboxLayout51.addWidget(self.gb_sensor_overview)


        self.vLayout_sensors.addLayout(self.hboxLayout51)

        self.hboxLayout53 = QHBoxLayout()
        self.hboxLayout53.setSpacing(4)
        self.hboxLayout53.setObjectName(u"hboxLayout53")
        self.gb_history = QGroupBox(self.page_sensors)
        self.gb_history.setObjectName(u"gb_history")
        sizePolicy.setHeightForWidth(self.gb_history.sizePolicy().hasHeightForWidth())
        self.gb_history.setSizePolicy(sizePolicy)
        self.vboxLayout35 = QVBoxLayout(self.gb_history)
        self.vboxLayout35.setSpacing(4)
        self.vboxLayout35.setObjectName(u"vboxLayout35")
        self.label365 = QLabel(self.gb_history)
        self.label365.setObjectName(u"label365")
        self.label365.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout35.addWidget(self.label365)


        self.hboxLayout53.addWidget(self.gb_history)

        self.gb_filter = QGroupBox(self.page_sensors)
        self.gb_filter.setObjectName(u"gb_filter")
        sizePolicy.setHeightForWidth(self.gb_filter.sizePolicy().hasHeightForWidth())
        self.gb_filter.setSizePolicy(sizePolicy)
        self.formLayout29 = QFormLayout(self.gb_filter)
        self.formLayout29.setObjectName(u"formLayout29")
        self.formLayout29.setHorizontalSpacing(4)
        self.formLayout29.setVerticalSpacing(4)
        self.label366 = QLabel(self.gb_filter)
        self.label366.setObjectName(u"label366")

        self.formLayout29.setWidget(0, QFormLayout.LabelRole, self.label366)

        self.comboBox1 = QComboBox(self.gb_filter)
        self.comboBox1.setObjectName(u"comboBox1")

        self.formLayout29.setWidget(0, QFormLayout.FieldRole, self.comboBox1)

        self.label367 = QLabel(self.gb_filter)
        self.label367.setObjectName(u"label367")

        self.formLayout29.setWidget(1, QFormLayout.LabelRole, self.label367)

        self.comboBox2 = QComboBox(self.gb_filter)
        self.comboBox2.setObjectName(u"comboBox2")

        self.formLayout29.setWidget(1, QFormLayout.FieldRole, self.comboBox2)

        self.pushButton101 = QPushButton(self.gb_filter)
        self.pushButton101.setObjectName(u"pushButton101")
        self.pushButton101.setMinimumSize(QSize(0, 20))

        self.formLayout29.setWidget(2, QFormLayout.SpanningRole, self.pushButton101)


        self.hboxLayout53.addWidget(self.gb_filter)

        self.gb_calibration_sensors = QGroupBox(self.page_sensors)
        self.gb_calibration_sensors.setObjectName(u"gb_calibration_sensors")
        sizePolicy.setHeightForWidth(self.gb_calibration_sensors.sizePolicy().hasHeightForWidth())
        self.gb_calibration_sensors.setSizePolicy(sizePolicy)
        self.vboxLayout36 = QVBoxLayout(self.gb_calibration_sensors)
        self.vboxLayout36.setSpacing(4)
        self.vboxLayout36.setObjectName(u"vboxLayout36")
        self.tableWidget1 = QTableWidget(self.gb_calibration_sensors)
        if (self.tableWidget1.columnCount() < 4):
            self.tableWidget1.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        self.tableWidget1.setObjectName(u"tableWidget1")
        sizePolicy.setHeightForWidth(self.tableWidget1.sizePolicy().hasHeightForWidth())
        self.tableWidget1.setSizePolicy(sizePolicy)
        self.tableWidget1.setColumnCount(4)

        self.vboxLayout36.addWidget(self.tableWidget1)

        self.pushButton102 = QPushButton(self.gb_calibration_sensors)
        self.pushButton102.setObjectName(u"pushButton102")
        self.pushButton102.setMinimumSize(QSize(0, 20))

        self.vboxLayout36.addWidget(self.pushButton102)


        self.hboxLayout53.addWidget(self.gb_calibration_sensors)


        self.vLayout_sensors.addLayout(self.hboxLayout53)

        self.stackedWidget.addWidget(self.page_sensors)
        self.page_alarm_events = QWidget()
        self.page_alarm_events.setObjectName(u"page_alarm_events")
        self.vLayout_alarm_events = QVBoxLayout(self.page_alarm_events)
        self.vLayout_alarm_events.setSpacing(4)
        self.vLayout_alarm_events.setObjectName(u"vLayout_alarm_events")
        self.hboxLayout54 = QHBoxLayout()
        self.hboxLayout54.setSpacing(4)
        self.hboxLayout54.setObjectName(u"hboxLayout54")
        self.gb_active_alarms = QGroupBox(self.page_alarm_events)
        self.gb_active_alarms.setObjectName(u"gb_active_alarms")
        sizePolicy.setHeightForWidth(self.gb_active_alarms.sizePolicy().hasHeightForWidth())
        self.gb_active_alarms.setSizePolicy(sizePolicy)
        self.vboxLayout37 = QVBoxLayout(self.gb_active_alarms)
        self.vboxLayout37.setSpacing(4)
        self.vboxLayout37.setObjectName(u"vboxLayout37")
        self.label368 = QLabel(self.gb_active_alarms)
        self.label368.setObjectName(u"label368")

        self.vboxLayout37.addWidget(self.label368)

        self.label369 = QLabel(self.gb_active_alarms)
        self.label369.setObjectName(u"label369")

        self.vboxLayout37.addWidget(self.label369)

        self.label370 = QLabel(self.gb_active_alarms)
        self.label370.setObjectName(u"label370")

        self.vboxLayout37.addWidget(self.label370)

        self.hboxLayout55 = QHBoxLayout()
        self.hboxLayout55.setSpacing(4)
        self.hboxLayout55.setObjectName(u"hboxLayout55")
        self.pushButton103 = QPushButton(self.gb_active_alarms)
        self.pushButton103.setObjectName(u"pushButton103")
        self.pushButton103.setMinimumSize(QSize(0, 20))

        self.hboxLayout55.addWidget(self.pushButton103)

        self.pushButton104 = QPushButton(self.gb_active_alarms)
        self.pushButton104.setObjectName(u"pushButton104")
        self.pushButton104.setMinimumSize(QSize(0, 20))

        self.hboxLayout55.addWidget(self.pushButton104)


        self.vboxLayout37.addLayout(self.hboxLayout55)


        self.hboxLayout54.addWidget(self.gb_active_alarms)

        self.gb_alarm_summary = QGroupBox(self.page_alarm_events)
        self.gb_alarm_summary.setObjectName(u"gb_alarm_summary")
        sizePolicy.setHeightForWidth(self.gb_alarm_summary.sizePolicy().hasHeightForWidth())
        self.gb_alarm_summary.setSizePolicy(sizePolicy)
        self.gridLayout5 = QGridLayout(self.gb_alarm_summary)
        self.gridLayout5.setSpacing(4)
        self.gridLayout5.setObjectName(u"gridLayout5")
        self.label371 = QLabel(self.gb_alarm_summary)
        self.label371.setObjectName(u"label371")
        self.label371.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout5.addWidget(self.label371, 0, 0, 1, 1)

        self.label372 = QLabel(self.gb_alarm_summary)
        self.label372.setObjectName(u"label372")
        self.label372.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout5.addWidget(self.label372, 0, 1, 1, 1)

        self.label373 = QLabel(self.gb_alarm_summary)
        self.label373.setObjectName(u"label373")
        self.label373.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout5.addWidget(self.label373, 1, 0, 1, 1)

        self.label374 = QLabel(self.gb_alarm_summary)
        self.label374.setObjectName(u"label374")
        self.label374.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout5.addWidget(self.label374, 1, 1, 1, 1)


        self.hboxLayout54.addWidget(self.gb_alarm_summary)

        self.gb_alarm_category = QGroupBox(self.page_alarm_events)
        self.gb_alarm_category.setObjectName(u"gb_alarm_category")
        sizePolicy.setHeightForWidth(self.gb_alarm_category.sizePolicy().hasHeightForWidth())
        self.gb_alarm_category.setSizePolicy(sizePolicy)
        self.hboxLayout56 = QHBoxLayout(self.gb_alarm_category)
        self.hboxLayout56.setSpacing(4)
        self.hboxLayout56.setObjectName(u"hboxLayout56")
        self.label375 = QLabel(self.gb_alarm_category)
        self.label375.setObjectName(u"label375")

        self.hboxLayout56.addWidget(self.label375)

        self.formLayout30 = QFormLayout()
        self.formLayout30.setObjectName(u"formLayout30")
        self.formLayout30.setHorizontalSpacing(4)
        self.formLayout30.setVerticalSpacing(4)
        self.label376 = QLabel(self.gb_alarm_category)
        self.label376.setObjectName(u"label376")

        self.formLayout30.setWidget(0, QFormLayout.LabelRole, self.label376)

        self.label377 = QLabel(self.gb_alarm_category)
        self.label377.setObjectName(u"label377")

        self.formLayout30.setWidget(0, QFormLayout.FieldRole, self.label377)

        self.label378 = QLabel(self.gb_alarm_category)
        self.label378.setObjectName(u"label378")

        self.formLayout30.setWidget(1, QFormLayout.LabelRole, self.label378)

        self.label379 = QLabel(self.gb_alarm_category)
        self.label379.setObjectName(u"label379")

        self.formLayout30.setWidget(1, QFormLayout.FieldRole, self.label379)

        self.label380 = QLabel(self.gb_alarm_category)
        self.label380.setObjectName(u"label380")

        self.formLayout30.setWidget(2, QFormLayout.LabelRole, self.label380)

        self.label381 = QLabel(self.gb_alarm_category)
        self.label381.setObjectName(u"label381")

        self.formLayout30.setWidget(2, QFormLayout.FieldRole, self.label381)

        self.label382 = QLabel(self.gb_alarm_category)
        self.label382.setObjectName(u"label382")

        self.formLayout30.setWidget(3, QFormLayout.LabelRole, self.label382)

        self.label383 = QLabel(self.gb_alarm_category)
        self.label383.setObjectName(u"label383")

        self.formLayout30.setWidget(3, QFormLayout.FieldRole, self.label383)

        self.label384 = QLabel(self.gb_alarm_category)
        self.label384.setObjectName(u"label384")

        self.formLayout30.setWidget(4, QFormLayout.LabelRole, self.label384)

        self.label385 = QLabel(self.gb_alarm_category)
        self.label385.setObjectName(u"label385")

        self.formLayout30.setWidget(4, QFormLayout.FieldRole, self.label385)

        self.label386 = QLabel(self.gb_alarm_category)
        self.label386.setObjectName(u"label386")

        self.formLayout30.setWidget(5, QFormLayout.LabelRole, self.label386)

        self.label387 = QLabel(self.gb_alarm_category)
        self.label387.setObjectName(u"label387")

        self.formLayout30.setWidget(5, QFormLayout.FieldRole, self.label387)

        self.label388 = QLabel(self.gb_alarm_category)
        self.label388.setObjectName(u"label388")

        self.formLayout30.setWidget(6, QFormLayout.LabelRole, self.label388)

        self.label389 = QLabel(self.gb_alarm_category)
        self.label389.setObjectName(u"label389")

        self.formLayout30.setWidget(6, QFormLayout.FieldRole, self.label389)


        self.hboxLayout56.addLayout(self.formLayout30)


        self.hboxLayout54.addWidget(self.gb_alarm_category)


        self.vLayout_alarm_events.addLayout(self.hboxLayout54)

        self.hboxLayout57 = QHBoxLayout()
        self.hboxLayout57.setSpacing(4)
        self.hboxLayout57.setObjectName(u"hboxLayout57")
        self.gb_alarm_history = QGroupBox(self.page_alarm_events)
        self.gb_alarm_history.setObjectName(u"gb_alarm_history")
        sizePolicy.setHeightForWidth(self.gb_alarm_history.sizePolicy().hasHeightForWidth())
        self.gb_alarm_history.setSizePolicy(sizePolicy)
        self.vboxLayout38 = QVBoxLayout(self.gb_alarm_history)
        self.vboxLayout38.setSpacing(4)
        self.vboxLayout38.setObjectName(u"vboxLayout38")
        self.hboxLayout58 = QHBoxLayout()
        self.hboxLayout58.setSpacing(4)
        self.hboxLayout58.setObjectName(u"hboxLayout58")
        self.spacerItem11 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout58.addItem(self.spacerItem11)

        self.comboBox3 = QComboBox(self.gb_alarm_history)
        self.comboBox3.addItem("")
        self.comboBox3.setObjectName(u"comboBox3")

        self.hboxLayout58.addWidget(self.comboBox3)

        self.comboBox4 = QComboBox(self.gb_alarm_history)
        self.comboBox4.addItem("")
        self.comboBox4.setObjectName(u"comboBox4")

        self.hboxLayout58.addWidget(self.comboBox4)

        self.comboBox5 = QComboBox(self.gb_alarm_history)
        self.comboBox5.addItem("")
        self.comboBox5.setObjectName(u"comboBox5")

        self.hboxLayout58.addWidget(self.comboBox5)


        self.vboxLayout38.addLayout(self.hboxLayout58)

        self.tableWidget2 = QTableWidget(self.gb_alarm_history)
        if (self.tableWidget2.columnCount() < 7):
            self.tableWidget2.setColumnCount(7)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        self.tableWidget2.setObjectName(u"tableWidget2")
        sizePolicy.setHeightForWidth(self.tableWidget2.sizePolicy().hasHeightForWidth())
        self.tableWidget2.setSizePolicy(sizePolicy)
        self.tableWidget2.setColumnCount(7)

        self.vboxLayout38.addWidget(self.tableWidget2)

        self.hboxLayout59 = QHBoxLayout()
        self.hboxLayout59.setSpacing(4)
        self.hboxLayout59.setObjectName(u"hboxLayout59")
        self.label390 = QLabel(self.gb_alarm_history)
        self.label390.setObjectName(u"label390")

        self.hboxLayout59.addWidget(self.label390)

        self.spacerItem12 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout59.addItem(self.spacerItem12)

        self.pushButton105 = QPushButton(self.gb_alarm_history)
        self.pushButton105.setObjectName(u"pushButton105")
        self.pushButton105.setMinimumSize(QSize(0, 20))

        self.hboxLayout59.addWidget(self.pushButton105)

        self.pushButton106 = QPushButton(self.gb_alarm_history)
        self.pushButton106.setObjectName(u"pushButton106")
        self.pushButton106.setMinimumSize(QSize(0, 20))

        self.hboxLayout59.addWidget(self.pushButton106)

        self.pushButton107 = QPushButton(self.gb_alarm_history)
        self.pushButton107.setObjectName(u"pushButton107")
        self.pushButton107.setMinimumSize(QSize(0, 20))

        self.hboxLayout59.addWidget(self.pushButton107)

        self.spacerItem13 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout59.addItem(self.spacerItem13)

        self.pushButton108 = QPushButton(self.gb_alarm_history)
        self.pushButton108.setObjectName(u"pushButton108")
        self.pushButton108.setMinimumSize(QSize(0, 20))

        self.hboxLayout59.addWidget(self.pushButton108)


        self.vboxLayout38.addLayout(self.hboxLayout59)


        self.hboxLayout57.addWidget(self.gb_alarm_history)

        self.gb_alarm_actions = QGroupBox(self.page_alarm_events)
        self.gb_alarm_actions.setObjectName(u"gb_alarm_actions")
        sizePolicy.setHeightForWidth(self.gb_alarm_actions.sizePolicy().hasHeightForWidth())
        self.gb_alarm_actions.setSizePolicy(sizePolicy)
        self.vboxLayout39 = QVBoxLayout(self.gb_alarm_actions)
        self.vboxLayout39.setSpacing(4)
        self.vboxLayout39.setObjectName(u"vboxLayout39")
        self.pushButton109 = QPushButton(self.gb_alarm_actions)
        self.pushButton109.setObjectName(u"pushButton109")
        self.pushButton109.setMinimumSize(QSize(0, 20))

        self.vboxLayout39.addWidget(self.pushButton109)

        self.pushButton110 = QPushButton(self.gb_alarm_actions)
        self.pushButton110.setObjectName(u"pushButton110")
        self.pushButton110.setMinimumSize(QSize(0, 20))

        self.vboxLayout39.addWidget(self.pushButton110)

        self.pushButton111 = QPushButton(self.gb_alarm_actions)
        self.pushButton111.setObjectName(u"pushButton111")
        self.pushButton111.setMinimumSize(QSize(0, 20))

        self.vboxLayout39.addWidget(self.pushButton111)

        self.pushButton112 = QPushButton(self.gb_alarm_actions)
        self.pushButton112.setObjectName(u"pushButton112")
        self.pushButton112.setMinimumSize(QSize(0, 20))

        self.vboxLayout39.addWidget(self.pushButton112)

        self.pushButton113 = QPushButton(self.gb_alarm_actions)
        self.pushButton113.setObjectName(u"pushButton113")
        self.pushButton113.setMinimumSize(QSize(0, 20))

        self.vboxLayout39.addWidget(self.pushButton113)


        self.hboxLayout57.addWidget(self.gb_alarm_actions)


        self.vLayout_alarm_events.addLayout(self.hboxLayout57)

        self.stackedWidget.addWidget(self.page_alarm_events)
        self.page_logs = QWidget()
        self.page_logs.setObjectName(u"page_logs")
        self.hLayout_logs = QHBoxLayout(self.page_logs)
        self.hLayout_logs.setSpacing(4)
        self.hLayout_logs.setObjectName(u"hLayout_logs")
        self.gb_system_logs = QGroupBox(self.page_logs)
        self.gb_system_logs.setObjectName(u"gb_system_logs")
        sizePolicy.setHeightForWidth(self.gb_system_logs.sizePolicy().hasHeightForWidth())
        self.gb_system_logs.setSizePolicy(sizePolicy)
        self.vboxLayout40 = QVBoxLayout(self.gb_system_logs)
        self.vboxLayout40.setSpacing(4)
        self.vboxLayout40.setObjectName(u"vboxLayout40")
        self.hboxLayout60 = QHBoxLayout()
        self.hboxLayout60.setSpacing(4)
        self.hboxLayout60.setObjectName(u"hboxLayout60")
        self.lineEdit9 = QLineEdit(self.gb_system_logs)
        self.lineEdit9.setObjectName(u"lineEdit9")

        self.hboxLayout60.addWidget(self.lineEdit9)

        self.pushButton114 = QPushButton(self.gb_system_logs)
        self.pushButton114.setObjectName(u"pushButton114")
        self.pushButton114.setMinimumSize(QSize(0, 20))

        self.hboxLayout60.addWidget(self.pushButton114)

        self.pushButton115 = QPushButton(self.gb_system_logs)
        self.pushButton115.setObjectName(u"pushButton115")
        self.pushButton115.setMinimumSize(QSize(0, 20))

        self.hboxLayout60.addWidget(self.pushButton115)


        self.vboxLayout40.addLayout(self.hboxLayout60)

        self.tableWidget3 = QTableWidget(self.gb_system_logs)
        if (self.tableWidget3.columnCount() < 4):
            self.tableWidget3.setColumnCount(4)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget3.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget3.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget3.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget3.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        self.tableWidget3.setObjectName(u"tableWidget3")
        sizePolicy.setHeightForWidth(self.tableWidget3.sizePolicy().hasHeightForWidth())
        self.tableWidget3.setSizePolicy(sizePolicy)
        self.tableWidget3.setColumnCount(4)

        self.vboxLayout40.addWidget(self.tableWidget3)

        self.hboxLayout61 = QHBoxLayout()
        self.hboxLayout61.setSpacing(4)
        self.hboxLayout61.setObjectName(u"hboxLayout61")
        self.label391 = QLabel(self.gb_system_logs)
        self.label391.setObjectName(u"label391")

        self.hboxLayout61.addWidget(self.label391)

        self.spacerItem14 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout61.addItem(self.spacerItem14)

        self.pushButton116 = QPushButton(self.gb_system_logs)
        self.pushButton116.setObjectName(u"pushButton116")
        self.pushButton116.setMinimumSize(QSize(0, 20))

        self.hboxLayout61.addWidget(self.pushButton116)

        self.pushButton117 = QPushButton(self.gb_system_logs)
        self.pushButton117.setObjectName(u"pushButton117")
        self.pushButton117.setMinimumSize(QSize(0, 20))

        self.hboxLayout61.addWidget(self.pushButton117)

        self.pushButton118 = QPushButton(self.gb_system_logs)
        self.pushButton118.setObjectName(u"pushButton118")
        self.pushButton118.setMinimumSize(QSize(0, 20))

        self.hboxLayout61.addWidget(self.pushButton118)


        self.vboxLayout40.addLayout(self.hboxLayout61)


        self.hLayout_logs.addWidget(self.gb_system_logs)

        self.vboxLayout41 = QVBoxLayout()
        self.vboxLayout41.setSpacing(4)
        self.vboxLayout41.setObjectName(u"vboxLayout41")
        self.gb_log_filters = QGroupBox(self.page_logs)
        self.gb_log_filters.setObjectName(u"gb_log_filters")
        sizePolicy.setHeightForWidth(self.gb_log_filters.sizePolicy().hasHeightForWidth())
        self.gb_log_filters.setSizePolicy(sizePolicy)
        self.formLayout31 = QFormLayout(self.gb_log_filters)
        self.formLayout31.setObjectName(u"formLayout31")
        self.formLayout31.setHorizontalSpacing(4)
        self.formLayout31.setVerticalSpacing(4)
        self.label392 = QLabel(self.gb_log_filters)
        self.label392.setObjectName(u"label392")

        self.formLayout31.setWidget(0, QFormLayout.LabelRole, self.label392)

        self.comboBox6 = QComboBox(self.gb_log_filters)
        self.comboBox6.addItem("")
        self.comboBox6.setObjectName(u"comboBox6")

        self.formLayout31.setWidget(0, QFormLayout.FieldRole, self.comboBox6)

        self.label393 = QLabel(self.gb_log_filters)
        self.label393.setObjectName(u"label393")

        self.formLayout31.setWidget(1, QFormLayout.LabelRole, self.label393)

        self.comboBox7 = QComboBox(self.gb_log_filters)
        self.comboBox7.addItem("")
        self.comboBox7.setObjectName(u"comboBox7")

        self.formLayout31.setWidget(1, QFormLayout.FieldRole, self.comboBox7)

        self.label394 = QLabel(self.gb_log_filters)
        self.label394.setObjectName(u"label394")

        self.formLayout31.setWidget(2, QFormLayout.LabelRole, self.label394)

        self.comboBox8 = QComboBox(self.gb_log_filters)
        self.comboBox8.addItem("")
        self.comboBox8.setObjectName(u"comboBox8")

        self.formLayout31.setWidget(2, QFormLayout.FieldRole, self.comboBox8)

        self.hboxLayout62 = QHBoxLayout()
        self.hboxLayout62.setSpacing(4)
        self.hboxLayout62.setObjectName(u"hboxLayout62")
        self.pushButton119 = QPushButton(self.gb_log_filters)
        self.pushButton119.setObjectName(u"pushButton119")
        self.pushButton119.setMinimumSize(QSize(0, 20))

        self.hboxLayout62.addWidget(self.pushButton119)

        self.pushButton160 = QPushButton(self.gb_log_filters)
        self.pushButton160.setObjectName(u"pushButton160")
        self.pushButton160.setMinimumSize(QSize(0, 20))

        self.hboxLayout62.addWidget(self.pushButton160)


        self.formLayout31.setLayout(3, QFormLayout.SpanningRole, self.hboxLayout62)


        self.vboxLayout41.addWidget(self.gb_log_filters)

        self.gb_log_stats = QGroupBox(self.page_logs)
        self.gb_log_stats.setObjectName(u"gb_log_stats")
        sizePolicy.setHeightForWidth(self.gb_log_stats.sizePolicy().hasHeightForWidth())
        self.gb_log_stats.setSizePolicy(sizePolicy)
        self.hboxLayout63 = QHBoxLayout(self.gb_log_stats)
        self.hboxLayout63.setSpacing(4)
        self.hboxLayout63.setObjectName(u"hboxLayout63")
        self.label395 = QLabel(self.gb_log_stats)
        self.label395.setObjectName(u"label395")
        self.label395.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hboxLayout63.addWidget(self.label395)

        self.formLayout32 = QFormLayout()
        self.formLayout32.setObjectName(u"formLayout32")
        self.formLayout32.setHorizontalSpacing(4)
        self.formLayout32.setVerticalSpacing(4)
        self.label396 = QLabel(self.gb_log_stats)
        self.label396.setObjectName(u"label396")

        self.formLayout32.setWidget(0, QFormLayout.LabelRole, self.label396)

        self.label397 = QLabel(self.gb_log_stats)
        self.label397.setObjectName(u"label397")

        self.formLayout32.setWidget(0, QFormLayout.FieldRole, self.label397)

        self.label398 = QLabel(self.gb_log_stats)
        self.label398.setObjectName(u"label398")

        self.formLayout32.setWidget(1, QFormLayout.LabelRole, self.label398)

        self.label399 = QLabel(self.gb_log_stats)
        self.label399.setObjectName(u"label399")

        self.formLayout32.setWidget(1, QFormLayout.FieldRole, self.label399)

        self.label400 = QLabel(self.gb_log_stats)
        self.label400.setObjectName(u"label400")

        self.formLayout32.setWidget(2, QFormLayout.LabelRole, self.label400)

        self.label401 = QLabel(self.gb_log_stats)
        self.label401.setObjectName(u"label401")

        self.formLayout32.setWidget(2, QFormLayout.FieldRole, self.label401)

        self.label402 = QLabel(self.gb_log_stats)
        self.label402.setObjectName(u"label402")

        self.formLayout32.setWidget(3, QFormLayout.LabelRole, self.label402)

        self.label403 = QLabel(self.gb_log_stats)
        self.label403.setObjectName(u"label403")

        self.formLayout32.setWidget(3, QFormLayout.FieldRole, self.label403)


        self.hboxLayout63.addLayout(self.formLayout32)


        self.vboxLayout41.addWidget(self.gb_log_stats)

        self.gb_export_logs = QGroupBox(self.page_logs)
        self.gb_export_logs.setObjectName(u"gb_export_logs")
        sizePolicy.setHeightForWidth(self.gb_export_logs.sizePolicy().hasHeightForWidth())
        self.gb_export_logs.setSizePolicy(sizePolicy)
        self.vboxLayout42 = QVBoxLayout(self.gb_export_logs)
        self.vboxLayout42.setSpacing(4)
        self.vboxLayout42.setObjectName(u"vboxLayout42")
        self.label404 = QLabel(self.gb_export_logs)
        self.label404.setObjectName(u"label404")

        self.vboxLayout42.addWidget(self.label404)

        self.hboxLayout64 = QHBoxLayout()
        self.hboxLayout64.setSpacing(4)
        self.hboxLayout64.setObjectName(u"hboxLayout64")
        self.comboBox9 = QComboBox(self.gb_export_logs)
        self.comboBox9.addItem("")
        self.comboBox9.setObjectName(u"comboBox9")

        self.hboxLayout64.addWidget(self.comboBox9)

        self.pushButton121 = QPushButton(self.gb_export_logs)
        self.pushButton121.setObjectName(u"pushButton121")
        self.pushButton121.setMinimumSize(QSize(0, 20))

        self.hboxLayout64.addWidget(self.pushButton121)


        self.vboxLayout42.addLayout(self.hboxLayout64)


        self.vboxLayout41.addWidget(self.gb_export_logs)


        self.hLayout_logs.addLayout(self.vboxLayout41)

        self.stackedWidget.addWidget(self.page_logs)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.hLayout_maintenance = QHBoxLayout(self.page_settings)
        self.hLayout_maintenance.setSpacing(4)
        self.hLayout_maintenance.setObjectName(u"hLayout_maintenance")
        self.vboxLayout43 = QVBoxLayout()
        self.vboxLayout43.setSpacing(4)
        self.vboxLayout43.setObjectName(u"vboxLayout43")
        self.gb_maint_tools = QGroupBox(self.page_settings)
        self.gb_maint_tools.setObjectName(u"gb_maint_tools")
        sizePolicy.setHeightForWidth(self.gb_maint_tools.sizePolicy().hasHeightForWidth())
        self.gb_maint_tools.setSizePolicy(sizePolicy)
        self.gridLayout6 = QGridLayout(self.gb_maint_tools)
        self.gridLayout6.setSpacing(4)
        self.gridLayout6.setObjectName(u"gridLayout6")
        self.vboxLayout44 = QVBoxLayout()
        self.vboxLayout44.setSpacing(4)
        self.vboxLayout44.setObjectName(u"vboxLayout44")
        self.label405 = QLabel(self.gb_maint_tools)
        self.label405.setObjectName(u"label405")

        self.vboxLayout44.addWidget(self.label405)

        self.pushButton122 = QPushButton(self.gb_maint_tools)
        self.pushButton122.setObjectName(u"pushButton122")
        self.pushButton122.setMinimumSize(QSize(0, 20))

        self.vboxLayout44.addWidget(self.pushButton122)


        self.gridLayout6.addLayout(self.vboxLayout44, 0, 0, 1, 1)

        self.vboxLayout45 = QVBoxLayout()
        self.vboxLayout45.setSpacing(4)
        self.vboxLayout45.setObjectName(u"vboxLayout45")
        self.label406 = QLabel(self.gb_maint_tools)
        self.label406.setObjectName(u"label406")

        self.vboxLayout45.addWidget(self.label406)

        self.pushButton123 = QPushButton(self.gb_maint_tools)
        self.pushButton123.setObjectName(u"pushButton123")
        self.pushButton123.setMinimumSize(QSize(0, 20))

        self.vboxLayout45.addWidget(self.pushButton123)


        self.gridLayout6.addLayout(self.vboxLayout45, 0, 1, 1, 1)

        self.vboxLayout46 = QVBoxLayout()
        self.vboxLayout46.setSpacing(4)
        self.vboxLayout46.setObjectName(u"vboxLayout46")
        self.label407 = QLabel(self.gb_maint_tools)
        self.label407.setObjectName(u"label407")

        self.vboxLayout46.addWidget(self.label407)

        self.pushButton124 = QPushButton(self.gb_maint_tools)
        self.pushButton124.setObjectName(u"pushButton124")
        self.pushButton124.setMinimumSize(QSize(0, 20))

        self.vboxLayout46.addWidget(self.pushButton124)


        self.gridLayout6.addLayout(self.vboxLayout46, 0, 2, 1, 1)

        self.vboxLayout47 = QVBoxLayout()
        self.vboxLayout47.setSpacing(4)
        self.vboxLayout47.setObjectName(u"vboxLayout47")
        self.label408 = QLabel(self.gb_maint_tools)
        self.label408.setObjectName(u"label408")

        self.vboxLayout47.addWidget(self.label408)

        self.pushButton125 = QPushButton(self.gb_maint_tools)
        self.pushButton125.setObjectName(u"pushButton125")
        self.pushButton125.setMinimumSize(QSize(0, 20))

        self.vboxLayout47.addWidget(self.pushButton125)


        self.gridLayout6.addLayout(self.vboxLayout47, 0, 3, 1, 1)

        self.vboxLayout48 = QVBoxLayout()
        self.vboxLayout48.setSpacing(4)
        self.vboxLayout48.setObjectName(u"vboxLayout48")
        self.label409 = QLabel(self.gb_maint_tools)
        self.label409.setObjectName(u"label409")

        self.vboxLayout48.addWidget(self.label409)

        self.pushButton126 = QPushButton(self.gb_maint_tools)
        self.pushButton126.setObjectName(u"pushButton126")
        self.pushButton126.setMinimumSize(QSize(0, 20))

        self.vboxLayout48.addWidget(self.pushButton126)


        self.gridLayout6.addLayout(self.vboxLayout48, 1, 0, 1, 1)

        self.vboxLayout49 = QVBoxLayout()
        self.vboxLayout49.setSpacing(4)
        self.vboxLayout49.setObjectName(u"vboxLayout49")
        self.label410 = QLabel(self.gb_maint_tools)
        self.label410.setObjectName(u"label410")

        self.vboxLayout49.addWidget(self.label410)

        self.pushButton127 = QPushButton(self.gb_maint_tools)
        self.pushButton127.setObjectName(u"pushButton127")
        self.pushButton127.setMinimumSize(QSize(0, 20))

        self.vboxLayout49.addWidget(self.pushButton127)


        self.gridLayout6.addLayout(self.vboxLayout49, 1, 1, 1, 1)

        self.vboxLayout50 = QVBoxLayout()
        self.vboxLayout50.setSpacing(4)
        self.vboxLayout50.setObjectName(u"vboxLayout50")
        self.label411 = QLabel(self.gb_maint_tools)
        self.label411.setObjectName(u"label411")

        self.vboxLayout50.addWidget(self.label411)

        self.pushButton128 = QPushButton(self.gb_maint_tools)
        self.pushButton128.setObjectName(u"pushButton128")
        self.pushButton128.setMinimumSize(QSize(0, 20))

        self.vboxLayout50.addWidget(self.pushButton128)


        self.gridLayout6.addLayout(self.vboxLayout50, 1, 2, 1, 1)

        self.vboxLayout51 = QVBoxLayout()
        self.vboxLayout51.setSpacing(4)
        self.vboxLayout51.setObjectName(u"vboxLayout51")
        self.label412 = QLabel(self.gb_maint_tools)
        self.label412.setObjectName(u"label412")

        self.vboxLayout51.addWidget(self.label412)

        self.pushButton129 = QPushButton(self.gb_maint_tools)
        self.pushButton129.setObjectName(u"pushButton129")
        self.pushButton129.setMinimumSize(QSize(0, 20))

        self.vboxLayout51.addWidget(self.pushButton129)


        self.gridLayout6.addLayout(self.vboxLayout51, 1, 3, 1, 1)


        self.vboxLayout43.addWidget(self.gb_maint_tools)

        self.hboxLayout65 = QHBoxLayout()
        self.hboxLayout65.setSpacing(4)
        self.hboxLayout65.setObjectName(u"hboxLayout65")
        self.gb_comp_health = QGroupBox(self.page_settings)
        self.gb_comp_health.setObjectName(u"gb_comp_health")
        sizePolicy.setHeightForWidth(self.gb_comp_health.sizePolicy().hasHeightForWidth())
        self.gb_comp_health.setSizePolicy(sizePolicy)
        self.vboxLayout52 = QVBoxLayout(self.gb_comp_health)
        self.vboxLayout52.setSpacing(4)
        self.vboxLayout52.setObjectName(u"vboxLayout52")
        self.tableWidget4 = QTableWidget(self.gb_comp_health)
        if (self.tableWidget4.columnCount() < 4):
            self.tableWidget4.setColumnCount(4)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget4.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget4.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget4.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget4.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        self.tableWidget4.setObjectName(u"tableWidget4")
        sizePolicy.setHeightForWidth(self.tableWidget4.sizePolicy().hasHeightForWidth())
        self.tableWidget4.setSizePolicy(sizePolicy)
        self.tableWidget4.setColumnCount(4)

        self.vboxLayout52.addWidget(self.tableWidget4)

        self.pushButton130 = QPushButton(self.gb_comp_health)
        self.pushButton130.setObjectName(u"pushButton130")
        self.pushButton130.setMinimumSize(QSize(0, 20))

        self.vboxLayout52.addWidget(self.pushButton130)


        self.hboxLayout65.addWidget(self.gb_comp_health)

        self.gb_maint_schedule = QGroupBox(self.page_settings)
        self.gb_maint_schedule.setObjectName(u"gb_maint_schedule")
        sizePolicy.setHeightForWidth(self.gb_maint_schedule.sizePolicy().hasHeightForWidth())
        self.gb_maint_schedule.setSizePolicy(sizePolicy)
        self.vboxLayout53 = QVBoxLayout(self.gb_maint_schedule)
        self.vboxLayout53.setSpacing(4)
        self.vboxLayout53.setObjectName(u"vboxLayout53")
        self.tableWidget5 = QTableWidget(self.gb_maint_schedule)
        if (self.tableWidget5.columnCount() < 5):
            self.tableWidget5.setColumnCount(5)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget5.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget5.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget5.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget5.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget5.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        self.tableWidget5.setObjectName(u"tableWidget5")
        sizePolicy.setHeightForWidth(self.tableWidget5.sizePolicy().hasHeightForWidth())
        self.tableWidget5.setSizePolicy(sizePolicy)
        self.tableWidget5.setColumnCount(5)

        self.vboxLayout53.addWidget(self.tableWidget5)

        self.pushButton131 = QPushButton(self.gb_maint_schedule)
        self.pushButton131.setObjectName(u"pushButton131")
        self.pushButton131.setMinimumSize(QSize(0, 20))

        self.vboxLayout53.addWidget(self.pushButton131)


        self.hboxLayout65.addWidget(self.gb_maint_schedule)


        self.vboxLayout43.addLayout(self.hboxLayout65)


        self.hLayout_maintenance.addLayout(self.vboxLayout43)

        self.vboxLayout54 = QVBoxLayout()
        self.vboxLayout54.setSpacing(4)
        self.vboxLayout54.setObjectName(u"vboxLayout54")
        self.gb_service_info = QGroupBox(self.page_settings)
        self.gb_service_info.setObjectName(u"gb_service_info")
        sizePolicy.setHeightForWidth(self.gb_service_info.sizePolicy().hasHeightForWidth())
        self.gb_service_info.setSizePolicy(sizePolicy)
        self.formLayout33 = QFormLayout(self.gb_service_info)
        self.formLayout33.setObjectName(u"formLayout33")
        self.formLayout33.setHorizontalSpacing(4)
        self.formLayout33.setVerticalSpacing(4)
        self.label413 = QLabel(self.gb_service_info)
        self.label413.setObjectName(u"label413")

        self.formLayout33.setWidget(0, QFormLayout.LabelRole, self.label413)

        self.label414 = QLabel(self.gb_service_info)
        self.label414.setObjectName(u"label414")

        self.formLayout33.setWidget(0, QFormLayout.FieldRole, self.label414)

        self.label415 = QLabel(self.gb_service_info)
        self.label415.setObjectName(u"label415")

        self.formLayout33.setWidget(1, QFormLayout.LabelRole, self.label415)

        self.label416 = QLabel(self.gb_service_info)
        self.label416.setObjectName(u"label416")

        self.formLayout33.setWidget(1, QFormLayout.FieldRole, self.label416)

        self.label417 = QLabel(self.gb_service_info)
        self.label417.setObjectName(u"label417")

        self.formLayout33.setWidget(2, QFormLayout.LabelRole, self.label417)

        self.label418 = QLabel(self.gb_service_info)
        self.label418.setObjectName(u"label418")

        self.formLayout33.setWidget(2, QFormLayout.FieldRole, self.label418)

        self.label419 = QLabel(self.gb_service_info)
        self.label419.setObjectName(u"label419")

        self.formLayout33.setWidget(3, QFormLayout.SpanningRole, self.label419)

        self.pushButton132 = QPushButton(self.gb_service_info)
        self.pushButton132.setObjectName(u"pushButton132")
        self.pushButton132.setMinimumSize(QSize(0, 20))

        self.formLayout33.setWidget(4, QFormLayout.SpanningRole, self.pushButton132)


        self.vboxLayout54.addWidget(self.gb_service_info)

        self.gb_maint_notes = QGroupBox(self.page_settings)
        self.gb_maint_notes.setObjectName(u"gb_maint_notes")
        sizePolicy.setHeightForWidth(self.gb_maint_notes.sizePolicy().hasHeightForWidth())
        self.gb_maint_notes.setSizePolicy(sizePolicy)
        self.vboxLayout55 = QVBoxLayout(self.gb_maint_notes)
        self.vboxLayout55.setSpacing(4)
        self.vboxLayout55.setObjectName(u"vboxLayout55")
        self.pushButton133 = QPushButton(self.gb_maint_notes)
        self.pushButton133.setObjectName(u"pushButton133")
        self.pushButton133.setMinimumSize(QSize(0, 20))

        self.vboxLayout55.addWidget(self.pushButton133)

        self.textEdit1 = QTextEdit(self.gb_maint_notes)
        self.textEdit1.setObjectName(u"textEdit1")
        sizePolicy.setHeightForWidth(self.textEdit1.sizePolicy().hasHeightForWidth())
        self.textEdit1.setSizePolicy(sizePolicy)

        self.vboxLayout55.addWidget(self.textEdit1)

        self.pushButton134 = QPushButton(self.gb_maint_notes)
        self.pushButton134.setObjectName(u"pushButton134")
        self.pushButton134.setMinimumSize(QSize(0, 20))

        self.vboxLayout55.addWidget(self.pushButton134)


        self.vboxLayout54.addWidget(self.gb_maint_notes)


        self.hLayout_maintenance.addLayout(self.vboxLayout54)

        self.stackedWidget.addWidget(self.page_settings)
        self.page_settings_2 = QWidget()
        self.page_settings_2.setObjectName(u"page_settings_2")
        self.hLayout_settings = QHBoxLayout(self.page_settings_2)
        self.hLayout_settings.setSpacing(4)
        self.hLayout_settings.setObjectName(u"hLayout_settings")
        self.tabWidget = QTabWidget(self.page_settings_2)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.gridLayout7 = QGridLayout(self.tab_general)
        self.gridLayout7.setSpacing(4)
        self.gridLayout7.setObjectName(u"gridLayout7")
        self.gb_general_settings = QGroupBox(self.tab_general)
        self.gb_general_settings.setObjectName(u"gb_general_settings")
        sizePolicy.setHeightForWidth(self.gb_general_settings.sizePolicy().hasHeightForWidth())
        self.gb_general_settings.setSizePolicy(sizePolicy)
        self.formLayout34 = QFormLayout(self.gb_general_settings)
        self.formLayout34.setObjectName(u"formLayout34")
        self.formLayout34.setHorizontalSpacing(4)
        self.formLayout34.setVerticalSpacing(4)
        self.label420 = QLabel(self.gb_general_settings)
        self.label420.setObjectName(u"label420")

        self.formLayout34.setWidget(0, QFormLayout.LabelRole, self.label420)

        self.comboBox10 = QComboBox(self.gb_general_settings)
        self.comboBox10.addItem("")
        self.comboBox10.setObjectName(u"comboBox10")

        self.formLayout34.setWidget(0, QFormLayout.FieldRole, self.comboBox10)

        self.label421 = QLabel(self.gb_general_settings)
        self.label421.setObjectName(u"label421")

        self.formLayout34.setWidget(1, QFormLayout.LabelRole, self.label421)

        self.comboBox11 = QComboBox(self.gb_general_settings)
        self.comboBox11.addItem("")
        self.comboBox11.setObjectName(u"comboBox11")

        self.formLayout34.setWidget(1, QFormLayout.FieldRole, self.comboBox11)

        self.label422 = QLabel(self.gb_general_settings)
        self.label422.setObjectName(u"label422")

        self.formLayout34.setWidget(2, QFormLayout.LabelRole, self.label422)

        self.comboBox12 = QComboBox(self.gb_general_settings)
        self.comboBox12.addItem("")
        self.comboBox12.setObjectName(u"comboBox12")

        self.formLayout34.setWidget(2, QFormLayout.FieldRole, self.comboBox12)

        self.label423 = QLabel(self.gb_general_settings)
        self.label423.setObjectName(u"label423")

        self.formLayout34.setWidget(3, QFormLayout.LabelRole, self.label423)

        self.comboBox13 = QComboBox(self.gb_general_settings)
        self.comboBox13.addItem("")
        self.comboBox13.setObjectName(u"comboBox13")

        self.formLayout34.setWidget(3, QFormLayout.FieldRole, self.comboBox13)


        self.gridLayout7.addWidget(self.gb_general_settings, 0, 0, 1, 1)

        self.gb_display_settings = QGroupBox(self.tab_general)
        self.gb_display_settings.setObjectName(u"gb_display_settings")
        sizePolicy.setHeightForWidth(self.gb_display_settings.sizePolicy().hasHeightForWidth())
        self.gb_display_settings.setSizePolicy(sizePolicy)
        self.formLayout35 = QFormLayout(self.gb_display_settings)
        self.formLayout35.setObjectName(u"formLayout35")
        self.formLayout35.setHorizontalSpacing(4)
        self.formLayout35.setVerticalSpacing(4)
        self.label424 = QLabel(self.gb_display_settings)
        self.label424.setObjectName(u"label424")

        self.formLayout35.setWidget(0, QFormLayout.LabelRole, self.label424)

        self.comboBox14 = QComboBox(self.gb_display_settings)
        self.comboBox14.addItem("")
        self.comboBox14.setObjectName(u"comboBox14")

        self.formLayout35.setWidget(0, QFormLayout.FieldRole, self.comboBox14)

        self.label425 = QLabel(self.gb_display_settings)
        self.label425.setObjectName(u"label425")

        self.formLayout35.setWidget(1, QFormLayout.LabelRole, self.label425)

        self.comboBox15 = QComboBox(self.gb_display_settings)
        self.comboBox15.addItem("")
        self.comboBox15.setObjectName(u"comboBox15")

        self.formLayout35.setWidget(1, QFormLayout.FieldRole, self.comboBox15)

        self.label426 = QLabel(self.gb_display_settings)
        self.label426.setObjectName(u"label426")

        self.formLayout35.setWidget(2, QFormLayout.LabelRole, self.label426)

        self.checkBox5 = QCheckBox(self.gb_display_settings)
        self.checkBox5.setObjectName(u"checkBox5")

        self.formLayout35.setWidget(2, QFormLayout.FieldRole, self.checkBox5)


        self.gridLayout7.addWidget(self.gb_display_settings, 0, 1, 1, 1)

        self.gb_notif_settings = QGroupBox(self.tab_general)
        self.gb_notif_settings.setObjectName(u"gb_notif_settings")
        sizePolicy.setHeightForWidth(self.gb_notif_settings.sizePolicy().hasHeightForWidth())
        self.gb_notif_settings.setSizePolicy(sizePolicy)
        self.formLayout36 = QFormLayout(self.gb_notif_settings)
        self.formLayout36.setObjectName(u"formLayout36")
        self.formLayout36.setHorizontalSpacing(4)
        self.formLayout36.setVerticalSpacing(4)
        self.label427 = QLabel(self.gb_notif_settings)
        self.label427.setObjectName(u"label427")

        self.formLayout36.setWidget(0, QFormLayout.LabelRole, self.label427)

        self.checkBox6 = QCheckBox(self.gb_notif_settings)
        self.checkBox6.setObjectName(u"checkBox6")

        self.formLayout36.setWidget(0, QFormLayout.FieldRole, self.checkBox6)

        self.label428 = QLabel(self.gb_notif_settings)
        self.label428.setObjectName(u"label428")

        self.formLayout36.setWidget(1, QFormLayout.LabelRole, self.label428)

        self.checkBox7 = QCheckBox(self.gb_notif_settings)
        self.checkBox7.setObjectName(u"checkBox7")

        self.formLayout36.setWidget(1, QFormLayout.FieldRole, self.checkBox7)

        self.pushButton135 = QPushButton(self.gb_notif_settings)
        self.pushButton135.setObjectName(u"pushButton135")
        self.pushButton135.setMinimumSize(QSize(0, 20))

        self.formLayout36.setWidget(2, QFormLayout.SpanningRole, self.pushButton135)


        self.gridLayout7.addWidget(self.gb_notif_settings, 0, 2, 1, 1)

        self.gb_alarm_thresholds = QGroupBox(self.tab_general)
        self.gb_alarm_thresholds.setObjectName(u"gb_alarm_thresholds")
        sizePolicy.setHeightForWidth(self.gb_alarm_thresholds.sizePolicy().hasHeightForWidth())
        self.gb_alarm_thresholds.setSizePolicy(sizePolicy)
        self.vboxLayout56 = QVBoxLayout(self.gb_alarm_thresholds)
        self.vboxLayout56.setSpacing(4)
        self.vboxLayout56.setObjectName(u"vboxLayout56")
        self.tableWidget6 = QTableWidget(self.gb_alarm_thresholds)
        if (self.tableWidget6.columnCount() < 3):
            self.tableWidget6.setColumnCount(3)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget6.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget6.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget6.setHorizontalHeaderItem(2, __qtablewidgetitem38)
        self.tableWidget6.setObjectName(u"tableWidget6")
        sizePolicy.setHeightForWidth(self.tableWidget6.sizePolicy().hasHeightForWidth())
        self.tableWidget6.setSizePolicy(sizePolicy)
        self.tableWidget6.setColumnCount(3)

        self.vboxLayout56.addWidget(self.tableWidget6)

        self.pushButton136 = QPushButton(self.gb_alarm_thresholds)
        self.pushButton136.setObjectName(u"pushButton136")
        self.pushButton136.setMinimumSize(QSize(0, 20))

        self.vboxLayout56.addWidget(self.pushButton136)


        self.gridLayout7.addWidget(self.gb_alarm_thresholds, 1, 0, 1, 1)

        self.gb_file_settings = QGroupBox(self.tab_general)
        self.gb_file_settings.setObjectName(u"gb_file_settings")
        sizePolicy.setHeightForWidth(self.gb_file_settings.sizePolicy().hasHeightForWidth())
        self.gb_file_settings.setSizePolicy(sizePolicy)
        self.formLayout37 = QFormLayout(self.gb_file_settings)
        self.formLayout37.setObjectName(u"formLayout37")
        self.formLayout37.setHorizontalSpacing(4)
        self.formLayout37.setVerticalSpacing(4)
        self.label429 = QLabel(self.gb_file_settings)
        self.label429.setObjectName(u"label429")

        self.formLayout37.setWidget(0, QFormLayout.LabelRole, self.label429)

        self.lineEdit10 = QLineEdit(self.gb_file_settings)
        self.lineEdit10.setObjectName(u"lineEdit10")

        self.formLayout37.setWidget(0, QFormLayout.FieldRole, self.lineEdit10)

        self.label430 = QLabel(self.gb_file_settings)
        self.label430.setObjectName(u"label430")

        self.formLayout37.setWidget(1, QFormLayout.LabelRole, self.label430)

        self.lineEdit11 = QLineEdit(self.gb_file_settings)
        self.lineEdit11.setObjectName(u"lineEdit11")

        self.formLayout37.setWidget(1, QFormLayout.FieldRole, self.lineEdit11)

        self.label431 = QLabel(self.gb_file_settings)
        self.label431.setObjectName(u"label431")

        self.formLayout37.setWidget(2, QFormLayout.LabelRole, self.label431)

        self.checkBox8 = QCheckBox(self.gb_file_settings)
        self.checkBox8.setObjectName(u"checkBox8")

        self.formLayout37.setWidget(2, QFormLayout.FieldRole, self.checkBox8)


        self.gridLayout7.addWidget(self.gb_file_settings, 1, 1, 1, 1)

        self.gb_data_backup = QGroupBox(self.tab_general)
        self.gb_data_backup.setObjectName(u"gb_data_backup")
        sizePolicy.setHeightForWidth(self.gb_data_backup.sizePolicy().hasHeightForWidth())
        self.gb_data_backup.setSizePolicy(sizePolicy)
        self.vboxLayout57 = QVBoxLayout(self.gb_data_backup)
        self.vboxLayout57.setSpacing(4)
        self.vboxLayout57.setObjectName(u"vboxLayout57")
        self.pushButton137 = QPushButton(self.gb_data_backup)
        self.pushButton137.setObjectName(u"pushButton137")
        self.pushButton137.setMinimumSize(QSize(0, 20))

        self.vboxLayout57.addWidget(self.pushButton137)

        self.pushButton138 = QPushButton(self.gb_data_backup)
        self.pushButton138.setObjectName(u"pushButton138")
        self.pushButton138.setMinimumSize(QSize(0, 20))

        self.vboxLayout57.addWidget(self.pushButton138)

        self.pushButton139 = QPushButton(self.gb_data_backup)
        self.pushButton139.setObjectName(u"pushButton139")
        self.pushButton139.setMinimumSize(QSize(0, 20))

        self.vboxLayout57.addWidget(self.pushButton139)


        self.gridLayout7.addWidget(self.gb_data_backup, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_general, "")

        self.hLayout_settings.addWidget(self.tabWidget)

        self.vboxLayout58 = QVBoxLayout()
        self.vboxLayout58.setSpacing(4)
        self.vboxLayout58.setObjectName(u"vboxLayout58")
        self.gb_sys_info = QGroupBox(self.page_settings_2)
        self.gb_sys_info.setObjectName(u"gb_sys_info")
        sizePolicy.setHeightForWidth(self.gb_sys_info.sizePolicy().hasHeightForWidth())
        self.gb_sys_info.setSizePolicy(sizePolicy)
        self.formLayout38 = QFormLayout(self.gb_sys_info)
        self.formLayout38.setObjectName(u"formLayout38")
        self.formLayout38.setHorizontalSpacing(4)
        self.formLayout38.setVerticalSpacing(4)
        self.label432 = QLabel(self.gb_sys_info)
        self.label432.setObjectName(u"label432")

        self.formLayout38.setWidget(0, QFormLayout.LabelRole, self.label432)

        self.label433 = QLabel(self.gb_sys_info)
        self.label433.setObjectName(u"label433")

        self.formLayout38.setWidget(0, QFormLayout.FieldRole, self.label433)

        self.label434 = QLabel(self.gb_sys_info)
        self.label434.setObjectName(u"label434")

        self.formLayout38.setWidget(1, QFormLayout.LabelRole, self.label434)

        self.label435 = QLabel(self.gb_sys_info)
        self.label435.setObjectName(u"label435")

        self.formLayout38.setWidget(1, QFormLayout.FieldRole, self.label435)

        self.label436 = QLabel(self.gb_sys_info)
        self.label436.setObjectName(u"label436")

        self.formLayout38.setWidget(2, QFormLayout.LabelRole, self.label436)

        self.label437 = QLabel(self.gb_sys_info)
        self.label437.setObjectName(u"label437")

        self.formLayout38.setWidget(2, QFormLayout.FieldRole, self.label437)


        self.vboxLayout58.addWidget(self.gb_sys_info)

        self.gb_data_mgmt = QGroupBox(self.page_settings_2)
        self.gb_data_mgmt.setObjectName(u"gb_data_mgmt")
        sizePolicy.setHeightForWidth(self.gb_data_mgmt.sizePolicy().hasHeightForWidth())
        self.gb_data_mgmt.setSizePolicy(sizePolicy)
        self.vboxLayout59 = QVBoxLayout(self.gb_data_mgmt)
        self.vboxLayout59.setSpacing(4)
        self.vboxLayout59.setObjectName(u"vboxLayout59")
        self.pushButton140 = QPushButton(self.gb_data_mgmt)
        self.pushButton140.setObjectName(u"pushButton140")
        self.pushButton140.setMinimumSize(QSize(0, 20))

        self.vboxLayout59.addWidget(self.pushButton140)

        self.pushButton141 = QPushButton(self.gb_data_mgmt)
        self.pushButton141.setObjectName(u"pushButton141")
        self.pushButton141.setMinimumSize(QSize(0, 20))

        self.vboxLayout59.addWidget(self.pushButton141)


        self.vboxLayout58.addWidget(self.gb_data_mgmt)

        self.gb_quick_settings = QGroupBox(self.page_settings_2)
        self.gb_quick_settings.setObjectName(u"gb_quick_settings")
        sizePolicy.setHeightForWidth(self.gb_quick_settings.sizePolicy().hasHeightForWidth())
        self.gb_quick_settings.setSizePolicy(sizePolicy)
        self.vboxLayout60 = QVBoxLayout(self.gb_quick_settings)
        self.vboxLayout60.setSpacing(4)
        self.vboxLayout60.setObjectName(u"vboxLayout60")
        self.pushButton142 = QPushButton(self.gb_quick_settings)
        self.pushButton142.setObjectName(u"pushButton142")
        self.pushButton142.setMinimumSize(QSize(0, 20))

        self.vboxLayout60.addWidget(self.pushButton142)

        self.pushButton143 = QPushButton(self.gb_quick_settings)
        self.pushButton143.setObjectName(u"pushButton143")
        self.pushButton143.setMinimumSize(QSize(0, 20))

        self.vboxLayout60.addWidget(self.pushButton143)

        self.pushButton144 = QPushButton(self.gb_quick_settings)
        self.pushButton144.setObjectName(u"pushButton144")
        self.pushButton144.setMinimumSize(QSize(0, 20))

        self.vboxLayout60.addWidget(self.pushButton144)


        self.vboxLayout58.addWidget(self.gb_quick_settings)


        self.hLayout_settings.addLayout(self.vboxLayout58)

        self.stackedWidget.addWidget(self.page_settings_2)

        self.rightAreaLayout.addWidget(self.stackedWidget)


        self.mainLayout.addLayout(self.rightAreaLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metal 3D Printer Control Panel", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"    QMainWindow { background-color: #0d1117; }\n"
"    QFrame { background-color: #161b22; border-radius: 8px; color: #FFFFFF; }\n"
"    QLabel { color: #8b949e; font-family: 'Segoe UI', Arial; }\n"
"    QPushButton { background-color: #21262d; border: 1px solid #30363d; border-radius: 4px; color: #c9d1d9; padding: 6px; }\n"
"    QPushButton:hover { background-color: #30363d; }\n"
"    QPushButton:checked { background-color: #1f6feb; color: white; border: none; }\n"
"    QGroupBox { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; margin-top: 1ex; color: #FFFFFF; font-weight: bold; }\n"
"    QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; color: #8b949e; }\n"
"    QComboBox { background-color: #0d1117; border: 1px solid #30363d; border-radius: 4px; color: white; padding: 4px; }\n"
"    QProgressBar { border: 1px solid #30363d; border-radius: 4px; text-align: center; color: white; }\n"
"    QProgressBar::chunk { background-color: #1f6feb"
                        "; }\n"
"    QLineEdit { background-color: #0d1117; border: 1px solid #30363d; border-radius: 4px; color: white; padding: 4px; }\n"
"   ", None))
        self.logoLabel.setText(QCoreApplication.translate("MainWindow", u"<b style='color:white; font-size:16px;'>METAL 3D PRINTER</b><br/><span style='font-size:12px;'>CONTROL PANEL</span>", None))
        self.btnDashboard.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.btnBuildSetup.setText(QCoreApplication.translate("MainWindow", u"BUILD SETUP", None))
        self.btnGCode.setText(QCoreApplication.translate("MainWindow", u"G-CODE", None))
        self.btnMachineControl.setText(QCoreApplication.translate("MainWindow", u"MACHINE CONTROL", None))
        self.btnLaserGalvo.setText(QCoreApplication.translate("MainWindow", u"LASER / GALVO", None))
        self.btnMotors.setText(QCoreApplication.translate("MainWindow", u"MOTORS", None))
        self.btnSensors.setText(QCoreApplication.translate("MainWindow", u"SENSORS", None))
        self.btnAlarmEvents.setText(QCoreApplication.translate("MainWindow", u"ALARM / EVENTS", None))
        self.btnLogs.setText(QCoreApplication.translate("MainWindow", u"LOGS", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.btnSettings_2.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.btnEmergencyStop.setStyleSheet(QCoreApplication.translate("MainWindow", u"QPushButton { background-color: #3b1618; color: #f85149; border: 1px solid #f85149; } QPushButton:hover { background-color: #4b1a1c; }", None))
        self.btnEmergencyStop.setText(QCoreApplication.translate("MainWindow", u"EMERGENCY STOP", None))
        self.lblConnectionStatus.setText(QCoreApplication.translate("MainWindow", u"CONNECTION\n"
"\ud83d\udfe2 Connected", None))
        self.comboPort.setItemText(0, QCoreApplication.translate("MainWindow", u"COM5", None))

        self.btnDisconnect.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #f85149; border-color: #f85149; background: transparent;", None))
        self.btnDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.lblJobInfo.setText(QCoreApplication.translate("MainWindow", u"JOB\n"
"gear_sample.gcode\n"
"Layer: 245 / 1250", None))
        self.comboUser.setItemText(0, QCoreApplication.translate("MainWindow", u"\ud83d\udc64 USER: Operator", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><body>SYSTEM UPTIME<br><b style='color:white;'>2d 14h 32m</b></body></html>", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"<html><body>BUILD PLATE TEMP.<br><b style='color:white;'>160.5 \u00b0C</b></body></html>", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"<html><body>BASE PLATE TEMP.<br><b style='color:white;'>118.3 \u00b0C</b></body></html>", None))
        self.label3.setText(QCoreApplication.translate("MainWindow", u"<html><body>SCAN HEAD TEMP.<br><b style='color:white;'>36.2 \u00b0C</b></body></html>", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"<html><body>POWDER LEVEL<br><b style='color:white;'>78%</b></body></html>", None))
        self.label5.setText(QCoreApplication.translate("MainWindow", u"<html><body>FILTER STATUS<br><b style='color:#3fb950;'>\ud83d\udfe2 Good</b></body></html>", None))
        self.label6.setText(QCoreApplication.translate("MainWindow", u"<html><body>07 Jul 2026<br>10:46:23 AM</body></html>", None))
        self.gb_machine_status.setTitle(QCoreApplication.translate("MainWindow", u"MACHINE STATUS", None))
        self.lbl_status_icon.setText(QCoreApplication.translate("MainWindow", u"[Icon]", None))
        self.lbl_status_text.setText(QCoreApplication.translate("MainWindow", u"<b>Ready</b><br>All systems normal", None))
        self.gb_build_progress.setTitle(QCoreApplication.translate("MainWindow", u"BUILD PROGRESS", None))
        self.lbl_prog_circle.setText(QCoreApplication.translate("MainWindow", u"[Dial Graphic]", None))
        self.label7.setText(QCoreApplication.translate("MainWindow", u"Layer", None))
        self.label8.setText(QCoreApplication.translate("MainWindow", u"245 / 1250", None))
        self.label9.setText(QCoreApplication.translate("MainWindow", u"Time Elapsed", None))
        self.label10.setText(QCoreApplication.translate("MainWindow", u"01:24:30", None))
        self.label11.setText(QCoreApplication.translate("MainWindow", u"Est. Remaining", None))
        self.label12.setText(QCoreApplication.translate("MainWindow", u"05:38:15", None))
        self.gb_laser_power_dash.setTitle(QCoreApplication.translate("MainWindow", u"LASER POWER", None))
        self.lbl_laser_gauge.setText(QCoreApplication.translate("MainWindow", u"[Dial Graphic]", None))
        self.gb_chamber_temp_dash.setTitle(QCoreApplication.translate("MainWindow", u"CHAMBER TEMP.", None))
        self.label13.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.label14.setText(QCoreApplication.translate("MainWindow", u"<b>32.5 C</b>", None))
        self.label15.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label16.setText(QCoreApplication.translate("MainWindow", u"35 C", None))
        self.label17.setText(QCoreApplication.translate("MainWindow", u"Gas/Flow", None))
        self.label18.setText(QCoreApplication.translate("MainWindow", u"Argon 12.5 L/min", None))
        self.gb_oxygen_level_dash.setTitle(QCoreApplication.translate("MainWindow", u"OXYGEN LEVEL", None))
        self.lbl_oxy_gauge.setText(QCoreApplication.translate("MainWindow", u"[Dial Graphic]", None))
        self.gb_build_preview_dash.setTitle(QCoreApplication.translate("MainWindow", u"BUILD PREVIEW", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Rot", None))
        self.pushButton1.setText(QCoreApplication.translate("MainWindow", u"Pan", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"Zoom", None))
        self.pushButton3.setText(QCoreApplication.translate("MainWindow", u"Top", None))
        self.pushButton4.setText(QCoreApplication.translate("MainWindow", u"Frt", None))
        self.pushButton5.setText(QCoreApplication.translate("MainWindow", u"Rgt", None))
        self.pushButton6.setText(QCoreApplication.translate("MainWindow", u"Rst", None))
        self.label19.setText(QCoreApplication.translate("MainWindow", u"3D PREVIEW GRAPHIC", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Show Travels", None))
        self.checkBox1.setText(QCoreApplication.translate("MainWindow", u"Show Layers", None))
        self.label20.setText(QCoreApplication.translate("MainWindow", u"Layer: 245", None))
        self.gb_axis_position.setTitle(QCoreApplication.translate("MainWindow", u"AXIS POSITION (mm)", None))
        self.uposlcddisplay.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.zposlcddisplay.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.galvohomepushButton.setText(QCoreApplication.translate("MainWindow", u"Galvo Home", None))
        self.vposlcddisplay.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.allhomepushButton.setText(QCoreApplication.translate("MainWindow", u"Home All Axis", None))
        self.label21.setText(QCoreApplication.translate("MainWindow", u"<font color='#3B82F6'>U</font>", None))
        self.label22.setText(QCoreApplication.translate("MainWindow", u"<font color='#F59E0B'>Z</font>", None))
        self.label23.setText(QCoreApplication.translate("MainWindow", u"<font color='#10B981'>V</font>", None))
        self.gb_jog_control.setTitle(QCoreApplication.translate("MainWindow", u"JOG CONTROL", None))
        self.travelpushButton_1.setText(QCoreApplication.translate("MainWindow", u"0.01", None))
        self.travelpushButton_2.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color:#2563EB;", None))
        self.travelpushButton_2.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.travelpushButton_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.travelpushButton_4.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.travelpushButton_5.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.upluspushButton.setText(QCoreApplication.translate("MainWindow", u"+U", None))
        self.vminuspushButton.setText(QCoreApplication.translate("MainWindow", u"-V", None))
        self.pushButton7.setText(QCoreApplication.translate("MainWindow", u"UV", None))
        self.vpluspushButton.setText(QCoreApplication.translate("MainWindow", u"+V", None))
        self.uminuspushButton.setText(QCoreApplication.translate("MainWindow", u"-U", None))
        self.zpluspushButton.setText(QCoreApplication.translate("MainWindow", u"+Z", None))
        self.zminuspushButton.setText(QCoreApplication.translate("MainWindow", u"-Z", None))
        self.gb_job_control.setTitle(QCoreApplication.translate("MainWindow", u"JOB CONTROL", None))
        self.pushButton8.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color:#2563EB; font-weight:bold;", None))
        self.pushButton8.setText(QCoreApplication.translate("MainWindow", u"Start / Resume", None))
        self.pushButton9.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.pushButton10.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton11.setText(QCoreApplication.translate("MainWindow", u"Abort Job", None))
        self.gb_layer_control_dash.setTitle(QCoreApplication.translate("MainWindow", u"LAYER CONTROL", None))
        self.label24.setText(QCoreApplication.translate("MainWindow", u"245 / 1250", None))
        self.pushButton12.setText(QCoreApplication.translate("MainWindow", u"-10", None))
        self.pushButton13.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.pushButton14.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.pushButton15.setText(QCoreApplication.translate("MainWindow", u"+10", None))
        self.pushButton16.setText(QCoreApplication.translate("MainWindow", u"Go to Layer", None))
        self.gb_console_log.setTitle(QCoreApplication.translate("MainWindow", u"CONSOLE LOG", None))
        self.textEdit.setProperty(u"text", QCoreApplication.translate("MainWindow", u"<font color='#10B981'>[10:42:11] System initialized</font><br><font color='#10B981'>[10:42:13] Connection established on COM5</font><br><font color='#3B82F6'>[10:42:15] File loaded: gear_sample.gcode</font><br><font color='#10B981'>[10:42:17] Build job ready</font><br><font color='#10B981'>[10:42:20] Build started</font><br><font color='#3B82F6'>[10:43:33] Layer 100 completed</font><br><font color='#F59E0B'>[10:46:23] Layer 245 in progress</font>", None))
        self.pushButton17.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.checkBox2.setText(QCoreApplication.translate("MainWindow", u"Auto Scroll", None))
        self.gb_overrides.setTitle(QCoreApplication.translate("MainWindow", u"OVERRIDES", None))
        self.lbl_override_laser.setText(QCoreApplication.translate("MainWindow", u"[Dial Graphic]", None))
        self.lbl_override_scan.setText(QCoreApplication.translate("MainWindow", u"[Dial Graphic]", None))
        self.lbl_override_hatch.setText(QCoreApplication.translate("MainWindow", u"[Dial Graphic]", None))
        self.gb_build_files.setTitle(QCoreApplication.translate("MainWindow", u"BUILD FILES", None))
        self.btn_import_build.setText(QCoreApplication.translate("MainWindow", u"+ Import Build", None))
        self.btn_refresh_build.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.gb_machine_profile.setTitle(QCoreApplication.translate("MainWindow", u"MACHINE PROFILE", None))
        self.gb_material_profile.setTitle(QCoreApplication.translate("MainWindow", u"MATERIAL PROFILE", None))
        self.gb_build_preview.setTitle(QCoreApplication.translate("MainWindow", u"BUILD PREVIEW", None))
        self.btn_view_iso.setText(QCoreApplication.translate("MainWindow", u"ISO", None))
        self.btn_view_top.setText(QCoreApplication.translate("MainWindow", u"Top", None))
        self.btn_view_front.setText(QCoreApplication.translate("MainWindow", u"Front", None))
        self.lbl_3d_preview_placeholder.setText(QCoreApplication.translate("MainWindow", u"3D Preview Placeholder", None))
        self.btn_rotate.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.btn_pan.setText(QCoreApplication.translate("MainWindow", u"Pan", None))
        self.btn_zoom.setText(QCoreApplication.translate("MainWindow", u"Zoom", None))
        self.chk_section_view.setText(QCoreApplication.translate("MainWindow", u"Section View", None))
        self.gb_job_info.setTitle(QCoreApplication.translate("MainWindow", u"JOB INFORMATION", None))
        self.lbl_job_name.setText(QCoreApplication.translate("MainWindow", u"Job Name", None))
        self.val_job_name.setText(QCoreApplication.translate("MainWindow", u"gear_sample.gcode", None))
        self.lbl_job_material.setText(QCoreApplication.translate("MainWindow", u"Material", None))
        self.val_job_material.setText(QCoreApplication.translate("MainWindow", u"SS 316L", None))
        self.lbl_job_thickness.setText(QCoreApplication.translate("MainWindow", u"Layer Thickness", None))
        self.val_job_thickness.setText(QCoreApplication.translate("MainWindow", u"0.03 mm", None))
        self.lbl_job_layers.setText(QCoreApplication.translate("MainWindow", u"Total Layers", None))
        self.val_job_layers.setText(QCoreApplication.translate("MainWindow", u"1250", None))
        self.lbl_job_btime.setText(QCoreApplication.translate("MainWindow", u"Build Time", None))
        self.val_job_btime.setText(QCoreApplication.translate("MainWindow", u"07h 36m", None))
        self.lbl_job_powder.setText(QCoreApplication.translate("MainWindow", u"Powder Required", None))
        self.val_job_powder.setText(QCoreApplication.translate("MainWindow", u"3.42 kg", None))
        self.lbl_job_parts.setText(QCoreApplication.translate("MainWindow", u"Number of Parts", None))
        self.val_job_parts.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.gb_validation.setTitle(QCoreApplication.translate("MainWindow", u"VALIDATION", None))
        self.lbl_val_vol.setText(QCoreApplication.translate("MainWindow", u"Build Volume Check", None))
        self.val_val_vol.setText(QCoreApplication.translate("MainWindow", u"Passed", None))
        self.lbl_val_mat.setText(QCoreApplication.translate("MainWindow", u"Material Check", None))
        self.val_val_mat.setText(QCoreApplication.translate("MainWindow", u"Passed", None))
        self.lbl_val_geo.setText(QCoreApplication.translate("MainWindow", u"Geometry Check", None))
        self.val_val_geo.setText(QCoreApplication.translate("MainWindow", u"Passed", None))
        self.lbl_val_comp.setText(QCoreApplication.translate("MainWindow", u"Machine Compatibility", None))
        self.val_val_comp.setText(QCoreApplication.translate("MainWindow", u"Passed", None))
        self.gb_est_stats.setTitle(QCoreApplication.translate("MainWindow", u"ESTIMATED STATISTICS", None))
        self.lbl_stat_time.setText(QCoreApplication.translate("MainWindow", u"Build Time", None))
        self.val_stat_time.setText(QCoreApplication.translate("MainWindow", u"07h 36m", None))
        self.lbl_stat_scan.setText(QCoreApplication.translate("MainWindow", u"Scan Time", None))
        self.val_stat_scan.setText(QCoreApplication.translate("MainWindow", u"06h 15m", None))
        self.lbl_stat_jump.setText(QCoreApplication.translate("MainWindow", u"Jump Time", None))
        self.val_stat_jump.setText(QCoreApplication.translate("MainWindow", u"01h 21m", None))
        self.lbl_stat_layers.setText(QCoreApplication.translate("MainWindow", u"Layers", None))
        self.val_stat_layers.setText(QCoreApplication.translate("MainWindow", u"1250", None))
        self.lbl_stat_scan_len.setText(QCoreApplication.translate("MainWindow", u"Total Scan Length", None))
        self.val_stat_scan_len.setText(QCoreApplication.translate("MainWindow", u"1,245.36 m", None))
        self.lbl_stat_jump_len.setText(QCoreApplication.translate("MainWindow", u"Total Jump Length", None))
        self.val_stat_jump_len.setText(QCoreApplication.translate("MainWindow", u"231.45 m", None))
        self.lbl_stat_powder.setText(QCoreApplication.translate("MainWindow", u"Powder Required", None))
        self.val_stat_powder.setText(QCoreApplication.translate("MainWindow", u"3.42 kg", None))
        self.lbl_stat_power.setText(QCoreApplication.translate("MainWindow", u"Avg. Laser Power", None))
        self.val_stat_power.setText(QCoreApplication.translate("MainWindow", u"195 W", None))
        self.lbl_stat_energy.setText(QCoreApplication.translate("MainWindow", u"Energy / Layer", None))
        self.val_stat_energy.setText(QCoreApplication.translate("MainWindow", u"4.32 kJ", None))
        self.gb_actions.setTitle(QCoreApplication.translate("MainWindow", u"ACTIONS", None))
        self.btn_verify_build.setText(QCoreApplication.translate("MainWindow", u"Verify Build", None))
        self.btn_send_queue.setText(QCoreApplication.translate("MainWindow", u"Send to Queue", None))
        self.btn_prepare_machine.setText(QCoreApplication.translate("MainWindow", u"Prepare Machine", None))
        self.gb_build_queue.setTitle(QCoreApplication.translate("MainWindow", u"BUILD QUEUE", None))
        ___qtablewidgetitem = self.tableWidget_queue.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem1 = self.tableWidget_queue.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Job Name", None));
        ___qtablewidgetitem2 = self.tableWidget_queue.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem3 = self.tableWidget_queue.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Layers", None));
        ___qtablewidgetitem4 = self.tableWidget_queue.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Estimated Time", None));
        ___qtablewidgetitem5 = self.tableWidget_queue.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.gb_build_notes.setTitle(QCoreApplication.translate("MainWindow", u"BUILD NOTES", None))
        self.txt_build_notes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add notes about this build...", None))
        self.btn_save_notes.setText(QCoreApplication.translate("MainWindow", u"Save Notes", None))
        self.gb_layer_controls.setTitle(QCoreApplication.translate("MainWindow", u"LAYER CONTROLS", None))
        self.lbl_layer_text.setText(QCoreApplication.translate("MainWindow", u"Layer", None))
        self.lbl_layer_val.setText(QCoreApplication.translate("MainWindow", u"245 / 1250", None))
        self.btn_layer_first.setText(QCoreApplication.translate("MainWindow", u"|<", None))
        self.btn_layer_prev.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.btn_layer_next.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.btn_layer_last.setText(QCoreApplication.translate("MainWindow", u">|", None))
        self.btn_jump_layer.setText(QCoreApplication.translate("MainWindow", u"Jump to Layer", None))
        self.lbl_range_text.setText(QCoreApplication.translate("MainWindow", u"Layer Range", None))
        self.lbl_range_val.setText(QCoreApplication.translate("MainWindow", u"1 - 1250", None))
        self.gb_display_options.setTitle(QCoreApplication.translate("MainWindow", u"DISPLAY OPTIONS", None))
        self.chk_show_contours.setText(QCoreApplication.translate("MainWindow", u"Show Contours", None))
        self.chk_show_hatch.setText(QCoreApplication.translate("MainWindow", u"Show Hatch", None))
        self.chk_show_supports.setText(QCoreApplication.translate("MainWindow", u"Show Supports", None))
        self.chk_show_jump.setText(QCoreApplication.translate("MainWindow", u"Show Jump Moves", None))
        self.chk_show_scan_dir.setText(QCoreApplication.translate("MainWindow", u"Show Scan Direction", None))
        self.chk_only_current.setText(QCoreApplication.translate("MainWindow", u"Only Current Layer", None))
        self.gb_view_mode.setTitle(QCoreApplication.translate("MainWindow", u"VIEW MODE", None))
        self.btn_view_2d.setText(QCoreApplication.translate("MainWindow", u"2D", None))
        self.btn_view_3d.setText(QCoreApplication.translate("MainWindow", u"3D", None))
        self.btn_view_25d.setText(QCoreApplication.translate("MainWindow", u"2.5D", None))
        self.gb_layer_info.setTitle(QCoreApplication.translate("MainWindow", u"LAYER INFORMATION", None))
        self.lbl_linfo_thick.setText(QCoreApplication.translate("MainWindow", u"Layer Thickness", None))
        self.val_linfo_thick.setText(QCoreApplication.translate("MainWindow", u"0.03 mm", None))
        self.lbl_linfo_ltime.setText(QCoreApplication.translate("MainWindow", u"Layer Time", None))
        self.val_linfo_ltime.setText(QCoreApplication.translate("MainWindow", u"12.45 s", None))
        self.lbl_linfo_stime.setText(QCoreApplication.translate("MainWindow", u"Scan Time", None))
        self.val_linfo_stime.setText(QCoreApplication.translate("MainWindow", u"10.32 s", None))
        self.lbl_linfo_jtime.setText(QCoreApplication.translate("MainWindow", u"Jump Time", None))
        self.val_linfo_jtime.setText(QCoreApplication.translate("MainWindow", u"2.13 s", None))
        self.lbl_linfo_hlen.setText(QCoreApplication.translate("MainWindow", u"Hatch Length", None))
        self.val_linfo_hlen.setText(QCoreApplication.translate("MainWindow", u"125.43 m", None))
        self.lbl_linfo_jlen.setText(QCoreApplication.translate("MainWindow", u"Jump Length", None))
        self.val_linfo_jlen.setText(QCoreApplication.translate("MainWindow", u"18.27 m", None))
        self.lbl_linfo_energy.setText(QCoreApplication.translate("MainWindow", u"Energy / Layer", None))
        self.val_linfo_energy.setText(QCoreApplication.translate("MainWindow", u"4.32 kJ", None))
        self.lbl_coord_x.setText(QCoreApplication.translate("MainWindow", u"X: 45.230 mm\n"
"Min: -90.000\n"
"Max: 90.000", None))
        self.lbl_coord_y.setText(QCoreApplication.translate("MainWindow", u"Y: 67.890 mm\n"
"Min: -90.000\n"
"Max: 90.000", None))
        self.lbl_coord_z.setText(QCoreApplication.translate("MainWindow", u"Z: 7.320 mm\n"
"Min: 0.000\n"
"Max: 37.500", None))
        self.lbl_coord_zoom.setText(QCoreApplication.translate("MainWindow", u"Zoom: 2.36x\n"
"Speed: 2500 mm/s\n"
"Power: 195 W", None))
        self.gb_layer_thumbnails.setTitle(QCoreApplication.translate("MainWindow", u"LAYER THUMBNAILS", None))
        self.btn_thumb_prev.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.lbl_thumb_1.setText(QCoreApplication.translate("MainWindow", u"243", None))
        self.lbl_thumb_2.setText(QCoreApplication.translate("MainWindow", u"244", None))
        self.lbl_thumb_3.setText(QCoreApplication.translate("MainWindow", u"245", None))
        self.lbl_thumb_4.setText(QCoreApplication.translate("MainWindow", u"246", None))
        self.lbl_thumb_5.setText(QCoreApplication.translate("MainWindow", u"247", None))
        self.btn_thumb_next.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.gb_scan_strategy.setTitle(QCoreApplication.translate("MainWindow", u"SCAN STRATEGY", None))
        self.lbl_strat_type.setText(QCoreApplication.translate("MainWindow", u"Strategy", None))
        self.val_strat_type.setText(QCoreApplication.translate("MainWindow", u"Island Scan", None))
        self.lbl_strat_rot.setText(QCoreApplication.translate("MainWindow", u"Rotation Angle", None))
        self.val_strat_rot.setText(QCoreApplication.translate("MainWindow", u"67\u00b0", None))
        self.lbl_strat_hatch.setText(QCoreApplication.translate("MainWindow", u"Hatch Spacing", None))
        self.val_strat_hatch.setText(QCoreApplication.translate("MainWindow", u"0.10 mm", None))
        self.lbl_strat_hatch_angle.setText(QCoreApplication.translate("MainWindow", u"Hatch Angle", None))
        self.val_strat_hatch_angle.setText(QCoreApplication.translate("MainWindow", u"67\u00b0", None))
        self.lbl_strat_island.setText(QCoreApplication.translate("MainWindow", u"Island Size", None))
        self.val_strat_island.setText(QCoreApplication.translate("MainWindow", u"5.00 mm", None))
        self.lbl_strat_border.setText(QCoreApplication.translate("MainWindow", u"Border Offset", None))
        self.val_strat_border.setText(QCoreApplication.translate("MainWindow", u"0.05 mm", None))
        self.lbl_strat_contour.setText(QCoreApplication.translate("MainWindow", u"Contour Offset", None))
        self.val_strat_contour.setText(QCoreApplication.translate("MainWindow", u"0.02 mm", None))
        self.lbl_strat_img_placeholder.setText(QCoreApplication.translate("MainWindow", u"Strategy\n"
"Image", None))
        self.gb_layer_statistics.setTitle(QCoreApplication.translate("MainWindow", u"LAYER STATISTICS", None))
        self.lbl_stats_pie_placeholder.setText(QCoreApplication.translate("MainWindow", u"Pie Chart", None))
        self.lbl_stat_contour.setText(QCoreApplication.translate("MainWindow", u"Contour", None))
        self.val_stat_contour.setText(QCoreApplication.translate("MainWindow", u"12.45 m (6.2%)", None))
        self.lbl_stat_hatch.setText(QCoreApplication.translate("MainWindow", u"Hatch", None))
        self.val_stat_hatch.setText(QCoreApplication.translate("MainWindow", u"125.43 m (62.7%)", None))
        self.lbl_stat_supp.setText(QCoreApplication.translate("MainWindow", u"Supports", None))
        self.val_stat_supp.setText(QCoreApplication.translate("MainWindow", u"32.18 m (16.1%)", None))
        self.lbl_stat_jump1.setText(QCoreApplication.translate("MainWindow", u"Jump Moves", None))
        self.val_stat_jump1.setText(QCoreApplication.translate("MainWindow", u"30.27 m (15.0%)", None))
        self.lbl_stat_total.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.val_stat_total.setText(QCoreApplication.translate("MainWindow", u"200.33 m", None))
        self.gb_layer_actions.setTitle(QCoreApplication.translate("MainWindow", u"ACTIONS", None))
        self.btn_act_export_img.setText(QCoreApplication.translate("MainWindow", u"Export Layer Image", None))
        self.btn_act_export_data.setText(QCoreApplication.translate("MainWindow", u"Export Layer Data", None))
        self.btn_act_simulate.setText(QCoreApplication.translate("MainWindow", u"Simulate From Here", None))
        self.btn_act_clear.setText(QCoreApplication.translate("MainWindow", u"Clear Selection", None))
        self.gb_build_platform.setTitle(QCoreApplication.translate("MainWindow", u"BUILD PLATFORM", None))
        self.label25.setText(QCoreApplication.translate("MainWindow", u"Position\n"
"125.300 mm", None))
        self.label26.setText(QCoreApplication.translate("MainWindow", u"Status\n"
"Ready", None))
        self.pushButton18.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.pushButton19.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.pushButton20.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton21.setText(QCoreApplication.translate("MainWindow", u"Move To...", None))
        self.label27.setText(QCoreApplication.translate("MainWindow", u"[Graphic]", None))
        self.label28.setText(QCoreApplication.translate("MainWindow", u"Target (mm)", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"125.300", None))
        self.pushButton22.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.gb_powder_feed.setTitle(QCoreApplication.translate("MainWindow", u"POWDER FEED", None))
        self.label29.setText(QCoreApplication.translate("MainWindow", u"Position\n"
"45.670 mm", None))
        self.label30.setText(QCoreApplication.translate("MainWindow", u"Status\n"
"Ready", None))
        self.pushButton23.setText(QCoreApplication.translate("MainWindow", u"Raise", None))
        self.pushButton24.setText(QCoreApplication.translate("MainWindow", u"Lower", None))
        self.pushButton25.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label31.setText(QCoreApplication.translate("MainWindow", u"[Graphic]", None))
        self.label32.setText(QCoreApplication.translate("MainWindow", u"Target (mm)", None))
        self.lineEdit1.setText(QCoreApplication.translate("MainWindow", u"45.670", None))
        self.pushButton26.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.gb_recoater.setTitle(QCoreApplication.translate("MainWindow", u"RECOATER", None))
        self.label33.setText(QCoreApplication.translate("MainWindow", u"Position\n"
"0.00 mm", None))
        self.label34.setText(QCoreApplication.translate("MainWindow", u"Status\n"
"Ready", None))
        self.label35.setText(QCoreApplication.translate("MainWindow", u"[Recoater Graphic]", None))
        self.pushButton27.setText(QCoreApplication.translate("MainWindow", u"Move Left", None))
        self.pushButton28.setText(QCoreApplication.translate("MainWindow", u"Move Right", None))
        self.pushButton29.setText(QCoreApplication.translate("MainWindow", u"Home Recoater", None))
        self.pushButton30.setText(QCoreApplication.translate("MainWindow", u"Single Spread Cycle", None))
        self.gb_chamber_door.setTitle(QCoreApplication.translate("MainWindow", u"CHAMBER DOOR", None))
        self.label36.setText(QCoreApplication.translate("MainWindow", u"Status\n"
"Closed & Locked", None))
        self.label37.setText(QCoreApplication.translate("MainWindow", u"[Door Graphic]", None))
        self.pushButton31.setText(QCoreApplication.translate("MainWindow", u"Unlock", None))
        self.pushButton32.setText(QCoreApplication.translate("MainWindow", u"Open Door", None))
        self.gb_gas_system.setTitle(QCoreApplication.translate("MainWindow", u"GAS SYSTEM", None))
        self.label38.setText(QCoreApplication.translate("MainWindow", u"Argon Pressure", None))
        self.label39.setText(QCoreApplication.translate("MainWindow", u"12.3 bar", None))
        self.label40.setText(QCoreApplication.translate("MainWindow", u"Argon Flow", None))
        self.label41.setText(QCoreApplication.translate("MainWindow", u"12.5 L/min", None))
        self.label42.setText(QCoreApplication.translate("MainWindow", u"Nitrogen Pressure", None))
        self.label43.setText(QCoreApplication.translate("MainWindow", u"11.8 bar", None))
        self.label44.setText(QCoreApplication.translate("MainWindow", u"Chamber Pressure", None))
        self.label45.setText(QCoreApplication.translate("MainWindow", u"-0.02 bar", None))
        self.label46.setText(QCoreApplication.translate("MainWindow", u"PURGE CONTROL", None))
        self.pushButton33.setText(QCoreApplication.translate("MainWindow", u"Start Purge", None))
        self.pushButton34.setText(QCoreApplication.translate("MainWindow", u"Stop Purge", None))
        self.label47.setText(QCoreApplication.translate("MainWindow", u"Auto Purge", None))
        self.checkBox3.setText("")
        self.label48.setText(QCoreApplication.translate("MainWindow", u"Elapsed 00:05:32", None))
        self.gb_environment_control.setTitle(QCoreApplication.translate("MainWindow", u"ENVIRONMENT CONTROL", None))
        self.label49.setText(QCoreApplication.translate("MainWindow", u"Chamber Temp.", None))
        self.label50.setText(QCoreApplication.translate("MainWindow", u"32.5 C", None))
        self.label51.setText(QCoreApplication.translate("MainWindow", u"Set Temperature", None))
        self.label52.setText(QCoreApplication.translate("MainWindow", u"35.0 C", None))
        self.label53.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.label54.setText(QCoreApplication.translate("MainWindow", u"15.3 %", None))
        self.label55.setText(QCoreApplication.translate("MainWindow", u"Oxygen Level", None))
        self.label56.setText(QCoreApplication.translate("MainWindow", u"0.05 %", None))
        self.label57.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURE CONTROL", None))
        self.label58.setText(QCoreApplication.translate("MainWindow", u"Set Temperature (C)", None))
        self.lineEdit2.setText(QCoreApplication.translate("MainWindow", u"35.0", None))
        self.pushButton35.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label59.setText(QCoreApplication.translate("MainWindow", u"Heater Status: ON", None))
        self.gb_auxiliary_systems.setTitle(QCoreApplication.translate("MainWindow", u"AUXILIARY SYSTEMS", None))
        self.label60.setText(QCoreApplication.translate("MainWindow", u"Filter Unit", None))
        self.label61.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton36.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label62.setText(QCoreApplication.translate("MainWindow", u"Powder Vac System", None))
        self.label63.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton37.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label64.setText(QCoreApplication.translate("MainWindow", u"Cooling System", None))
        self.label65.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton38.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label66.setText(QCoreApplication.translate("MainWindow", u"Exhaust System", None))
        self.label67.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton39.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.gb_quick_actions.setTitle(QCoreApplication.translate("MainWindow", u"QUICK ACTIONS", None))
        self.pushButton40.setText(QCoreApplication.translate("MainWindow", u"System Home", None))
        self.pushButton41.setText(QCoreApplication.translate("MainWindow", u"Safe Position", None))
        self.pushButton42.setText(QCoreApplication.translate("MainWindow", u"System Check", None))
        self.pushButton43.setText(QCoreApplication.translate("MainWindow", u"Zero All Axes", None))
        self.pushButton44.setText(QCoreApplication.translate("MainWindow", u"Unlock All", None))
        self.pushButton45.setText(QCoreApplication.translate("MainWindow", u"Refresh Status", None))
        self.gb_laser_control.setTitle(QCoreApplication.translate("MainWindow", u"LASER CONTROL", None))
        self.label68.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label69.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label70.setText(QCoreApplication.translate("MainWindow", u"Laser State", None))
        self.label71.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.label72.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.label73.setText(QCoreApplication.translate("MainWindow", u"CW", None))
        self.pushButton46.setText(QCoreApplication.translate("MainWindow", u"Laser Enable", None))
        self.pushButton47.setText(QCoreApplication.translate("MainWindow", u"Laser Disable", None))
        self.label74.setText(QCoreApplication.translate("MainWindow", u"LASER POWER", None))
        self.label75.setText(QCoreApplication.translate("MainWindow", u"[Dial Graphic]", None))
        self.label76.setText(QCoreApplication.translate("MainWindow", u"Set Power", None))
        self.lineEdit3.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label77.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.pushButton48.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label78.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.label79.setText(QCoreApplication.translate("MainWindow", u"50 kHz", None))
        self.label80.setText(QCoreApplication.translate("MainWindow", u"Duty Cycle", None))
        self.label81.setText(QCoreApplication.translate("MainWindow", u"100 %", None))
        self.label82.setText(QCoreApplication.translate("MainWindow", u"Pulse Width", None))
        self.label83.setText(QCoreApplication.translate("MainWindow", u"200 ns", None))
        self.label84.setText(QCoreApplication.translate("MainWindow", u"Beam Diameter", None))
        self.label85.setText(QCoreApplication.translate("MainWindow", u"70 \u03bcm", None))
        self.label86.setText(QCoreApplication.translate("MainWindow", u"Wavelength", None))
        self.label87.setText(QCoreApplication.translate("MainWindow", u"1070 nm", None))
        self.label88.setText(QCoreApplication.translate("MainWindow", u"Laser Hours", None))
        self.label89.setText(QCoreApplication.translate("MainWindow", u"1245.6 h", None))
        self.label90.setText(QCoreApplication.translate("MainWindow", u"Laser Temperature", None))
        self.label91.setText(QCoreApplication.translate("MainWindow", u"25.2 C", None))
        self.label92.setText(QCoreApplication.translate("MainWindow", u"Driver Temperature", None))
        self.label93.setText(QCoreApplication.translate("MainWindow", u"31.4 C", None))
        self.gb_galvo_control.setTitle(QCoreApplication.translate("MainWindow", u"GALVO CONTROL", None))
        self.label94.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label95.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label96.setText(QCoreApplication.translate("MainWindow", u"Galvo State", None))
        self.label97.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.label98.setText(QCoreApplication.translate("MainWindow", u"Scan Field", None))
        self.label99.setText(QCoreApplication.translate("MainWindow", u"160 mm", None))
        self.pushButton49.setText(QCoreApplication.translate("MainWindow", u"Galvo Enable", None))
        self.pushButton50.setText(QCoreApplication.translate("MainWindow", u"Galvo Disable", None))
        self.label100.setText(QCoreApplication.translate("MainWindow", u"GALVO SPEED", None))
        self.label101.setText(QCoreApplication.translate("MainWindow", u"[Dial Graphic]", None))
        self.label102.setText(QCoreApplication.translate("MainWindow", u"Set Speed", None))
        self.lineEdit4.setText(QCoreApplication.translate("MainWindow", u"16000", None))
        self.label103.setText(QCoreApplication.translate("MainWindow", u"mm/s", None))
        self.pushButton51.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label104.setText(QCoreApplication.translate("MainWindow", u"X Offset", None))
        self.label105.setText(QCoreApplication.translate("MainWindow", u"0.000 mm", None))
        self.label106.setText(QCoreApplication.translate("MainWindow", u"Y Offset", None))
        self.label107.setText(QCoreApplication.translate("MainWindow", u"0.000 mm", None))
        self.label108.setText(QCoreApplication.translate("MainWindow", u"X Scale", None))
        self.label109.setText(QCoreApplication.translate("MainWindow", u"1.000", None))
        self.label110.setText(QCoreApplication.translate("MainWindow", u"Y Scale", None))
        self.label111.setText(QCoreApplication.translate("MainWindow", u"1.000", None))
        self.label112.setText(QCoreApplication.translate("MainWindow", u"Galvo Hours", None))
        self.label113.setText(QCoreApplication.translate("MainWindow", u"1240.0 h", None))
        self.label114.setText(QCoreApplication.translate("MainWindow", u"Mirror Temp X", None))
        self.label115.setText(QCoreApplication.translate("MainWindow", u"27.2 C", None))
        self.label116.setText(QCoreApplication.translate("MainWindow", u"Mirror Temp Y", None))
        self.label117.setText(QCoreApplication.translate("MainWindow", u"28.4 C", None))
        self.gb_laser_diag.setTitle(QCoreApplication.translate("MainWindow", u"LASER DIAGNOSTICS", None))
        self.label118.setText(QCoreApplication.translate("MainWindow", u"Laser Source", None))
        self.label119.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label160.setText(QCoreApplication.translate("MainWindow", u"Power Supply", None))
        self.label121.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label122.setText(QCoreApplication.translate("MainWindow", u"Water Cooling", None))
        self.label123.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label124.setText(QCoreApplication.translate("MainWindow", u"Interlock Status", None))
        self.label125.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label126.setText(QCoreApplication.translate("MainWindow", u"Emission Status", None))
        self.label127.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label128.setText(QCoreApplication.translate("MainWindow", u"Error Code", None))
        self.label129.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label130.setText(QCoreApplication.translate("MainWindow", u"DETAILS", None))
        self.label131.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.label132.setText(QCoreApplication.translate("MainWindow", u"32.5 A", None))
        self.label133.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.label134.setText(QCoreApplication.translate("MainWindow", u"24.1 V", None))
        self.label135.setText(QCoreApplication.translate("MainWindow", u"Cooling Flow", None))
        self.label136.setText(QCoreApplication.translate("MainWindow", u"2.35 L/min", None))
        self.label137.setText(QCoreApplication.translate("MainWindow", u"Water Temp. In", None))
        self.label138.setText(QCoreApplication.translate("MainWindow", u"22.1 C", None))
        self.label139.setText(QCoreApplication.translate("MainWindow", u"Water Temp. Out", None))
        self.label140.setText(QCoreApplication.translate("MainWindow", u"24.8 C", None))
        self.gb_galvo_diag.setTitle(QCoreApplication.translate("MainWindow", u"GALVO DIAGNOSTICS", None))
        self.label141.setText(QCoreApplication.translate("MainWindow", u"X Axis Driver", None))
        self.label142.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label143.setText(QCoreApplication.translate("MainWindow", u"Y Axis Driver", None))
        self.label144.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label145.setText(QCoreApplication.translate("MainWindow", u"X Axis Feedback", None))
        self.label146.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label147.setText(QCoreApplication.translate("MainWindow", u"Y Axis Feedback", None))
        self.label148.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label149.setText(QCoreApplication.translate("MainWindow", u"Interlock Status", None))
        self.label150.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label151.setText(QCoreApplication.translate("MainWindow", u"Error Code", None))
        self.label152.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label153.setText(QCoreApplication.translate("MainWindow", u"DETAILS", None))
        self.label154.setText(QCoreApplication.translate("MainWindow", u"X Position", None))
        self.label155.setText(QCoreApplication.translate("MainWindow", u"0.000 mm", None))
        self.label156.setText(QCoreApplication.translate("MainWindow", u"Y Position", None))
        self.label157.setText(QCoreApplication.translate("MainWindow", u"0.000 mm", None))
        self.label158.setText(QCoreApplication.translate("MainWindow", u"X Actual Speed", None))
        self.label159.setText(QCoreApplication.translate("MainWindow", u"0 mm/s", None))
        self.label160.setText(QCoreApplication.translate("MainWindow", u"Y Actual Speed", None))
        self.label161.setText(QCoreApplication.translate("MainWindow", u"0 mm/s", None))
        self.label162.setText(QCoreApplication.translate("MainWindow", u"Tracking Error", None))
        self.label163.setText(QCoreApplication.translate("MainWindow", u"0.002 mm", None))
        self.gb_test_patterns.setTitle(QCoreApplication.translate("MainWindow", u"TEST PATTERNS", None))
        self.pushButton52.setText(QCoreApplication.translate("MainWindow", u"Mark Square", None))
        self.pushButton53.setText(QCoreApplication.translate("MainWindow", u"Mark Circle", None))
        self.pushButton54.setText(QCoreApplication.translate("MainWindow", u"Cross Hair", None))
        self.pushButton55.setText(QCoreApplication.translate("MainWindow", u"Spiral", None))
        self.pushButton56.setText(QCoreApplication.translate("MainWindow", u"Line Test", None))
        self.pushButton57.setText(QCoreApplication.translate("MainWindow", u"Custom Pattern", None))
        self.gb_pattern_settings.setTitle(QCoreApplication.translate("MainWindow", u"PATTERN SETTINGS", None))
        self.label164.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.lineEdit5.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label165.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.lineEdit6.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label166.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.lineEdit7.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label167.setText(QCoreApplication.translate("MainWindow", u"Loops", None))
        self.lineEdit8.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton58.setText(QCoreApplication.translate("MainWindow", u"Run Pattern", None))
        self.gb_calibration.setTitle(QCoreApplication.translate("MainWindow", u"CALIBRATION", None))
        self.label168.setText(QCoreApplication.translate("MainWindow", u"GALVO FIELD CALIBRATION\n"
"Calibrate the galvo scan field and linearity.", None))
        self.pushButton59.setText(QCoreApplication.translate("MainWindow", u"Start Calibration", None))
        self.pushButton60.setText(QCoreApplication.translate("MainWindow", u"View Last Result", None))
        self.label169.setText(QCoreApplication.translate("MainWindow", u"[Grid Graphic]", None))
        self.label170.setText(QCoreApplication.translate("MainWindow", u"DELAY COMPENSATION\n"
"Adjust laser on/off delay for corners.", None))
        self.pushButton61.setText(QCoreApplication.translate("MainWindow", u"Start Calibration", None))
        self.pushButton62.setText(QCoreApplication.translate("MainWindow", u"View Last Result", None))
        self.label171.setText(QCoreApplication.translate("MainWindow", u"[Plot Graphic]", None))
        self.label172.setText(QCoreApplication.translate("MainWindow", u"LASER POWER CALIBRATION\n"
"Calibrate actual laser power output.", None))
        self.pushButton63.setText(QCoreApplication.translate("MainWindow", u"Start Calibration", None))
        self.pushButton64.setText(QCoreApplication.translate("MainWindow", u"View Last Result", None))
        self.label173.setText(QCoreApplication.translate("MainWindow", u"[Curve Graphic]", None))
        self.label174.setText(QCoreApplication.translate("MainWindow", u"LAST CALIBRATION", None))
        self.label175.setText(QCoreApplication.translate("MainWindow", u"Galvo Field", None))
        self.label176.setText(QCoreApplication.translate("MainWindow", u"07 Jul 2026 Pass", None))
        self.label177.setText(QCoreApplication.translate("MainWindow", u"Delay Comp.", None))
        self.label178.setText(QCoreApplication.translate("MainWindow", u"07 Jul 2026 Pass", None))
        self.label179.setText(QCoreApplication.translate("MainWindow", u"Laser Power", None))
        self.label180.setText(QCoreApplication.translate("MainWindow", u"07 Jul 2026 Pass", None))
        self.gb_motor_build.setTitle(QCoreApplication.translate("MainWindow", u"BUILD PLATFORM MOTOR", None))
        self.label181.setText(QCoreApplication.translate("MainWindow", u"[Icon]", None))
        self.label182.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label183.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label184.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label185.setText(QCoreApplication.translate("MainWindow", u"125.300 mm", None))
        self.label186.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.label187.setText(QCoreApplication.translate("MainWindow", u"2.0 mm/s", None))
        self.label188.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.label189.setText(QCoreApplication.translate("MainWindow", u"1.25 A", None))
        self.label190.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label191.setText(QCoreApplication.translate("MainWindow", u"18 %", None))
        self.label192.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.pushButton65.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton66.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.pushButton67.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.label193.setText(QCoreApplication.translate("MainWindow", u"Jog", None))
        self.pushButton68.setText(QCoreApplication.translate("MainWindow", u"-10", None))
        self.pushButton69.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.pushButton70.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.pushButton71.setText(QCoreApplication.translate("MainWindow", u"+10", None))
        self.gb_motor_powder.setTitle(QCoreApplication.translate("MainWindow", u"POWDER FEED MOTOR", None))
        self.label194.setText(QCoreApplication.translate("MainWindow", u"[Icon]", None))
        self.label195.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label196.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label197.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label198.setText(QCoreApplication.translate("MainWindow", u"45.670 mm", None))
        self.label199.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.label200.setText(QCoreApplication.translate("MainWindow", u"1.5 mm/s", None))
        self.label201.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.label202.setText(QCoreApplication.translate("MainWindow", u"1.02 A", None))
        self.label203.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label204.setText(QCoreApplication.translate("MainWindow", u"16 %", None))
        self.label205.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.pushButton72.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton73.setText(QCoreApplication.translate("MainWindow", u"Raise", None))
        self.pushButton74.setText(QCoreApplication.translate("MainWindow", u"Lower", None))
        self.label206.setText(QCoreApplication.translate("MainWindow", u"Jog", None))
        self.pushButton75.setText(QCoreApplication.translate("MainWindow", u"-10", None))
        self.pushButton76.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.pushButton77.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.pushButton78.setText(QCoreApplication.translate("MainWindow", u"+10", None))
        self.gb_motor_recoater.setTitle(QCoreApplication.translate("MainWindow", u"RECOATER MOTOR", None))
        self.label207.setText(QCoreApplication.translate("MainWindow", u"[Icon]", None))
        self.label208.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label209.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label210.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label211.setText(QCoreApplication.translate("MainWindow", u"0.000 mm", None))
        self.label212.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.label213.setText(QCoreApplication.translate("MainWindow", u"150.0 mm/s", None))
        self.label214.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.label215.setText(QCoreApplication.translate("MainWindow", u"1.80 A", None))
        self.label216.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label217.setText(QCoreApplication.translate("MainWindow", u"22 %", None))
        self.label218.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.pushButton79.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton80.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.pushButton81.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.label219.setText(QCoreApplication.translate("MainWindow", u"Jog", None))
        self.pushButton82.setText(QCoreApplication.translate("MainWindow", u"-10", None))
        self.pushButton83.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.pushButton84.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.pushButton85.setText(QCoreApplication.translate("MainWindow", u"+10", None))
        self.gb_motor_piston.setTitle(QCoreApplication.translate("MainWindow", u"POWDER FEED PISTON MOTOR", None))
        self.label220.setText(QCoreApplication.translate("MainWindow", u"[Icon]", None))
        self.label221.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label222.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label223.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label224.setText(QCoreApplication.translate("MainWindow", u"12.450 mm", None))
        self.label225.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.label226.setText(QCoreApplication.translate("MainWindow", u"2.5 mm/s", None))
        self.label227.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.label228.setText(QCoreApplication.translate("MainWindow", u"0.85 A", None))
        self.label229.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label230.setText(QCoreApplication.translate("MainWindow", u"12 %", None))
        self.label231.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.pushButton86.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton87.setText(QCoreApplication.translate("MainWindow", u"Extend", None))
        self.pushButton88.setText(QCoreApplication.translate("MainWindow", u"Retract", None))
        self.label232.setText(QCoreApplication.translate("MainWindow", u"Jog", None))
        self.pushButton89.setText(QCoreApplication.translate("MainWindow", u"-10", None))
        self.pushButton90.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.pushButton91.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.pushButton92.setText(QCoreApplication.translate("MainWindow", u"+10", None))
        self.gb_motors_overview.setTitle(QCoreApplication.translate("MainWindow", u"MOTORS OVERVIEW", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Motor", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Velocity", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Current", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Load", None));
        self.gb_motor_diag.setTitle(QCoreApplication.translate("MainWindow", u"MOTOR DIAGNOSTICS", None))
        self.label233.setText(QCoreApplication.translate("MainWindow", u"Driver Status", None))
        self.label234.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label235.setText(QCoreApplication.translate("MainWindow", u"Encoder Status", None))
        self.label236.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label237.setText(QCoreApplication.translate("MainWindow", u"Overcurrent", None))
        self.label238.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label239.setText(QCoreApplication.translate("MainWindow", u"Overvoltage", None))
        self.label240.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label241.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label242.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label243.setText(QCoreApplication.translate("MainWindow", u"Communication", None))
        self.label244.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label245.setText(QCoreApplication.translate("MainWindow", u"Limit Switch", None))
        self.label246.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.gb_motor_temp.setTitle(QCoreApplication.translate("MainWindow", u"TEMPERATURES", None))
        self.label247.setText(QCoreApplication.translate("MainWindow", u"Build Motor", None))
        self.label248.setText(QCoreApplication.translate("MainWindow", u"32.1 C [Bar]", None))
        self.label249.setText(QCoreApplication.translate("MainWindow", u"Feed Motor", None))
        self.label250.setText(QCoreApplication.translate("MainWindow", u"30.4 C [Bar]", None))
        self.label251.setText(QCoreApplication.translate("MainWindow", u"Recoater Motor", None))
        self.label252.setText(QCoreApplication.translate("MainWindow", u"33.6 C [Bar]", None))
        self.label253.setText(QCoreApplication.translate("MainWindow", u"Piston Motor", None))
        self.label254.setText(QCoreApplication.translate("MainWindow", u"28.7 C [Bar]", None))
        self.label255.setText(QCoreApplication.translate("MainWindow", u"Z Lift Motor", None))
        self.label256.setText(QCoreApplication.translate("MainWindow", u"31.2 C [Bar]", None))
        self.gb_motor_actions.setTitle(QCoreApplication.translate("MainWindow", u"ACTIONS", None))
        self.pushButton93.setText(QCoreApplication.translate("MainWindow", u"Home All Axes", None))
        self.pushButton94.setText(QCoreApplication.translate("MainWindow", u"Disable All Motors", None))
        self.pushButton95.setText(QCoreApplication.translate("MainWindow", u"Reset All Alarms", None))
        self.pushButton96.setText(QCoreApplication.translate("MainWindow", u"Clear Faults", None))
        self.gb_motor_graph.setTitle(QCoreApplication.translate("MainWindow", u"MOTOR GRAPH", None))
        self.pushButton97.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.pushButton98.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.pushButton99.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.pushButton100.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label257.setText(QCoreApplication.translate("MainWindow", u"[Graph Placeholder]", None))
        self.gb_graph_settings.setTitle(QCoreApplication.translate("MainWindow", u"GRAPH SETTINGS", None))
        self.label258.setText(QCoreApplication.translate("MainWindow", u"Time Range", None))
        self.label259.setText(QCoreApplication.translate("MainWindow", u"Auto Refresh", None))
        self.gb_motor_info.setTitle(QCoreApplication.translate("MainWindow", u"MOTOR INFORMATION", None))
        self.label260.setText(QCoreApplication.translate("MainWindow", u"Total Motors", None))
        self.label261.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label262.setText(QCoreApplication.translate("MainWindow", u"Enabled Motors", None))
        self.label263.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label264.setText(QCoreApplication.translate("MainWindow", u"Disabled Motors", None))
        self.label265.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label266.setText(QCoreApplication.translate("MainWindow", u"Active Alarms", None))
        self.label267.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label268.setText(QCoreApplication.translate("MainWindow", u"Total Faults", None))
        self.label269.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.gb_env.setTitle(QCoreApplication.translate("MainWindow", u"ENVIRONMENT", None))
        self.label270.setText(QCoreApplication.translate("MainWindow", u"Chamber Temperature", None))
        self.label271.setText(QCoreApplication.translate("MainWindow", u"32.5 C", None))
        self.label272.setText(QCoreApplication.translate("MainWindow", u"Set Temperature", None))
        self.label273.setText(QCoreApplication.translate("MainWindow", u"35.0 C", None))
        self.label274.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.label275.setText(QCoreApplication.translate("MainWindow", u"15.3 %", None))
        self.label276.setText(QCoreApplication.translate("MainWindow", u"Oxygen Level", None))
        self.label277.setText(QCoreApplication.translate("MainWindow", u"0.05 %", None))
        self.label278.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.label279.setText(QCoreApplication.translate("MainWindow", u"-0.02 bar", None))
        self.label280.setText(QCoreApplication.translate("MainWindow", u"Atmospheric Pressure", None))
        self.label281.setText(QCoreApplication.translate("MainWindow", u"1.02 bar", None))
        self.gb_gas.setTitle(QCoreApplication.translate("MainWindow", u"GAS SYSTEM", None))
        self.label282.setText(QCoreApplication.translate("MainWindow", u"Argon Pressure", None))
        self.label283.setText(QCoreApplication.translate("MainWindow", u"12.3 bar", None))
        self.label284.setText(QCoreApplication.translate("MainWindow", u"Argon Flow", None))
        self.label285.setText(QCoreApplication.translate("MainWindow", u"12.5 L/min", None))
        self.label286.setText(QCoreApplication.translate("MainWindow", u"Nitrogen Pressure", None))
        self.label287.setText(QCoreApplication.translate("MainWindow", u"11.8 bar", None))
        self.label288.setText(QCoreApplication.translate("MainWindow", u"Gas Inlet Pressure", None))
        self.label289.setText(QCoreApplication.translate("MainWindow", u"12.1 bar", None))
        self.label290.setText(QCoreApplication.translate("MainWindow", u"Gas Outlet Pressure", None))
        self.label291.setText(QCoreApplication.translate("MainWindow", u"11.9 bar", None))
        self.label292.setText(QCoreApplication.translate("MainWindow", u"Gas Purity (O2)", None))
        self.label293.setText(QCoreApplication.translate("MainWindow", u"0.05 %", None))
        self.gb_powder.setTitle(QCoreApplication.translate("MainWindow", u"POWDER SYSTEM", None))
        self.label294.setText(QCoreApplication.translate("MainWindow", u"Powder Level", None))
        self.label295.setText(QCoreApplication.translate("MainWindow", u"78 % [Bar]", None))
        self.label296.setText(QCoreApplication.translate("MainWindow", u"Overflow Sensor", None))
        self.label297.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label298.setText(QCoreApplication.translate("MainWindow", u"Hopper Level Sensor", None))
        self.label299.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label300.setText(QCoreApplication.translate("MainWindow", u"Feed Piston Upper Limit", None))
        self.label301.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label302.setText(QCoreApplication.translate("MainWindow", u"Feed Piston Lower Limit", None))
        self.label303.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.gb_door.setTitle(QCoreApplication.translate("MainWindow", u"CHAMBER DOOR", None))
        self.label304.setText(QCoreApplication.translate("MainWindow", u"Door Status", None))
        self.label305.setText(QCoreApplication.translate("MainWindow", u"Closed & Locked", None))
        self.label306.setText(QCoreApplication.translate("MainWindow", u"Door Lock", None))
        self.label307.setText(QCoreApplication.translate("MainWindow", u"Locked", None))
        self.label308.setText(QCoreApplication.translate("MainWindow", u"Safety Interlock", None))
        self.label309.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label310.setText(QCoreApplication.translate("MainWindow", u"Door Seal Pressure", None))
        self.label311.setText(QCoreApplication.translate("MainWindow", u"-0.01 bar", None))
        self.gb_safety.setTitle(QCoreApplication.translate("MainWindow", u"SAFETY SYSTEMS", None))
        self.label312.setText(QCoreApplication.translate("MainWindow", u"Emergency Stop", None))
        self.label313.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label314.setText(QCoreApplication.translate("MainWindow", u"Safety PLC", None))
        self.label315.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label316.setText(QCoreApplication.translate("MainWindow", u"Laser Safety Interlock", None))
        self.label317.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label318.setText(QCoreApplication.translate("MainWindow", u"Door Interlock", None))
        self.label319.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label320.setText(QCoreApplication.translate("MainWindow", u"Gas Pressure Switch", None))
        self.label321.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label322.setText(QCoreApplication.translate("MainWindow", u"Over Temp Switch", None))
        self.label323.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label324.setText(QCoreApplication.translate("MainWindow", u"Smoke Detector", None))
        self.label325.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label326.setText(QCoreApplication.translate("MainWindow", u"Fire Suppression", None))
        self.label327.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label328.setText(QCoreApplication.translate("MainWindow", u"Power Supply Status", None))
        self.label329.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label330.setText(QCoreApplication.translate("MainWindow", u"Ground Fault", None))
        self.label331.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.gb_temps.setTitle(QCoreApplication.translate("MainWindow", u"TEMPERATURES", None))
        self.label332.setText(QCoreApplication.translate("MainWindow", u"Laser Head Temp.\n"
"25.2 C", None))
        self.label333.setText(QCoreApplication.translate("MainWindow", u"Chiller Inlet Temp.\n"
"22.1 C", None))
        self.label334.setText(QCoreApplication.translate("MainWindow", u"Galvo Driver Temp.\n"
"27.2 C", None))
        self.label335.setText(QCoreApplication.translate("MainWindow", u"Chiller Outlet Temp.\n"
"24.8 C", None))
        self.label336.setText(QCoreApplication.translate("MainWindow", u"Power Supply Temp.\n"
"31.4 C", None))
        self.label337.setText(QCoreApplication.translate("MainWindow", u"Powder Bed Temp.\n"
"32.5 C", None))
        self.label338.setText(QCoreApplication.translate("MainWindow", u"Control Cabinet Temp.\n"
"30.1 C", None))
        self.label339.setText(QCoreApplication.translate("MainWindow", u"Recoater Motor Temp.\n"
"33.6 C", None))
        self.gb_misc.setTitle(QCoreApplication.translate("MainWindow", u"MISCELLANEOUS", None))
        self.label340.setText(QCoreApplication.translate("MainWindow", u"UPS Status", None))
        self.label341.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label342.setText(QCoreApplication.translate("MainWindow", u"Main Power", None))
        self.label343.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.label344.setText(QCoreApplication.translate("MainWindow", u"24V Power Supply", None))
        self.label345.setText(QCoreApplication.translate("MainWindow", u"24.1 V", None))
        self.label346.setText(QCoreApplication.translate("MainWindow", u"5V Power Supply", None))
        self.label347.setText(QCoreApplication.translate("MainWindow", u"5.02 V", None))
        self.label348.setText(QCoreApplication.translate("MainWindow", u"Battery Voltage", None))
        self.label349.setText(QCoreApplication.translate("MainWindow", u"25.6 V", None))
        self.label350.setText(QCoreApplication.translate("MainWindow", u"Air Pressure", None))
        self.label351.setText(QCoreApplication.translate("MainWindow", u"6.5 bar", None))
        self.label352.setText(QCoreApplication.translate("MainWindow", u"Water Flow (Chiller)", None))
        self.label353.setText(QCoreApplication.translate("MainWindow", u"2.35 L/min", None))
        self.label354.setText(QCoreApplication.translate("MainWindow", u"Filter Diff. Pressure", None))
        self.label355.setText(QCoreApplication.translate("MainWindow", u"78 Pa", None))
        self.gb_sensor_overview.setTitle(QCoreApplication.translate("MainWindow", u"SENSOR STATUS OVERVIEW", None))
        self.label356.setText(QCoreApplication.translate("MainWindow", u"[Pie Chart]", None))
        self.label357.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label358.setText(QCoreApplication.translate("MainWindow", u"42", None))
        self.label359.setText(QCoreApplication.translate("MainWindow", u"Warning", None))
        self.label360.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label361.setText(QCoreApplication.translate("MainWindow", u"Fault", None))
        self.label362.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label363.setText(QCoreApplication.translate("MainWindow", u"Total Sensors", None))
        self.label364.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.gb_history.setTitle(QCoreApplication.translate("MainWindow", u"SENSOR HISTORY (Last 1 Hour)", None))
        self.label365.setText(QCoreApplication.translate("MainWindow", u"[Line Chart]", None))
        self.gb_filter.setTitle(QCoreApplication.translate("MainWindow", u"SENSOR FILTER", None))
        self.label366.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label367.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.pushButton101.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.gb_calibration_sensors.setTitle(QCoreApplication.translate("MainWindow", u"SENSOR CALIBRATION", None))
        ___qtablewidgetitem12 = self.tableWidget1.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Sensor", None));
        ___qtablewidgetitem13 = self.tableWidget1.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Last Calibrated", None));
        ___qtablewidgetitem14 = self.tableWidget1.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Next Due", None));
        ___qtablewidgetitem15 = self.tableWidget1.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.pushButton102.setText(QCoreApplication.translate("MainWindow", u"View All Calibration", None))
        self.gb_active_alarms.setTitle(QCoreApplication.translate("MainWindow", u"ACTIVE ALARMS (3)", None))
        self.label368.setText(QCoreApplication.translate("MainWindow", u"<b>OXYGEN LEVEL HIGH</b><br>Oxygen level is above limit. [Critical]", None))
        self.label369.setText(QCoreApplication.translate("MainWindow", u"<b>RECOATER MOTOR OVERLOAD</b><br>Recoater motor current exceeds limit. [Major]", None))
        self.label370.setText(QCoreApplication.translate("MainWindow", u"<b>POWDER LEVEL LOW</b><br>Powder level is below warning limit. [Warning]", None))
        self.pushButton103.setText(QCoreApplication.translate("MainWindow", u"Acknowledge All", None))
        self.pushButton104.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.gb_alarm_summary.setTitle(QCoreApplication.translate("MainWindow", u"ALARM SUMMARY", None))
        self.label371.setText(QCoreApplication.translate("MainWindow", u"3\n"
"Active", None))
        self.label372.setText(QCoreApplication.translate("MainWindow", u"2\n"
"Unacknowledged", None))
        self.label373.setText(QCoreApplication.translate("MainWindow", u"5\n"
"Warnings (24H)", None))
        self.label374.setText(QCoreApplication.translate("MainWindow", u"0\n"
"Alarms Cleared (24H)", None))
        self.gb_alarm_category.setTitle(QCoreApplication.translate("MainWindow", u"ALARM BY CATEGORY", None))
        self.label375.setText(QCoreApplication.translate("MainWindow", u"[Pie Chart]", None))
        self.label376.setText(QCoreApplication.translate("MainWindow", u"Environment", None))
        self.label377.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label378.setText(QCoreApplication.translate("MainWindow", u"Motion", None))
        self.label379.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label380.setText(QCoreApplication.translate("MainWindow", u"Power / Laser", None))
        self.label381.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label382.setText(QCoreApplication.translate("MainWindow", u"Safety", None))
        self.label383.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label384.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.label385.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label386.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.label387.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label388.setText(QCoreApplication.translate("MainWindow", u"Total (24H)", None))
        self.label389.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.gb_alarm_history.setTitle(QCoreApplication.translate("MainWindow", u"ALARM HISTORY", None))
        self.comboBox3.setItemText(0, QCoreApplication.translate("MainWindow", u"All Categories", None))

        self.comboBox4.setItemText(0, QCoreApplication.translate("MainWindow", u"All Severities", None))

        self.comboBox5.setItemText(0, QCoreApplication.translate("MainWindow", u"Last 24 Hours", None))

        ___qtablewidgetitem16 = self.tableWidget2.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"TIME", None));
        ___qtablewidgetitem17 = self.tableWidget2.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"DATE", None));
        ___qtablewidgetitem18 = self.tableWidget2.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"ALARM", None));
        ___qtablewidgetitem19 = self.tableWidget2.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"CATEGORY", None));
        ___qtablewidgetitem20 = self.tableWidget2.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"SEVERITY", None));
        ___qtablewidgetitem21 = self.tableWidget2.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem22 = self.tableWidget2.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"DURATION", None));
        self.label390.setText(QCoreApplication.translate("MainWindow", u"Showing 1 to 8 of 8 entries", None))
        self.pushButton105.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton106.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton107.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton108.setText(QCoreApplication.translate("MainWindow", u"Export History", None))
        self.gb_alarm_actions.setTitle(QCoreApplication.translate("MainWindow", u"QUICK ACTIONS", None))
        self.pushButton109.setText(QCoreApplication.translate("MainWindow", u"Acknowledge All", None))
        self.pushButton110.setText(QCoreApplication.translate("MainWindow", u"Reset Alarms", None))
        self.pushButton111.setText(QCoreApplication.translate("MainWindow", u"Alarm Sound", None))
        self.pushButton112.setText(QCoreApplication.translate("MainWindow", u"Test Alarms", None))
        self.pushButton113.setText(QCoreApplication.translate("MainWindow", u"Export Alarm Log", None))
        self.gb_system_logs.setTitle(QCoreApplication.translate("MainWindow", u"SYSTEM LOGS", None))
        self.lineEdit9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search logs...", None))
        self.pushButton114.setText(QCoreApplication.translate("MainWindow", u"Pause Auto Scroll", None))
        self.pushButton115.setText(QCoreApplication.translate("MainWindow", u"Clear Logs", None))
        ___qtablewidgetitem23 = self.tableWidget3.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"TIME", None));
        ___qtablewidgetitem24 = self.tableWidget3.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"LEVEL", None));
        ___qtablewidgetitem25 = self.tableWidget3.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"SOURCE", None));
        ___qtablewidgetitem26 = self.tableWidget3.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"MESSAGE", None));
        self.label391.setText(QCoreApplication.translate("MainWindow", u"Showing 1 to 15 of 1,248 entries", None))
        self.pushButton116.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton117.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton118.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.gb_log_filters.setTitle(QCoreApplication.translate("MainWindow", u"LOG FILTERS", None))
        self.label392.setText(QCoreApplication.translate("MainWindow", u"Log Level", None))
        self.comboBox6.setItemText(0, QCoreApplication.translate("MainWindow", u"All Levels", None))

        self.label393.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.comboBox7.setItemText(0, QCoreApplication.translate("MainWindow", u"All Sources", None))

        self.label394.setText(QCoreApplication.translate("MainWindow", u"Time Range", None))
        self.comboBox8.setItemText(0, QCoreApplication.translate("MainWindow", u"Last 24 Hours", None))

        self.pushButton119.setText(QCoreApplication.translate("MainWindow", u"Apply Filters", None))
        self.pushButton160.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.gb_log_stats.setTitle(QCoreApplication.translate("MainWindow", u"LOG STATISTICS", None))
        self.label395.setText(QCoreApplication.translate("MainWindow", u"[Pie Chart]\n"
"1,248", None))
        self.label396.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label397.setText(QCoreApplication.translate("MainWindow", u"972", None))
        self.label398.setText(QCoreApplication.translate("MainWindow", u"Warning", None))
        self.label399.setText(QCoreApplication.translate("MainWindow", u"156", None))
        self.label400.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label401.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.label402.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.label403.setText(QCoreApplication.translate("MainWindow", u"92", None))
        self.gb_export_logs.setTitle(QCoreApplication.translate("MainWindow", u"EXPORT LOGS", None))
        self.label404.setText(QCoreApplication.translate("MainWindow", u"Export filtered logs to file", None))
        self.comboBox9.setItemText(0, QCoreApplication.translate("MainWindow", u"CSV (.csv)", None))

        self.pushButton121.setText(QCoreApplication.translate("MainWindow", u"Export Logs", None))
        self.gb_maint_tools.setTitle(QCoreApplication.translate("MainWindow", u"MAINTENANCE TOOLS", None))
        self.label405.setText(QCoreApplication.translate("MainWindow", u"<b>SYSTEM DIAGNOSTICS</b>", None))
        self.pushButton122.setText(QCoreApplication.translate("MainWindow", u"Run Diagnostics", None))
        self.label406.setText(QCoreApplication.translate("MainWindow", u"<b>LUBRICATION REMINDER</b>", None))
        self.pushButton123.setText(QCoreApplication.translate("MainWindow", u"View Schedule", None))
        self.label407.setText(QCoreApplication.translate("MainWindow", u"<b>CLEANING GUIDE</b>", None))
        self.pushButton124.setText(QCoreApplication.translate("MainWindow", u"Open Guide", None))
        self.label408.setText(QCoreApplication.translate("MainWindow", u"<b>CALIBRATION WIZARD</b>", None))
        self.pushButton125.setText(QCoreApplication.translate("MainWindow", u"Start Calibration", None))
        self.label409.setText(QCoreApplication.translate("MainWindow", u"<b>FIRMWARE UPDATE</b>", None))
        self.pushButton126.setText(QCoreApplication.translate("MainWindow", u"Check Updates", None))
        self.label410.setText(QCoreApplication.translate("MainWindow", u"<b>EXPORT MAINTENANCE LOG</b>", None))
        self.pushButton127.setText(QCoreApplication.translate("MainWindow", u"Export Logs", None))
        self.label411.setText(QCoreApplication.translate("MainWindow", u"<b>FACTORY RESET</b>", None))
        self.pushButton128.setText(QCoreApplication.translate("MainWindow", u"Factory Reset", None))
        self.label412.setText(QCoreApplication.translate("MainWindow", u"<b>BACKUP / RESTORE</b>", None))
        self.pushButton129.setText(QCoreApplication.translate("MainWindow", u"Manage Backup", None))
        self.gb_comp_health.setTitle(QCoreApplication.translate("MainWindow", u"COMPONENT HEALTH", None))
        ___qtablewidgetitem27 = self.tableWidget4.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Component", None));
        ___qtablewidgetitem28 = self.tableWidget4.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem29 = self.tableWidget4.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Health", None));
        ___qtablewidgetitem30 = self.tableWidget4.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Last Checked", None));
        self.pushButton130.setText(QCoreApplication.translate("MainWindow", u"Refresh Health Status", None))
        self.gb_maint_schedule.setTitle(QCoreApplication.translate("MainWindow", u"MAINTENANCE SCHEDULE", None))
        ___qtablewidgetitem31 = self.tableWidget5.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Task", None));
        ___qtablewidgetitem32 = self.tableWidget5.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Interval", None));
        ___qtablewidgetitem33 = self.tableWidget5.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Last Done", None));
        ___qtablewidgetitem34 = self.tableWidget5.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Next Due", None));
        ___qtablewidgetitem35 = self.tableWidget5.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.pushButton131.setText(QCoreApplication.translate("MainWindow", u"View Full Schedule", None))
        self.gb_service_info.setTitle(QCoreApplication.translate("MainWindow", u"SERVICE INFORMATION", None))
        self.label413.setText(QCoreApplication.translate("MainWindow", u"Machine Model", None))
        self.label414.setText(QCoreApplication.translate("MainWindow", u"M3D-500", None))
        self.label415.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None))
        self.label416.setText(QCoreApplication.translate("MainWindow", u"M3D500-2026-00125", None))
        self.label417.setText(QCoreApplication.translate("MainWindow", u"Service Status", None))
        self.label418.setText(QCoreApplication.translate("MainWindow", u"Up to Date", None))
        self.label419.setText(QCoreApplication.translate("MainWindow", u"[!] Next service due in 68 days", None))
        self.pushButton132.setText(QCoreApplication.translate("MainWindow", u"View Service Schedule", None))
        self.gb_maint_notes.setTitle(QCoreApplication.translate("MainWindow", u"MAINTENANCE NOTES", None))
        self.pushButton133.setText(QCoreApplication.translate("MainWindow", u"+ Add Note", None))
        self.textEdit1.setProperty(u"text", QCoreApplication.translate("MainWindow", u"07 Jul 2026 09:15 AM by Operator\n"
"Checked laser optics and cleaned protective window. All systems are working normally.", None))
        self.pushButton134.setText(QCoreApplication.translate("MainWindow", u"View All Notes", None))
        self.gb_general_settings.setTitle(QCoreApplication.translate("MainWindow", u"GENERAL SETTINGS", None))
        self.label420.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.comboBox10.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))

        self.label421.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.comboBox11.setItemText(0, QCoreApplication.translate("MainWindow", u"Dark", None))

        self.label422.setText(QCoreApplication.translate("MainWindow", u"Distance Units", None))
        self.comboBox12.setItemText(0, QCoreApplication.translate("MainWindow", u"mm", None))

        self.label423.setText(QCoreApplication.translate("MainWindow", u"Temperature Units", None))
        self.comboBox13.setItemText(0, QCoreApplication.translate("MainWindow", u"C", None))

        self.gb_display_settings.setTitle(QCoreApplication.translate("MainWindow", u"DISPLAY SETTINGS", None))
        self.label424.setText(QCoreApplication.translate("MainWindow", u"Refresh Interval", None))
        self.comboBox14.setItemText(0, QCoreApplication.translate("MainWindow", u"500 ms", None))

        self.label425.setText(QCoreApplication.translate("MainWindow", u"Graph Time Range", None))
        self.comboBox15.setItemText(0, QCoreApplication.translate("MainWindow", u"3 Minutes", None))

        self.label426.setText(QCoreApplication.translate("MainWindow", u"Show Grid in Graph", None))
        self.gb_notif_settings.setTitle(QCoreApplication.translate("MainWindow", u"NOTIFICATION SETTINGS", None))
        self.label427.setText(QCoreApplication.translate("MainWindow", u"Alarm Notifications", None))
        self.label428.setText(QCoreApplication.translate("MainWindow", u"Sound Alerts", None))
        self.pushButton135.setText(QCoreApplication.translate("MainWindow", u"Test Notification", None))
        self.gb_alarm_thresholds.setTitle(QCoreApplication.translate("MainWindow", u"ALARM THRESHOLDS", None))
        ___qtablewidgetitem36 = self.tableWidget6.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Parameter", None));
        ___qtablewidgetitem37 = self.tableWidget6.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Warning", None));
        ___qtablewidgetitem38 = self.tableWidget6.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Critical", None));
        self.pushButton136.setText(QCoreApplication.translate("MainWindow", u"Save Thresholds", None))
        self.gb_file_settings.setTitle(QCoreApplication.translate("MainWindow", u"FILE SETTINGS", None))
        self.label429.setText(QCoreApplication.translate("MainWindow", u"Default G-code", None))
        self.lineEdit10.setText(QCoreApplication.translate("MainWindow", u"D:\\Metal3D\\Gcode", None))
        self.label430.setText(QCoreApplication.translate("MainWindow", u"Default Export", None))
        self.lineEdit11.setText(QCoreApplication.translate("MainWindow", u"D:\\Metal3D\\Exports", None))
        self.label431.setText(QCoreApplication.translate("MainWindow", u"Enable Auto Save", None))
        self.gb_data_backup.setTitle(QCoreApplication.translate("MainWindow", u"DATA & BACKUP", None))
        self.pushButton137.setText(QCoreApplication.translate("MainWindow", u"Backup Now", None))
        self.pushButton138.setText(QCoreApplication.translate("MainWindow", u"Restore", None))
        self.pushButton139.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), QCoreApplication.translate("MainWindow", u"GENERAL", None))
        self.gb_sys_info.setTitle(QCoreApplication.translate("MainWindow", u"SYSTEM INFORMATION", None))
        self.label432.setText(QCoreApplication.translate("MainWindow", u"Software Version", None))
        self.label433.setText(QCoreApplication.translate("MainWindow", u"2.4.1", None))
        self.label434.setText(QCoreApplication.translate("MainWindow", u"Build Number", None))
        self.label435.setText(QCoreApplication.translate("MainWindow", u"20260707.1", None))
        self.label436.setText(QCoreApplication.translate("MainWindow", u"UI Framework", None))
        self.label437.setText(QCoreApplication.translate("MainWindow", u"Qt 6.6.2", None))
        self.gb_data_mgmt.setTitle(QCoreApplication.translate("MainWindow", u"DATA MANAGEMENT", None))
        self.pushButton140.setText(QCoreApplication.translate("MainWindow", u"Export Report", None))
        self.pushButton141.setText(QCoreApplication.translate("MainWindow", u"Clear Data", None))
        self.gb_quick_settings.setTitle(QCoreApplication.translate("MainWindow", u"QUICK SETTINGS", None))
        self.pushButton142.setText(QCoreApplication.translate("MainWindow", u"Communication Ports", None))
        self.pushButton143.setText(QCoreApplication.translate("MainWindow", u"Bloodhound Access", None))
        self.pushButton144.setText(QCoreApplication.translate("MainWindow", u"License Information", None))
    # retranslateUi

