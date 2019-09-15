#包图网的数据http://ibaotu.com/
import requests
from lxml import html

response=requests.get("https://ibaotu.com/shipin/7-0-0-0-0-1.html")
#print(response.text)

html=html.etree.HTML(response.text)

src_list=html.xpath('//div[@class="video-play"]/video/@src')
tit_list=html.xpath('//span[@class="video-title"]/text()')
for src,tit in zip(src_list,tit_list):
    print(src,tit)
    response=requests.get("http:"+src)
    content=requests.get("http:"+src).content
    #确定文件名
    filename=tit+".mp4"
    # with open(filename,"wb")  as f:
    #    f.write(content)
#视频链接