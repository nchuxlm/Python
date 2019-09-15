# -*- coding:utf-8 -*-
#dateTime:2019/2/28 0028 下午 20:15
#file:download.py
#程序设计: 夏利民  https://www.duitang.com/topics/
import requests
import urllib.parse
import threading
#设置最大线程锁
thread_lock=threading.BoundedSemaphore(value=5)
# 动态加载和json串   http://www.bejson.com/


# 字体串的高级查找


# 图片的下载及写入




# 多线程
#https://www.duitang.com/search/?kw=%E6%A0%A1%E8%8A%B1&type=feed
#从HXR 向下翻页,从左边选择数据进行复制
#https://www.duitang.com/napi/blog/list/by_search/?kw=%E6%A0%A1%E8%8A%B1&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&start=96&_=1551359055335

#第一步通过URL获取数据
def get_page(url):
    page=requests.get(url).content.decode("utf-8")  #200 请求成功 bytes

    return page
#第二步

def findll_in_page(page,startpart,endpat):
    all_strings=[]
    end=0
    while page.find(startpart,end)!=-1:
        #起始坐标
        start=page.find(startpart,end)+len(startpart)

        end=page.find(endpat,start)
        #print (start),(end)  110 461  814 1165
        string=page[start:end]

        all_strings.append(string)
    return all_strings

#3.网络链接
def pic_urls_pages(pages):
    pic_urls=[]
    for page in pages:
        urls=findll_in_page(page,'"path":"','"')


        pic_urls.extend(urls)
    return pic_urls

#4 请求得到所有页面的URL并获取 数据
def pages_from_url_tang(label):
    pages=[]
    url = "https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}&limit=100"
    #将中文转换成URL码
    label=urllib.parse.quote(label)

    for index in range(0,100,100):   # 总共300张,每一张100个,共三页

        u=url.format(label,index)   #这是U的值 https://www.duitang.com/napi/blog/list/by_search/?kw=杨幂&start=0&limit=100

        page=get_page(u)
        pages.append(page)

    return pages
#5 通过URL下载单张图片

def download_pics(url,name):
    req=requests.get(url)
    path='tmwj/'+str(name)+'.jpg'

    with open(path,'wb+') as file:
        file.write(req.content)
    #下载完成 解锁,否则停了不下去
    thread_lock.release()

# 6 汇总文件
def main(label):
    pages=pages_from_url_tang(label)
    #print(pages)
    pic_urls=pic_urls_pages(pages)
    #print(pic_urls)
    numbers=0
    for url in pic_urls:
        numbers+=1
        print("正在下载的是第{}张".format(numbers))
        #上锁 监控线程数
        thread_lock.acquire()
        #将单个 下载的函数当成一个
        t=threading.Thread(target=download_pics,args=(url,numbers))
        t.start()
        #ownload_pics(url,numbers)


main('杨幂')













