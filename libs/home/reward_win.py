#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QPixmap
from PySide6.QtWidgets import QMainWindow

from common import reward_label
from tools.paths import path_conn
from views.reward import Ui_MainWindow as reward_ui


class RewardMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = reward_ui()
        self.ui.setupUi(self)

        # 隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)  # 窗口置顶, 无任务栏图标
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明
        print(path_conn("/resource/img/wx.png"))
        pixmap_2 = QPixmap(path_conn("/resource/img/wx.png"))
        pixmap_3 = QPixmap(path_conn("/resource/img/zfb.png"))

        self.ui.label_2.setPixmap(pixmap_2)
        self.ui.label_3.setPixmap(pixmap_3)
        self.ui.label_2.setScaledContents(True)
        self.ui.label_3.setScaledContents(True)

        self.ui.label.setText(reward_label)
        self.ui.pushButton_3.clicked.connect(self.close)

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
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = RewardMainWin()
    win.show()
    sys.exit(app.exec())
