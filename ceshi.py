# !/usr/bin/env python
# -*- codeing: utf-8 -*-

pygame.init()
playSurface = pygame.display.set_mode((800,600))#窗口的宽，高
pygame.display.set_caption('贪吃蛇')# 设置窗口标题

def WelcomeDisplay():
    WELCOMECOUNT=0
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

pygame.display.update()