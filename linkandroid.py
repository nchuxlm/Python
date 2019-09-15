#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-08 下午 15:07
#file:linkandroid.py
#design: nchu xlm
from socket import *
from time import ctime


Host,Port='',8888    #为空代表为本地host
Buffer_size=1024
ADDR=(Host,Port)


tcpServerSocket=socket(AF_INET,SOCK_STREAM)  # IPV4, 传输协议

#绑定域名和端口号
tcpServerSocket.bind(ADDR)

#监听连接,
tcpServerSocket.listen(5)


print("服务器创建成功,等待客户连接...")



while True:

    tcpClientSocket,addr=tcpServerSocket.accept()
    print("连接服务器的客户端对象",addr)
    data=tcpClientSocket.recv(Buffer_size).decode()  # 解码decode, bytes-->str
    while True:
        if not data:break
        print('data=',data)
        tcpClientSocket.send(('[%s]%s'%(ctime(),data)).encode())
        break
        #tcpClientSocket.sendall(data)  # 把接收到数据原封不动的发送回去

    tcpClientSocket.close()

tcpServerSocket.close()




