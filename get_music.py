#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-04-13 下午 15:03
#file:get_music.py
#design: 夏利民
#Lib\urllib文件下发现urllib的__init__.py（初始化函数）是空的，
# 所以当导入urllib时无法使用。只能导入urllib相应的模块。正确的用法应该是：
import urllib.request as urllib
import json

def getmp3url(name):
    html=urllib.urlopen('http://s.music.163.com/search/get/?type=1&s=%s&limit=1'%name).read()
    text=json.loads(html)
    mp3url=text['result']['songs'][0]['page']
    mp3url=mp3url[-8:]   #截取倒数第8位到结尾
    mp3img = text['result']['songs'][0]['album']['picUrl']
    print  (mp3url)
    return  mp3url,mp3img
