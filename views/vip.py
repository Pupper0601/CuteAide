# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vip.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(432, 368)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(120, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 361, 311))
        self.widget.setStyleSheet(u"#widget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(182, 182, 182);\n"
"	\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setStyleSheet(u"#frame_6{\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"#pushButton_2{\n"
"	border: none;\n"
"	font: 700 16pt;\n"
"	color: rgb(170, 0, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/resource/icon/vip.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setStyleSheet(u"#frame{\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(212, 212, 212)\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"#label_4{\n"
"	color: rgb(255, 169, 64);\n"
"	letter-spacing: 1px;\n"
"	font: 500 10pt;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.frame)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(3)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.widget_2.setStyleSheet(u"#widget_2{\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(212, 212, 212)\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	border: none;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(23, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"#radioButton{\n"
"	font: 700 10pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.radioButton)

        self.horizontalSpacer_6 = QSpacerItem(22, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.radioButton_2 = QRadioButton(self.frame_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"#radioButton_2{\n"
"	font: 700 10pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.radioButton_2)

        self.horizontalSpacer_7 = QSpacerItem(22, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.radioButton_4 = QRadioButton(self.frame_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"#radioButton_4{\n"
"	font: 700 10pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.radioButton_4)

        self.horizontalSpacer_8 = QSpacerItem(22, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.radioButton_5 = QRadioButton(self.frame_2)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"#radioButton_5{\n"
"	font: 700 10pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.radioButton_5)

        self.horizontalSpacer_9 = QSpacerItem(23, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setStyleSheet(u"#frame_4{\n"
"	border: none;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_12 = QSpacerItem(11, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"#label{\n"
"	color:rgb(255, 78, 24);\n"
"	font: 700 12pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_13 = QSpacerItem(0, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_13)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"#label_2{\n"
"	color:rgb(255, 0, 0);\n"
"	font: 700 14pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_14 = QSpacerItem(3, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_14)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"#label_3{\n"
"	color:rgb(255, 0, 0);\n"
"	font: 700 14pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_10 = QSpacerItem(13, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 0))
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.setStyleSheet(u"#pushButton{\n"
"	font: 700 16pt ;\n"
"	background-color: rgb(71,157,168);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(71,157,168);\n"
"	letter-spacing: 1px;\n"
"\n"
"}\n"
"\n"
"#pushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border: 3px solid rgb(255, 0, 0);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.horizontalSpacer_15 = QSpacerItem(21, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(80, 0))
        self.pushButton_3.setMaximumSize(QSize(80, 16777215))
        self.pushButton_3.setStyleSheet(u"#pushButton_3{\n"
"	font: 700 14pt ;\n"
"	background-color: rgb(158, 158, 158);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(158, 158, 158);\n"
"	letter-spacing: 1px;\n"
"\n"
"}\n"
"\n"
"#pushButton_3:hover{\n"
"	background-color: rgb(12, 12, 12);\n"
"	color: rgb(255,255,255);\n"
"border: 3px solid rgb(12, 12, 12);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.horizontalSpacer_11 = QSpacerItem(11, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" VIP\u6743\u76ca\u8bf4\u660e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"1.\u6c38\u4e45 VIP \u7528\u6237\u80fd\u591f\u4f7f\u7528\u8f6f\u4ef6\u6240\u6709\u529f\u80fd;\n"
"2.\u9650\u65f6 VIP \u7528\u6237\u5728\u6709\u6548\u671f\u4e3a\u5185\u53ef\u4ee5\u4f7f\u7528\u4ed8\u8d39\u529f\u80fd;\n"
"3.\u6240\u6709 VIP \u7528\u6237\n"
"1.\u6c38\u4e45 VIP \u7528\u6237\u80fd\u591f\u4f7f\u7528\u8f6f\u4ef6\u6240\u6709\u529f\u80fd;\n"
"2.\u9650\u65f6 VIP \u7528\u6237\u5728\u6709\u6548\u671f\u4e3a\u5185\u53ef\u4ee5\u4f7f\u7528\u4ed8\u8d39\u529f\u80fd;\n"
"3.\u6240\u6709 VIP \u7528\u6237\n"
"1.\u6c38\u4e45 VIP \u7528\u6237\u80fd\u591f\u4f7f\u7528\u8f6f\u4ef6\u6240\u6709\u529f\u80fd;\n"
"", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5468\u5361", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6708\u5361", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u5361", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6c38\u4e45", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"168", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u00a5", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u8d2d\u4e70", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
    # retranslateUi

