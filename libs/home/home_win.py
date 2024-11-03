#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

from libs.state_win import StateMainWin
from views.home import Ui_MainWindow as home_ui
from tools.screen_resolution import get_monitor_info



class HomeMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = home_ui()
        self.ui.setupUi(self)
        self.setWindowTitle("CuteAide")
        #隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.init_slot()

    # 初始化槽函数
    def init_slot(self):
        self.resolution()
        self.ui.checkBox_2.stateChanged.connect(self.state_show)
        self.ui.pushButton_2.clicked.connect(self.start_gun)


    # 设置屏幕分辨率
    def resolution(self):
        monitor_info = get_monitor_info()
        self.ui.label_2.setText(f"{monitor_info['width']}x{monitor_info['height']}")

    # 显示状态窗口
    def state_show(self):
        self.child_win_state = StateMainWin()
        self.state_win = StateMainWin()
        if self.ui.checkBox_2.isChecked():
            self.child_win_state.show()
        else:
            self.state_win.close()

    def start_gun(self):
        text = self.ui.pushButton_2.text()
        if text == " 开始识别压枪":
            self.ui.pushButton_2.setText(" 暂停识别压枪")
            self.ui.pushButton_2.setIcon(QIcon("../../resource/icon/stop.png"))
            self.ui.pushButton_2.setStyleSheet("#pushButton_2{font: 700 20pt ;background-color: rgb(255,85,"
                                               "0);color: rgb(255,255,255);border-radius: 10px;border: 3px solid "
                                               "rgb(255,85,0);letter-spacing: 1px;}#pushButton_2:hover{"
                                               "background-color: rgb(255,255,255);color: rgb(0,0,0);}")
        else:
            self.ui.pushButton_2.setText(" 开始识别压枪")
            self.ui.pushButton_2.setIcon(QIcon("../../resource/icon/start.png"))
            self.ui.pushButton_2.setStyleSheet("#pushButton_2{font: 700 20pt ;background-color: rgb(71,157,"
                                               "168);color: rgb(255,255,255);border-radius: 10px;border: 3px solid "
                                               "rgb(71,157,168);letter-spacing: 1px;}#pushButton_2:hover{"
                                               "background-color: rgb(255,255,255);color: rgb(0,0,0);}")





    # ----------- 窗口拖动 -----------
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and not self.isMaximized():
            self.mm_flag = True
            self.m_Position = event.globalPosition().toPoint() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, mouseMove):
        if Qt.LeftButton and self.mm_flag:
            self.move(mouseMove.globalPosition().toPoint() - self.m_Position)
            mouseMove.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.mm_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HomeMainWin()
    window.show()
    sys.exit(app.exec())

