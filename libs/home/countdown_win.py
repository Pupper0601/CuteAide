#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import time

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from views.countdown import Ui_MainWindow as countdown_ui


class CountDownMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = countdown_ui()
        self.ui.setupUi(self)

        #隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool) # 窗口置顶, 无任务栏图标
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)

        self.set_countdown(5)


    def move_to_top_center(self):
        screen_geometry = QApplication.primaryScreen().geometry()  # 获取屏幕大小
        screen_center = screen_geometry.center()    # 获取屏幕中心点
        frame_geometry = self.frameGeometry()   # 获取窗口大小
        frame_geometry.moveCenter(screen_center)
        frame_geometry.moveRight(-80)  # 将窗口移动到屏幕顶部
        self.move(frame_geometry.topLeft())

    def set_countdown(self, countdown):
        self.countdown = float(countdown)
        self.timer.start(10)

    def update_countdown(self):
        if self.countdown > 0:
            self.ui.label.setText(f"{self.countdown:.2f}")
            self.countdown -= 0.01
        else:
            self.timer.stop()
            self.close()


if __name__ == '__main__':
    app = QApplication([])
    window = CountDownMainWin()
    window.show()
    app.exec()