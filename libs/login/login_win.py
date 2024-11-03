#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from PySide6.QtGui import QCursor, Qt
from PySide6.QtWidgets import QMainWindow

from views.login import Ui_MainWindow as login_ui


class LoginMainWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.login_ui = login_ui()
        self.login_ui.setupUi(self)
        self.setWindowTitle("CuteAide")

        #隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def login_flow(self):
        login_data = {}
        login_data['username'] = self.login_ui.lineEdit.text().strip()
        login_data['password'] = self.login_ui.lineEdit_2.text().strip()
        login_data['email'] = self.login_ui.lineEdit_3.text().strip()
        login_data['check_box'] = self.login_ui.checkBox.isChecked()
        return True


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