#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-22 下午 22:47
#file:登录微信获取帐号信息.py
#design: 夏利民   https://cloud.tencent.com/developer/news/309057


"""

Module implementing MainWindow.

"""
from PyQt5.QtCore import QThread, pyqtSignal, Qt, pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from mainwindow import Ui_MainWindow
import sys
import itchat
from itchat.content import *
import datetime
import time
import os
import requests
import json
import re
from urllib.request import urlretrieve
import traceback

current_path = os.path.dirname(os.path.abspath(__file__))

# 登陆微信

class LoginWechat(QThread):

    # 自定义一个信号

    finished_signal = pyqtSignal(object)

    def __init__(self, parent=None, label=None, scroll_widget_layout=None, refresh_button=None, exit_button=None):

        super().__init__(parent)

        self.l = label

        self.scroll_widget_layout = scroll_widget_layout

        self.refresh_button = refresh_button

        self.exit_button = exit_button

    # 在控制台中写入信息

    def outputWritten(self, text=None):

        cursor = self.l.textCursor()

        cursor.movePosition(QtGui.QTextCursor.End)

        cursor.insertText(text)

        self.l.setTextCursor(cursor)

        self.l.ensureCursorVisible()

    # 获取uuid

    def open_qr(self):

        for get_count in range(1):

            self.outputWritten('获取uuid中…… ')

            uuid = itchat.get_QRuuid()

            while uuid is None:

                uuid = itchat.get_QRuuid()

                time.sleep(1)

                self.outputWritten('成功获取uuid ')

                if itchat.get_QR(uuid, picDir=r'%s' % os.path.join(current_path, 'qrcode.jpg')):

                    break

                elif get_count >= 1:

                    self.outputWritten("获取二维码出错，请重启程序 ")

            sys.exit()

        return uuid

    # 二维码登陆

    def login_wechat(self):

        try:

            uuid = self.open_qr()

            self.outputWritten("请扫描二维码 ")

            waitForConfirm = False

            while 1:

                status = itchat.check_login(uuid)

                if status == '200':

                    break

                elif status == '201':

                    if waitForConfirm:

                        self.outputWritten('请进行确认 ')

                        waitForConfirm = True

                elif status == '408':

                    self.outputWritten('重新加载二维码 ')

                    time.sleep(3)
                    uuid = self.open_qr()

            waitForConfirm = False

            userInfo = itchat.web_init()

            # print(userInfo)

            itchat.show_mobile_login()

            print('itchat.show_mobile_login() 执行完成!')

            # itchat.get_friends(True)

            itchat.get_friends()

            print('itchat.get_friends(update=True)[0:] 执行完成!')

            self.outputWritten('登陆成功！账号为：%s ' % userInfo['User']['NickName'])

            itchat.start_receiving()

            print('itchat.start_receiving() 执行完成!')

            self.refresh_button.setText("已登录：{}".format(userInfo['User']['NickName']))

            self.exit_button.setEnabled(True)

        except Exception as e:

            print("登录出错：", e)

            self.outputWritten('登陆出错：{} '.format(e))

        try:

            # 获取群聊列表

            chatrooms = itchat.get_chatrooms()

            print('chatrooms = itchat.get_chatrooms() 执行完成!')

            print(type(chatrooms))

            #return chatrooms

        except Exception as e:

            self.outputWritten("获取群聊列表出错:{} ".format(e))

        try:

            # 获取好友列表

            friends = itchat.get_friends()

            print('friends = itchat.get_friends() 执行完成!')

            print(type(friends))

            #return friends

        except Exception as e:

            self.outputWritten("获取群聊列表出错:{} ".format(e))

        try:

            # 获取好友列表

            mps = itchat.get_mps()

            print('mps = itchat.get_mps() 执行完成!')

            print(type(mps))

            #return mps

        except Exception as e:

            self.outputWritten("获取群聊列表出错:{} ".format(e))

        if chatrooms and friends and mps:

            return [chatrooms, friends, mps]

    def run(self):

        try:

            self.refresh_button.setEnabled(False)

            self.exit_button.setEnabled(True)

            self.finished_signal.emit(self.login_wechat())

        except Exception as e:

            self.outputWritten("运行登录线程出错：{} ".format(e))


