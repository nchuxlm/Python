#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-24 下午 12:14
#file:test.py
#design: 夏利民
# -- coding: utf-8 --
""" Module implementing MainWindow. """
from PyQt5.QtCore import QThread, pyqtSignal, Qt, pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from mainwindow import MainWindow
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
class LoginWechat(QThread):
    finished_signal = pyqtSignal(object)
    def init(self, parent=None, label=None, scroll_widget_layout=None, refresh_button=None, exit_button=None):
        super().init(parent)
        self.l = label
        self.scroll_widget_layout = scroll_widget_layout
        self.refresh_button = refresh_button
        self.exit_button = exit_button
    def outputWritten(self, text=None):
        cursor = self.l.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.l.setTextCursor(cursor)
        self.l.ensureCursorVisible()
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
    def login_wechat(self):
        try:
            uuid = self.open_qr()
            self.outputWritten("请扫描二维码 ")
            waitForConfirm = False
            while 1:
                status = itchat.check_login(uuid)
                if status == '200': break
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
            itchat.show_mobile_login()
            print('itchat.show_mobile_login() 执行完成!')
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
                chatrooms = itchat.get_chatrooms()
                print('chatrooms = itchat.get_chatrooms() 执行完成!')
                print(type(chatrooms))
            except Exception as e:
                self.outputWritten("获取群聊列表出错:{} ".format(e))
                try:
                    friends = itchat.get_friends()
                    print('friends = itchat.get_friends() 执行完成!')
                    print(type(friends))
                except Exception as e:
                    self.outputWritten("获取群聊列表出错:{} ".format(e))
                    try:
                        mps = itchat.get_mps()
                        print('mps = itchat.get_mps() 执行完成!')
                        print(type(mps))
                    except Exception as e:
                        self.outputWritten("获取群聊列表出错:{} ".format(e))
                        if chatrooms and friends and mps:return [chatrooms, friends, mps]
                        def run(self):
                                try:
                                    self.refresh_button.setEnabled(False)
                                    self.exit_button.setEnabled(True)
                                    self.finished_signal.emit(self.login_wechat())
                                except Exception as e:
                                    self.outputWritten("运行登录线程出错：{} ".format(e))
class MainWindow(QMainWindow, Ui_MainWindow):
    """ Class documentation goes here. """
    def init(self, parent=None):
        """ Constructor
@param parent reference to the parent widget @type QWidget """
    super(MainWindow, self).init(parent)
    self.setupUi(self)
    def outputWritten(self, text=None):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()
    ''' ItChat登陆功能 '''
    @staticmethod
    def _show_message(message):
        print('{}'.format(message))
    def checkChatRoom(self, state):
        try:
            checkBox = self.sender()
            if state == Qt.Unchecked:
                self.outputWritten(u'取消选择了{0}: {1} '.format(checkBox.id_, checkBox.text()))
                self.chatroom_list.remove(self.chatroom_dict[checkBox.text()])
            elif state == Qt.Checked: self.outputWritten(u'选择了{0}: {1} '.format(checkBox.id_, checkBox.text()))
            self.chatroom_list.append(self.chatroom_dict[checkBox.text()])
        except Exception as e:
            self.outputWritten("获取群聊选择状态失败：{} ".format(e))
    def generate_chatroom(self, chatrooms):
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
                    checkbox.stateChanged.connect(self.checkChatRoom) # 1 self.gridLayout.addWidget(checkbox)
                    self.outputWritten("生成群聊成功！ ")
            except Exception as e:
                print(e)
    def generate_friends(self, chatrooms):
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
                    checkbox.stateChanged.connect(self.checkChatRoom)
                    # 1 self.verticalLayout_4.addWidget(checkbox)
                    self.outputWritten("生成好友成功！ ")
            except Exception as e:
                print(e)
    def generate_mps(self, chatrooms):
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
                    checkbox.stateChanged.connect(self.checkChatRoom)
                    # 1 self.verticalLayout_6.addWidget(checkbox)
                    self.outputWritten("生成公众号成功！ ")
            except Exception as e:
                print(e)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        """
        try:
            self.login_wechat_thread = LoginWechat( label=self.textEdit, scroll_widget_layout=self.verticalLayout, refresh_button=self.pushButton, exit_button=self.pushButton_2, )
            self.login_wechat_thread.finished_signal.connect(self.generate_chatroom)
            self.login_wechat_thread.finished_signal.connect(self.generate_friends)
            self.login_wechat_thread.finished_signal.connect(self.generate_mps)
            self.login_wechat_thread.start()
        except Exception as e:
            print("执行登录线程出错：", e)
            self.outputWritten("执行登录线程出错：{} ".format(e))
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """ 注销按钮 """
        self.pushButton.setEnabled(True)
        self.outputWritten("退出微信登录 ")
        itchat.logout()
        self.pushButton_2.setEnabled(False)
        self.pushButton.setText("登录")
if name == 'main':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())