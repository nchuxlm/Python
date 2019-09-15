#!/usr/bin/env pytho
# -*- coding:utf-8 -*-
#dateTime:2019/3/4 0004 下午 15:07
#file:mtxx.py
#design: nchu xlm
# openCV 实现图片的点击效果 pip install opencv-python ,https://pypi.org/project/opencv-python/
#安装后无法使用,下载对应的wheel 文件https://pypi.org/project/opencv-python/#files,找到对应的版本
#pip install opencv-python 安装最新的OpenCV3.3开发包

#pip install opencv-contrib-python 安装最新的OpenCV3.3扩展
#pip install matplotlib
#如果你不想安装扩展模块，只运行第一行命令即可
#PyCharm 中安装 opencv-python 包之后，会出现 PyCharm 的自动补全功能不能正确识别 cv2 模块的问题。
# 使用pip 或者 PyCharm 的包管理界面安装 jedi 包可解决。
import cv2


image=cv2.imread('C:/Users/Administrator/Pictures/xlm.jpg')   #写绝对路径,加载一张图片

# #定义一个窗口,展示图片https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html
#--->Gui Features in OpenCV 进入 --->Mouse as a Paint-Brush--->Simple Demo

cv2.namedWindow('window')

"""

cv2.WINDOW_NORMAL     窗口大小可改变

cv2.WINDOW_AUTOSIZE   窗口大小不可改变

cv2.WINDOW_FREERATIO  自适应比例

cv2.WINDOW_KEEPRATIO  保持比例饿

cv2.WINDOW_GUI_NORMAL

cv2.WINDOW_GUI_EXPANDED
"""

def draw(event,x,y,flags,param):
     if event==cv2.EVENT_LBUTTONDOWN:
         print("鼠标---->按下")
     elif event==cv2.EVENT_MOUSEMOVE:
         print("鼠标---->滑动")
     elif event==cv2.EVENT_LBUTTONUP:
         print("鼠标---->抬起")
#cv2.setMouseCallback('window',draw)
#cv2.imshow('window',image)   #展示窗口
#cv2.waitKey()    #窗口闪退   2000时间
#cv2.destroyAllWindows()     #销毁窗口

#图片的模糊效果
# image_dst=cv2.blur(image,(15,15))

# #cv2.namedWindow('window')
# #
# cv2.imshow('window',image_dst)   #展示窗口
# #
# cv2.waitKey(0)    #窗口闪退   2000时间
# #
# cv2.destroyAllWindows()     #销毁窗口
#
# #图片的美颜效果,第一个参数美颜的对象,第二个参数 美颜的程度 ,值越大程度越大.值越小程度越小
#双边滤波是一种非线性的滤波方法，是结合图像的空间邻近度和像素值相似度的一种折衷处理，
# 同时考虑空间与信息和灰度相似性，达到保边去噪的目的，具有简单、非迭代、局部处理的特点。
# 之所以能够达到保边去噪的滤波效果是因为滤波器由两个函数构成：一个函数是由几何空间距离
# 决定滤波器系数，另一个是由像素差值决定滤波器系数.
#Python: cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]])
value=20
mage_dst=cv2.bilateralFilter(image,value,value*2,value/2)
# 参数解释：
# src：输入图像
# d：过滤时周围每个像素领域的直径
# sigmaColor：在color space中过滤sigma。参数越大，临近像素将会在越远的地方mix。
# sigmaSpace：在coordinate space中过滤sigma。参数越大，那些颜色足够相近的的颜色的影响越大。

# 其中mage_dst是blur处理后返回的图像，参数一是输入的待处理图像，
# 参数2是低通滤波器的大小。其后含有几个可选参数，
# 用来设置滤波器的细节，具体可查阅参考资料
#
cv2.imwrite("C:\\Users\\Administrator\\Pictures\\xlm_new.jpg",mage_dst)
cv2.imshow('window',mage_dst)   #展示窗口

cv2.waitKey()    #窗口闪退   2000时间
#
cv2.destroyAllWindows()     #销毁窗口

