# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RGB_CHANGE.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 220)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 38, 121, 121))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(211, 39, 150, 21))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.horizontalScrollBar.setFont(font)
        self.horizontalScrollBar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalScrollBar.setStyleSheet("border-color: rgb(255, 0, 0);")
        self.horizontalScrollBar.setMaximum(255)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(171, 39, 23, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(171, 81, 23, 16))
        self.label_3.setObjectName("label_3")
        self.horizontalScrollBar_2 = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar_2.setGeometry(QtCore.QRect(211, 81, 150, 21))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.horizontalScrollBar_2.setFont(font)
        self.horizontalScrollBar_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalScrollBar_2.setStyleSheet("border-color: rgb(0, 255, 127);")
        self.horizontalScrollBar_2.setMaximum(255)
        self.horizontalScrollBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_2.setObjectName("horizontalScrollBar_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(171, 123, 23, 16))
        self.label_4.setObjectName("label_4")
        self.horizontalScrollBar_3 = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar_3.setGeometry(QtCore.QRect(211, 123, 150, 21))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.horizontalScrollBar_3.setFont(font)
        self.horizontalScrollBar_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalScrollBar_3.setStyleSheet("\n"
"border-color: rgb(0, 255, 255);")
        self.horizontalScrollBar_3.setMaximum(255)
        self.horizontalScrollBar_3.setSliderPosition(0)
        self.horizontalScrollBar_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_3.setObjectName("horizontalScrollBar_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(163, 175, 72, 15))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 171, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 40, 41, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 80, 41, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 120, 41, 20))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "R："))
        self.label_3.setText(_translate("MainWindow", "G："))
        self.label_4.setText(_translate("MainWindow", "B："))
        self.label_5.setText(_translate("MainWindow", "十六进制："))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "0"))
