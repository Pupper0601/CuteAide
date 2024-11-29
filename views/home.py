# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(634, 423)
        icon = QIcon()
        icon.addFile(u":/images/resource/images/log.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 600, 360))
        self.widget.setMinimumSize(QSize(600, 360))
        self.widget.setMaximumSize(QSize(600, 360))
        self.widget.setStyleSheet(u"#widget{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.widget_5)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setMinimumSize(QSize(0, 40))
        self.frame_16.setStyleSheet(u"#frame_16{\n"
"	border: none;\n"
"	border-top-left-radius: 10px;\n"
"}")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_5 = QPushButton(self.frame_16)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"#pushButton_5{\n"
"	border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/resource/icon/versrion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setFlat(False)

        self.horizontalLayout_7.addWidget(self.pushButton_5)

        self.horizontalSpacer_9 = QSpacerItem(5, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.pushButton_7 = QPushButton(self.frame_16)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"#pushButton_7{\n"
"	border: none;\n"
"	color: rgb(0, 170, 0);\n"
"	font: 700 10pt;\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_7)

        self.horizontalSpacer_48 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_48)


        self.horizontalLayout_4.addWidget(self.frame_16)

        self.frame_18 = QFrame(self.widget_5)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setMinimumSize(QSize(0, 40))
        self.frame_18.setStyleSheet(u"#frame_18{\n"
"	border: none;\n"
"}")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(45, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.label_18 = QLabel(self.frame_18)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"#label_18{\n"
"	font: 700 24pt \"\u65b0\u5b8b\u4f53\";\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_18)

        self.horizontalSpacer_7 = QSpacerItem(44, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.horizontalLayout_4.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.widget_5)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy2)
        self.frame_17.setMinimumSize(QSize(0, 40))
        self.frame_17.setStyleSheet(u"#frame_17{\n"
"	border: none;\n"
"	border-top-right-radius:10px;\n"
"}")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_5 = QSpacerItem(60, 11, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.pushButton_8 = QPushButton(self.frame_17)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(110, 30))
        self.pushButton_8.setStyleSheet(u"#pushButton_8{\n"
"	font: 700 10pt;\n"
"	background: rgb(255, 85, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#pushButton_8:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border: 3px solid rgb(255, 0, 0);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 3px;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/resource/icon/github.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.pushButton_8)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_47)

        self.pushButton_4 = QPushButton(self.frame_17)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(20, 20))
        self.pushButton_4.setMaximumSize(QSize(20, 20))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(4, 51, 255);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/resource/icon/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_17)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(20, 20))
        self.pushButton_3.setMaximumSize(QSize(20, 20))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(4, 51, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/resource/icon/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addWidget(self.frame_17)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(12)
        sizePolicy3.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy3)
        self.horizontalLayout = QHBoxLayout(self.widget_6)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_6)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.frame_24 = QFrame(self.widget_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 38))
        self.frame_24.setStyleSheet(u"#frame_24{\n"
"	border: 1px solid rgb(214,214,214);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_44)

        self.pushButton_9 = QPushButton(self.frame_24)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy4)
        self.pushButton_9.setStyleSheet(u"#pushButton_9{\n"
"	border: none;\n"
"	font: 700 12pt rgb(255, 147, 0);\n"
"	color: rgb(255, 147, 0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon/resource/icon/Tips.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon5)

        self.horizontalLayout_21.addWidget(self.pushButton_9)

        self.horizontalSpacer_45 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_45)

        self.pushButton_10 = QPushButton(self.frame_24)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy5)
        self.pushButton_10.setStyleSheet(u"#pushButton_10{\n"
"	border: none;\n"
"	color: rgb(255, 38, 0);\n"
"	letter-spacing: 1px;\n"
"}")

        self.horizontalLayout_21.addWidget(self.pushButton_10)

        self.horizontalSpacer_46 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_46)


        self.verticalLayout_6.addWidget(self.frame_24)

        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setMinimumSize(QSize(0, 32))
        self.frame.setMaximumSize(QSize(16777215, 32))
        self.frame.setStyleSheet(u"#frame{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(214, 214, 214);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy7)
        self.frame_8.setMinimumSize(QSize(0, 32))
        self.frame_8.setMaximumSize(QSize(16777215, 32))
        self.frame_8.setStyleSheet(u"#frame_8{\n"
"	border: nome;\n"
"	\n"
"}")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(15, 23, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"#label_2{\n"
"	font: 700 13pt;\n"
"	color: rgb(124, 233, 209)\n"
"}")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(15, 23, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_8)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy6.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy6)
        self.frame_5.setMinimumSize(QSize(0, 70))
        self.frame_5.setMaximumSize(QSize(16777215, 70))
        self.frame_5.setStyleSheet(u"#frame_5{\n"
"	border: 1px solid rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy8)
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	border: none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_29 = QSpacerItem(13, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_29)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy9)
        icon6 = QIcon()
        icon6.addFile(u":/icon/resource/icon/mouse.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.radioButton.setIcon(icon6)
        self.radioButton.setIconSize(QSize(20, 20))
        self.radioButton.setChecked(True)

        self.horizontalLayout_16.addWidget(self.radioButton)

        self.horizontalSpacer_30 = QSpacerItem(13, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_30)

        self.radioButton_2 = QRadioButton(self.frame_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy9.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy9)

        self.horizontalLayout_16.addWidget(self.radioButton_2)

        self.horizontalSpacer_31 = QSpacerItem(13, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_31)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_19 = QFrame(self.frame_5)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy8.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy8)
        self.frame_19.setStyleSheet(u"#frame_19{\n"
"	border: none;\n"
"}")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_32 = QSpacerItem(13, 16, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_32)

        self.radioButton_3 = QRadioButton(self.frame_19)
        self.radioButton_3.setObjectName(u"radioButton_3")
        sizePolicy9.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy9)
        icon7 = QIcon()
        icon7.addFile(u":/icon/resource/icon/keyboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.radioButton_3.setIcon(icon7)
        self.radioButton_3.setIconSize(QSize(20, 20))
        self.radioButton_3.setChecked(True)

        self.horizontalLayout_15.addWidget(self.radioButton_3)

        self.horizontalSpacer_33 = QSpacerItem(13, 16, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_33)

        self.radioButton_4 = QRadioButton(self.frame_19)
        self.radioButton_4.setObjectName(u"radioButton_4")
        sizePolicy9.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy9)

        self.horizontalLayout_15.addWidget(self.radioButton_4)

        self.horizontalSpacer_35 = QSpacerItem(13, 16, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_35)


        self.verticalLayout_5.addWidget(self.frame_19)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.widget_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy6.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy6)
        self.frame_6.setMaximumSize(QSize(16777215, 40))
        self.frame_6.setStyleSheet(u"#frame_6{\n"
"	border: 1px solid rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_34 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_34)

        self.checkBox = QCheckBox(self.frame_6)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy9)
        icon8 = QIcon()
        icon8.addFile(u":/icon/resource/icon/time.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.checkBox.setIcon(icon8)
        self.checkBox.setIconSize(QSize(20, 20))
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)

        self.horizontalLayout_17.addWidget(self.checkBox)

        self.horizontalSpacer_36 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_36)

        self.checkBox_2 = QCheckBox(self.frame_6)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy9.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy9)
        icon9 = QIcon()
        icon9.addFile(u":/icon/resource/icon/floating.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.checkBox_2.setIcon(icon9)
        self.checkBox_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_17.addWidget(self.checkBox_2)

        self.horizontalSpacer_37 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_37)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.frame_20 = QFrame(self.widget_2)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy6.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy6)
        self.frame_20.setMaximumSize(QSize(16777215, 55))
        self.frame_20.setStyleSheet(u"#frame_20{\n"
"	border: none;\n"
"}")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(10, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.pushButton_2 = QPushButton(self.frame_20)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy9.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy9)
        self.pushButton_2.setMinimumSize(QSize(0, 46))
        self.pushButton_2.setStyleSheet(u"#pushButton_2{\n"
"	font: 700 20pt ;\n"
"	background-color: rgb(71,157,168);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 8px;\n"
"	border: 3px solid rgb(71,157,168);\n"
"	letter-spacing: 1px;\n"
"\n"
"}\n"
"\n"
"#pushButton_2:hover{\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icon/resource/icon/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon10)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.pushButton_2)

        self.horizontalSpacer_12 = QSpacerItem(11, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)


        self.verticalLayout_6.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.widget_2)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy6.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy6)
        self.frame_21.setMaximumSize(QSize(16777215, 55))
        self.frame_21.setStyleSheet(u"#frame_21{\n"
"	border: none;\n"
"}")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_38 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_38)

        self.pushButton_11 = QPushButton(self.frame_21)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy9)
        self.pushButton_11.setMinimumSize(QSize(0, 46))
        self.pushButton_11.setStyleSheet(u"#pushButton_11{\n"
"	font: 700 16pt ;\n"
"	background-color: rgb(255, 97, 6);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 8px;\n"
"	border: 3px solid rgb(255, 97, 6);\n"
"	letter-spacing: 1px;\n"
"\n"
"}\n"
"\n"
"#pushButton_11:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border: 3px solid rgb(255, 0, 0);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icon/resource/icon/dashang.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon11)
        self.pushButton_11.setIconSize(QSize(30, 30))

        self.horizontalLayout_18.addWidget(self.pushButton_11)

        self.horizontalSpacer_39 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_39)


        self.verticalLayout_6.addWidget(self.frame_21)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget_6)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 4, 2, 2)
        self.frame_3 = QFrame(self.widget_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"	border: 1px solid rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy7.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy7)
        self.frame_10.setStyleSheet(u"#frame_10{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background: rgb(70,157,168);\n"
"	\n"
"}")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 0, 5, 0)
        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy10)
        self.pushButton.setMinimumSize(QSize(200, 0))
        self.pushButton.setStyleSheet(u"#pushButton{\n"
"	border: none;\n"
"	font: 500 12pt rgb(255, 255, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	letter-spacing: 2px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icon/resource/icon/now.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon12)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.pushButton)

        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(2)
        sizePolicy11.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy11)
        self.frame_11.setStyleSheet(u"#frame_11{\n"
"	border: none;\n"
"}")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 5, 0, 5)
        self.horizontalSpacer_14 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_14)

        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(3)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy12)
        self.label_6.setStyleSheet(u"#label_6{\n"
"	border: 2px solid rgb(70,157,168);\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.horizontalSpacer_15 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)

        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.horizontalSpacer_16 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy13.setHorizontalStretch(1)
        sizePolicy13.setVerticalStretch(2)
        sizePolicy13.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy13)
        self.frame_12.setStyleSheet(u"#frame_12{\n"
"	border: none;\n"
"}\n"
"")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_17)

        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.horizontalSpacer_18 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_18)

        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.horizontalSpacer_19 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_19)

        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.horizontalSpacer_20 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_20)


        self.verticalLayout_3.addWidget(self.frame_12)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.widget_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"#frame_4{\n"
