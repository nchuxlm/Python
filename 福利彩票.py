# -*- coding:utf-8 -*-
#dateTime:2019/2/25 0025 下午 20:35
#file:福利彩票.py
#程序设计: 夏利民
#这个网站先是http://www.cwl.gov.cn/  ,怕个网站是老师给的http://kaijiang.zhcw.com/zhcw/html/3d/list_1.html
import requests
import xlwt
from lxml import etree

f=xlwt.Workbook()
sheet1=f.add_sheet("3D",cell_overwrite_ok=True)
row0=["开奖日期","期号","个位数","十位数","百位数","单选","组选3","组选6","销售额","返奖比例"]
#写入第一行
for j in range(0,len(row0)):
    sheet1.write(0,j,row0[j])
i=1
base_url="http://kaijiang.zhcw.com/zhcw/html/3d/list_{}.html"      #这量的{} 是为了进行翻页时到不同的页面

def get_reponse(target_url):
    #print(requests.get(url=target_url).url) 取了网站的19页内容
    return requests.get(url=target_url)


def write(response):
    global i
    response_xpath=etree.HTML(response.text)
    nodes=response_xpath.xpath("//tr")
    for node in nodes[2:-1]: #参数保存到文本文件
        sheet1.write(i, 0, node.xpath("./td[1]/text()"))
        sheet1.write(i, 1, node.xpath("./td[2]/text()"))
        sheet1.write(i, 2, node.xpath("./td[3]/em[1]/text()"))
        sheet1.write(i, 3, node.xpath("./td[3]/em[2]/text()"))
        sheet1.write(i, 4, node.xpath("./td[3]/em[3]/text()"))
        sheet1.write(i, 5, node.xpath("./td[4]/text()"))
        sheet1.write(i, 6, node.xpath("./td[5]/text()"))
        sheet1.write(i, 7, node.xpath("./td[7]/text()"))
        sheet1.write(i, 8, node.xpath("./td[8]/strong/text()"))
        sheet1.write(i, 9, node.xpath("./td[9]/text()"))
        i+=1


for j in range(1,20):           #功能是为了得到1-19页的信息
    response=get_reponse(base_url.format(j))
    #print(response)
    write(response)

f.save("3d.xls")
