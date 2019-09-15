#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-07 下午 15:39
#file:ciyun.py
#design: nchu xlm
from wordcloud import WordCloud
import matplotlib.pyplot as plt


f=open(r'tanmu.txt','r',encoding='utf-8').read()
backgroup=plt.imread(r'xlm.jpg')   #背景图


#构造词云图
word=WordCloud(
    mask=backgroup,
    background_color='white',
    font_path=r'wrhzt.TTF',
    width=1000,
    height=800,
    max_words=3000,
    min_font_size=10
).generate(f)

plt.imshow(word)
plt.axis('off')  #默认开启
plt.show()

