#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-11 下午 20:36
#file:百度fanyi.py
#design: nchu xlm

#https://fanyi.baidu.com/?aldtype=16047#auto/zh    f12 在网络选项 XHR 中左边有一个v2transapi

import requests
import json

class FanYi(object):
    def __init__(self,query_sting,zh="zh",en="en"):
        self.url="https://fanyi.baidu.com/transapi"    #去了这个单诩V2transapi前面 的 V2

        self.query_string=query_sting

        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        self.zh=zh
        self.en=en

    def get_post_data(self):
        #这个格式从网站上可以找到,From Data
        post_data={
            "from":self.zh,
            "to":self.en ,
            "query":self.query_string
        }
        return post_data


    def get_url(self,url,data):
        response=requests.post(url,data=data,headers=self.headers)
        return  response.content.decode()


    def get_data(self,json_str):
        data_dict=json.loads(json_str)

        fy=data_dict["data"][0]["dst"]

        print("{}:{}".format(self. query_string, fy))


    def run(self):
        post_data=self.get_post_data()

        json_str=self.get_url(self.url,post_data)
        self.get_data(json_str)


if __name__ == '__main__':
    while True:
        try:
            strs=input("请输入要翻译的内容:")
            ss=input("从中文到英文请输入zh,否则输入en")
            aa=input("翻译成英语输入en,否则输入zh")
            fanyi=FanYi(strs,ss,aa)
            fanyi.run()
        except Exception as ss:
            print("您输入的参数有误")
            break




