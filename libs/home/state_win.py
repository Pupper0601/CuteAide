#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from libs.global_variable import GDV
from tools.log import logger
from views.state import Ui_MainWindow as state_ui


class StateMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = state_ui()
        self.ui.setupUi(self)

        # 隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)  # 窗口置顶, 无任务栏图标
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明

        # 设置鼠标穿透
        self.setWindowFlags(self.windowFlags() | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.move_to_top_center()
        self.posture = 0

    def move_to_top_center(self):
        screen_geometry = QApplication.primaryScreen().geometry()  # 获取屏幕大小
        screen_center = screen_geometry.center()  # 获取屏幕中心点
        frame_geometry = self.frameGeometry()  # 获取窗口大小
        frame_geometry.moveCenter(screen_center)
        frame_geometry.moveTop(-80)  # 将窗口移动到屏幕顶部
        self.move(frame_geometry.topLeft())

    def update_state_gun_info(self, gun_key="0"):
        _num = self.ui.pushButton_11.text()
        _guns = GDV.weapon_information
        _gun_info = None
        if len(_guns) > 0:
            if gun_key == "0":
                if _guns[f"gun_{_num}"]["weapon"][1] != "weapon_none":
                    _gun_info = _guns[f"gun_{_num}"]
                    self.ui.pushButton_11.setText(_num)
                else:
                    _gun_info = _guns[f"gun_{ '2' if _num == '1' else '1'}"]
                    self.ui.pushButton_11.setText('2' if _num == '1' else '1')
            else:
                if _guns[f"gun_{gun_key}"]["weapon"][1] != "weapon_none":
                    _gun_info = _guns[f"gun_{gun_key}"]
                    self.ui.pushButton_11.setText(gun_key)
                else:
                    _gun_info = _guns[f"gun_{'2' if gun_key == '1' else '1'}"]
                    self.ui.pushButton_11.setText('2' if gun_key == '1' else '1')

            logger.info(f"更新 state_win 窗口枪械信息: {_gun_info}")
            GDV.current_weapon_information = _gun_info
            if _gun_info is not None:
                self.ui.pushButton_2.setText(_gun_info["weapon"][0])
                self.ui.pushButton_3.setText(_gun_info["scope"][0])
                self.ui.pushButton_4.setText(_gun_info["muzzle"][0])
                self.ui.pushButton_5.setText(_gun_info["grip"][0])
                self.ui.pushButton_6.setText(_gun_info["stock"][0])

    def update_posture(self, key):
        # 更新姿势
        posture = self.ui.pushButton_12.text()
        posture_map = {
            "c"    : ("蹲姿", "站姿", "squat", "stand"),
            "ctrl_l" : ("蹲姿", "站姿", "squat", "stand"),
            "z"    : ("卧姿", "站姿", "crawl", "stand"),
            "space": ("站姿", "站姿", "stand", "stand")
        }
        if key in posture_map and GDV.posture_state_button == key:
            if posture == posture_map[key][0]:
                self.ui.pushButton_12.setText(posture_map[key][1])
                GDV.posture_state = posture_map[key][3]
            else:
                self.ui.pushButton_12.setText(posture_map[key][0])
                GDV.posture_state = posture_map[key][2]
        elif key in posture_map and key == "z":
            if posture == posture_map[key][0]:
                self.ui.pushButton_12.setText(posture_map[key][1])
                GDV.posture_state = posture_map[key][3]
            else:
                self.ui.pushButton_12.setText(posture_map[key][0])
                GDV.posture_state = posture_map[key][2]
        elif key in posture_map and key == "space":
            self.ui.pushButton_12.setText(posture_map[key][0])
            GDV.posture_state = posture_map[key][2]

    def update_state_shooting_state(self):
        # 更新射击状态
        _state = GDV.shooting_state
        _text = self.ui.pushButton_9.text()
        if _state == "fired":
            if _text == "暂停":
                self.ui.pushButton_9.setText("压枪")
        else:
            if _text == "压枪":
                self.ui.pushButton_9.setText("暂停")


if __name__ == '__main__':
    app = QApplication([])
    window = StateMainWin()
    window.show()
    app.exec()
