import sys

from PySide6.QtWidgets import QApplication, QDialog, QLabel, QMainWindow, QPushButton, QVBoxLayout

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

        label = QLabel(
            """
登录成功! \n
    欢迎使用 CuteAide 应用程序。\n\n
公告：\n
    1. 目前应用只适用于 1920*1080 分辨率, 如能提供其他分辨率资源图不胜感谢.\n
    2. 目前使用的是其他群友提供的弹道, 后续会进行精调, 有能力的用户可以自己调试.\n
    3. 目前有些功能比较粗糙, 后续会进行优化.\n
    4. 欢迎加入 QQ群, 后续更新优先在群内发布.\n
    5. 如有好的思路或者建议,请联系管理员.\n
    6. 文明、 和谐、理性、互助、共赢\n
            """)
        layout.addWidget(label)

        button = QPushButton("确定")
        button.clicked.connect(dialog.accept)
        layout.addWidget(button)

        dialog.setLayout(layout)
        dialog.exec()


app = QApplication(sys.argv)
window = MainWin()
sys.exit(app.exec())
