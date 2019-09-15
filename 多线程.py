import threading
import time
def demo1():
    for i in range(5):
        print(".....")
        time.sleep(i)
def demo2():
    for i in range(5):
        print(".....")
        time.sleep(i)

def main():
    demo1()
    demo2()

if __name__ == '__main__':
    main()



