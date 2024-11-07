#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from views.state import Ui_MainWindow as state_ui
from PySide6.QtWidgets import QApplication, QMainWindow



class StateMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = state_ui()
        self.ui.setupUi(self)

        #隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool) # 窗口置顶, 无任务栏图标
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明
        self.move_to_top_center()

    def move_to_top_center(self):
        screen_geometry = QApplication.primaryScreen().geometry()  # 获取屏幕大小
        screen_center = screen_geometry.center()    # 获取屏幕中心点
        frame_geometry = self.frameGeometry()   # 获取窗口大小
        frame_geometry.moveCenter(screen_center)
        frame_geometry.moveTop(-80)  # 将窗口移动到屏幕顶部
        self.move(frame_geometry.topLeft())

    def update_gun(self, gun_info, gun_key):
        num = self.ui.pushButton_11.text()
        if gun_key == "1":
            gun = gun_info.get("gun_1")
        else:
            gun = gun_info.get("gun_2")
        self.ui.pushButton_11.setText(gun_key)
        self.ui.pushButton_2.setText(gun.get("weapon"))
        self.ui.pushButton_3.setText(gun.get("scope"))
        self.ui.pushButton_4.setText(gun.get("muzzle"))
        self.ui.pushButton_5.setText(gun.get("grip"))
        self.ui.pushButton_6.setText(gun.get("stock"))




if __name__ == '__main__':
    app = QApplication([])
    window = StateMainWin()
    window.show()
    app.exec()
