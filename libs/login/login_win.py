#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
from pathlib import Path

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QCursor, QRegularExpressionValidator, Qt
from PySide6.QtWidgets import QMainWindow

from views.login import Ui_MainWindow as login_ui


class LoginMainWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.login_ui = login_ui()
        self.login_ui.setupUi(self)
        self.setWindowTitle("CuteAide")

        # 隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        regex = QRegularExpression(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        validator = QRegularExpressionValidator(regex)
        self.login_ui.username.setValidator(validator)
        self.login_ui.password.setValidator(validator)

        # self.login_text()  # 读取登录信息

    def login_flow(self):
        username = self.login_ui.username.text()
        password = self.login_ui.password.text()
        record_password = self.login_ui.checkBox.isChecked()
        return True
        # _res = Login(username, password, record_password).login()
        # logger.info(f"登录结果: {_res}")
        # if _res["code"] == "101":
        #     return True
        # else:
        #     return _res["message"]

    def login_text(self):
        _file_path = "C:/CuteAide/login_info.txt"

        path = Path(_file_path)  # 创建文件
        if not path.is_file():  # 如果文件不存在, 则创建文件
            path.parent.mkdir(parents=True, exist_ok=True)  # 创建文件夹
            path.touch()  # 创建文件

        if Path(_file_path).exists():
            with open(_file_path, 'r') as f:
                _user = f.read()
        else:
            return
        if _user:
            _user = _user.split(",")
            if _user[2] == "True":
                self.login_ui.username.setText(_user[0])
                self.login_ui.password.setText(_user[1])
                self.login_ui.checkBox.setChecked(_user[2] == "True")

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
