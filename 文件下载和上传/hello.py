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
             
                # 点一下鼠标创建一个球
                ball = {
                    'r': random.randint(10, 15),
                    'pos':event.pos,
                    'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    'x_speed': random.randint(0, 1),
                    'y_speed': random.randint(0, 1),
                    'live': True
                }
                # 保存球
                all_balls.append(ball)
         # 刷新届面
        screen.fill((255, 255, 255))
        for ball in all_balls:
            # 取出原来球的X,y以及速度的值
            x,y = ball['pos']
            x_speed = ball['x_speed']
            y_speed = ball['y_speed']

            if x + ball['r'] >= 800:
                x_speed += -1
            if x - ball['r'] <= 0:
                x_speed *= -1
            if y + ball['r'] >= 600:
                y_speed += -1
            if y - ball['r'] <= 0:
                y_speed += -1
            x += x_speed
            y += y_speed
            pygame.draw.circle(screen, ball['color'],(x, y), ball['r'])
            # 更新Qiu的坐标
            ball['pos'] = x, y

            ball['x_speed'] = x_speed
            ball['y_speed'] = y_speed

            for ball2 in all_balls:
                if all_balls.index(ball) == all_balls.index(ball2):
                    pass
                else:
                    other_x, other_y = ball2['pos']
                    dx = x - other_x
                    dy = y - other_y

                    distance = math.sqrt(dx ** 2 + dy ** 2)
                    if distance < ball['r'] + ball2['r']:
                        if ball['r'] > ball2['r']:
                            ball['r'] = int(ball['r'] + ball2['r'] / 5)
                            all_balls.remove(ball2)

        pygame.display.update()
