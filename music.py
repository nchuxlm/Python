#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-04-13 上午 11:25
#file:music.py
#design: 夏利民
import web
from get_music import getmp3url
urls=(
    '/','Index',
    '/s','So',

)
app=web.application(urls,globals())
render=web.template.render('templates')


class Index:
    def GET(self):
        return  render.index();

class So:
    def GET(self):
        i = web.input()  # 获取数据
        name = i.get('name')
        mp3url,mp3pic=getmp3url(name)
        return  render.index(mp3url=mp3url,bgimg=mp3pic)
if __name__ == '__main__':
    app.run()
