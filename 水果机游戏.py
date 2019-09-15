import tkinter
import threading
import time


root=tkinter.Tk()
root.title("水果机游戏")
root.minsize(300,300)

#摆放按钮
btn1=tkinter.Button(root,text="樱桃",bg="red")
btn1.place(x=20,y=20,width=50,height=50)

btn2=tkinter.Button(root,text="香蕉",bg="white")
btn2.place(x=90,y=20,width=50,height=50)

btn3=tkinter.Button(root,text="平果",bg="blue")
btn3.place(x=160,y=20,width=50,height=50)

btn4=tkinter.Button(root,text="篮球",bg="red")
btn4.place(x=230,y=20,width=50,height=50)

btn5=tkinter.Button(root,text="香梨",bg="white")
btn5.place(x=230,y=90,width=50,height=50)

btn6=tkinter.Button(root,text="柚子",bg="green")
btn6.place(x=230,y=160,width=50,height=50)

btn7=tkinter.Button(root,text="蜜桃",bg="red")
btn7.place(x=230,y=230,width=50,height=50)

btn8=tkinter.Button(root,text="橘子",bg="red")
btn8.place(x=160,y=230,width=50,height=50)

btn9=tkinter.Button(root,text="菠萝",bg="red")
btn9.place(x=90,y=230,width=50,height=50)

btn10=tkinter.Button(root,text="荔枝",bg="red")
btn10.place(x=20,y=230,width=50,height=50)

btn11=tkinter.Button(root,text="山竹",bg="red")
btn11.place(x=20,y=160,width=50,height=50)

btn12=tkinter.Button(root,text="甘蔗",bg="red")
btn12.place(x=20,y=90,width=50,height=50)

#将所有的按钮添加到列表
fruitlists=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12]
#是否开户循环
isloop=False
stopsign=False    #是否接收停止信号
stopid=None

def round():
    global isloop
    global stopid

    #是否开始
    if isloop==True:
        return
    i=1
    if isinstance(stopid,int):
        i=stopid
    while True:
        #延时操作
        time.sleep(0.1)
        #将所有的组件背景变为白色
        for x in fruitlists:
            x["bg"]="white"
        #将当前的数值对应的组件变色
        fruitlists[i]["bg"]="red"
        #变量+1
        i +=1
        print("当前i为",i)
        #如果i大于最大索引
        if i>=len(fruitlists):
            i=0
        if stopsign==True:
            isloop=False
            stopid=i
            break

def stop1():
    global stopsign
    if stopsign==True:
        return
    stopsign=True
#建立一个线程
def netstart():
    global isloop
    global stopsign
    stopsign=False

    #建立线程
    t=threading.Thread(target=round)

    #开启线程
    t.start()
    isloop=True

#开始按钮
btn_start=tkinter.Button(root,text="启动",command=netstart)
btn_start.place(x=100,y=125,width=50,height=50)

stop_start=tkinter.Button(root,text="停止",command=stop1)
stop_start.place(x=160,y=125,width=50,height=50)

root.mainloop()  #mainloop()就是一直不停地循环啊


# 打包成一个可执行文件的方法, pyinstaller -F dpython.py