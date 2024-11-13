#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

from libs import global_variable
from libs.home.state_win import StateMainWin
from libs.mouselisten import MouseListen
from libs.pressure import Pressure
from tools.log import logger
from views.home import Ui_MainWindow as home_ui

from tools.paths import path_conn
from .resolution_state import resolution
from libs.keylisten import KeyListen


class HomeMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = home_ui()
        self.ui.setupUi(self)
        self.setWindowTitle("CuteAide")
        #隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.state_win = StateMainWin()  # 初始化 state_win
        self.key_listener = None
        self.mouse_listener = None
        self.init_slot()

    # 初始化槽函数
    def init_slot(self):
        self.resolution()
        self.ui.checkBox_2.stateChanged.connect(self.state_show)
        self.ui.pushButton_2.clicked.connect(self.start_gun)
        self.ui.radioButton_3.clicked.connect(self.update_posture_buttons)
        self.ui.radioButton_4.clicked.connect(self.update_posture_buttons)
        self.ui.radioButton.clicked.connect(self.update_mouse_gun)
        self.ui.radioButton_2.clicked.connect(self.update_mouse_gun)
        self.ui.checkBox_3.clicked.connect(self.update_continuous_clicks)

    # 设置屏幕分辨率
    def resolution(self):
        _info = resolution()
        self.ui.label_2.setText(f"{_info['resolution']}")
        self.ui.label_4.setText(_info['state'])

    # 更新识别状态
    def update_way(self, text):
        self.ui.pushButton_10.setText(text)

    # 显示悬浮窗窗口
    def state_show(self):
        if self.ui.checkBox_2.isChecked():
            self.state_win.show()
        else:
            self.state_win.close()

    # 开始识别压枪
    def start_gun(self):
        text = self.ui.pushButton_2.text()
        if text == " 开始识别压枪":
            self.ui.pushButton_2.setText(" 暂停识别压枪")
            self.ui.pushButton_2.setIcon(QIcon(path_conn("/resource/icon/stop.png")))
            self.ui.pushButton_2.setStyleSheet("#pushButton_2{font: 700 20pt ;background-color: rgb(255,85,"
                                               "0);color: rgb(255,255,255);border-radius: 10px;border: 3px solid "
                                               "rgb(255,85,0);letter-spacing: 1px;}#pushButton_2:hover{"
                                               "background-color: rgb(255,255,255);color: rgb(0,0,0);}")

            self.key_listener = KeyListen(self) # 启动键盘监听器并传递 self 作为父对象
            self.key_listener.start()

            self.mouse_listener = MouseListen(self)  # 启动鼠标监听器并传递 self 作为父对象
            self.mouse_listener.start()

        else:
            self.ui.pushButton_2.setText(" 开始识别压枪")
            self.ui.pushButton_2.setIcon(QIcon(path_conn("/resource/icon/start.png")))
            self.ui.pushButton_2.setStyleSheet("#pushButton_2{font: 700 20pt ;background-color: rgb(71,157,"
                                               "168);color: rgb(255,255,255);border-radius: 10px;border: 3px solid "
                                               "rgb(71,157,168);letter-spacing: 1px;}#pushButton_2:hover{"
                                               "background-color: rgb(255,255,255);color: rgb(0,0,0);}")
            if self.key_listener:
                self.key_listener.stop_event.set()  # 停止延时任务
                self.key_listener.stop_listener()
                self.key_listener = None

            if self.mouse_listener:  # 停止鼠标监听器
                self.mouse_listener.stop_event.set()
                self.mouse_listener.stop_listener()
                self.mouse_listener = None


    def update_home_gun_info(self, _gun_info):
        # 更新枪械信息
        if len(_gun_info) > 0:
            # 在这里添加显示枪械信息的代码，例如更新UI组件
            logger.info(f"接收到的枪械信息: {_gun_info}")
            self.ui.label_6.setText(f"{_gun_info['gun_1']['weapon'][0]}")
            self.ui.label_7.setText(f"{_gun_info['gun_1']['scope'][0]}")
            self.ui.label_8.setText(f"{_gun_info['gun_1']['muzzle'][0]}")
            self.ui.label_10.setText(f"{_gun_info['gun_1']['grip'][0]}")
            self.ui.label_9.setText(f"{_gun_info['gun_1']['stock'][0]}")

            self.ui.label_11.setText(f"{_gun_info['gun_2']['weapon'][0]}")
            self.ui.label_12.setText(f"{_gun_info['gun_2']['scope'][0]}")
            self.ui.label_13.setText(f"{_gun_info['gun_2']['muzzle'][0]}")
            self.ui.label_14.setText(f"{_gun_info['gun_2']['grip'][0]}")
            self.ui.label_15.setText(f"{_gun_info['gun_2']['stock'][0]}")

            self.state_win.update_state_gun_info()
            logger.info("枪械信息更新完成")
            self.update_way("识别完成")
        else:
            logger.info("未识别到枪械信息, 请重新识别")

    def update_home_current_gun(self, gun_key):
        # 更新当前枪械
        if gun_key == "1":
            self.ui.pushButton.setIcon(QIcon(path_conn("/resource/icon/now.png")))
            self.ui.pushButton_6.setIcon(QIcon())
        elif gun_key == "2":
            self.ui.pushButton.setIcon(QIcon())
            self.ui.pushButton_6.setIcon(QIcon(path_conn("/resource/icon/now.png")))

    def update_posture_buttons(self):
        # 判断当前选中的姿势
        if self.ui.radioButton_3.isChecked():   # C 键 下蹲
            global_variable.posture_state_button = "c"
            self.ui.radioButton_4.setIcon(QIcon())
            self.ui.radioButton_3.setIcon(QIcon(path_conn("/resource/icon/keyboard.png")))
        elif self.ui.radioButton_4.isChecked(): # ctrl 键 下蹲
            global_variable.posture_state_button = "ctrl"
            self.ui.radioButton_3.setIcon(QIcon())
            self.ui.radioButton_4.setIcon(QIcon(path_conn("/resource/icon/keyboard.png")))

    def update_mouse_gun(self):
        # 更新开镜方式
        if self.ui.radioButton.isChecked():
            self.ui.radioButton_2.setIcon(QIcon())
            self.ui.radioButton.setIcon(QIcon(path_conn("/resource/icon/mouse.png")))
            global_variable.opening_method = "click"
            Pressure()
        elif self.ui.radioButton_2.isChecked():
            self.ui.radioButton.setIcon(QIcon())
            self.ui.radioButton_2.setIcon(QIcon(path_conn("/resource/icon/mouse.png")))
            global_variable.opening_method = "long_press"
            Pressure()

    def update_continuous_clicks(self):
        # 更新连点开关
        if self.ui.checkBox.isChecked():
            global_variable.continuous_clicks = "open"
            Pressure()
        else:
            global_variable.continuous_clicks = "close"
            Pressure()


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