"	border: 1px solid rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy7.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy7)
        self.frame_13.setStyleSheet(u"#frame_13{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background: rgb(70,157,168);\n"
"	\n"
"}")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 0, 5, 0)
        self.horizontalSpacer_10 = QSpacerItem(9, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)

        self.pushButton_6 = QPushButton(self.frame_13)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy10.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy10)
        self.pushButton_6.setMinimumSize(QSize(200, 0))
        self.pushButton_6.setStyleSheet(u"#pushButton_6{\n"
"	border: none;\n"
"	font: 500 12pt rgb(255, 255, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	letter-spacing: 2px;\n"
"}")
        self.pushButton_6.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.pushButton_6)

        self.horizontalSpacer_21 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_21)


        self.verticalLayout_4.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_4)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy11.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy11)
        self.frame_14.setStyleSheet(u"#frame_14{\n"
"	border: none;\n"
"}")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 5, 0, 5)
        self.horizontalSpacer_22 = QSpacerItem(5, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_22)

        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")
        sizePolicy12.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy12)
        self.label_11.setStyleSheet(u"#label_11{\n"
"	border: 2px solid rgb(70,157,168);\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.horizontalSpacer_23 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_23)

        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.horizontalSpacer_24 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_24)


        self.verticalLayout_4.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_4)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy13.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy13)
        self.frame_15.setStyleSheet(u"#frame_15{\n"
"	border: none;\n"
"}\n"
"")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_25 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_25)

        self.label_13 = QLabel(self.frame_15)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_13)

        self.horizontalSpacer_26 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_26)

        self.label_14 = QLabel(self.frame_15)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_14)

        self.horizontalSpacer_27 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_27)

        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_15)

        self.horizontalSpacer_28 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_28)


        self.verticalLayout_4.addWidget(self.frame_15)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_22 = QFrame(self.widget_3)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy8.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy8)
        self.frame_22.setMinimumSize(QSize(0, 50))
        self.frame_22.setMaximumSize(QSize(16777215, 50))
        self.frame_22.setStyleSheet(u"#frame_21{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(214, 214, 214);\n"
"}")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_51 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_51)

        self.label_20 = QLabel(self.frame_22)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setMinimumSize(QSize(42, 0))
        self.label_20.setMaximumSize(QSize(42, 16777215))

        self.horizontalLayout_20.addWidget(self.label_20)

        self.horizontalSpacer_52 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_52)

        self.label_21 = QLabel(self.frame_22)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setStyleSheet(u"#label_17{\n"
"	color: red;\n"
"	font: 700 10pt;\n"
"}")

        self.horizontalLayout_20.addWidget(self.label_21)

        self.horizontalSpacer_53 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_53)

        self.pushButton_12 = QPushButton(self.frame_22)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy14.setHorizontalStretch(3)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy14)
        self.pushButton_12.setMinimumSize(QSize(20, 35))
        self.pushButton_12.setMaximumSize(QSize(16777215, 35))
        icon13 = QIcon()
        icon13.addFile(u":/icon/resource/icon/qq.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon13)

        self.horizontalLayout_20.addWidget(self.pushButton_12)

        self.horizontalSpacer_54 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_54)


        self.verticalLayout_7.addWidget(self.frame_22)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(MainWindow.showMinimized)

        self.pushButton_5.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"v0.23", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"(\u9879\u76ee\u5df2\u5f00\u6e90)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"CuteAide", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u" Github\u5730\u5740", None))
        self.pushButton_4.setText("")
        self.pushButton_3.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u" \u72b6\u6001:", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u7b49\u5f85\u6253\u5f00\u80cc\u5305\u8bc6\u522b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u5206\u8fa8\u7387:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u672a\u8bc6\u522b", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5355\u51fb\u5f00\u955c", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u957f\u6309\u5f00\u955c", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u" C \u952e\u4e0b\u8e72", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u" Ctrl \u952e\u4e0b\u8e72", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u624b\u96f7\u5012\u8ba1\u65f6", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u60ac\u6d6e\u7a97", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" \u5f00\u59cb\u8bc6\u522b\u538b\u67aa", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u" \u8bf7\u4f5c\u8005\u559d\u676f\u5496\u5561\u5427", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" >>>\u6b66\u5668 1 \u914d\u7f6e<<<", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u6b66\u5668", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u500d\u955c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u67aa\u53e3", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u63e1\u628a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u67aa\u6258", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u" >>>\u6b66\u5668 2 \u914d\u7f6e<<<", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u6b66\u5668", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u500d\u955c", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u67aa\u53e3", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u63e1\u628a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u67aa\u6258", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u53d1\u8005: ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Pupper", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u52a0\u7fa4(679556431)", None))
    # retranslateUi

