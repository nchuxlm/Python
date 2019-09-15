# -*- coding:utf-8 -*-
#dateTime:2019/2/22 0022 下午 22:04
#file:view.py
#程序设计: 夏利民
# Lib\site-packages\web 下的utils文件
# Chances are they'll need to change:
#
# yield next(seq)
# to:
#
# try:
# yield next(seq)
# except StopIteration:
# return


# URL映射有3种类型：
#  1.URL完全匹配
#  '/index','Index'，由Index类处理 http://127.0.0.1:8080/index
# 2.URL模糊匹配
#  '/post/\d+','Post'，由Post类处理 如http://127.0.0.1:8080/post/3，post/后面带一个数字的URL
#  3.URL带组匹配
#  '/post2/(\d+)','Post2',Post2类处理 如http://127.0.0.1:8080/post2/3，post2/后面带一个数字的URL，Post2类会接受处理url post2后面的参数。而模糊匹配的方式是不处理参数的。
import web   #pip install web.py==0.40.dev1 文件夹下安装:python setup.py install
import sys
from tkinter import *
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

urls = (
    '/', 'Index',

)
app = web.application(urls, globals())
#指定模板目录,并设定公共模板
render=web.template.render('templates')
#db=web.database(dbn='mysql')
class Index:
    def GET(self):
       return render.index()
class Reg:
    def GET(self):
        return render.reg()
    def POST(self):
        i=web.input()  #获得用户发起的请求
        userName=i.username   #u 前面有个U 代表编码
        Password=i.password
        return 'OK'
if __name__ == "__main__":
    app.run()
