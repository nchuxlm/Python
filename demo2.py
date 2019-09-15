import time
import threading

def say_hell():
    print("hello word")
    time.sleep(1)

if __name__ == '__main__':
    for a in range(1,10,-2):
        print(a,end="  ")   #效果为1  2  3  4  5  6  7  8  9
    for i in range(5):
       t=threading.Thread(target=say_hell)  #创建线程,say_hell() 就是一秒一个输出.不加()就一次输出五个hello word,target=say_hell目标指向say_hell,加括号是执行了函数
       t.start()   #开启线程