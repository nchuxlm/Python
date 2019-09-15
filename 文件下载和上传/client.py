# -*- coding:utf-8 -*-
#dateTime:2019/3/4 0004 下午 20:20
#file:fileupload.py
#design: nchu xlm
import socket

def main():
    #创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("请输入服务器的地址:")

    server_port =int(input("请输入服务器的端口:"))

    try:
        #tcp_client_socket.bind(server_ip, server_port)
        tcp_client_socket.connect((server_ip, server_port))
    except socket.error:
        print("连接服务器出错...")
        tcp_client_socket.sendall('echo message')

    download_file_name = input("请输入要下载的种子名:")

    tcp_client_socket.send(download_file_name.encode("utf-8"))


    get_data=tcp_client_socket.recv(1024)

    if get_data:
        with open("[新]" + download_file_name , "wb") as f:
            f.write(get_data)
    else:

        print("你的种子被人删除了!")

    tcp_client_socket.close()


if __name__ == '__main__':
    main()

