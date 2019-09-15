#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019/3/5 0005 下午 22:35
#file:downloadimg.py
#design: nchu xlm

import requests
from pyquery import PyQuery as py
html=requests.get("http://news.4399.com/gonglue/lscs/kptj").content.decode("gb2312")

doc=py(html)
#查询到所有的li 条目  id(#) class(.)
item=doc("#dq_list > li").items()

for item_xlm in item:
    url=item_xlm.find('img').attr('lz_src')
    name=item_xlm.find('.kp-name').text()

    download_url=requests.get(url).content
    #print(name,url)
    with open('xlm_4399/'+name+'.jpg','wb') as file:
        file.write(download_url)
print('下载完毕............')


