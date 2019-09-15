# -*- coding:utf-8 -*-
#dateTime:2019/3/4 0004 下午 20:22
#file:sevver.py
#design: nchu xlm

import socket

def send_file(new_client_socket,client_add ):
    file_name=new_client_socket.recv(1024).decode("utf-8")
    print ("客户端需要下载的文件是{},客户端口的地址是{}".format(file_name,client_add))

    try:
        file=open(file_name,"rb")
        file_name1=file.read()
        print("%s文件下载完毕!" % str(file_name))
        file.close()

    except Exception as a:
        print("没有你要下载的{}种子".format(file_name))



    if file_name1:
        new_client_socket.send(file_name1)

    else:
        print("文件下载出错!")

def main():
    #创建套接字
    host=""
    port=8888
    tcp_server_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定本地信息  ip=""

    tcp_server_socket.bind((host,port))
    tcp_server_socket.listen(128)

    while True:
        new_client_socket,client_add = tcp_server_socket.accept()
        #print (new_client_socket,client_add)
        send_file(new_client_socket,client_add )


        new_client_socket.close()
    #tcp_server_socket.close()

if __name__ == '__main__':
    main()
