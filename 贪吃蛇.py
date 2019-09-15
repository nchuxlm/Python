#!/usr/bin/env python
# -*- coding:utf-8 -*-
#dateTime:2019-03-07 下午 20:27
#file:贪吃蛇.py
#design: nchu xlm
import pygame
import sys
import random
from pygame.locals import *

#定义颜色

redColor=pygame.Color(255,0,0)   #目标方块

whiteColor=pygame.Color(255,255,255)  #贪吃蛇
blackColor=pygame.Color(0,0,0)

def gameOver():
    pygame.quit()
    sys.exit()

# 工作方式
def main():
    pygame.init()
    #定义一个变量来控制游戏的速度
    fpsClock=pygame.time.Clock()
    playSurface=pygame.display.set_mode((640,480))
    pygame.display.set_caption("贪吃蛇")
    #初始化变量,起始位置及
    snakePostion=[100,100]
    snakebody=[[100,100],[80,100],[60,100]]
    targetPostion=[300,300]
    targetflag=1   # 标记判断目标方块是否被吃掉
    direction='right'
    changeDirection=direction    #方向变量


    #pygame 放到一个实时身在当中
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                # 判断键盘事件
                if event.key==K_RIGHT or event.key == ord('d'):
                    changeDirection='right'
                if event.key==K_LEFT or event.key == ord('a'):
                    changeDirection='left'
                if event.key==K_UP or event.key == ord('w'):
                    changeDirection='up'
                if event.key==K_DOWN or event.key == ord('s'):
                    changeDirection='down'
                #对应键盘上的ESC
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        # 判断是否输入了反方向
        if changeDirection=="left" and not direction=='right':    #不能倒着走
            direction=changeDirection
        if changeDirection=="right" and not direction=='left':    #不能倒着走
            direction=changeDirection
        if changeDirection=="up" and not direction=='down':    #不能倒着走
            direction=changeDirection
        if changeDirection=="down" and not direction=='up':    #不能倒着走
            direction=changeDirection




        # 蛇头的位置,在左右移动时必须向下或向上掉头
        # 根据方向移动蛇头的坐标
        if direction=='right':
            snakePostion[0] +=20
        if direction=='left':
            snakePostion[0] -=20
        if direction=='up':
            snakePostion[1] -=20
        if direction=='down':
            snakePostion[1] +=20

        #增加蛇的长度
        snakebody.insert(0,list(snakePostion))

        # 如果蛇的位置和方块 重合
        if snakePostion[0]==targetPostion[0] and snakePostion[1]==targetPostion[1]:
            targetflag=0
        else:
            snakebody.pop()

        if targetflag==0:    #640,480
             x=random.randrange(1,32)
             y=random.randrange(1,24)
             targetPostion=[int(x*20),int(y*20)]
             targetflag=1

        # 绘制pygame显示层
        playSurface.fill(blackColor)
        for postion in snakebody:
            pygame.draw.rect(playSurface,whiteColor,Rect(postion[0],postion[1],20,20)) #蛇
            pygame.draw.rect(playSurface,redColor, Rect(targetPostion[0],targetPostion[1], 20, 20)) #目标方块

        # 刷新pygame显示层游戏结束
        pygame.display.flip()
        # 判断是否死亡
        if snakePostion[0]>620 or snakePostion[0]<0:
            gameOver()
        elif snakePostion[1]>460 or snakePostion[1]<0:
            gameOver()


        # 控制游戏速度
        fpsClock.tick(1)

if __name__ == '__main__':
    main()
















