#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-05-13 下午 22:32
#file:wifipwd.py
#design: 夏利民
import pywifi
from pywifi import const


#判断是否连接到wifi
def gic():
    #创建一个无线对象
    wifi=pywifi.PyWiFi()
    #获取到第一个无线网卡
    ifaces=wifi.interfaces()[0]
    #打印网卡的名称
    #print(ifaces.name())
    #列表
    #print(ifaces)
    #(ifaces.status())   #打印网卡的状态,0 末连接到wifi环境, 连接到 4
    if ifaces.status()==const.IFACE_CONNECTED:
        print("已连接")
    else:
        print("末连接")
#gic()

#扫描附件的wifi
def bies():
    wifi=pywifi.PyWiFi()
    ifaces=wifi.interfaces()[0]
    #扫描wifi
    ifaces.scan()
    #获取扫描结果
    result=ifaces.scan_results()
    for name in result:
       print(name.ssid)

bies()