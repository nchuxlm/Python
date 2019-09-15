#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019/3/5 0005 下午 15:25
#file:copyfile.py
#design: nchu xlm
#浅copy只会copy最顶层的数据,对于不可变的数据类型,只会copy它的引用
# 深拷贝它会递归拷贝,如果是不可变数据类型他只会引用不会拷贝,如果是可变数据类型,它会递归拷贝
# 1. copy.copy 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象。
# 2. copy.deepcopy 深拷贝 拷贝对象及其子对象
import requests

url="https://www.baidu.com/img/baidu_resultlogo@2.png"
response=requests.get(url)

with open("baidu.jpg","wb") as f:
    f.write(response.content)