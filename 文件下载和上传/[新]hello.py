import pygame
import random
import math


# 随机生成3原色
def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))
    pygame.display.set_caption('大球吃小球')
    pygame.display.flip()
    # all_balls 中保存创建的每一个球
    #每个球要保存：半径，黑心坐标，颜色，X轴方向的速度，y轴方向的速度
    all_balls = [
        {
            'r': random.randint(10, 15),
            'pos': (100, 100),
            'color': (random_color()),
            'x_speed': random.randint(0, 1),
            'y_speed': random.randint(0, 1),
            'live': True
        }
    ]

    while True:
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
             
       