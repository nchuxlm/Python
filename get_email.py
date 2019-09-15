#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-04-24 下午 15:13
#file:get_email.py
#design: 夏利民
from GetEmail import get_email_subject
import os
import time

#os.system("ping www.baidu.com")


# while True:
#     f=open('conf.txt','r')
#     content=f.read()
#     os.system(content)
#     time.sleep(5)

command_set={
    "重启":"shutdown -r -t ",
    "关机":"shutdown -s -t ",
    "excel":r"E:\test.xlsx ",
}#shutdown -a 取消自动关机
email_addr="xlm@nchu.edu.cn"
email_password= "Nchu13!$"
control_password="67515"

#"关机,600,8831632" =>["关机","600","883162"] "600"  =>600
while True:
    subject,read,total_num=get_email_subject(email_addr,email_password)
    subject=subject.replace("，",",")   # 把中文的标点换成英文的标点  "关机，600，控制密码"
    subject_list=subject.split(",")

    if len(subject_list)>=3:
        command,execute_time,con_password=subject_list  #相当于subject_list[0],subject_list[1],subject_list [2]

        #设置关机时间为2分钟, 防止0直接关机 ,如果没有设置时间为空也将报错isdecimal()
        if execute_time.isdecimal() and int(execute_time)<120:
            execute_time="120"
        execute_command=command_set[command]+execute_time
        print(subject_list,execute_command)
        read.dele(total_num)
        read.quit()
        if control_password==con_password:
            os.system(execute_command)
            break

    else:
        time.sleep(10)




