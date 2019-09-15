#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-17 下午 15:07
#file:计算器的设计.py
#design: nchu xlm   讲课子阳老师   颜色https://www.sojson.com/web/panel.html
# 使用tkinter编写登录窗口
# Grid(网格)布局管理器会将控件放置到一个二维的表格里，主控件被分割为一系列的行和列
# stricky设置对齐方式，参数N/S/W/E分别表示上、下、左、右
# columnspan：指定控件跨越多列显示
# rowspan：指定控件跨越多行显示
# padx、pady分别设置横向和纵向间隔大小
import tkinter
import tkinter.font as tkFont
from functools import partial

def get_input(entry,argu):

    input_data=entry.get()
    #检测是否出现++
    if (input_data[-1:]=='+') and (argu=='+'):
        return

    #检测是否出现---
    #检测是否出现--+
    if (input_data[-2:] == '--') and (argu in ['+','-'] ):
        return
    #检测是否出现+--
    if (input_data[-2:] == '+-') and (argu =='-'):
        return
    #检测是否出现***
    #检测是否出现**/

    if (input_data[-2:] == '**') and (argu in ['*', '/']):
        return

    entry.insert("end",argu)




def  backspace(entry):
    input_len=len(entry.get())
    entry.delete(input_len-1)


def clear(entry):
    entry.delete(0,"end")


def calc(entry):
    input_data=entry.get()
    if not input_data:
        return

    try:
        out_data=str(eval(input_data.strip()))      #去除空格
    except Exception as e:
        clear(entry)
        entry.insert("end","Calculation error")
    else:
        clear(entry)
        entry.insert("end",out_data)



def  cal():
    root=tkinter.Tk()
    root.title("Calculator")

    root.resizable(0,0)     #窗口自动大小


    btn_bg='#f5cba7'
    math_sign_bg="#d6eaf8"
    cal_output_bg="#d35400"
    btn_active_bg="#b2babb"

    entry_font=tkFont.Font(size=15)
    entry=tkinter.Entry(root,justify='right',font=entry_font)

    #下面是一个横跨4列的文本框
    entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)       #columnspan 表示横向四列

    # 模板
    myButton=partial(tkinter.Button,root,bg=btn_bg,padx=10,pady=3,activebackground=btn_active_bg)

    button7=myButton(text='7',command=lambda:get_input(entry,'7'))
    button7.grid(row=1,column=0,padx=5,pady=5)

    button8 = myButton(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=1, column=1, padx=5, pady=5)

    button9 = myButton(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=1, column=2, padx=5, pady=5)

    button10 = myButton(text='+', command=lambda: get_input(entry, '+'),bg=math_sign_bg)
    button10.grid(row=1, column=3, padx=5, pady=5)

    button4 = myButton(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=2, column=0, padx=5, pady=5)

    button5 = myButton(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=2, column=1, padx=5, pady=5)

    button6 = myButton(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=2, column=2, padx=5, pady=5)

    button11 = myButton(text='-', command=lambda: get_input(entry, '-'),bg=math_sign_bg)
    button11.grid(row=2, column=3, padx=5, pady=5)

    button1 = myButton(text='1', command=lambda: get_input(entry, '1'))
    button1.grid(row=3, column=0, padx=5, pady=5)

    button2 = myButton(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=3, column=1, padx=5, pady=5)

    button3 = myButton(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=3, column=2, padx=5, pady=5)

    button12 = myButton(text='*', command=lambda: get_input(entry, '*'), bg=math_sign_bg)
    button12.grid(row=3, column=3, padx=5, pady=5)


    button0 = myButton(text='0', command=lambda: get_input(entry, '0'))
    button0.grid(row=4, column=0, columnspan=2,padx=5,ipadx=5, pady=5,sticky=tkinter.E+tkinter.W+tkinter.N+tkinter.S)

    button13= myButton(text='.', command=lambda: get_input(entry, '.'))
    button13.grid(row=4, column=2,ipadx=7, padx=5, pady=5)

    button14 = myButton(text='/', command=lambda: get_input(entry, '/'), bg=math_sign_bg)
    button14.grid(row=4, column=3, columnspan=2, padx=5, pady=5)

    button15 = myButton(text='<-', command=lambda:backspace(entry))
    button15.grid(row=5, column=0, padx=5, pady=5)

    button16 = myButton(text='C', command=lambda:clear(entry))
    button16.grid(row=5, column=1, padx=5, pady=5)

    button17 = myButton(text='=', command=lambda:calc(entry),bg=cal_output_bg)
    button17.grid(row=5, column=2,columnspan=2, padx=5, pady=5,sticky=tkinter.E+tkinter.W+tkinter.N+tkinter.S)



    root.mainloop()


if __name__ == '__main__':
    cal()