#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019/3/5 0005 下午 20:29
#file:股票软件.py
#design: nchu xlm
import json
import requests
import pygal
import math
from itertools import groupby

json_url="https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
num=requests.get(json_url)

with open("gs.json","w") as f:
    f.write(num.text)
    file_requests=num.json()   #将json转成列表形式

file_num="gs.json"
with open(file_num) as f:
    gs_data=json.load(f)


dates=[]
months=[]
weeks=[]
weekdays=[]
closes=[]

for gs_data in gs_data:
    #print(gs_data)   #数据成了一条一条
    dates.append(gs_data['date'])
    months.append(gs_data['month'])
    weeks.append(gs_data['week'])
    weekdays.append(gs_data['weekday'])
    closes.append(float(gs_data['close']))


view=pygal.Line()   #柱形 Bar()
view.title="收盘价(￥)"
view.x_labels=dates
closes_log=[math.log(i) for i in closes]
view.add("收盘价",closes_log)
view.render_in_browser()

#分组展示收盘价均值
def day(x_data,y_data,title,y_legend):
   xy_map=[]
   for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda i:i[0]):
       y_list=[v for i,v in y]
       xy_map.append([x,sum(y_list)/len(y_list)])
       x_f1,y_f1=[*zip(*xy_map)]
       view=pygal.Bar()
       view.title=title
       view.x_labels=x_f1
       view.add(y_legend,y_f1)
       view.render_in_browser()
       return view

id_month=dates.index('2017-06-10')
print(id_month)
line_month=day(months[:id_month],closes[:id_month],"收盘价月日均值(￥)","月日均值")
