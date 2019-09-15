# -*- coding:utf-8 -*-
#dateTime:2019/2/27 0027 下午 15:25
#file:调用图灵的代码.py
#程序设计: 夏利民
import requests

url = "http://openapi.tuling123.com/openapi/api/v2"

data_dict = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": "北京"
        },
    },
    "userInfo": {
        "apiKey": "efcb2b5289324ce9a994b82f69bc7691",
        "userId": "asd",
    }
}


def tl(text, uid):
    # 给字典赋值text,这个text是传过来的用户输入的内容
    data_dict["perception"]["inputText"]["text"] = text
    # 并给字典赋值是哪个用户的要求
    data_dict["userInfo"]["userInfo"] = uid
    # 把这个消息数据反送给图灵
    res = requests.post(url, json=data_dict)
    # 会得到一个响应值,去json的方法
    res_json = res.json()
    print("res:", res, type(res))
    # res: <Response [200]> <class 'requests.models.Response'>
    print("res_json:", res_json,type(res_json))
    # res_json: {'intent': {'actionName': '', 'code': 10006, 'intentName': ''}, 'results': [{'groupType': 1, 'resultType': 'text', 'values': {'text': '猪猪与爸爸 小猪与爸爸在谈话小猪说：爸爸为什么上个月有人来要钱你说没有，这个月那个人来要钱你说又没有？小猪爸爸：哎呀，爸爸要讲信用嘛！'}}]} <class 'dict'>
    # 返回图灵相应的数据
    return res_json.get("results")[0]["values"]["text"]