import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from libs.login.login_win import LoginMainWin
from libs.home.home_win import HomeMainWin


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
            self.home_win = HomeMainWin()
            self.home_win.show()
            self.login_win.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("resource/images/log.png"))  # 设置应用图标
    window = MainWin()
    sys.exit(app.exec())
