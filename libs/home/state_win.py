#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

from tools.log import logger
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
        self.posture = 0

    def move_to_top_center(self):
        screen_geometry = QApplication.primaryScreen().geometry()  # 获取屏幕大小
        screen_center = screen_geometry.center()    # 获取屏幕中心点
        frame_geometry = self.frameGeometry()   # 获取窗口大小
        frame_geometry.moveCenter(screen_center)
        frame_geometry.moveTop(-80)  # 将窗口移动到屏幕顶部
        self.move(frame_geometry.topLeft())

    def update_gun(self, gun_info, gun_key=0):
        num = self.ui.pushButton_11.text()
        if gun_key == 0:
            gun = gun_info.get(f"gun_{num}")
            self.ui.pushButton_11.setText(num)
        else:
            gun = gun_info.get(f"gun_{gun_key}")
            self.ui.pushButton_11.setText(gun_key)
        logger.info(f"更新 state_win 窗口枪械信息: {gun}")
        self.ui.pushButton_2.setText(gun.get("weapon"))
        self.ui.pushButton_3.setText(gun.get("scope"))
        self.ui.pushButton_4.setText(gun.get("muzzle"))
        self.ui.pushButton_5.setText(gun.get("grip"))
        self.ui.pushButton_6.setText(gun.get("stock"))
        logger.info(f"更新 state_win 窗口枪械信息完成")

    def update_posture(self, key):
        # 更新姿势
        posture = self.ui.pushButton_12.text()
        if key == "c":
            if posture == "蹲姿":
                self.ui.pushButton_12.setText("站姿")
            else:
                self.ui.pushButton_12.setText("蹲姿")
        elif key == "ctrl":
            if posture == "蹲姿":
                self.ui.pushButton_12.setText("站姿")
            else:
                self.ui.pushButton_12.setText("蹲姿")
        elif key == "z":
            if posture == "卧姿":
                self.ui.pushButton_12.setText("站姿")
            else:
                self.ui.pushButton_12.setText("卧姿")
        elif key == "space":
            self.ui.pushButton_12.setText("站姿")



if __name__ == '__main__':
    app = QApplication([])
    window = StateMainWin()
    window.show()
    app.exec()
