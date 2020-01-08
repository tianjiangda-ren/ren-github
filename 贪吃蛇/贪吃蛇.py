# !/usr/bin/env python
# -*- codeing: utf-8 -*-

import pygame,random
from sys import exit #系统退出功能
from time import sleep#时间休眠/等待功能
from pygame.locals import *

# 定义gameOver函数
def gameOver(playSurface):
    gameOverFont = pygame.font.SysFont('arial',72)
    gameOverSurf = gameOverFont.render('Game Over', True,(12,12,12))
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (400, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    pygame.time.delay(1000)
    pygame.quit()
    exit()

# 欢迎页面
def WelcomeDisplay():
    my_font=pygame.font.Font(r"MMM.ttf",16) 
    # my_font = pygame.font.SysFont('arial',20)
    font_height = my_font.get_linesize()
    txt=[u'操作说明:',u'开始/跳跃:空格',u'移动方向:←↓→↑ 攻击:F']
    text_surface=[]
    for i in range(len(txt)):
        text_surface.append(my_font.render(txt[i],True,(12,12,12)))
    playSurface.blit(back,(0,0))
    if (WELCOMECOUNT<200):
        playSurface.blit(WelcomeLogo,((400-(WELCOMECOUNT*1.6)),10))
        playSurface.blit(WelcomeChar,((600-(WELCOMECOUNT*1.6)),80))
        y=100
        for i in range(len(txt)):
            playSurface.blit(text_surface[i],(400-(WELCOMECOUNT*1.6),y))
            y+=font_height
        WELCOMECOUNT=WELCOMECOUNT+1
    else:
        playSurface.blit(WelcomeLogo,((400-(WELCOMECOUNT*1.6)),10))
        playSurface.blit(WelcomeChar,((600-(WELCOMECOUNT*1.6)),80))
        y=100
        for i in range(len(txt)):
            playSurface.blit(text_surface[i],(400-(WELCOMECOUNT*1.6),y))
            y+=font_height
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                if (WELCOMECOUNT>150):
                    pMODE=1
        elif event.type==QUIT:
            exit()
    return 0
# 定义main函数
def main():
    # 初始化pygame
    pygame.init()
    #定义一个变量用来控制游戏速度
    fpsClock = pygame.time.Clock()
    # 创建pygame显示层
    aa=[800,600]
    playSurface = pygame.display.set_mode(aa)#窗口的宽，高
    pygame.display.set_caption('贪吃蛇')# 设置窗口标题
    # image = pygame.image.load("图片的路径")#加载图片
    # pygame.display.set_icon(image)#设置窗口图标
    # window.blit(image, (0, 0))#放置图标
    back=pygame.image.load('img/back.png')# 加载开局/结束背景
    Map1=pygame.image.load(r'img/Map1.png')# 加载地图
    sheshen=pygame.image.load('img/inBar.png').convert_alpha()
    shetou=pygame.image.load('img/outBar2.png').convert_alpha()
    # 初始化变量
    snakePosition = [100,100]
    playSurface.blit(shetou,snakePosition)
    #列表元素个数=蛇长度
    snakeSegments = [[100,100],[80,100],[60,100]]
    for i in snakeSegments:
        playSurface.blit(sheshen,i)
    foodPosition = [300,300]
    foodFlag = 1 #食物标志位，1表示没被吃
    direction = 'right'
    changeDirection = direction
    while True:
        # 监听pygame按键事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                # 判断键盘事件
                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changeDirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        # 与非逻辑判断是否输入了反方向
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection
        # 根据方向移动蛇头的坐标
        if direction == 'right':
            snakePosition[0] += 100
        if direction == 'left':
            snakePosition[0] -= 100
        if direction == 'up':
            snakePosition[1] -= 100
        if direction == 'down':
            snakePosition[1] += 100
        # 增加蛇的长度
        snakeSegments.insert(0,list(snakePosition))
        # 判断是否吃掉了食物
        if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
            foodFlag = 0
        else:
            snakeSegments.pop()
        # 如果吃掉食物，则重新生成食物,生成的食物不能与蛇重合
        if foodFlag == 0:
        	while foodPosition in snakeSegments :
		        x = random.randrange(1,40)
		        y = random.randrange(1,30)
		        foodPosition = [int(x*20),int(y*20)]
        foodFlag = 1
        # 绘制pygame显示层
        # playSurface.fill(blackColour)
        # 遍历，把蛇和食物画出来
        # for position in snakeSegments:
            # pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))
            # pygame.draw.rect(playSurface,headColour,Rect(snakePosition[0],snakePosition[1],20,20))
            # pygame.draw.rect(playSurface,redColour,Rect(foodPosition[0], foodPosition[1],20,20))
        # 刷新pygame显示层
        pygame.display.flip()
        # 判断是否死亡，分为撞墙和撞自己
        if snakePosition[0] > 780 or snakePosition[0] < 0:
            gameOver(playSurface)
        if snakePosition[1] > 580 or snakePosition[1] < 0:
            gameOver(playSurface)
        for snakeBody in snakeSegments[1:]:
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                gameOver(playSurface)
        # 控制游戏速度
        fpsClock.tick(2)

if __name__ == "__main__":
    main()
