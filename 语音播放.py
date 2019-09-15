# -*- coding:utf-8 -*-
#dateTime:2019/2/26 0026 下午 21:38
#file:yyhc2.py
#程序设计: 夏利民
#引用http://www.cnblogs.com/ljc-0923/p/10265894.html
from  aip import AipSpeech

import os
# 申请的Ai.baidu.com的ID,接口,密钥
#APP_ID = '15217709'
#API_KEY = 'eNiP5QUsgBh6QwpbNv8Qmsy3'
#SECRET_KEY = 'gwhM3wDo0Kjjd1PDIxqqW4Bfex10Y4f3'   # 这个是网站上的
#app_id="14975947"
#api_key="X9f3qewZCohppMHxlunznUbi"
#secret_key="p1bMLME6msfQZlRL4HP12S1C"   #这个是上课老师的帐号
APP_ID = '15640852'
API_KEY = 'p1bMLME6msfQZlRL4HP12S1C'
SECRET_KEY = 'w8u1OpoeUmiOxr08O9bHhEzY6Ojxhh6Q'
# 实例化AipSpeech,AipNlp对象
client=AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 调节发音的会泽的
# 第一个可以放要转化吃那个语音的文字
result=client.synthesis('同志们好,南昌航空大学欢迎您的到来','zh',1,{
    "per":4, #表示是男音还是女音 0 普通女声 1为普通男 3 为情感合成-度逍遥 4. 为情感合成度YY
    "spd":6, #音速
    "pir":7, #语调
    "vol":10, #音量
})
# 识别正确返回语音二进制 错误则返回dict ,这时返回的是文件文本
#isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
if not isinstance(result, dict):

    with open("audio.mp3","wb") as f:
        f.write(result) # 把二进制语音写入到文件中
'''
# 定义一个读取文件的函数
def get_file_content(filePath):
    # 把wma格式的文件转化为.pcm格式的文件
    os.system(f"ffmpeg -y -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.wma.pcm")
    # 把转化了的格式保存到当前目录
    with open(f"{filePath}.wma.pcm", 'rb') as fp:
        # 返回这个文件读取的内容
        return fp.read()  # 并把这个文件返回给调用者


# get_file_content("cg.m4a")
# 识别本地文件,  把本地的语音文件转成pcm个格式的文件并把语音转化成二进制文件
res = client.asr(get_file_content('xh.m4a'), 'pcm', 16000, {
    'dev_pid': 1536,
})
print(res, type(res))
 {'corpus_no': '6637053740205578210', 'err_msg': 'success.', 'err_no': 0, 'result': ['给我讲个笑话'], 'sn': '757488757051545309494'}, <class 'dict'>

Q = res.get("result")[0]
# 取到输入的主要内容
print(1,Q)  # 1 给我讲个笑话
# 判断是不是问的是名字,是拿Q和"你叫什么"做相似度匹配如果大于0.7,则表明用户表达的是这个意思
if nlp_client.simnet(Q, "你叫什么?").get("score") >= 0.7:
    A = "我的名字叫雪雪"
    result = client.synthesis(A, "zh", 1, {
        "per": 4,
        "pit": 8,
        "spd": 4,
        "vol": 5,
    })
    # 如果不存在result,就打开audio.mp3的文件
    if not isinstance(result, dict):
        with open("audio.mp3", "wb") as f:
            f.write(result)
    os.system("audio.mp3")

else:
    # 调用图灵机器人
    import go_tuling
    # 传2个参数,一个是用户输入的内容,并赋值给A
    A = go_tuling.tl(Q, "asd")
    # 结果赋值给result,并读取这个文件
    result = client.synthesis(A, "zh", 1, {
        "per": 4,
        "pit": 8,
        "spd": 4,
        "vol": 5,
    })
    if not isinstance(result, dict):
        with open("audio.mp3", "wb") as f:
            f.write(result)

        os.system("audio.mp3")
'''