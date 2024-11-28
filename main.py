import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QMainWindow, QPushButton, QVBoxLayout

from common import notice
from libs.home.home_win import HomeMainWin
from libs.login.login_win import LoginMainWin
from tools.paths import path_conn


class MainWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.login_win = LoginMainWin()
        self.login_win.show()
        self.home_win = HomeMainWin()
        self.init_slot()

    def init_slot(self):
        self.login_win.login_ui.login_button.clicked.connect(self.show_home)

    def show_home(self):
        _res = self.login_win.login_flow()
        self.home_win.show()
        self.login_win.close()
        self.show_message_box(notice, "提示", path_conn("resource/icon/success.png"))

        # if _res is True:
        #     self.show_message_box(notice, "提示", path_conn("resource/icon/success.png"))
        #     self.home_win.show()
        #     self.login_win.close()
        # else:
        #     self.show_message_box(_res, "错误", path_conn("resource/icon/error.png"))

    def show_message_box(self, info, title, icon):
        dialog = QDialog(self)
        dialog.setWindowTitle(title)
        dialog.setStyleSheet("padding: 10px;")
        dialog.setWindowIcon(QIcon(icon))
        layout = QVBoxLayout()

        label = QLabel(info)
        layout.addWidget(label)

        button = QPushButton("确定")
        button.clicked.connect(dialog.accept)
        layout.addWidget(button)

        dialog.setLayout(layout)
        dialog.exec()


app = QApplication(sys.argv)
window = MainWin()
sys.exit(app.exec())
