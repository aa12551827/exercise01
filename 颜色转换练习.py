# Author WangKun
# date:20210103
from PyQt5 import QtCore, QtGui, QtWidgets
from RGB_CHANGE import Ui_MainWindow
import sys


class window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.horizontalScrollBar.valueChanged.connect(self.value_1)
        self.horizontalScrollBar_2.valueChanged.connect(self.value_1)
        self.horizontalScrollBar_3.valueChanged.connect(self.value_1)

    def value_1(self):
        self.label_6.setText(str(self.horizontalScrollBar.value()))
        self.label_7.setText(str(self.horizontalScrollBar_2.value()))
        self.label_8.setText(str(self.horizontalScrollBar_3.value()))
        stylesheet = "background-color: rgb(%s, %s, %s)" % \
                     (
        self.horizontalScrollBar.value(), self.horizontalScrollBar_2.value(), self.horizontalScrollBar_3.value()
        )
        self.label.setStyleSheet(stylesheet)
        hex16 =hex(self.horizontalScrollBar.value()).replace('0x','',1)+hex(self.horizontalScrollBar_2.value()).replace('0x','',1)+hex(self.horizontalScrollBar_3.value()).replace('0x','',1)
        print(hex16)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = window()  # 创建窗体对象
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
