#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-05-13 下午 23:04
#file:password.py
#design: 夏利民https://v.youku.com/v_show/id_XMzczMjA3NzAzNg==.html?spm=a2h0j.11185381.listitem_page1.5!14~A
import itertools as its
import random
#迭代器

words="xialimin"
r=its.product(words,repeat=4)
#r=its.combinations(words,4)

#保存在文件中,追加
dic=open("pass.txt","a")


for i in r:
    #12345
    #("c','c')  i 是无组
    #print (i)
    dic.write("".join(i))  #按空格来连接
    dic.write("".join("\n"))
dic.close()