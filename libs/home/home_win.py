#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QMainWindow
from views.home import Ui_MainWindow as home_ui


class HomeMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = home_ui()
        self.ui.setupUi(self)
        #隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)



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
