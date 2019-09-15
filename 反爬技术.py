# -*- coding:utf-8 -*-
#dateTime:2019/2/23 0023 下午 20:56
#file:反爬技术.py
#程序设计: 夏利民
import requests
from lxml import etree
index=1
#response=requests.get("https://maoyan.com/board/7")
#html=html.etree.HTML(response.text)

def get_request(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    html=requests.get(url,headers=headers)

    if html.status_code==200:
        return html.text
    else:
        return None

def get_content_page(text):
    html=etree.HTML(text)
    name=html.xpath('//p[@class="name"]//text()')

    star = html.xpath('//p[@class="star"]//text()')
    time = html.xpath('//p[@class="releasetime"]//text()')
    global index
    with open("电影口碑榜前十条.txt",'a+',encoding='utf-8') as file:
        for item in range(10):
            file.write('排名第%s'%index+
                       "的电影名称:\t"+name[item].strip()+
                       "\t"+star[item].strip()+
                       "\t" + time[item].strip() +"\n")
            print('排名第%s'%index+
                       "的电影名称:\t"+name[item].strip()+
                       "\t"+star[item].strip()+
                       "\t" + time[item].strip())
            index+=1
if __name__ == '__main__':
    with open("电影口碑榜前十条.txt", 'w', encoding='utf-8') as file:
        file.write('昨天国内电影前10名排名如下:\n')
    url="https://maoyan.com/board/7"
    html=get_request(url)
    get_content_page(html)

