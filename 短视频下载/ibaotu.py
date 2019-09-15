#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-16 下午 21:27
#file:ibaotu.py
#design: nchu xlm
import requests
from lxml import etree


response=requests.get("http://ibaotu.com/shipin/")   #网站下的文件都可以http://ibaotu.com/shipin/7-5138-0-0-2-1.html

html=etree.HTML(response.text)

tit_list=html.xpath('//span[@class="video-title"]/text()')

src_list=html.xpath('//div[@class="video-play"]/video/@src')

for tit,src in zip(tit_list,src_list):
    response=requests.get("http:"+src)

    fileName="video\\"+tit+".mp4"
    print("正在保存视频文件:"+fileName)

    with open(fileName,"wb") as f:
        f.write(response.content)