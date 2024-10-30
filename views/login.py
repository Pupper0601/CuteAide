# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(658, 486)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 40, 600, 400))
        self.widget.setMinimumSize(QSize(600, 400))
        self.widget.setMaximumSize(QSize(600, 400))
        self.widget.setStyleSheet(u"#widget{\n"
"	border-radius: 20px;\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rbg(0,0,0);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"#label{\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"	\n"
"	background-image: url(:/images/resource/images/login_bg.png);\n"
"}")
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.widget_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setStyleSheet(u"#frame_4{\n"
"	border-top-right-radius: 20px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 5, 12, -1)
        self.horizontalSpacer_16 = QSpacerItem(205, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_16)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(20, 20))
        self.pushButton_2.setMaximumSize(QSize(20, 20))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background:rgb(104,202,93);\n"
"	border: 1px solid rgba(113,17,15,50);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(139,29,31);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_9.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(20, 20))
        self.pushButton_3.setMaximumSize(QSize(20, 20))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background:rgb(234,108,100);\n"
"	border: 1px solid rgba(113,17,15,50);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(139,29,31);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:rgb(232,59,35);\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.widget_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"#frame_5{\n"
"	border: none;\n"
"}")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(93, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"#pushButton{\n"
"	border: none;\n"
"	letter-spacing: 3px;\n"
"	font: 700 20pt \"\u65b0\u5b8b\u4f53\";\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(93, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.widget_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(3)
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setStyleSheet(u"#frame_6{\n"
"	border: none;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setStyleSheet(u"#frame_7{\n"
"	border: none;\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"#label_2{\n"
"	border: none;\n"
"	font: 700 16pt \"Yuanti SC\";\n"
"	letter-spacing: 2px;\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)
        self.lineEdit.setMinimumSize(QSize(186, 25))
        self.lineEdit.setMaximumSize(QSize(186, 16777215))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	font-size: 14px;\n"
"	font: 9pt \"Yuanti SC\";\n"
"	background:rgba(253,253,253,1);\n"
"	border:1px solid rgb(0, 0, 0);\n"
"	border-radius:5px;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:3px solid rgb(44,169,225);\n"
"}")
        self.lineEdit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.horizontalSpacer_7 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setStyleSheet(u"#frame_8{\n"
"	border: none;\n"
"}")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_10 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"#label_3{\n"
"border: none;\n"
"	font: 700 16pt \"Yuanti SC\";\n"
"	letter-spacing: 2px;\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(186, 25))
        self.lineEdit_2.setMaximumSize(QSize(186, 16777215))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	font-size: 23px;\n"
"	font: 9pt \"Yuanti SC\";\n"
"	background:rgba(253,253,253,1);\n"
"	border:1px solid rgb(0, 0, 0);\n"
"	border-radius:5px;\n"
"padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:3px solid rgb(44,169,225);\n"
"}")
        self.lineEdit_2.setDragEnabled(False)

        self.horizontalLayout_5.addWidget(self.lineEdit_2)

        self.horizontalSpacer_8 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"#frame_11{\n"
"	border: none;\n"
"}")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(12, 12, 12, 12)
        self.horizontalSpacer_13 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)

        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"#label_5{\n"
"border: none;\n"
"	font: 700 16pt \"Yuanti SC\";\n"
"	letter-spacing: 2px;\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(self.frame_11)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(186, 25))
        self.lineEdit_3.setMaximumSize(QSize(186, 16777215))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	font-size: 23px;\n"
"	font: 9pt \"Yuanti SC\";\n"
"	background:rgba(253,253,253,1);\n"
"	border:1px solid rgb(0, 0, 0);\n"
"	border-radius:5px;\n"
"padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:3px solid rgb(44,169,225);\n"
"}")

        self.horizontalLayout_8.addWidget(self.lineEdit_3)

        self.horizontalSpacer_15 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setStyleSheet(u"#frame_9{\n"
"	border-bottom-right-radius: 20px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 20, -1, 20)
        self.horizontalSpacer_3 = QSpacerItem(21, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.login_button = QPushButton(self.frame_9)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMinimumSize(QSize(260, 0))
        self.login_button.setMaximumSize(QSize(260, 16777215))
        self.login_button.setStyleSheet(u"#login_button{\n"
"	font: 700 24pt \"Yuanti SC\";\n"
"	background-color: rgb(71,157,168);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 8px;\n"
"	border: 3px solid rgb(71,157,168);\n"
"	letter-spacing: 2px;\n"
"\n"
"}\n"
"\n"
"#login_button:hover{\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"#login_button:pressed{\n"
"	padding-top:8px;\n"
"	padding-left: 8px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.login_button)

        self.horizontalSpacer_4 = QSpacerItem(21, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_10 = QFrame(self.widget_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setStyleSheet(u"#frame_10{\n"
"	border-bottom-right-radius: 20px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_11 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(250, 0))
        self.label_4.setMaximumSize(QSize(250, 16777215))
        self.label_4.setStyleSheet(u"#label_4{	\n"
"	\n"
"	color: rgb(189, 151, 93);\n"
"	letter-spacing: 2px;\n"
"	font: 12pt \"Yuanti SC\";\n"
"}")
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.horizontalSpacer_12 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addWidget(self.frame_10)


        self.horizontalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(MainWindow.showMinimized)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55/\u6ce8\u518c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7:", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801:", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u7bb1:", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u90ae\u7bb1", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55/\u6ce8\u518c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u793a: \u6ce8\u518c\u548c\u767b\u5f55\u4f1a\u540c\u65f6\u8fdb\u884c. \n"
"       \u5982\u679c\u6ca1\u6709\u6ce8\u518c\u4f1a\u76f4\u63a5\u6ce8\u518c! ", None))
    # retranslateUi

