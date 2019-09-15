#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-27 上午 10:48
#file:replaywx.py
#design: 夏利民
#登录网页版本的微信后,别人发什么内容 就回复什么内容

import itchat



@itchat.msg_register(itchat.content.TEXT)

def text_reply(msg):

    itchat.send(msg['Text'], msg['FromUserName'])



itchat.auto_login()

itchat.run()