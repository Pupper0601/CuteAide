import sys

from PySide6.QtWidgets import QApplication, QDialog, QLabel, QMainWindow, QPushButton, QVBoxLayout

from common import notice
from libs.home.home_win import HomeMainWin
from libs.login.login_win import LoginMainWin


class MainWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.login_win = LoginMainWin()
        self.login_win.show()
        self.init_slot()

    def init_slot(self):
        self.login_win.login_ui.login_button.clicked.connect(self.show_home)

    def show_home(self):
        if self.login_win.login_flow():
            self.show_message_box()
            self.home_win = HomeMainWin()
            self.home_win.show()
            self.login_win.close()

    def show_message_box(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("提示")
        layout = QVBoxLayout()

        label = QLabel(notice)
        layout.addWidget(label)

        button = QPushButton("确定")
        button.clicked.connect(dialog.accept)
        layout.addWidget(button)

        dialog.setLayout(layout)
        dialog.exec()


app = QApplication(sys.argv)
window = MainWin()
sys.exit(app.exec())
