#author:Administrator
#dateTime:2019/2/22 0022 下午 20:15
#file:微信.py
#程序设计: 夏利民
from wxpy import *

#扫码登录,网页端的微信
bot=Bot()
my_friend=bot.friends()
#print(my_friend)
#f=open("friends.txt","w",encoding="utf-8")
for friend in my_friend:
    with open("friends.txt","a",encoding="utf-8") as f:
        f.write(str(friend)+"\n")
        #f.write(str(friend)+'\n')