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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(633, 435)
        MainWindow.setMouseTracking(True)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 600, 400))
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
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"#pushButton_4{\n"
"	border: none;\n"
"	font: 700 9pt rgb(255, 0, 0);\n"
"	color: rgb(255, 85, 0);\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_4)

        self.horizontalSpacer_16 = QSpacerItem(150, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_16)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(20, 20))
        self.pushButton_2.setMaximumSize(QSize(20, 20))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(4, 51, 255);\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/resource/icon/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(20, 20))
        self.pushButton_3.setMaximumSize(QSize(20, 20))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(4, 51, 255);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/resource/icon/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(20, 20))

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
"	font: 700 24pt \n"
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
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
"	font: 700 16pt;\n"
"	letter-spacing: 2px;\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.username = QLineEdit(self.frame_7)
        self.username.setObjectName(u"username")
        self.username.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy4)
        self.username.setMinimumSize(QSize(186, 25))
        self.username.setMaximumSize(QSize(186, 16777215))
        self.username.setStyleSheet(u"QLineEdit{\n"
"	font: 10pt;\n"
"	background:rgba(253,253,253,1);\n"
"	border:1px solid rgb(0, 0, 0);\n"
"	border-radius:5px;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:1px solid rgb(44,169,225);\n"
"}")
        self.username.setMaxLength(30)
        self.username.setEchoMode(QLineEdit.EchoMode.Normal)
        self.username.setDragEnabled(False)
        self.username.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.username.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.username)

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
"	font: 700 16pt;\n"
"	letter-spacing: 2px;\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.password = QLineEdit(self.frame_8)
        self.password.setObjectName(u"password")
        self.password.setEnabled(False)
        self.password.setMinimumSize(QSize(186, 25))
        self.password.setMaximumSize(QSize(186, 16777215))
        self.password.setStyleSheet(u"QLineEdit{\n"
"	font: 10pt;\n"
"	background:rgba(253,253,253,1);\n"
"	border:1px solid rgb(0, 0, 0);\n"
"	border-radius:5px;\n"
"padding-left: 5px;\n"
"	padding-right: 5px;\n"
"letter-spacing: 1px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:1px solid rgb(44,169,225);\n"
"}")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setDragEnabled(False)
        self.password.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.password.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.password)

        self.horizontalSpacer_8 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setStyleSheet(u"#frame{\n"
"	border: none;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_6 = QSpacerItem(218, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout_10.addWidget(self.checkBox)


        self.verticalLayout_2.addWidget(self.frame)

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
        self.horizontalLayout_6.setContentsMargins(-1, 12, -1, 9)
        self.horizontalSpacer_3 = QSpacerItem(21, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.login_button = QPushButton(self.frame_9)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMinimumSize(QSize(260, 0))
        self.login_button.setMaximumSize(QSize(260, 16777215))
        self.login_button.setStyleSheet(u"#login_button{\n"
"	font: 700 24pt \"YouSheShaYuFeiTeJianKangTi\";\n"
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
"	padding:8px;\n"
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
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 13)
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
"	font: 9pt ;\n"
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
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u5df2\u5f00\u6e90, \u53ef\u81ea\u884c\u4fee\u6539", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
#if QT_CONFIG(tooltip)
        self.frame_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8bf7\u8f93\u51656~30\u4f4d\u5bc6\u7801</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"CuteAide", None))
#if QT_CONFIG(tooltip)
        self.frame_7.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u51656~30\u4f4d\u5bc6\u7801", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u7bb1:", None))
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6b63\u786e\u7684\u90ae\u7bb1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801:", None))
#if QT_CONFIG(statustip)
        self.password.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u51656~20\u4f4d\u5bc6\u7801", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5f55\u8d26\u53f7", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55/\u6ce8\u518c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u793a:\n"
"  --->> \u76f4\u63a5\u70b9\u51fb\u767b\u5f55\u5373\u53ef\n"
"  --->> \u76f4\u63a5\u70b9\u51fb\u767b\u5f55\u5373\u53ef\n"
"  --->> \u76f4\u63a5\u70b9\u51fb\u767b\u5f55\u5373\u53ef", None))
    # retranslateUi

