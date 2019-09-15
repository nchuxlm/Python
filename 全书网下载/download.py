# -*- coding:utf-8 -*-
#dateTime:2019/2/26 0026 下午 20:34
#file:语音合成.py
#程序设计: 夏利民  https://www.qidian.com/all
#请求网站全书网 http://www.quanshuwang.com/list/1_1.html
#面向对象的设计模式
import requests
from lxml import etree
import re
import os

def get_novel_list():
    response=requests.get("http://www.quanshuwang.com/list/1_1.html")
    response.encoding='gbk'
    html=response.text
    reg = r'<a target="_blank" href="(.*?)" class="l mr10">'
    return re.findall(reg, html)
    #print(re.findall(reg,html))
    #得到网址http://www.quanshuwang.com/book_171152.html


#定义第二个函数 目的:获取章节
def get_chapter_list(novel_url):
    #print(novel_url)
    #请求每一部小说所对应 的URL
    response=requests.get(novel_url)
    response.encoding='gbk'
    html=response.text
    reg='<a href="(.*?)" class="reader"'
    chapter_list_url=re.findall(reg,html)[0]
    #print(chapter_list_url)
    #请求每部小说所对应的开始阅读 章节列表
    response=requests.get(chapter_list_url)

    response.encoding='gbk'
    html=response.text

    reg='<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    #print(re.findall(reg,html))
    return re.findall(reg,html)

def get_chapter_content(chapter_url):
    response=requests.get(chapter_url)
    response.encoding = 'gbk'
    html = response.text
    # 用正则表达式去匹配每一部小说的url

    reg=r'style5\(\);</script>(.*?)<script type="text/javascript">style6\(\)'
    return re.findall(reg,html,re.S)[0]


for novel_url in get_novel_list():
    #print (novel_url)
    #get_chapter_list(novel_url)

    for chapter_url,chapter_name in get_chapter_list(novel_url):

        #print (chapter_url,chapter_name)
        # chspter_url=i[0]
        # chspter_name = i[1]
        # print(chapter_name)
        # print(chapter_url)
        chapter_content=get_chapter_content(chapter_url)

        #保存文件
        fn=open(chapter_name+'.html','w')
        fn.write(chapter_content)
        fn.close()
    break
#不要打开链接



