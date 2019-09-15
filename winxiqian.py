#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-08 下午 14:56
#file:winxiqian.py
#design: nchu xlm
# pip3 install turtle  因为turtle库主要是在Python2中使用的，所以安装的时候可能会提示错误：
#import turtle  打包 pip install pyinstaller

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget,QDesktopWidget,QLCDNumber,QApplication,QVBoxLayout
import  sys
import time
from time import strftime,localtime

class MyTime(QWidget):
     """
     面向对象的特点：封装、继承、多态---（类、方法、数据）
      __init__是python语言里面的构造方法
     """
    #构造方法
     def __init__(self):
        # 用于解决多重继承的问题
        super().__init__()
        self.initUI()
        self.init_timer()
    #设置 更新时间
     def update_time(self):

        #通过时间无组 获取本地系统时间,作为显示时间 x:03 23 19j 是日期, 大写X 表示时钟09:46:54
        #print(strftime('%Y-%m-%d %H:%M:%S', localtime()))
        self.lcd.display(time.strftime('%X',time.localtime()))
     #设置定时器
     def init_timer(self):
        #初始化定时器
        self.timer=QTimer()
        #设置发送信号的间隔时间
        self.timer.setInterval(1000)
        self.timer.start()
        #发送信号
        self.timer.timeout.connect(self.update_time)

    #绘制UI界面

     def initUI(self):
        #设置窗口显示组件大小
        self.resize(260,150)
        #设置标题
        self.setWindowTitle("创意个性的LCD电子时钟")
        #设置图标
        self.setWindowIcon(QIcon('logo.png'))



        #初始化  调色板
        self.plt=QPalette()
        #设置背景颜色
        self.plt.setColor(QPalette.Background,Qt.darkYellow)
        #设置窗体自动填充背景颜色
        self.setAutoFillBackground(True)
        #设置给顶层布局
        self.setPalette(self.plt)
        self.show()

        #初始化LCD组件
        self.lcd=QLCDNumber()

        #设置显示的个数
        self.lcd.setDigitCount(10)

        #设置显示的模式为十进制

        self.lcd.setMode(QLCDNumber.Dec)

        # 设置当前显示的样式为平面模式
        self.lcd.setSegmentStyle(QLCDNumber.Flat)

        #初始化盒子布局
        self.box=QVBoxLayout()

        #将显示的组件添加到盒子布局里面
        self.box.addWidget(self.lcd)
        self.box.setAlignment(Qt.AlignCenter)
        #设置窗口背景透明
        self.setWindowOpacity(1)
        #self.setAttribute(QtCore.Qt.WA_TransIucentBackground)
        # 设置给顶层布局
        self.setLayout(self.box)
        #设置布局内部件的间隙来把哪条缝隙去除掉
        self.box.setSpacing(0)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    my_time=MyTime()
    #消息循环结束之后返回0，接着调用sys.exit(0)退出程序
    #app.exec_()--------------消息循环结束之后，进程自然也会结束
    sys.exit(app.exec_())