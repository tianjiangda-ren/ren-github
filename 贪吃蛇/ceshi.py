# !/usr/bin/env python
# -*- codeing: utf-8 -*-
import pygame
from random import randrange#只导入随机数字功能
from sys import exit #只导入系统模块里退出功能
from pygame.locals import *

# 初始化pygame，为使用硬件做准备
pygame.init()
# 创建一个窗口
screen = pygame.display.set_mode((640,480),0,32)#width 窗口的宽  hight 窗口的高
# 设置窗口标题
pygame.display.set_caption("窗口标题")
# 加载资源图片，返回图片对象
back = pygame.image.load("img/back.png")# 场景
mouse_cursor = pygame.image.load("img/WelcomeLogo.png")
# 设置窗口图标
pygame.display.set_icon(image)
# 指定坐标，将图片绘制到窗口
screen.blit(image,(0,0))
# 游戏主循环
fullscreen = False#默认不全屏
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出时间后退出程序
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_F1:
                fullscreen = not fullscreen#改变全屏状态
                if fullscreen:
                    screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((640, 480), 0, 32)
    screen.blit(back, (0, 0))# 将背景图画上去

    pygame.display.update()# 刷新画面
    