import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from libs.login.login_win import LoginMainWin
from libs.home.home_win import HomeMainWin


class MainWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.login_win = LoginMainWin()
        self.login_win.show()

    def show_home(self):
        self.home_win = HomeMainWin()
        self.home_win.show()
        self.login_win.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())
