#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-19 下午 20:48
#file:mzitu.py
#design: nchu xlm
import  requests
from lxml import etree

# 网站上的头部信息及地址,用逗号分开 Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Referer":"https://www.mzitu.com/tag/ugirls/"
}

response=requests.get("http://www.mzitu.com/tag/ugirls/")
xml=etree.HTML(response.text)


tit_list=xml.xpath('//img[@class="lazy"]/@alt')
src_list=xml.xpath('//img[@class="lazy"]/@data-original')

for tit,src in zip(tit_list,src_list):
    response=requests.get(src,headers=headers)
    #response=requests.get(src)    上面加上headers 是防止反爬设定的
    fileName="photos\\"+tit+".jpg"

    with open(fileName,"wb") as f:
        print ("正在保存照片"+fileName)
        f.write(response.content)


