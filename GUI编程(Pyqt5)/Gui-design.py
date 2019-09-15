#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-13 下午 20:17
#file:Gui-design.py
#design: nchu xlm
#pip install pyQt5  学习进度条的使用方法 Gui编程


import sys

from PyQt5.QtWidgets import  QApplication,QWidget,QProgressBar,QPushButton,QDialog
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Test(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        btn = QPushButton('关闭', self)

        btn.clicked.connect(self.my_close)  # ①  信号(btn.clicked)是内置的、槽(self.my_close)是自定义的

    def my_close(self):  # ② 自定义槽
        self.close()
class ProgressBar(QWidget):    #继承自QWidget窗口模块
    #构建方法
    def __init__(self):
        super().__init__()
        self.initUI()
        #点击按钮之后 发送信号  信号和槽函数
        self.btn.clicked.connect(self.doAction)
     #事件处理
    def  timerEvent(self,*args,**kwargs):
        if self.step>=100:
            #停止进度条
            self.timer.stop()
            self.btn.setText('Good')
            return
        self.step+=1
        #把每次重置的值   都赋值给进度条
        self.pbar.setValue(self.step)


        #构建槽函数
    def doAction(self):
        #判断进度条是否牌运行状态
        if self.timer.isActive():
            #停止
            self.timer.stop()

            self.btn.setText("start")
        else:
            self.timer.start(100,self)
            self.btn.setText('Stop')

    # 构建UI界面  -- 实例方法
    def initUI(self):
        #通过对称坐标构建窗口组件大小  280px * 170Px
        self.setGeometry(300,300,280,170)

        self.setWindowTitle('简易进度条的演示')
        #设置图标
        self.setWindowIcon(QIcon('xlm.jpg'))
        #初始化进度条
        self.pbar=QProgressBar(self)
        #设置进度条的界面
        self.pbar.setGeometry(30,50,251,20)
        #初始化按钮
        self.btn=QPushButton('start',self)
        #移动按钮的位置
        self.btn.move(50,90)
        #激活进度条
        self.timer=QBasicTimer()

        self.step=0
        # 显示界面
        self.show()

if __name__ == '__main__':
    #构建应用程序
    app=QApplication(sys.argv)
    #实例化对象
    pbr=ProgressBar()
    dlg = Test()
    dlg.show()
    sys.exit(app.exec_())
