# -*- coding:utf-8 -*-
#dateTime:2019/2/24 0024 下午 20:10
#file:查票12306.py
#程序设计: 夏利民 爬虫 就是代替人去模拟流览器进行网页操作
#第一个作用抓取数据

#买票
#先查询票 -->登录--->订单  异步请求 :一个页面局部的数据进行请求,一个页面的整体框架不变 ajax,

#查询一等软卧的位置,分析,查到车次信息数据,接下来确定一等级软卧票的索引值  南昌 到成都
import requests

def query():

    response=requests.get('https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=2019-03-12&leftTicketDTO.from_station=NCG&leftTicketDTO.to_station=CDW&purpose_codes=ADULT')
    return response.json()['data']['result']
#返回来的数据是个列表
for i in query():
#     #以| 分割数据,更好找到票的位置
     temp_list=i.split('|')
#     #定义一个变量,给每个做个标记
     #j=0
     #for n in temp_list:
#         print(j,n)
#         #下标3 为车次,23 为一等软卧
          #j+=1
#判断
     if temp_list[23]!='无' and temp_list[23]!='':
         #车次 票数
        print(temp_list[3]+'还有',temp_list[23]+'张票')
     else:
        print(temp_list[3],'无票')



