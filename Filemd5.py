#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-06 下午 20:16
#file:Filemd5.py
#design: nchu xlm
import random   #随机数
import string
import os
#加密逻辑
def encode(plain_text, key):
    # //地板除 + 余数 +切片
    ker = key*(len(plain_text)//len(key)) + key[:len(plain_text)%len(key)]
    cipher_text = []
    for item in range(len(plain_text)):
        cipher_text.append(str(ord(plain_text[item])^ord(key[item])))
    return ','.join(cipher_text)


# 解密逻辑   - 解密就是加密的逆过程

def decode(cipher_text, key):
    cipher_text = cipher_text.split(',')
    # //地板除 + 余数 +   切片
    ker = key * (len(cipher_text) // len(key)) + key[:len(cipher_text) % len(key)]
    plain_text = []
    for item in range(len(cipher_text)):
        plain_text.append(chr(int(cipher_text[item]) ^ ord(key[item])))
    return ''.join(plain_text)


if __name__ == '__main__':
    function = input('请输入1为加密模式,输入2为解密模式:')

    if function == "1":
        plain_text = input('请输入要加密的明文')
        key = input("请输入密钥:")
        print('密文为:%s' %encode(plain_text, key).encode('utf-8'))
        os.system('pause')
    if function == '2':
        cipher_text = input('请输入要解密的密文')
        key = input("请输入密钥")
        print('明文为:%s'%decode(cipher_text, key).encode('utf-8'))
        os.system('pause')
#加密的逻辑
# def encode(str_1,key):
#     random.seed(key)
#     str_2=" "
#     for item in str_1:
#         #相同为0,不同为1
#         str_2 += str(ord(item) ^ random.randint(0,255))+','     #ord('a') 结果97
#     str_2=str_2.strip(',')
#1

#     return  str_2
#
#
# #解密逻辑
# def decode(str_2,key):
#    random.seed(key)
#    str_1=""
#    for item in str_2.split(','):
#        item=int(item)
#        str_1+=chr(item ^ random.randint(0, 255))
#
#    return str_1
#
# choice=input('加密(1) 解密(2):')
# if choice=='1':
#     str_1=input('请输入要加密的明文')
#     key=input("请输入密钥:")
#     print(encode(str_1,key))
# elif choice=='2':
#     str_2=input('请输入要解密的密文')
#     key=input("请输入密钥")
#     print(decode(str_2,key))
# else:
#     print("输入错误!")

# numbers = 0
# # while numbers <= 5:
# #     random.seed(6)
# #     # [0.0 -1.0]
# #     print(random.random())
# #     numbers += 1