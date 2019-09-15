#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-22 下午 21:09
#file:微信签到.py
#design: 夏利民
import threading
from itchat.content import TEXT
import itchat, time, sys,os
def output_info(msg):
    print('[INFO] %s' % msg)
def open_QR():
    num=input("请输入今天签到的人数")
    try:
        num=int(num)
    except Exception as e:
        num=1
    for get_count in range(num):
        output_info('Getting uuid')
        uuid = itchat.get_QRuuid()
        while uuid is None:
            uuid = itchat.get_QRuuid()
            time.sleep(10)
            output_info('Getting QR Code')
        if itchat.get_QR(uuid):
            break
        elif get_count >= num:
            output_info('获取二维码出错，请重启程序')
            sys.exit()
            output_info('请重新扫二维码')
    return uuid
#得到微信的UID1
uuid = open_QR()    #已扫描二维码uuid ->'201'

waitForConfirm = False
while 1:
    status = itchat.check_login(uuid)      #返回值：登陆成功->'200'，已扫描二维码->'201'，二维码失效->'408'，未获取到信息->'0'

    if status == '200':
        break
    elif status == '201':
        if waitForConfirm:
            output_info('Please press confirm')
            waitForConfirm = True
    elif status == '408':
        output_info('Reloading QR Code')
        uuid = open_QR()
        waitForConfirm = False

userInfo = itchat.web_init()
itchat.show_mobile_login()
itchat.get_contact()
# 用当天的时间作为文件名.txt,记录点名的学生信息
filename = time.strftime("%Y-%m-%d", time.localtime(time.time())) + ".txt"
if not os.path.exists(filename):
    os.system(r"touch{}".format(filename))
with open(filename, "a", encoding="utf-8") as f:
   f.write(userInfo['User']['NickName'] + "同学于" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "上课签到" + "\n")
output_info('Login successfully as %s' % userInfo['User']['NickName'])
itchat.start_receiving()
# Start auto-replying
@itchat.msg_register(itchat.content.TEXT)
def simple_reply(msg):
    if msg['Type'] == 'Text':
        return 'I received: %s' % msg['Content']
itchat.run()
