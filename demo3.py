import time
import threading

def sing():
    for i in range(3):    # i 的值从0 1 2
        print("正在唱歌..{}".format(i))
        time.sleep(1)
def danc():
    for i in range(3):
        print("正在跳舞..{}".format(i))
        time.sleep(1)
if __name__ == '__main__':
    print("程序开始运行:{}".format(time.ctime()))
    t1=threading.Thread(target=sing)
    t2=threading.Thread(target=danc)
    t1.start()
    t2.start()

    while True:
        length=len(threading.enumerate())
        print("当前运行的线程数:{}".format(length))
        if length<=1:
            break
        time.sleep(0.5)
    #print("结束")