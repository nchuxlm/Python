#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-05-26 上午 11:59
#file:wifi_test1.py
#design: 夏利民
import pywifi
from pywifi import const
import time
#导入模块
#抓取网卡接口
#断开所有wifi
#读取密码本
#测试连接
#设置睡眠时间


#测试连接.返回连接结果
def wificonnect(pwd):
    wifi=pywifi.PyWiFi()
    ifaces=wifi.interfaces()[0]
    #断开所有连接
    time.sleep(1)
    wifistatus=ifaces.status()
    if wifistatus==const.IFACE_DISCONNECTED:
        #print("未连接")
        #创建wifi 连接
        profile=pywifi.Profile()
        #要连接wifi的名称
        profile.ssid="xlm"
        profile.auth=const.AUTH_ALG_OPEN
        #wifi加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #加密单元
        profile.cipher=const.CIPHER_TYPE_CCMP
        #密码
        profile.key=pwd
        #删除所有的wifi文件
        ifaces.remove_all_network_profiles()
        #设定新的连接文件
        tep_profile=ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        #wifi 连接时间
        time.sleep(4)
        if ifaces.status()==const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已连接")

#wificonnect()
def readPassword():
    print("开始读取")
    path="pass.txt"
    file=open(path,"r")
    while True:
        #如果读取文件错误
        try:
            passStr=file.readline()
            bool=wificonnect(passStr)
            if bool:
                print("密码正确",passStr)
                #跳出当前
                break
            else:
                print("密码不正确", passStr)
        except:
            continue
readPassword()