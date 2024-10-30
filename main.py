import sys

from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QGridLayout,QFileDialog,QMessageBox
from PySide6.QtCore import Qt,QThread,Signal
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QEvent, QTimer,QTime
from PySide6.QtGui import QIcon,QPainter,QBrush,QColor,QCursor,QPixmap,QImage,QConicalGradient,QPen,QFont
from PySide6 import QtCore,QtWidgets

# from views.login_win import Ui_MainWindow


from views.login import Ui_MainWindow


class LoginMainWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

    #窗口拖动
    ##############################################################################
    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton and self.isMaximized() == False:
            self.mm_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self,mouseMove):
        if Qt.LeftButton and self.mm_flag:
            self.move(mouseMove.globalPos()-self.m_Position)
            mouseMove.accept()
    def mouseReleaseEvent(self,mouse_event):
        self.mm_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
    ##############################################################################


if __name__ == '__main__':
    app = QApplication(sys.argv)    # 创建APP，将运行脚本时（可能的）的其他参数传给Qt以初始化
    window = LoginMainWin()   # 实例化一个MyWidget类对象
    # window.show()  # 显示窗口
    sys.exit(app.exec())    # 正常退出APP：app.exec()关闭app，sys.exit()退出进程