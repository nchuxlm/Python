#author:Administrator
#dateTime:2019/2/22 0022 下午 20:40
#file:群聊.py
#程序设计: 夏利民
from wxpy import *
bot=Bot()
#初始化机器人(api_key:图灵http://www.turingapi.com/)

tuling=Tuling(api_key="efcb2b5289324ce9a994b82f69bc7691")

#自动回复的文字消息     装饰器：用于注册消息配置
@bot.register()
def auto_reply_all(msg):
    #tuling.do_reply(msg)
    print("接收:"+str(msg))
    s=input("输入要回复的内容:")     #任意位置换行通过快捷键 Shfit + Enter

    msg.reply(s)
    #msg.reply("这是自动回复")
    #msg.reply_image("xlm.jpg")

#开始运行

bot.join()    #shift+Tab 向左缩进