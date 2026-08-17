# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'metal_dashboardYBxREH.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1380, 850)
        MainWindow.setMinimumSize(QSize(1100, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.topNavFrame = QFrame(self.centralwidget)
        self.topNavFrame.setObjectName(u"topNavFrame")
        self.topNavFrame.setMinimumSize(QSize(0, 96))
        self.topNavFrame.setMaximumSize(QSize(16777215, 96))
        self.topNavFrame.setStyleSheet(u"background-color: #1a1b22; border-bottom: 1px solid #444653;")
        self.headerLayout = QHBoxLayout(self.topNavFrame)
        self.headerLayout.setSpacing(12)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(16, 8, 16, 8)
        self.logoLabel = QLabel(self.topNavFrame)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(110, 110))
        self.logoLabel.setMaximumSize(QSize(110, 110))
        self.logoLabel.setStyleSheet(u"background-color: #ffffff; border-radius: 6px; padding: 4px;")
        self.logoLabel.setScaledContents(True)

        self.headerLayout.addWidget(self.logoLabel)

        self.brandBox = QWidget(self.topNavFrame)
        self.brandBox.setObjectName(u"brandBox")
        self.brandLayout = QVBoxLayout(self.brandBox)
        self.brandLayout.setSpacing(2)
        self.brandLayout.setObjectName(u"brandLayout")
        self.brandLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.brandBox)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"color: #b8c4ff; letter-spacing: 0.5px;")

        self.brandLayout.addWidget(self.titleLabel)

        self.subtitleLabel = QLabel(self.brandBox)
        self.subtitleLabel.setObjectName(u"subtitleLabel")
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        self.subtitleLabel.setFont(font1)
        self.subtitleLabel.setStyleSheet(u"color: #8e909f;")

        self.brandLayout.addWidget(self.subtitleLabel)


        self.headerLayout.addWidget(self.brandBox)

        self.lblStatusBadge = QLabel(self.topNavFrame)
        self.lblStatusBadge.setObjectName(u"lblStatusBadge")
        self.lblStatusBadge.setFont(font)
        self.lblStatusBadge.setStyleSheet(u"background-color: rgba(16,185,129,0.15); color: #10b981; border: 1px solid #10b981; padding: 4px 10px; border-radius: 0px;")

        self.headerLayout.addWidget(self.lblStatusBadge)

        self.headerSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.headerSpacer)

        self.telemetryFrame = QFrame(self.topNavFrame)
        self.telemetryFrame.setObjectName(u"telemetryFrame")
        self.telemetryFrame.setStyleSheet(u"border: none; background: transparent;")
        self.telemetryLayout = QHBoxLayout(self.telemetryFrame)
        self.telemetryLayout.setSpacing(16)
        self.telemetryLayout.setObjectName(u"telemetryLayout")
        self.telemetryLayout.setContentsMargins(0, 0, 0, 0)
        self.lblChamberP = QLabel(self.telemetryFrame)
        self.lblChamberP.setObjectName(u"lblChamberP")
        self.lblChamberP.setFont(font)
        self.lblChamberP.setStyleSheet(u"color: #c4c5d5;")

        self.telemetryLayout.addWidget(self.lblChamberP)

        self.lblO2 = QLabel(self.telemetryFrame)
        self.lblO2.setObjectName(u"lblO2")
        self.lblO2.setFont(font)
        self.lblO2.setStyleSheet(u"color: #f59e0b;")

        self.telemetryLayout.addWidget(self.lblO2)

        self.lblBedTemp = QLabel(self.telemetryFrame)
        self.lblBedTemp.setObjectName(u"lblBedTemp")
        self.lblBedTemp.setFont(font)
        self.lblBedTemp.setStyleSheet(u"color: #c4c5d5;")

        self.telemetryLayout.addWidget(self.lblBedTemp)


        self.headerLayout.addWidget(self.telemetryFrame)

        self.btnEmergencyStop = QPushButton(self.topNavFrame)
        self.btnEmergencyStop.setObjectName(u"btnEmergencyStop")
        self.btnEmergencyStop.setFont(font)
        self.btnEmergencyStop.setStyleSheet(u"background-color: #ef4444; color: white; border: 1px solid #ffb4ab; padding: 8px 16px; font-weight: bold; border-radius: 0px;")

        self.headerLayout.addWidget(self.btnEmergencyStop)


        self.mainLayout.addWidget(self.topNavFrame)

        self.bodyContainer = QWidget(self.centralwidget)
        self.bodyContainer.setObjectName(u"bodyContainer")
        self.bodyLayout = QHBoxLayout(self.bodyContainer)
        self.bodyLayout.setSpacing(0)
        self.bodyLayout.setObjectName(u"bodyLayout")
        self.bodyLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarFrame = QFrame(self.bodyContainer)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setMinimumSize(QSize(220, 0))
        self.sidebarFrame.setMaximumSize(QSize(220, 16777215))
        self.sidebarFrame.setStyleSheet(u"background-color: #1a1b22; border-right: 1px solid #444653;")
        self.sidebarLayout = QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setSpacing(8)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.sidebarLayout.setContentsMargins(12, 16, 12, 16)
        self.lblNavHeader = QLabel(self.sidebarFrame)
        self.lblNavHeader.setObjectName(u"lblNavHeader")
        self.lblNavHeader.setFont(font)
        self.lblNavHeader.setStyleSheet(u"color: #8e909f; letter-spacing: 1px; margin-bottom: 8px;")

        self.sidebarLayout.addWidget(self.lblNavHeader)

        self.btnDashboard = QPushButton(self.sidebarFrame)
        self.btnDashboard.setObjectName(u"btnDashboard")
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setWeight(QFont.DemiBold)
        self.btnDashboard.setFont(font2)
        self.btnDashboard.setStyleSheet(u"text-align: left; padding: 10px 14px;")
        self.btnDashboard.setCheckable(True)
        self.btnDashboard.setChecked(True)

        self.sidebarLayout.addWidget(self.btnDashboard)

        self.btnMachineControl = QPushButton(self.sidebarFrame)
        self.btnMachineControl.setObjectName(u"btnMachineControl")
        self.btnMachineControl.setFont(font2)
        self.btnMachineControl.setStyleSheet(u"text-align: left; padding: 10px 14px;")
        self.btnMachineControl.setCheckable(True)

        self.sidebarLayout.addWidget(self.btnMachineControl)

        self.btnBuildSetup = QPushButton(self.sidebarFrame)
        self.btnBuildSetup.setObjectName(u"btnBuildSetup")
        self.btnBuildSetup.setFont(font2)
        self.btnBuildSetup.setStyleSheet(u"text-align: left; padding: 10px 14px;")
        self.btnBuildSetup.setCheckable(True)

        self.sidebarLayout.addWidget(self.btnBuildSetup)

        self.btnSettings = QPushButton(self.sidebarFrame)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setFont(font2)
        self.btnSettings.setStyleSheet(u"text-align: left; padding: 10px 14px;")
        self.btnSettings.setCheckable(True)

        self.sidebarLayout.addWidget(self.btnSettings)

        self.sidebarSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.sidebarSpacer)


        self.bodyLayout.addWidget(self.sidebarFrame)

        self.stackedWidget = QStackedWidget(self.bodyContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.dashboardLayout = QVBoxLayout(self.page_dashboard)
        self.dashboardLayout.setSpacing(16)
        self.dashboardLayout.setObjectName(u"dashboardLayout")
        self.dashboardLayout.setContentsMargins(16, 16, 16, 16)
        self.columnsWidget = QWidget(self.page_dashboard)
        self.columnsWidget.setObjectName(u"columnsWidget")
        self.columnsLayout = QHBoxLayout(self.columnsWidget)
        self.columnsLayout.setSpacing(16)
        self.columnsLayout.setObjectName(u"columnsLayout")
        self.columnsLayout.setContentsMargins(0, 0, 0, 0)
        self.gb_active_job = QGroupBox(self.columnsWidget)
        self.gb_active_job.setObjectName(u"gb_active_job")
        self.activeJobLayout = QVBoxLayout(self.gb_active_job)
        self.activeJobLayout.setSpacing(8)
        self.activeJobLayout.setObjectName(u"activeJobLayout")
        self.fileRow = QHBoxLayout()
        self.fileRow.setObjectName(u"fileRow")
        self.lbl_active_file = QLabel(self.gb_active_job)
        self.lbl_active_file.setObjectName(u"lbl_active_file")
        self.lbl_active_file.setFont(font)
        self.lbl_active_file.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px;")

        self.fileRow.addWidget(self.lbl_active_file)

        self.btn_import_build = QPushButton(self.gb_active_job)
        self.btn_import_build.setObjectName(u"btn_import_build")
        self.btn_import_build.setStyleSheet(u"background-color: #ec6a06; color: white; border: 1px solid #ffb690; font-weight: bold; border-radius: 0px;")

        self.fileRow.addWidget(self.btn_import_build)


        self.activeJobLayout.addLayout(self.fileRow)

        self.calcGrid = QGridLayout()
        self.calcGrid.setSpacing(6)
        self.calcGrid.setObjectName(u"calcGrid")
        self.lbl_calc_dims = QLabel(self.gb_active_job)
        self.lbl_calc_dims.setObjectName(u"lbl_calc_dims")
        self.lbl_calc_dims.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px; font-family: 'JetBrains Mono'; font-weight: bold;")

        self.calcGrid.addWidget(self.lbl_calc_dims, 0, 0, 1, 1)

        self.lbl_calc_layers = QLabel(self.gb_active_job)
        self.lbl_calc_layers.setObjectName(u"lbl_calc_layers")
        self.lbl_calc_layers.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px; font-family: 'JetBrains Mono'; font-weight: bold;")

        self.calcGrid.addWidget(self.lbl_calc_layers, 0, 1, 1, 1)

        self.lbl_calc_dose = QLabel(self.gb_active_job)
        self.lbl_calc_dose.setObjectName(u"lbl_calc_dose")
        self.lbl_calc_dose.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px; font-family: 'JetBrains Mono'; font-weight: bold;")

        self.calcGrid.addWidget(self.lbl_calc_dose, 1, 0, 1, 1)

        self.lbl_calc_vol = QLabel(self.gb_active_job)
        self.lbl_calc_vol.setObjectName(u"lbl_calc_vol")
        self.lbl_calc_vol.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px; font-family: 'JetBrains Mono'; font-weight: bold;")

        self.calcGrid.addWidget(self.lbl_calc_vol, 1, 1, 1, 1)

        self.lbl_calc_vectors = QLabel(self.gb_active_job)
        self.lbl_calc_vectors.setObjectName(u"lbl_calc_vectors")
        self.lbl_calc_vectors.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px; font-family: 'JetBrains Mono'; font-weight: bold;")

        self.calcGrid.addWidget(self.lbl_calc_vectors, 2, 0, 1, 1)

        self.lbl_calc_time = QLabel(self.gb_active_job)
        self.lbl_calc_time.setObjectName(u"lbl_calc_time")
        self.lbl_calc_time.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px; font-family: 'JetBrains Mono'; font-weight: bold;")

        self.calcGrid.addWidget(self.lbl_calc_time, 2, 1, 1, 1)


        self.activeJobLayout.addLayout(self.calcGrid)

        self.progressBar = QProgressBar(self.gb_active_job)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 24))
        self.progressBar.setValue(0)

        self.activeJobLayout.addWidget(self.progressBar)

        self.btn_act_simulate = QPushButton(self.gb_active_job)
        self.btn_act_simulate.setObjectName(u"btn_act_simulate")
        self.btn_act_simulate.setMinimumSize(QSize(0, 38))
        self.btn_act_simulate.setFont(font)
        self.btn_act_simulate.setStyleSheet(u"background-color: #ec6a06; color: white; border: 1px solid #ffb690; font-weight: bold; border-radius: 0px;")

        self.activeJobLayout.addWidget(self.btn_act_simulate)


        self.columnsLayout.addWidget(self.gb_active_job)

        self.gb_build_preview_dash = QGroupBox(self.columnsWidget)
        self.gb_build_preview_dash.setObjectName(u"gb_build_preview_dash")
        self.previewLayout = QVBoxLayout(self.gb_build_preview_dash)
        self.previewLayout.setSpacing(8)
        self.previewLayout.setObjectName(u"previewLayout")
        self.camBar = QHBoxLayout()
        self.camBar.setObjectName(u"camBar")
        self.btn_view_iso = QPushButton(self.gb_build_preview_dash)
        self.btn_view_iso.setObjectName(u"btn_view_iso")

        self.camBar.addWidget(self.btn_view_iso)

        self.btn_view_top = QPushButton(self.gb_build_preview_dash)
        self.btn_view_top.setObjectName(u"btn_view_top")

        self.camBar.addWidget(self.btn_view_top)

        self.btn_view_front = QPushButton(self.gb_build_preview_dash)
        self.btn_view_front.setObjectName(u"btn_view_front")

        self.camBar.addWidget(self.btn_view_front)

        self.btn_rotate = QPushButton(self.gb_build_preview_dash)
        self.btn_rotate.setObjectName(u"btn_rotate")

        self.camBar.addWidget(self.btn_rotate)

        self.btn_pan = QPushButton(self.gb_build_preview_dash)
        self.btn_pan.setObjectName(u"btn_pan")

        self.camBar.addWidget(self.btn_pan)

        self.btn_zoom = QPushButton(self.gb_build_preview_dash)
        self.btn_zoom.setObjectName(u"btn_zoom")

        self.camBar.addWidget(self.btn_zoom)


        self.previewLayout.addLayout(self.camBar)

        self.lbl_3d_preview_placeholder = QLabel(self.gb_build_preview_dash)
        self.lbl_3d_preview_placeholder.setObjectName(u"lbl_3d_preview_placeholder")
        self.lbl_3d_preview_placeholder.setStyleSheet(u"background-color: #0d0e14; border: 1px solid #444653; color: #8e909f; font-family: 'JetBrains Mono';")
        self.lbl_3d_preview_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.previewLayout.addWidget(self.lbl_3d_preview_placeholder)

        self.sliderRow = QHBoxLayout()
        self.sliderRow.setObjectName(u"sliderRow")
        self.lblSlice = QLabel(self.gb_build_preview_dash)
        self.lblSlice.setObjectName(u"lblSlice")

        self.sliderRow.addWidget(self.lblSlice)

        self.slider_layer = QSlider(self.gb_build_preview_dash)
        self.slider_layer.setObjectName(u"slider_layer")
        self.slider_layer.setOrientation(Qt.Orientation.Horizontal)

        self.sliderRow.addWidget(self.slider_layer)

        self.chk_section_view = QCheckBox(self.gb_build_preview_dash)
        self.chk_section_view.setObjectName(u"chk_section_view")

        self.sliderRow.addWidget(self.chk_section_view)


        self.previewLayout.addLayout(self.sliderRow)


        self.columnsLayout.addWidget(self.gb_build_preview_dash)

        self.gb_telemetry = QGroupBox(self.columnsWidget)
        self.gb_telemetry.setObjectName(u"gb_telemetry")
        self.telemetryColLayout = QVBoxLayout(self.gb_telemetry)
        self.telemetryColLayout.setSpacing(10)
        self.telemetryColLayout.setObjectName(u"telemetryColLayout")
        self.lbl_laser_gauge = QLabel(self.gb_telemetry)
        self.lbl_laser_gauge.setObjectName(u"lbl_laser_gauge")
        self.lbl_laser_gauge.setStyleSheet(u"background-color: #0d0e14; border: 1px solid #444653; color: #b8c4ff; font-family: 'JetBrains Mono';")
        self.lbl_laser_gauge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.telemetryColLayout.addWidget(self.lbl_laser_gauge)

        self.lbl_oxy_gauge = QLabel(self.gb_telemetry)
        self.lbl_oxy_gauge.setObjectName(u"lbl_oxy_gauge")
        self.lbl_oxy_gauge.setStyleSheet(u"background-color: #0d0e14; border: 1px solid #444653; color: #10b981; font-family: 'JetBrains Mono';")
        self.lbl_oxy_gauge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.telemetryColLayout.addWidget(self.lbl_oxy_gauge)

        self.lblAxisHeader = QLabel(self.gb_telemetry)
        self.lblAxisHeader.setObjectName(u"lblAxisHeader")
        self.lblAxisHeader.setFont(font)

        self.telemetryColLayout.addWidget(self.lblAxisHeader)

        self.lbl_dash_u = QLabel(self.gb_telemetry)
        self.lbl_dash_u.setObjectName(u"lbl_dash_u")
        self.lbl_dash_u.setFont(font)
        self.lbl_dash_u.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px;")

        self.telemetryColLayout.addWidget(self.lbl_dash_u)

        self.lbl_dash_v = QLabel(self.gb_telemetry)
        self.lbl_dash_v.setObjectName(u"lbl_dash_v")
        self.lbl_dash_v.setFont(font)
        self.lbl_dash_v.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px;")

        self.telemetryColLayout.addWidget(self.lbl_dash_v)

        self.lbl_dash_z = QLabel(self.gb_telemetry)
        self.lbl_dash_z.setObjectName(u"lbl_dash_z")
        self.lbl_dash_z.setFont(font)
        self.lbl_dash_z.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 6px;")

        self.telemetryColLayout.addWidget(self.lbl_dash_z)


        self.columnsLayout.addWidget(self.gb_telemetry)


        self.dashboardLayout.addWidget(self.columnsWidget)

        self.gb_console_log = QGroupBox(self.page_dashboard)
        self.gb_console_log.setObjectName(u"gb_console_log")
        self.logLayout = QVBoxLayout(self.gb_console_log)
        self.logLayout.setObjectName(u"logLayout")
        self.textEdit = QTextEdit(self.gb_console_log)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 140))
        self.textEdit.setReadOnly(True)

        self.logLayout.addWidget(self.textEdit)

        self.logBtnRow = QHBoxLayout()
        self.logBtnRow.setObjectName(u"logBtnRow")
        self.checkBox = QCheckBox(self.gb_console_log)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.logBtnRow.addWidget(self.checkBox)

        self.logSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logBtnRow.addItem(self.logSpacer)

        self.pushButton = QPushButton(self.gb_console_log)
        self.pushButton.setObjectName(u"pushButton")

        self.logBtnRow.addWidget(self.pushButton)


        self.logLayout.addLayout(self.logBtnRow)


        self.dashboardLayout.addWidget(self.gb_console_log)

        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_machine_control = QWidget()
        self.page_machine_control.setObjectName(u"page_machine_control")
        self.motionLayout = QVBoxLayout(self.page_machine_control)
        self.motionLayout.setSpacing(16)
        self.motionLayout.setObjectName(u"motionLayout")
        self.motionLayout.setContentsMargins(16, 16, 16, 16)
        self.lblMotionTitle = QLabel(self.page_machine_control)
        self.lblMotionTitle.setObjectName(u"lblMotionTitle")
        self.lblMotionTitle.setFont(font)
        self.lblMotionTitle.setStyleSheet(u"color: #b8c4ff;")

        self.motionLayout.addWidget(self.lblMotionTitle)

        self.cardsLayout = QHBoxLayout()
        self.cardsLayout.setSpacing(16)
        self.cardsLayout.setObjectName(u"cardsLayout")
        self.gb_powder_bay = QGroupBox(self.page_machine_control)
        self.gb_powder_bay.setObjectName(u"gb_powder_bay")
        self.uLayout = QVBoxLayout(self.gb_powder_bay)
        self.uLayout.setSpacing(10)
        self.uLayout.setObjectName(u"uLayout")
        self.uposlcddisplay = QLabel(self.gb_powder_bay)
        self.uposlcddisplay.setObjectName(u"uposlcddisplay")
        font3 = QFont()
        font3.setFamilies([u"JetBrains Mono"])
        font3.setBold(True)
        self.uposlcddisplay.setFont(font3)
        self.uposlcddisplay.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 10px;")
        self.uposlcddisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.uLayout.addWidget(self.uposlcddisplay)

        self.upluspushButton = QPushButton(self.gb_powder_bay)
        self.upluspushButton.setObjectName(u"upluspushButton")
        self.upluspushButton.setMinimumSize(QSize(0, 38))
        self.upluspushButton.setFont(font2)

        self.uLayout.addWidget(self.upluspushButton)

        self.uminuspushButton = QPushButton(self.gb_powder_bay)
        self.uminuspushButton.setObjectName(u"uminuspushButton")
        self.uminuspushButton.setMinimumSize(QSize(0, 38))
        self.uminuspushButton.setFont(font2)

        self.uLayout.addWidget(self.uminuspushButton)

        self.btnhomeU = QPushButton(self.gb_powder_bay)
        self.btnhomeU.setObjectName(u"btnhomeU")

        self.uLayout.addWidget(self.btnhomeU)


        self.cardsLayout.addWidget(self.gb_powder_bay)

        self.gb_build_plate = QGroupBox(self.page_machine_control)
        self.gb_build_plate.setObjectName(u"gb_build_plate")
        self.vLayout = QVBoxLayout(self.gb_build_plate)
        self.vLayout.setSpacing(10)
        self.vLayout.setObjectName(u"vLayout")
        self.vposlcddisplay = QLabel(self.gb_build_plate)
        self.vposlcddisplay.setObjectName(u"vposlcddisplay")
        self.vposlcddisplay.setFont(font3)
        self.vposlcddisplay.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 10px;")
        self.vposlcddisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vLayout.addWidget(self.vposlcddisplay)

        self.vpluspushButton = QPushButton(self.gb_build_plate)
        self.vpluspushButton.setObjectName(u"vpluspushButton")
        self.vpluspushButton.setMinimumSize(QSize(0, 38))
        self.vpluspushButton.setFont(font2)

        self.vLayout.addWidget(self.vpluspushButton)

        self.vminuspushButton = QPushButton(self.gb_build_plate)
        self.vminuspushButton.setObjectName(u"vminuspushButton")
        self.vminuspushButton.setMinimumSize(QSize(0, 38))
        self.vminuspushButton.setFont(font2)

        self.vLayout.addWidget(self.vminuspushButton)

        self.btnhomeV = QPushButton(self.gb_build_plate)
        self.btnhomeV.setObjectName(u"btnhomeV")

        self.vLayout.addWidget(self.btnhomeV)


        self.cardsLayout.addWidget(self.gb_build_plate)

        self.gb_recoater = QGroupBox(self.page_machine_control)
        self.gb_recoater.setObjectName(u"gb_recoater")
        self.zLayout = QVBoxLayout(self.gb_recoater)
        self.zLayout.setSpacing(10)
        self.zLayout.setObjectName(u"zLayout")
        self.zposlcddisplay = QLabel(self.gb_recoater)
        self.zposlcddisplay.setObjectName(u"zposlcddisplay")
        self.zposlcddisplay.setFont(font3)
        self.zposlcddisplay.setStyleSheet(u"color: #b8c4ff; background-color: #0d0e14; border: 1px solid #444653; padding: 10px;")
        self.zposlcddisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.zLayout.addWidget(self.zposlcddisplay)

        self.zpluspushButton = QPushButton(self.gb_recoater)
        self.zpluspushButton.setObjectName(u"zpluspushButton")
        self.zpluspushButton.setMinimumSize(QSize(0, 38))
        self.zpluspushButton.setFont(font2)

        self.zLayout.addWidget(self.zpluspushButton)

        self.zminuspushButton = QPushButton(self.gb_recoater)
        self.zminuspushButton.setObjectName(u"zminuspushButton")
        self.zminuspushButton.setMinimumSize(QSize(0, 38))
        self.zminuspushButton.setFont(font2)

        self.zLayout.addWidget(self.zminuspushButton)

        self.btnrecoaterSweep = QPushButton(self.gb_recoater)
        self.btnrecoaterSweep.setObjectName(u"btnrecoaterSweep")
        self.btnrecoaterSweep.setStyleSheet(u"background-color: #1e40af; color: white; border: 1px solid #b8c4ff; font-weight: bold; border-radius: 0px;")

        self.zLayout.addWidget(self.btnrecoaterSweep)


        self.cardsLayout.addWidget(self.gb_recoater)


        self.motionLayout.addLayout(self.cardsLayout)

        self.gb_travel_step = QGroupBox(self.page_machine_control)
        self.gb_travel_step.setObjectName(u"gb_travel_step")
        self.stepLayout = QHBoxLayout(self.gb_travel_step)
        self.stepLayout.setSpacing(10)
        self.stepLayout.setObjectName(u"stepLayout")
        self.travelpushButton_1 = QPushButton(self.gb_travel_step)
        self.travelpushButton_1.setObjectName(u"travelpushButton_1")
        self.travelpushButton_1.setFont(font2)

        self.stepLayout.addWidget(self.travelpushButton_1)

        self.travelpushButton_2 = QPushButton(self.gb_travel_step)
        self.travelpushButton_2.setObjectName(u"travelpushButton_2")
        self.travelpushButton_2.setFont(font2)

        self.stepLayout.addWidget(self.travelpushButton_2)

        self.travelpushButton_3 = QPushButton(self.gb_travel_step)
        self.travelpushButton_3.setObjectName(u"travelpushButton_3")
        self.travelpushButton_3.setFont(font2)

        self.stepLayout.addWidget(self.travelpushButton_3)

        self.travelpushButton_4 = QPushButton(self.gb_travel_step)
        self.travelpushButton_4.setObjectName(u"travelpushButton_4")
        self.travelpushButton_4.setFont(font2)

        self.stepLayout.addWidget(self.travelpushButton_4)

        self.travelpushButton_5 = QPushButton(self.gb_travel_step)
        self.travelpushButton_5.setObjectName(u"travelpushButton_5")
        self.travelpushButton_5.setFont(font2)

        self.stepLayout.addWidget(self.travelpushButton_5)

        self.travelpushButton_6 = QPushButton(self.gb_travel_step)
        self.travelpushButton_6.setObjectName(u"travelpushButton_6")
        self.travelpushButton_6.setFont(font2)

        self.stepLayout.addWidget(self.travelpushButton_6)


        self.motionLayout.addWidget(self.gb_travel_step)

        self.gb_master_controls = QGroupBox(self.page_machine_control)
        self.gb_master_controls.setObjectName(u"gb_master_controls")
        self.masterLayout = QHBoxLayout(self.gb_master_controls)
        self.masterLayout.setSpacing(16)
        self.masterLayout.setObjectName(u"masterLayout")
        self.allhomepushButton = QPushButton(self.gb_master_controls)
        self.allhomepushButton.setObjectName(u"allhomepushButton")
        self.allhomepushButton.setFont(font2)

        self.masterLayout.addWidget(self.allhomepushButton)

        self.galvohomepushButton = QPushButton(self.gb_master_controls)
        self.galvohomepushButton.setObjectName(u"galvohomepushButton")
        self.galvohomepushButton.setFont(font2)

        self.masterLayout.addWidget(self.galvohomepushButton)

        self.btn_master_estop = QPushButton(self.gb_master_controls)
        self.btn_master_estop.setObjectName(u"btn_master_estop")
        self.btn_master_estop.setFont(font2)
        self.btn_master_estop.setStyleSheet(u"background-color: #ef4444; color: white; border: 1px solid #ffb4ab; border-radius: 0px;")

        self.masterLayout.addWidget(self.btn_master_estop)


        self.motionLayout.addWidget(self.gb_master_controls)

        self.stackedWidget.addWidget(self.page_machine_control)
        self.page_build_setup = QWidget()
        self.page_build_setup.setObjectName(u"page_build_setup")
        self.filesLayout = QVBoxLayout(self.page_build_setup)
        self.filesLayout.setObjectName(u"filesLayout")
        self.graphicsView_layer = QLabel(self.page_build_setup)
        self.graphicsView_layer.setObjectName(u"graphicsView_layer")
        self.graphicsView_layer.setStyleSheet(u"background-color: #0d0e14; border: 1px solid #444653; color: #b8c4ff; font-family: 'JetBrains Mono';")
        self.graphicsView_layer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.filesLayout.addWidget(self.graphicsView_layer)

        self.stackedWidget.addWidget(self.page_build_setup)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.settingsLayout = QVBoxLayout(self.page_settings)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.lblSettings = QLabel(self.page_settings)
        self.lblSettings.setObjectName(u"lblSettings")
        self.lblSettings.setStyleSheet(u"color: #b8c4ff; font-family: 'Inter'; font-size: 14px; font-weight: bold;")

        self.settingsLayout.addWidget(self.lblSettings)

        self.stackedWidget.addWidget(self.page_settings)

        self.bodyLayout.addWidget(self.stackedWidget)


        self.mainLayout.addWidget(self.bodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Specialise Products Private Limited - Metal 3D Printer", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"/* ===================================================================\n"
"   INDUSTRIAL PRECISION DESIGN SYSTEM - STYLESHEET FOR LPBF CONTROL\n"
"   =================================================================== */\n"
"\n"
"* {\n"
"    font-family: 'Inter', 'Segoe UI', sans-serif;\n"
"    color: #e3e1eb;\n"
"    font-size: 11px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QMainWindow, QDialog {\n"
"    background-color: #12131a;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #12131a;\n"
"    color: #e3e1eb;\n"
"}\n"
"\n"
"/* FRAMES & CONTAINERS - Modern Industrial Glassmorphic / Sharp High-Contrast */\n"
"QFrame {\n"
"    background-color: #1e1f26;\n"
"    border: 1px solid #444653;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QFrame#sidebarFrame {\n"
"    background-color: #1a1b22;\n"
"    border-right: 1px solid #444653;\n"
"}\n"
"\n"
"QFrame#topNavFrame {\n"
"    background-color: #1a1b22;\n"
"    border-bottom: 1px solid #444653;\n"
"}\n"
"\n"
"QFrame#cardFrame, QFrame[card=\"true\"] {\n"
"    backg"
                        "round-color: #1e1f26;\n"
"    border: 1px solid #444653;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* GROUP BOX CARDS */\n"
"QGroupBox {\n"
"    background-color: #1e1f26;\n"
"    border: 1px solid #444653;\n"
"    border-radius: 0px;\n"
"    margin-top: 18px;\n"
"    padding: 12px 8px 8px 8px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 8px;\n"
"    padding: 2px 8px;\n"
"    background-color: #282a31;\n"
"    color: #b8c4ff;\n"
"    font-family: 'JetBrains Mono', monospace;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    letter-spacing: 0.5px;\n"
"    border: 1px solid #444653;\n"
"    border-radius: 0px;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"/* BUTTONS */\n"
"QPushButton {\n"
"    background-color: #282a31;\n"
"    border: 1px solid #444653;\n"
"    border-radius: 0px;\n"
"    color: #e3e1eb;\n"
"    padding: 6px 14px;\n"
"    min-height: 24px;\n"
"    font-weight: 600;\n"
"    fon"
                        "t-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #33343c;\n"
"    border-color: #8e909f;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1a1b22;\n"
"    border-color: #1e40af;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #1e40af;\n"
"    color: #ffffff;\n"
"    border: 1px solid #b8c4ff;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* ACCENT BUTTON STYLES */\n"
"/* Primary Action Button (Secondary Orange) */\n"
"QPushButton#btn_start_print, QPushButton#btn_act_simulate, QPushButton#btn_import_build, QPushButton[accent=\"primary\"], QPushButton[accent=\"orange\"] {\n"
"    background-color: #ec6a06;\n"
"    color: #ffffff;\n"
"    border: 1px solid #ffb690;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QPushButton#btn_start_print:hover, QPushButton#btn_act_simulate:hover, QPushButton#btn_import_build:hover, QPushButton[accent=\"primary\"]:hover, QPushButton[accent=\"orange\"]:hover {\n"
"    background-color: #ff7715;\n"
"    border-col"
                        "or: #ffffff;\n"
"}\n"
"\n"
"/* Critical Emergency Stop Button (Crimson) */\n"
"QPushButton#btn_emergency_stop, QPushButton[accent=\"critical\"], QPushButton[accent=\"red\"] {\n"
"    background-color: #ef4444;\n"
"    color: #ffffff;\n"
"    border: 1px solid #ffb4ab;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QPushButton#btn_emergency_stop:hover, QPushButton[accent=\"critical\"]:hover, QPushButton[accent=\"red\"]:hover {\n"
"    background-color: #dc2626;\n"
"    border-color: #ffffff;\n"
"}\n"
"\n"
"/* Secondary Action Button (Primary Container Blue) */\n"
"QPushButton[accent=\"secondary\"], QPushButton[accent=\"blue\"] {\n"
"    background-color: #1e40af;\n"
"    color: #ffffff;\n"
"    border: 1px solid #b8c4ff;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton[accent=\"secondary\"]:hover, QPushButton[accent=\"blue\"]:hover {\n"
"    background-color: #2563eb;\n"
"    border-color: #ffffff;\n"
"}\n"
"\n"
"/* INPUT CONTROLS */\n"
"QLineEdit, QTextEdit, QSpinBox, QDoubleSpinBox, QComboBox {\n"
"    backgrou"
                        "nd-color: #0d0e14;\n"
"    border: 1px solid #444653;\n"
"    border-radius: 0px;\n"
"    color: #b8c4ff;\n"
"    padding: 5px 8px;\n"
"    font-family: 'JetBrains Mono', monospace;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus {\n"
"    border: 1px solid #1e40af;\n"
"    background-color: #12131a;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 24px;\n"
"    background: #1a1b22;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #1a1b22;\n"
"    border: 1px solid #444653;\n"
"    color: #e3e1eb;\n"
"    selection-background-color: #1e40af;\n"
"}\n"
"\n"
"/* PROGRESS BAR */\n"
"QProgressBar {\n"
"    background-color: #0d0e14;\n"
"    border: 1px solid #444653;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"    color: #ffffff;\n"
"    font-family: 'JetBrains Mono', monospace;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"   "
                        " background-color: #1e40af;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #444653;\n"
"    height: 8px;\n"
"    background: #0d0e14;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e40af;\n"
"    border: 1px solid #b8c4ff;\n"
"    width: 16px;\n"
"    margin: -5px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #ec6a06;\n"
"    border-color: #ffb690;\n"
"}\n"
"\n"
"/* DATA READOUT LCD / LABELS */\n"
"QLabel#uposlcddisplay, QLabel#vposlcddisplay, QLabel#zposlcddisplay, QLabel.data-value {\n"
"    font-family: 'JetBrains Mono', monospace;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: #b8c4ff;\n"
"    background-color: #0d0e14;\n"
"    border: 1px solid #444653;\n"
"    padding: 6px 12px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* STATUS BADGES */\n"
"QLabel.status-emerald {\n"
"    background-color: rgba(16, 185, 129, 0.15"
                        ");\n"
"    color: #10b981;\n"
"    border: 1px solid #10b981;\n"
"    padding: 3px 8px;\n"
"    font-family: 'JetBrains Mono', monospace;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel.status-amber {\n"
"    background-color: rgba(245, 158, 11, 0.15);\n"
"    color: #f59e0b;\n"
"    border: 1px solid #f59e0b;\n"
"    padding: 3px 8px;\n"
"    font-family: 'JetBrains Mono', monospace;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel.status-crimson {\n"
"    background-color: rgba(239, 68, 68, 0.15);\n"
"    color: #ef4444;\n"
"    border: 1px solid #ef4444;\n"
"    padding: 3px 8px;\n"
"    font-family: 'JetBrains Mono', monospace;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* TAB WIDGETS */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444653;\n"
"    background-color: #1e1f26;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #1a1b22;\n"
"    color: #c4c5d5;\n"
"    padding: 8px 16px;\n"
"    bord"
                        "er: 1px solid #444653;\n"
"    border-bottom: none;\n"
"    border-radius: 0px;\n"
"    margin-right: 2px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #1e1f26;\n"
"    color: #b8c4ff;\n"
"    border-top: 2px solid #1e40af;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    color: #ffffff;\n"
"    background-color: #282a31;\n"
"}\n"
"\n"
"/* SCROLLBARS */\n"
"QScrollBar:vertical, QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #0d0e14;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background: #33343c;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {\n"
"    background: #8e909f;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"   ", None))
        self.logoLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"SPECIALISE PRODUCTS PRIVATE LIMITED", None))
        self.subtitleLabel.setText(QCoreApplication.translate("MainWindow", u"Metal 3D Printer", None))
        self.lblStatusBadge.setText(QCoreApplication.translate("MainWindow", u"READY / SIMULATION MODE", None))
        self.lblChamberP.setText(QCoreApplication.translate("MainWindow", u"Chamber P: 1013 mbar", None))
        self.lblO2.setText(QCoreApplication.translate("MainWindow", u"O2: 0.04%", None))
        self.lblBedTemp.setText(QCoreApplication.translate("MainWindow", u"Bed Temp: 65\u00b0C", None))
        self.btnEmergencyStop.setText(QCoreApplication.translate("MainWindow", u"EMERGENCY STOP", None))
        self.lblNavHeader.setText(QCoreApplication.translate("MainWindow", u"NAVIGATION", None))
        self.btnDashboard.setText(QCoreApplication.translate("MainWindow", u"  Dashboard", None))
        self.btnMachineControl.setText(QCoreApplication.translate("MainWindow", u"  Motion Control", None))
        self.btnBuildSetup.setText(QCoreApplication.translate("MainWindow", u"  Files & Slicing", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"  System Settings", None))
        self.gb_active_job.setTitle(QCoreApplication.translate("MainWindow", u"ACTIVE JOB & CALCULATIONS", None))
        self.lbl_active_file.setText(QCoreApplication.translate("MainWindow", u"demo_cube.stl", None))
        self.btn_import_build.setText(QCoreApplication.translate("MainWindow", u"IMPORT FILE", None))
        self.lbl_calc_dims.setText(QCoreApplication.translate("MainWindow", u"Part Dims: 50.0 x 50.0 x 25.0 mm", None))
        self.lbl_calc_layers.setText(QCoreApplication.translate("MainWindow", u"Total Layers: 500 Layers", None))
        self.lbl_calc_dose.setText(QCoreApplication.translate("MainWindow", u"Powder Dose (+U): 0.075 mm", None))
        self.lbl_calc_vol.setText(QCoreApplication.translate("MainWindow", u"Powder Vol: 234.38 cm\u00b3", None))
        self.lbl_calc_vectors.setText(QCoreApplication.translate("MainWindow", u"Vectors: 12,500 Commands", None))
        self.lbl_calc_time.setText(QCoreApplication.translate("MainWindow", u"Est. Time: 01:14:30", None))
        self.btn_act_simulate.setText(QCoreApplication.translate("MainWindow", u"  START BUILD SIMULATION", None))
        self.gb_build_preview_dash.setTitle(QCoreApplication.translate("MainWindow", u"3D PART SLICER & PREVIEW", None))
        self.btn_view_iso.setText(QCoreApplication.translate("MainWindow", u"Iso", None))
        self.btn_view_top.setText(QCoreApplication.translate("MainWindow", u"Top", None))
        self.btn_view_front.setText(QCoreApplication.translate("MainWindow", u"Front", None))
        self.btn_rotate.setText(QCoreApplication.translate("MainWindow", u"Rot", None))
        self.btn_pan.setText(QCoreApplication.translate("MainWindow", u"Pan", None))
        self.btn_zoom.setText(QCoreApplication.translate("MainWindow", u"Zoom", None))
        self.lbl_3d_preview_placeholder.setText(QCoreApplication.translate("MainWindow", u"3D OPENGL PART VIEWPORT", None))
        self.lblSlice.setText(QCoreApplication.translate("MainWindow", u"Layer Cut:", None))
        self.chk_section_view.setText(QCoreApplication.translate("MainWindow", u"Section Cut", None))
        self.gb_telemetry.setTitle(QCoreApplication.translate("MainWindow", u"HARDWARE TELEMETRY", None))
        self.lbl_laser_gauge.setText(QCoreApplication.translate("MainWindow", u"LASER POWER GAUGE", None))
        self.lbl_oxy_gauge.setText(QCoreApplication.translate("MainWindow", u"O2 LEVEL GAUGE", None))
        self.lblAxisHeader.setText(QCoreApplication.translate("MainWindow", u"AXIS POSITIONS (mm):", None))
        self.lbl_dash_u.setText(QCoreApplication.translate("MainWindow", u"Powder Bay (U): +0.000 mm", None))
        self.lbl_dash_v.setText(QCoreApplication.translate("MainWindow", u"Build Plate (V): +0.000 mm", None))
        self.lbl_dash_z.setText(QCoreApplication.translate("MainWindow", u"Recoater Blade (Z): +0.000 mm", None))
        self.gb_console_log.setTitle(QCoreApplication.translate("MainWindow", u"SYSTEM TERMINAL & EXPOSURE LOG", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Auto-Scroll", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear Console Log", None))
        self.lblMotionTitle.setText(QCoreApplication.translate("MainWindow", u"MOTION CONTROL & MANUAL AXIS JOGGING", None))
        self.gb_powder_bay.setTitle(QCoreApplication.translate("MainWindow", u"POWDER BAY (FEEDER - U AXIS)", None))
        self.uposlcddisplay.setText(QCoreApplication.translate("MainWindow", u"+0.000 mm", None))
        self.upluspushButton.setText(QCoreApplication.translate("MainWindow", u"+U (Supply Powder UP)", None))
        self.uminuspushButton.setText(QCoreApplication.translate("MainWindow", u"-U (Supply Powder DOWN)", None))
        self.btnhomeU.setText(QCoreApplication.translate("MainWindow", u"Home Powder Bay (U)", None))
        self.gb_build_plate.setTitle(QCoreApplication.translate("MainWindow", u"BUILD PLATE (PLATFORM - V AXIS)", None))
        self.vposlcddisplay.setText(QCoreApplication.translate("MainWindow", u"+0.000 mm", None))
        self.vpluspushButton.setText(QCoreApplication.translate("MainWindow", u"+V (Platform UP)", None))
        self.vminuspushButton.setText(QCoreApplication.translate("MainWindow", u"-V (Platform DOWN)", None))
        self.btnhomeV.setText(QCoreApplication.translate("MainWindow", u"Home Build Plate (V)", None))
        self.gb_recoater.setTitle(QCoreApplication.translate("MainWindow", u"RECOATER BLADE (DOSING - Z AXIS)", None))
        self.zposlcddisplay.setText(QCoreApplication.translate("MainWindow", u"+0.000 mm", None))
        self.zpluspushButton.setText(QCoreApplication.translate("MainWindow", u"+Z (Recoater RIGHT)", None))
        self.zminuspushButton.setText(QCoreApplication.translate("MainWindow", u"-Z (Recoater LEFT)", None))
        self.btnrecoaterSweep.setText(QCoreApplication.translate("MainWindow", u"Home  Recoater  (Z)", None))
        self.gb_travel_step.setTitle(QCoreApplication.translate("MainWindow", u"JOG STEP TRAVEL DISTANCE (mm)", None))
        self.travelpushButton_1.setText(QCoreApplication.translate("MainWindow", u"0.01 mm", None))
        self.travelpushButton_2.setText(QCoreApplication.translate("MainWindow", u"0.1 mm", None))
        self.travelpushButton_3.setText(QCoreApplication.translate("MainWindow", u"1.0 mm", None))
        self.travelpushButton_4.setText(QCoreApplication.translate("MainWindow", u"5.0 mm", None))
        self.travelpushButton_5.setText(QCoreApplication.translate("MainWindow", u"10.0 mm", None))
        self.travelpushButton_6.setText(QCoreApplication.translate("MainWindow", u"50.0 mm", None))
        self.gb_master_controls.setTitle(QCoreApplication.translate("MainWindow", u"SYSTEM MASTER CONTROLS", None))
        self.allhomepushButton.setText(QCoreApplication.translate("MainWindow", u"  HOME ALL AXES (U, V, Z)", None))
        self.galvohomepushButton.setText(QCoreApplication.translate("MainWindow", u"  GALVO SCANNER HOME", None))
        self.btn_master_estop.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udea8  EMERGENCY STOP", None))
        self.graphicsView_layer.setText(QCoreApplication.translate("MainWindow", u"2D GALVO VECTOR PATH PREVIEW PLACEHOLDER", None))
        self.lblSettings.setText(QCoreApplication.translate("MainWindow", u"SYSTEM CONFIGURATION & CALIBRATION SETTINGS", None))
    # retranslateUi

