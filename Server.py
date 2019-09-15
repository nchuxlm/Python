from socket import *
from time import ctime


HOST,PORT='',666
BuFFER_SIZE=1024

ADDR=(HOST,PORT)

#创建服务器的套接字,第一个参数IPV4,第二个参数传输协议

tcpServerSocket=socket(AF_INET,SOCK_STREAM)


#绑定域名和端口号

tcpServerSocket.bind(ADDR)

#监听转接

tcpServerSocket.listen(5)
print('服务器创建成功.等待客户端连接....')
while True:
    tcpClientScoket,addr=tcpServerSocket.accept()
    print('连接服务器的客户端连对象....',addr)

    while True:
        #decode 解码,encoder 编码
        data=tcpClientScoket.recv(BuFFER_SIZE).decode()

        if not data:
            break
        print('data=',data)
        tcpClientScoket.send(('[%s]%s'%(ctime().data)).encode())
    tcpClientScoket.close()
tcpServerSocket.close()
