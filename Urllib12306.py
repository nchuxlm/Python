#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-12 下午 17:51
#file:Urllib12306.py
#design: nchu xlm
'''
第一行写了会在右下角显示成UTF-8,python3 默认的是Unicode
python 3.x中urllib库和urilib2库合并成了urllib库。。
其中urllib2.urlopen()变成了urllib.request.urlopen()
       urllib2.Request()变成了urllib.request.Request()
'''
import urllib.request
import ssl
from json import loads
#收下内容可以不用网站案例验证
ssl._create_default_https_context=ssl._create_unverified_context
def getTicketlist():
    res = urllib.request.urlopen(
    "https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=2019-03-12&leftTicketDTO.from_station=NCG&leftTicketDTO.to_station=BJP&purpose_codes=ADULT")

    html = res.read()
    result=loads(html)
    return result['data']['result']


'''

'''
m=1
for i in getTicketlist():
    a = 0
    temp_list=i.split('|')
    for n in  temp_list:
        print ('[%s]%s'%(a,n))
        a+=1
    m +=1
    if  (m==2):
         break


