#!/usr/bin/env python
# -*- coding: utf-8 -*-
#dateTime:2019/3/3 0003 下午 20:35
#file:download.py
#程序设计: 夏利民   百思不得姐http://www.budejie.com/video
'''
File》Setting》Editor》Code Style》File and Code Templates 右边三个卡边这file --->找到Python Script
#!/usr/bin/python是告诉操作系统执行这个脚本的时候，调用/usr/bin下的python解释器。
#!/usr/bin/env python这种用法是为了防止操作系统用户没有将python装在默认的/usr/bin路径里。当系统看到这一行的时候，首先会到env设置里查找python的安装路径，再调用对应路径下的解释器程序完成操作。这种写法会去环境设置寻找python目录,推荐这种写法
'''
import requests
import  os
import threading
from bs4 import BeautifulSoup

def get_requests(url):
    #   requests.get(url).content.decode('utf-8') 这样就可以看到中文了
    html=requests.get(url).content   #bytes 字节一样的文件,xe5\xbe\xae\xe5\x8
    # print(html)   #返回<Response [200]> 成功
    return html

#第二步 提取内容 方式有六种
def get_content(html):
    #1. 用html.parser   2.lxml    class="j-r-list-c"
    soup=BeautifulSoup(html,'html.parser')
    #根据HTML网页字符串创建BeautifulSoup对象
    '''
     soup=BeautifulSoup(
                    html,    #html 文档字符串
                    'html.parser' ,    #HTML 解释器
                    from_encoding='utf-8'  #HTML文档的编码
                    )
    '''
    """   id(#)  -css -class (.)    -    """
    content = soup.select('.j-r-list-c')
    url_list=[]

    for item in content:

        name=item.find('a').text
        #tem.find  这个find 不能弹出是什么原因?

        url_mp4_path=item.select('.j-video')[0].get('data-mp4')
        #print(url_mp4_path)
        url_list.append((name,url_mp4_path))
    return url_list

#第三步  通过多线程模块 异步下载这个视频
def get_mp4_url(url_list):
    file_path=os.path.join(os.getcwd(),'xlm_mp4')
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    for item in url_list:

        if item[1]==None:
            continue
        name_str=item[0].strip() if len(item[0])<30 else item[0].strip()[:27]+'...'
        url_list_mp4=os.path.join(file_path,'%s.%s'%(name_str.strip(),item[1][-3:]))
        t=threading.Thread(target=save_mp4,args=(item[1],url_list_mp4))
        t.start()

def save_mp4(url,url_list_mp4):
    response=get_requests(url)
    with open(url_list_mp4,'wb+')  as file:
        file.write(response)

if __name__ == '__main__':
    url = 'http://www.budejie.com/video/2'
    html=get_requests(url)
    url_list=get_content(html)
    get_mp4_url(url_list)