class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

    # 在控制台中写入信息

    def outputWritten(self, text=None):

        # 获取文本框中文本的游标

        cursor = self.textEdit.textCursor()

        # 将游标位置移动到当前文本的结束处

        cursor.movePosition(QtGui.QTextCursor.End)

        # 写入文本

        cursor.insertText(text)

        # 设置文本的游标为创建了cursor

        self.textEdit.setTextCursor(cursor)

        self.textEdit.ensureCursorVisible()

    '''
    
    ItChat登陆功能
    
    '''

    @staticmethod

    def _show_message(message):

        print('{}'.format(message))

    # 获取群聊复选框选择状态

    def checkChatRoom(self, state):

        try:

            checkBox = self.sender()

            if state == Qt.Unchecked:

                self.outputWritten(u'取消选择了: '.format(checkBox.id_, checkBox.text()))

                self.chatroom_list.remove(self.chatroom_dict[checkBox.text()])

            elif state == Qt.Checked:

                self.outputWritten(u'选择了: '.format(checkBox.id_, checkBox.text()))

                self.chatroom_list.append(self.chatroom_dict[checkBox.text()])

        except Exception as e:

            self.outputWritten("获取群聊选择状态失败：{} ".format(e))

    # 生成群聊列表

    def generate_chatroom(self, chatrooms):

        # 清空原有群里列表

        while self.gridLayout.count():

            item = self.gridLayout.takeAt(0)

            widget = item.widget()

            widget.deleteLater()

            chatrooms = chatrooms[0]

            self.chatroom_dict = dict()
            try:

                for c, i in zip(chatrooms, range(len(chatrooms))):

                    print(c['NickName'], c['UserName'])

                    checkbox = QCheckBox(c['NickName'])

                    checkbox.id_ = i

                    self.chatroom_dict[c['NickName']] = c['UserName']

                    checkbox.stateChanged.connect(self.checkChatRoom) # 1

                    self.gridLayout.addWidget(checkbox)

                    #self.horizontalLayout_3.addWidget(self.checkBox_2)

                    self.outputWritten("生成群聊成功！ ")

            except Exception as e:\

                print(e)

    # 生成好友列表

    def generate_friends(self, chatrooms):

        # 清空原有群里列表

        while self.verticalLayout_4.count():

            item = self.verticalLayout_4.takeAt(0)

            widget = item.widget()

            widget.deleteLater()

            chatrooms = chatrooms[1]

            self.chatroom_dict = dict()

        try:

            for c, i in zip(chatrooms, range(len(chatrooms))):

                print(c['NickName'], c['UserName'])

                checkbox = QCheckBox(c['NickName'])

                checkbox.id_ = i

                self.chatroom_dict[c['NickName']] = c['UserName']

                checkbox.stateChanged.connect(self.checkChatRoom) # 1

                self.verticalLayout_4.addWidget(checkbox)

                #self.horizontalLayout_3.addWidget(self.checkBox_2)

                self.outputWritten("生成好友成功！ ")

        except Exception as e:

            print(e)

    # 生成公众号列表

    def generate_mps(self, chatrooms):

        # 清空原有群里列表

        while self.verticalLayout_6.count():

            item = self.verticalLayout_6.takeAt(0)

            widget = item.widget()

            widget.deleteLater()

            chatrooms = chatrooms[2]

            self.chatroom_dict = dict()

            try:

                for c, i in zip(chatrooms, range(len(chatrooms))):

                    print(c['NickName'], c['UserName'])

                    checkbox = QCheckBox(c['NickName'])

                    checkbox.id_ = i

                    self.chatroom_dict[c['NickName']] = c['UserName']

                    checkbox.stateChanged.connect(self.checkChatRoom) # 1

                    self.verticalLayout_6.addWidget(checkbox)

                    #self.horizontalLayout_3.addWidget(self.checkBox_2)

                    self.outputWritten("生成公众号成功！ ")

            except Exception as e:

                print(e)

    @pyqtSlot()

    def on_pushButton_clicked(self):

        """

        # 登录微信 - 线程

        """

        # 登录微信 - 线程

        try:

            self.login_wechat_thread = LoginWechat(

            label=self.textEdit,

            scroll_widget_layout=self.verticalLayout,

            refresh_button=self.pushButton,

            exit_button=self.pushButton_2,

            )

            self.login_wechat_thread.finished_signal.connect(self.generate_chatroom)

            self.login_wechat_thread.finished_signal.connect(self.generate_friends)

            self.login_wechat_thread.finished_signal.connect(self.generate_mps)

            #self.login_wechat_thread.finished_signal.connect(self.generate_chatroom)

            self.login_wechat_thread.start()

        except Exception as e:

            print("执行登录线程出错：", e)

            self.outputWritten("执行登录线程出错：{} ".format(e))

    @pyqtSlot()

    def on_pushButton_2_clicked(self):

        """

        注销按钮

        """

        # 设置登录按钮为激活状态

        self.pushButton.setEnabled(True)

        # 在文本控制台中输入

        self.outputWritten("退出微信登录 ")

        # 注销微信登录

        itchat.logout()

        # 设置注销按钮为禁用状态

        self.pushButton_2.setEnabled(False)

        # 更改登陆按钮

        self.pushButton.setText("登录")

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ui = MainWindow()

    ui.show()

    sys.exit(app.exec_())
