# -*- coding:utf-8 -*-
#dateTime:2019/3/1 0001 下午 19:53
#file:download.py
#程序设计: 夏利民  https://movie.douban.com/top250用PythonXpath
import random
import requests
import csv
import lxml.html as HTML
from lxml import etree
import codecs

#第二步, 获取目标网页  start=25 (当面页数-1)*25
# https://movie.douban.com/top250?start=0&filter=  第一页
# https://movie.douban.com/top250?start=25&filter=
doubanUrl='https://movie.douban.com/top250?start={}&filter='
#第三步,解释目标网页

def getSourse(url):   #获取数据
    response=requests.get(url)
    response.encoding='utf-8'
    return response.text

def getEveryItem(source):  #第二个函数,获取电影
    #source=source.decode('utf-8','ignore')
    selector=HTML.document_fromstring(source)
    # //可以提取某个标签所有的信息 @选取属性
    movieItemList=selector.xpath('//div[@class="info"]')
    #定义一个列表,展示电影信息[{}.{}.{}...]
    movieList=[]
    for eachMovie in movieItemList:
        movieDict={}
        title=eachMovie.xpath('div[@class="hd"]/a/span[@class="title"]/text()')
        print(title)
        otherTitle = eachMovie.xpath('div[@class="hd"]/a/span[@class="other"]/text()')
        link = eachMovie.xpath('div[@class="hd"]/a/@href')[0]
        star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]
        quote =eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()')
        if quote:
            quote=quote[0]
        else:
            quote=''
        #把信息存贮到字典上
        movieDict['title']=''.join(title+otherTitle)
        movieDict['star'] = star
        movieDict['quote'] = quote
        movieDict['url']=link
        movieList.append(movieDict)

    return movieList

def writeData(movieList):
    with open('MoveDouban.csv','w',encoding='utf-8',newline='') as f:
        f.write(codecs.BOM_UTF8.decode('utf-8'))
        writer=csv.DictWriter(f,fieldnames=['title','star','quote','url'])
        writer.writeheader()  #写入表头

        for each in movieList:

            writer.writerow(each)

if __name__ == '__main__':
    movieList=[]

    for i in range(1):
        pageLink=doubanUrl.format(i*25)

        source=getSourse(pageLink)

        movieList += getEveryItem(source)

    writeData(movieList)


