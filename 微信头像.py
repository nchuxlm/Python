#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-20 下午 20:50
#file:微信头像.py
#design: nchu xlm
import itchat
import math
import os
import PIL.Image as Image
from os import listdir
#给auto_login方法传入值为真的hotReload.即使程序关闭，一定时间内重新开启也可以不用重新扫码
def get_imgs():
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends(update=True)
    # 获取自己的用户信息，返回自己的属性字典
    #itchat.search_friends()
    # 获取特定UserName的用户信息
    #itchat.search_friends(userName='@abcdefg1234567')
    # 获取任何一项等于name键值的用户
    #itchat.search_friends(name='littlecodersh')
    # 获取分别对应相应键值的用户
    itchat.search_friends(wechatAccount='littlecodersh')

    #下载所有好友的头像图片
    num = 0
    for friend in friends:
        img = itchat.get_head_img(userName=friend["UserName"])
        #print(userName=friend["UserName"])
        save_path='./headImg/' + str(num) + ".png"
        try:
            with open(save_path,'wb') as f:

                f.write(img)
                print("正在保存第"+str(num)+"张头像")
                f.close()
        except Exception as e:
            print(e)
        num += 1
#制作大的大头像
def get_big_img():

    length = len(os.listdir('./headImg'))   #获取文件夹内的文件个数
    #根据总面积求每一个的大小
    each_size = int(math.sqrt(float(810 * 810) / length))
    #每一行可以放多少个
    lines = int(810 / each_size)
    #生成白色背景新图片
    image = Image.new('RGBA', (810, 810),'white')
    x = 0
    y = 0
    for i in range(0,length):
        try:
            img = Image.open('./headImg/' + str(i) + ".png")

        except IOError:
             print("Error: 没有找到文件或读取文件失败",i)

        else:

            img = img.resize((each_size, each_size), Image.ANTIALIAS) #resize image with high-quality
            image.paste(img, (x * each_size, y * each_size))
            x += 1
            if x == lines:
                x = 0
                y += 1
    image.save('./headImg/' + "all.png")
    #通过文件传输助手发送到自己微信中
    itchat.send_image('./headImg/' + "all.png",'filehelper')

def main():
    get_imgs()
    get_big_img()
if __name__ == '__main__':
    main()