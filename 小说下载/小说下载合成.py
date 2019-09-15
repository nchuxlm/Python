# -*- coding:utf-8 -*-
#dateTime:2019/2/26 0026 下午 20:34
#file:语音合成.py
#程序设计: 夏利民  https://www.qidian.com/all
#请求网站 https://book.qidian.com/info/1010468795
#面向对象的设计模式
import requests
from lxml import etree
import os
class Spider(object):
    def start_request(self):
        response=requests.get("https://www.qidian.com/all")
        html=etree.HTML(response.text)
        Bigtit_list=html.xpath('//div[@class="book-mid-info"]/h4/a/text()')
        Bigsrc_list=html.xpath('//div[@class="book-mid-info"]/h4/a/@href')
        for Bigtit,Bigsrc in zip(Bigtit_list,Bigsrc_list):
            if os.path.exists(Bigtit)==False:
                os.mkdir(Bigtit)
            self.file_data(Bigsrc,Bigtit)

    def file_data(self, Bigsrc, Bigtit):
        #得到小说的数据,抽取章节名及文章链接
        response=requests.get("http:"+Bigsrc)
        html=etree.HTML(response.text)  #结构化
        Littit_list=html.xpath('//ul[@class="cf"]/li/a/text()')
        Litsrc_list=html.xpath('//ul[@class="cf"]/li/a/@href')
        for Littit,Litsrc in zip(Littit_list,Litsrc_list):
            #print(Littit,Litsrc)
            self.finally_file(Littit,Litsrc,Bigtit)

    def finally_file(self,Littit,Litsrc,Bigtit):
        #请求到文章内容 创建文件保存到相应的文件夹
        response=requests.get("http:"+Litsrc)
        html=etree.HTML(response.text)
        #read-content j_readContent 在内容页找到<div class="read-content j_readContent">
        content="\n".join(html.xpath('//div[@class="read-content j_readContent"]/p/text()'))

        file_name=Bigtit+"\\"+Littit+".txt"
        with open(file_name,"a",encoding="utf-8") as  f:
            f.write(content)
spider=Spider()
spider.start_request()
