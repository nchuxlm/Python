#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-20 上午 11:42
#file:远程关机.py
#design: nchu xlm
#本机程序中需要有一条执行关机的命令即可

#import os
#os.system('shutdown -s -t 00')  #关机的命令

import socket

def wake_up(request, mac='30-0E-D5-19-18-4F'):
    MAC = mac
    BROADCAST = "192.168.1.100"
    if len(MAC) != 17:
        raise ValueError("MAC address should be set as form 'XX-XX-XX-XX-XX-XX'")
    mac_address = MAC.replace("-", '')
    data = ''.join(['FFFFFFFFFFFF', mac_address * 20])  # 构造原始数据格式
    send_data = b''

    # 把原始数据转换为16进制字节数组，
    for i in range(0, len(data), 2):
        send_data = b''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])
    print(send_data)

    # 通过socket广播出去，为避免失败，间隔广播三次
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(send_data, (BROADCAST, 7))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 7))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 7))
        return HttpResponse()
        print("Done")
    except Exception as e:
        return HttpResponse()
        print(e)

if __name__ == '__main__':
    wake_up()