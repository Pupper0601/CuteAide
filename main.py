import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QApplication, QMainWindow

from views.login import Ui_MainWindow


# from views.login_win import Ui_MainWindow


class LoginMainWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

        #-----------------移动功能---------------------

        def mousePressEvent(self, event):  # 鼠标左键按下时获取鼠标坐标
            if event.button() == Qt.LeftButton:
                self._move_drag = True
                self.cursor_win_pos = event.globalPosition() - self.pos()
                event.accept()

        def mouseMoveEvent(self, event):  # 鼠标在按下左键的情况下移动时,根据坐标移动界面
            # 移动事件
            if Qt.LeftButton and self._move_drag:
                m_Point = event.globalPosition() - self.cursor_win_pos
                self.move(m_Point.x(), m_Point.y())
                event.accept()

        def mouseReleaseEvent(self, event):  # 鼠标按键释放时,取消移动
            self._move_drag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)    # 创建APP，将运行脚本时（可能的）的其他参数传给Qt以初始化
    window = LoginMainWin()   # 实例化一个MyWidget类对象
    # window.show()  # 显示窗口
    sys.exit(app.exec())    # 正常退出APP：app.exec()关闭app，sys.exit()退出进程