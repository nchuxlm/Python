#author:Administrator
#dateTime:2019/2/21 0021 下午 20:39
#file:数据挖掘.py
#程序设计: 夏利民http://pg.qq.com/zlkdatasys/data_zlk_zlzx.json
# 打开网站https://pg.qq.com/web201801/ziliao_detail.shtml?id=101001
#按F12打开源文件,左边选择网络,右边选择XHR,按f5刷新,得到了json网址,在"响应"下面刚有JSONew数据出现
import requests
import json
import jsonpath   #对JSON文件 信息提取库
import pygal   #SVG 图表库
#1.请求拿到全部json数据
url="http://pg.qq.com/zlkdatasys/data_zlk_zlzx.json"
#添加请求头  ----通行证 User-Agent用户代理
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/65.0X-Requested-WithXMLHttpRequest'}
#参数 如带个女伴参加活动
data={}
#respone=requests.get(url,headers=header,data=data)   #用 get 还是post 网页上会写上
respone=requests.get(url)   #get 或post 网页上会写上
#2.先把JSON 转化为PYTHON数据
html=respone.text  #respone.text网页源代码用文本形式
#respone.encoding='utf-8'    #如果出现乱码时更改一下
py_data=json.loads(html)     #把JSOn形式的字符串转换成python形式的unicode字符串

#print(py_data)
#3.从整体数据中抽取枪支名称及相关数据 进行相应处理
gun_name1=jsonpath.jsonpath(py_data,"$..mc_94")  # 根节点下$..两个点不代表任何位置
two=jsonpath.jsonpath(py_data,"$..yd_c6")

z=zip(gun_name1[1:8],two[:7])

#取gun_name1[1:8]从第二项到第7项的值['AKM', 'M16A4', 'M416', 'SCAR-L', 'Groza', 'AUG', 'QBZ'],也就是前面7个值
for x in z:
    print (x)

gun_name=jsonpath.jsonpath(py_data,"$..mc_94")[1:8]

qun_xinn=jsonpath.jsonpath(py_data,"$..ldtw_f2")[0:7]


data=[]

for i in qun_xinn:
    data.append([int(i[0]['wl_45']),int(i[0]["sc_54"]),int(i[0]['ss_d0']),int(i[0]['wdx_a7']),int(i[0]['zds_62'])])

#4.雷达图设计,调用Rader 这个类
radar_chart=pygal.Radar(fill=True)   #填充fill=True
#设置雷达图标题
radar_chart.title="步枪性能"
#添加雷达图各项顶点的含义
radar_chart.x_labels=["威力","射程","射速","稳定性","子弹数"]
for n,d in zip(gun_name,data):    #zip 拉链函数 ,前后两个数形成一个组
    radar_chart.add(n,d)       #添加数据  radar_chart.add("AK45",[100,50,41,58,78]),这种形式的数据

#5.保存到当前路径下面
radar_chart.render_to_file("gun.svg")   #保存到一个文件中,这里面也可写路径(r"c:\users\administrator\desktop\gun.svg")
