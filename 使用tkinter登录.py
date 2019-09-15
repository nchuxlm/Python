#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-17 下午 19:49
#file:使用tkinter登录.py
#design: nchu xlm
# 使用tkinter编写登录窗口
# 使用tkinter编写登录窗口
# Grid(网格)布局管理器会将控件放置到一个二维的表格里，主控件被分割为一系列的行和列
# stricky设置对齐方式，参数N/S/W/E分别表示上、下、左、右
# columnspan：指定控件跨越多列显示
# rowspan：指定控件跨越多行显示
# padx、pady分别设置横向和纵向间隔大小
#Python Tkinter Grid布局管理器详解https://www.cnblogs.com/ruo-li-suo-yi/p/7425307.html
#Grid(网格)布局管理器会将控件放置到一个二维的表格里。
# 主控件被分割成一系列的行和列，表格中的每个单元(cell)都可以放置一个控件。
import tkinter as tk
import tkinter.messagebox
import sys

root = tk.Tk()
root.title("用户登录")
root.geometry('250x140')

l_msg = tk.Label(root, text='请登录网站')
l_msg.grid(row=0, columnspan=2)  # 跨越两列显示

# 第一行用户名输入框
l_user = tk.Label(root, text='用户名：')
l_user.grid(row=1, sticky=tk.W)
e_user = tk.Entry(root)
e_user.grid(row=1, column=1, sticky=tk.E, padx=3)

# 第二行密码输入框
l_pwd = tk.Label(root, text='密码：')
l_pwd.grid(row=2, sticky=tk.E)
e_pwd = tk.Entry(root)
e_pwd['show'] = '*'  # 隐藏显示
e_pwd.grid(row=2, column=1, sticky=tk.E, padx=3)

def login():
    '''登录校验'''

    username = e_user.get()
    passwd = e_pwd.get()
    len_user = len(username)
    len_pwd = len(passwd)
    if passwd == '':
        tk.Label(root, text='请输入密码再试', fg='red').place(x=80, y=120)
        return ''
    if username == 'admin' and passwd == '123':
        l_msg['text'] = '登录成功！'
        tk.Label(root, text='', fg='white').place(x=80, y=120)
        l_msg['fg'] = 'green'
    else:
        l_msg.configure(text='登录失败！', fg='red')
        tk.Label(root, text='', fg='white').place(x=80, y=120)
    # e_user.delete(0, len_user)  # 清空输入框
    e_pwd.delete(0, len_pwd)

def quit():
    quit=tkinter.messagebox.askokcancel("提示",'真的要退出吗?')
    if quit==True:
        root.destroy()
# 登录结果提示
# 第三行登录按钮
f_btn = tk.Frame(root)
b_login = tk.Button(f_btn, text='登录', width=6, command=login)
b_login.grid(row=0, column=0)
b_cancel = tk.Button(f_btn, text='取消', width=6, command=quit)
b_cancel.grid(row=0, column=1)
f_btn.grid(row=3, columnspan=2, pady=10)



root.resizable(0, 0)  # 窗口自动大小
root.mainloop()


# 原始按钮布局
# b_login = tk.Button(root, text='登录', command=reg)
# b_login.grid(row=3, column=1, sticky=tk.W, pady=10)
# b_cancel = tk.Button(root, text='取消', command=root.quit)
# b_cancel.grid(row=3, column=1)