#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-04-10 下午 15:17
#file:spider_bais.py
#design: 夏利民   'http://www.budejie.com/video/'

import urllib.request,re,requests

url_name=[]


def get():
    #获取源码
    '''
    User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
    :return:
    '''
    hd={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    url="http://www.budejie.com/video/"
    html=requests.get(url, headers=hd).text
    # https: // www.crummy.com / software / BeautifulSoup / bs4 / doc / index.zh.html
    url_content=re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)',re.S)   #re.S 表示匹配所有
    url_contents=re.findall(url_content,html)

    #print(url_contents)
    for i in url_contents:
        url_reg=r'data-mp4="(.*?)"'     #视频
        url_items=re.findall(url_reg,i)

        if url_items:    #判断视频是否存在
            name_reg=re.compile(r'<a href="/detail-.{8}?.html">(.*?)</a>',re.S)
            #print(name_reg)
            name_items=re.findall(name_reg,i)

            for i,k in zip(name_items,url_items):
                url_name.append([i,k])
                print(i,k)
    #保存视频
    for  i in url_name:
        print(i[0])
        print(i[1])
        urllib.request.urlretrieve(i[1], '%s.mp4' % ( i[0] ))



if __name__ == '__main__':
    get()





