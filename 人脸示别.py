#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-04-01 上午 11:26
#file:人脸示别.py
#design: 夏利民

import cv2


filename = "C://Users/Administrator/Pictures/xy&gth.jpg"


def detect(filemame):

    # haarcascade_frontalface_default.xml存储在package安装的位置
    face_cascade=cv2.CascadeClassifier("D://Program Files/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    image = cv2.imread(filename)           #读取图片.encode('gbk')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  #灰度转换
    # 传递参数是scaleFactor和minNeighbors,分别表示人脸检测过程中每次迭代时图像的压缩率以及每个人脸矩形保留近邻数目的最小值
    # 检测结果返回人脸矩形数组
    # faces = face_cascade.detectMultiScale(         #探测人脸
    #     gray,
    #     scaleFactor = 1.15,
    #     minNeighbors = 5,
    #     minSize = (5,5),
    #     )
    # print("发现{0}个人脸！".format(len(faces)))
    # for(x,y,w,h) in faces:
    #     cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    # cv2.imshow('图像展示!',image)                #显示图像
    # cv2.waitKey(0)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.namedWindow("Face Detected!")
    cv2.imshow("Face Detected!", img)
    cv2.imwrite("images/Face.jpg", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect(filename)

