#南昌航空大学
#信息工程学院
#程序设计:夏利民
import requests
import json
import pygal
from pygal import Line
import math
from itertools import groupby

json_url="https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
num=requests.get(json_url)

with open("gs.json","w") as f:
    f.write(num.text)
    #print(f)
file_requests=num.json()
file_name="gs.json"
#print(file_requests)
with open(file_name) as f:
    gd_data=json.load(f)


#创建五个列表
dates=[]
months=[]
weeks=[]
weekdays=[]
closes=[]

for gs_gd_data in gd_data:
   # print(gd_data)
    dates.append(gs_gd_data["date"])
    months.append(gs_gd_data["month"])
    weeks.append(gs_gd_data["week"])
    weekdays.append(gs_gd_data["weekday"])
    closes.append(float(gs_gd_data["close"]))
    #print(closes)
view=pygal.Line(x_label_rotaion=20,show_minor_x_lables=False)
#view=pygal.StackedBar(x_label_rotaion=20,show_minor_x_lables=False)
view.title="收盘价(￥)"
view.x_lalels=dates
close_log=[math.log(i) for i in closes]
view.add("收盘价",close_log)
#view.render_in_browser()

def day(x_data,y_data,title,y_lengend):
    xy_map=[]
    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda i: i[0]):
        y_list=[v for i,v in y]
        xy_map.append([x,sum(y_list)/len(y_list)])
        x_uniqe,y_mean=[*zip(*xy_map)]
        view=pygal.Line()
        view.title=title
        view.x_lalels=x_uniqe
        view.add(y_lengend,y_mean)
        #view.render_in_browser()
        return view
idx_month=dates.index("2017-10-01")
line_chart_month=day(months[:idx_month],closes[:idx_month],"收盘价月日均值(￥)","月日均值")
line_chart_month

