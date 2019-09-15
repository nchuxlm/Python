#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-05-13 下午 20:57
#file:GetEmail.py
#design: 夏利民

import subprocess
import  os,sys
import time
import poplib,email,re
from email.header import decode_header
from email.parser import BytesParser, Parser
from email.utils import parseaddr
from bs4 import BeautifulSoup

def get_email_subject(addr,password):
    try:
        read=poplib.POP3('pop3.nchu.edu.cn',timeout=3600)
        read.user(addr)  #163邮箱名
        read.pass_(password )   #163信箱设置中的客户端授权码
        Allemial=read.stat()
        num, total_size=read.stat()  # 读取邮件信息(邮件总数,邮件大小)
        newemail= read.top(Allemial[0], 0)  #获得邮件中的第一封邮件主题
        emaillist=[]
        print(newemail[1].decode('gbk'))
        for i in  newemail[1]:  #邮件 主题的编程格式
            emaillist.append(i.decode())
            try:
                emaillist.append(i.decode('gbk'))
            except:
                emaillist.append(i.decode('big5'))
        emaillistadd=email.message_from_string('\n'.join(emaillist))
        emailSublist=decode_header(emaillistadd['Subject'])
        if emailSublist[0][1]:
             getsubject=emailSublist[0][0].decode(emailSublist[0][1])
        else:
             getsubject=emailSublist[0][0]
        return (getsubject,read,num)


        # return (top_email,mail_number,down)
    except poplib.error_proto:
        print ("登录失败:")
        return (-2,0,0)

if __name__ == '__main__':
    addr = "xlm@nchu.edu.cn"
    password = "Nchu13!$"
    get_email_subject(addr, password)
