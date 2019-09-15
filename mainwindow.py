#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-24 下午 22:43
#file:mainwindow.py.py
#design: 夏利民
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_mainwindow import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.Title.setText("hello Python")
        self.World.clicked.connect(self.onWorldClicked)
        self.China.clicked.connect(self.onChinaClicked)
        self.lineEdit.textChanged.connect(self.onlineEditTextChanged)

    def onWorldClicked(self, remark):
        print(remark)
        self.Title.setText("Hello World")

    def onChinaClicked(self):
        self.Title.setText("Hello China")

    def onlineEditTextChanged(self,p_str):
        self.Title.setText(p_str)

