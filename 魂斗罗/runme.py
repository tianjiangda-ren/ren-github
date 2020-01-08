# !/usr/bin/env python
# -*- codeing: utf-8 -*-
# --import CheckBarArray & pygame  ! PAGE >=0--

import pygame #python游戏模块
from pygame.locals import * #获取键盘按键模块

from sys import exit #系统退出功能
from time import sleep#时间休眠/等待功能
from math import sin,cos,pi # 数学三角函数/π值

PAGE=0
STEPINTERVAL=15
# --init pygame（初始化游戏框架）--
# pygame.mixer.init()#初始化声音模块
# pygame.mixer.set_num_channels(8)#声音通道，默认8
pygame.init()# 初始化pygame模块
pygame.mixer.pre_init(44100, 16, 2, 4096)#初始化声音
# pygame.mixer.pre_init(frequency(采集频率44.1KHz),size(量化精度16),stereo(立体声效果，1：mono，2：stereo), buffer(缓冲大小，2的倍数4096))
screen=pygame.display.set_mode((400,224),FULLSCREEN,32)#（400,224（宽，高），FULLSCREEN-全屏-，,32）
pygame.display.set_caption("魂斗罗")#窗口标题
# image = pygame.image.load("图片的路径")#加载图片
# pygame.display.set_icon(image)#设置窗口图标
# window.blit(image, (0, 0))#放置图标

# --init CONTRA image(引用游戏素材)--
# -游戏音效
pygame.mixer.music.load('music/BackMusic.MP3')# 加载背景音乐
# pygame.mixer.music.play(-1)# 循环播放背景音乐
# pygame.mixer.music.stop()# 停止背景音乐
GunSound2=pygame.mixer.Sound('music/GunSound2.ogg')# 加载跳跃音效
BombSound2=pygame.mixer.Sound('music/BombSound2.ogg')# 加载爆炸音效
# BombSound2.set_volume(0.20)#播放音量
# boom_sound.play()# 播放音效
# boom_sound.stop()#停止音效
# --init CONTRA image（加载图集）--
# -游戏图集
back=pygame.image.load('img/back.png')# 加载开局/结束背景
WelcomeChar=pygame.image.load('img/WelcomeChar.png').convert_alpha()#加载 首页人物图标
WelcomeLogo=pygame.image.load('img/WelcomeLogo.png').convert_alpha()#加载 首页logo
Map1=pygame.image.load(r'img/Map1.png')# 加载地图
inBar=pygame.image.load('img/inBar.png')#加载桥梁
outBar1=pygame.image.load('img/outBar1.png')#加载桥梁（左）
outBar2=pygame.image.load('img/outBar2.png')#加载桥梁（右）
BombImage=[]#爆炸图集
for i in range(3):
    BombImage.append(pygame.image.load('img/Bomb'+str(i+1)+'.png'))#加载爆炸


# -人物图集
MarkImage=pygame.image.load('img/Mark.png').convert_alpha()#生命值（徽章）
HeroBullet=pygame.image.load('img/HeroBullet.png').convert_alpha()#英雄的子弹
DieOnGround=pygame.image.load('img/DieOnGround.png')# 加载阵亡

JumpLeft=[]#左跳动作图集
JumpRight=[]#右跳动作图集
for i in range(4):
    JumpLeft.append(pygame.image.load('img/JumpLeft'+str(i+1)+'.png').convert_alpha())# 加载左跳convert_alpha（透明_像素）
    JumpRight.append(pygame.image.load('img/JumpRight'+str(i+1)+'.png').convert_alpha())# 加载右跳

LieShootLeft=pygame.image.load('img/LieShootLeft.png').convert_alpha()# 加载左下
LieShootRight=pygame.image.load('img/LieShootRight.png').convert_alpha()# 加载右下

RunLeft=[]#左跑动作图集
RunRight=[]#右跑动作图集
for i in range(5):
    RunLeft.append(pygame.image.load('img/RunLeft'+str(i+1)+'.png').convert_alpha())# 加载左跑
    RunRight.append(pygame.image.load('img/RunRight'+str(i+1)+'.png').convert_alpha())# 加载右跑

RunShootLeft=[]#左跑攻击图集
RunShootRight=[]#右跑攻击图集
ShootLeftDown=[]# 左跑下击图集
ShootRightDown=[]# 右跑下击图集
for i in range(3):
    RunShootLeft.append(pygame.image.load('img/RunShootLeft'+str(i+1)+'.png').convert_alpha())# 加载左跑攻击
    RunShootRight.append(pygame.image.load('img/RunShootRight'+str(i+1)+'.png').convert_alpha())# 加载右跑攻击
    ShootLeftDown.append(pygame.image.load('img/ShootLeftDown'+str(i+1)+'.png').convert_alpha())# 加载左跑下击
    ShootRightDown.append(pygame.image.load('img/ShootRightDown'+str(i+1)+'.png').convert_alpha())# 加载右跑下击

ShootLeftUp=pygame.image.load('img/ShootLeftUp.png').convert_alpha()# 加载左上攻击
ShootRightUp=pygame.image.load('img/SHootRightUp.png').convert_alpha()# 加载右上攻击
ShootUpLeft=pygame.image.load('img/ShootUpLeft.png').convert_alpha()# 加载上击（左）
ShootUpRight=pygame.image.load('img/ShootUpRight.png').convert_alpha()# 加载上击（右）

# -敌人图集
EnermyType1ImageLeft=[]#敌人左跑图集
EnermyType1ImageRight=[]#敌人右跑图集
for i in range(4):
    EnermyType1ImageLeft.append(pygame.image.load('img/EnermyType1ImageLeft'+str(i+1)+'.png').convert_alpha())#加载敌人左跑
    EnermyType1ImageRight.append(pygame.image.load('img/EnermyType1ImageRight'+str(i+1)+'.png').convert_alpha())#加载敌人右跑

EnermyType20=pygame.image.load('img/EnermyType20.png').convert_alpha()#敌人左攻击
EnermyType21=pygame.image.load('img/EnermyType21.png').convert_alpha()#敌人右攻击


#-boss图集
Boss1=pygame.image.load('img/Boss1.png').convert_alpha()#boss上左 基地
Boss2=pygame.image.load('img/Boss2.png').convert_alpha()#boss上右 基地
Boss3=pygame.image.load('img/Boss3.png').convert_alpha()#boss下 基地
Boss4=pygame.image.load('img/Boss4.png').convert_alpha()#boss后 基地
Boss1s=pygame.image.load('img/Boss1s.png').convert_alpha()#boss上左 基地被攻击
Boss2s=pygame.image.load('img/Boss2s.png').convert_alpha()#boss上右 基地被攻击
Boss3s=pygame.image.load('img/Boss3s.png').convert_alpha()#boss下 基地被攻击
BossBulletSImage=pygame.image.load('img/BossBulletS.png').convert_alpha()#boss 子弹
BossBulletImageS=pygame.image.load('img/BossBulletImageS.png').convert_alpha()#boss S子弹

# --init CheckBarArray（初始化桥梁位置）--
class Bar:
    def __init__(self,x,y,z):
        self.x1=x
        self.x2=y
        self.y=z

CheckBarArray=[]#创建桥梁位置（空），后面添加
#所有桥梁位置，地图很长
CheckBarArray.append(Bar(32,738,116))
CheckBarArray.append(Bar(160,253,224-141))
CheckBarArray.append(Bar(259,284,224-174))
CheckBarArray.append(Bar(290,350,224-205))
CheckBarArray.append(Bar(353,384,224-174))
CheckBarArray.append(Bar(420,480,224-140))
CheckBarArray.append(Bar(577,640,224-205))
CheckBarArray.append(Bar(611,706,224-159))
CheckBarArray.append(Bar(864,1024,224-108))
CheckBarArray.append(Bar(1151,1411,224-108))
CheckBarArray.append(Bar(1346,1854,224-78))
CheckBarArray.append(Bar(1376,1472,224-209))
CheckBarArray.append(Bar(1476,1536,224-158))
CheckBarArray.append(Bar(1569,1794,224-141))
CheckBarArray.append(Bar(1697,1888,224-208))
CheckBarArray.append(Bar(1828,2049,224-110))
CheckBarArray.append(Bar(1888,1951,224-173))
CheckBarArray.append(Bar(1987,2049,224-175))
CheckBarArray.append(Bar(2017,2175,224-80))
CheckBarArray.append(Bar(2081,2112,224-158))
CheckBarArray.append(Bar(2146,2241,224-142))
CheckBarArray.append(Bar(2211,2272,224-108))
CheckBarArray.append(Bar(2304,2334,224-207))
CheckBarArray.append(Bar(2304,2334,224-142))
CheckBarArray.append(Bar(2336,2432,224-173))
CheckBarArray.append(Bar(2423,2496,224-110))
CheckBarArray.append(Bar(2465,2524,224-78))
CheckBarArray.append(Bar(2465,2497,224-205))
CheckBarArray.append(Bar(2497,2524,224-159))
CheckBarArray.append(Bar(2560,2620,224-108))
CheckBarArray.append(Bar(2593,2753,224-140))
CheckBarArray.append(Bar(2688,2782,224-204))
CheckBarArray.append(Bar(2816,2878,224-173))
CheckBarArray.append(Bar(2913,2974,224-143))
CheckBarArray.append(Bar(2978,3134,224-110))
CheckBarArray.append(Bar(2977,3248,224-207))
CheckBarArray.append(Bar(3009,3132,224-157))
CheckBarArray.append(Bar(3135,3165,224-142))
CheckBarArray.append(Bar(3166,3269,224-173))
# --visual bar#桥梁视觉--
VisualBar1=[]
VisualBar1.append(Bar(736,767,224-108))
VisualBar1.append(Bar(767,799,224-108))
VisualBar1.append(Bar(799,831,224-108))
VisualBar1.append(Bar(831,867,224-108))
VisualBar2=[]#X,Y比bar1多289距离
VisualBar2.append(Bar(736+289,767+289,224-108))
VisualBar2.append(Bar(767+289,799+289,224-108))
VisualBar2.append(Bar(799+289,831+289,224-108))
VisualBar2.append(Bar(831+289,867+289,224-108))

''' --init bullet about direction:（子弹方向d）--
0:左  1:右  2:上  3:下  4:左上  5:左下  6:右上  7:右下 '''
BULLETSPEED=3 #子弹初始位置
class Bullet:#子弹属性x，y是坐标位置 d是方向（参考上面位置）
    def __init__(self,x,y,d):
        self.x=x
        self.y=y
        self.d=d
    def CheckIfOut(self,page):#检查子弹位置
        if (self.x<page)or(self.x>page+400)or(self.y>224)or(self.y<0):
            return True
        else:
            return False
BULLET=[]#人物子弹初始位置
ENERMYBULLET=[]#敌人子弹初始位置
def UpdateBullet(array):#子弹位置变动
    for bullet in array:
        if bullet.d==0:#子弹方向左
            bullet.x=bullet.x-BULLETSPEED#子弹当前位置-初始位置
        elif bullet.d==1:#子弹方向右
            bullet.x=bullet.x+BULLETSPEED#子弹当前位置+初始位置
        elif bullet.d==2:#子弹方向上
            bullet.y=bullet.y+BULLETSPEED
        elif bullet.d==3:#子弹方向下
            bullet.y=bullet.y-BULLETSPEED
        elif bullet.d==4:#子弹方向左上
            bullet.y=bullet.y+BULLETSPEED
            bullet.x=bullet.x-BULLETSPEED
        elif bullet.d==5:#子弹方向左下
            bullet.y=bullet.y-BULLETSPEED
            bullet.x=bullet.x-BULLETSPEED
        elif bullet.d==6:#子弹方向右上
            bullet.y=bullet.y+BULLETSPEED
            bullet.x=bullet.x+BULLETSPEED
        elif bullet.d==7:#子弹方向右下
            bullet.y=bullet.y-BULLETSPEED
            bullet.x=bullet.x+BULLETSPEED
'''
init PEOPLE
state:
      RunLeft:1 2 3 4 5 4 3 2（跑动图片播放顺序）
      RunShoot:1 2 3 2（攻击图片播放顺序）
'''
class People:
    def __init__(self,a,b):#初始化人物状态
        self.x=a
        self.y=b
        self.height=0
        self.state='stand'#状态：站
        self.inair=0
        self.statestep=0
        self.onfire=0
        self.d=1
        self.ondrop=0
        self.ondeath='alive'#状态：活/死
    def CheckOnBoard(self,array):#检查人物位置
     global HERO
     if HERO.state=='inair':
      if HERO.inair>0.76:#人物下水（位置低于水平）
        for i in range(len(array)):
            if self.x>array[i].x1-10:
                if self.x<array[i].x2:
                    if ((self.y+self.height)-array[i].y)<5 and((self.y+self.height)-array[i].y)>-5:
                        self.y=array[i].y
                        self.inair=0
                        self.height=0
                        return True
     elif HERO.ondrop==1:
       if HERO.inair>0.2:
         for i in range(len(array)):
            if self.x>array[i].x1-10:
                if self.x<array[i].x2:
                    if ((self.y+self.height)-array[i].y)<4 and((self.y+self.height)-array[i].y)>-4:
                        self.y=array[i].y
                        self.inair=0
                        self.height=0
                        self.ondrop=0
                        return True
         return False
     return False
HERO=People(44,224)#人物初始位置
# --init enermy（敌人位置）--
class Enermytype1():#敌人位置变化逻辑
    def __init__(self,a,b,c):#初始化敌人状态
        self.x=a
        self.y=b
        self.d=c
        self.height=0
        self.state='run'
        self.inair=0
        self.runstate=0
        self.ondeath='alive'
    def CheckOnBoard(self,array):#检查敌人位置
      if self.inair>0.5 and self.state=='inair':
        for i in range(len(array)):
            if self.x>array[i].x1:
                if self.x<array[i].x2:
                    if (((self.y+self.height)-array[i].y)<10)and(((self.y+self.height)-array[i].y)>-10):
                        self.y=array[i].y
                        self.height=0
                        return True
      if self.state=='run':
          for i in range(len(array)):
            if self.x>array[i].x1:
                if self.x<array[i].x2:
                    if (((self.y+self.height)-array[i].y)<10)and(((self.y+self.height)-array[i].y)>-10):
                        self.y=array[i].y
                        self.height=0
                        self.inair=0
                        return True
      return False

ENERMYTYPE1=[]#敌人状态
class Enermytype2():#敌人子弹位置逻辑
    def __init__(self,x,y,d):#初始化
        self.x=x
        self.y=y
        self.d=d
        self.onfire=1
        self.step=200
        self.ondeath='alive'
    def update(self):#位置变动
        if self.onfire==1:
            if self.step==0:
                ENERMYBULLET.append(Bullet(self.x-10,self.y+38,self.d))
                self.step=200
            self.step=self.step-1
        return 0
ENERMYTYPE2=[]#右边敌人图集
ENERMYTYPE2.append(Enermytype2(328,224-207,4))
ENERMYTYPE2.append(Enermytype2(680,224-112,0))
ENERMYTYPE2.append(Enermytype2(949,224-112,0))
ENERMYTYPE2.append(Enermytype2(1424,224-202,4))
ENERMYTYPE2.append(Enermytype2(1745,224-202,4))
ENERMYTYPE2.append(Enermytype2(1700,224-139,0))
ENERMYTYPE2.append(Enermytype2(1785,224-77,0))
def UpdateEnermyType1():#敌人状态变更逻辑
    for i in ENERMYTYPE1:
        if i.ondeath=='alive':
              i.x=i.x+i.d
              if (i.CheckOnBoard(CheckBarArray)):
                  if (i.state=='inair'):
                      i.state='run'
              else:
                  i.state='inair'
                  UpdateHeight(i)
              if (i.state=='run'):
                  if (i.runstate>5*STEPINTERVAL):
                      i.runstate=0
                  else:
                      i.runstate=i.runstate+1
        elif i.ondeath=='dead':
              i.x=i.x-i.d
              i.state='inair'
              UpdateHeight(i)
# --init Bomb--
class Bomb:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.state=3
        self.step=40
    def update(self):
        if self.step==0:
            self.step=40
            self.state=self.state-1
        if self.state>0:
            self.step=self.step-1
BombArray=[]           
# --init Boss--
class BossBullet:
    def __init__(self,x,y,a,b):
        self.x=x
        self.y=y
        self.a=a
        self.b=b
    def update(self):
        self.x=self.x+self.a
        self.y=self.y+self.b
class BossBulletS:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.state='inair'
        self.inair=0
        self.height=0
    def update(self):
        global BOSSBULLETS
        if self.state=='inair':
            if (self.height+self.y-23)>-4 and (self.height+self.y-23)<4:
                self.state='run'
                self.y=23
                self.height=0
            else:
                Drop(self)
        self.x=self.x-0.5
        if self.x<2979:
            BOSSBULLETS.remove(self)
BOSSBULLET=[]
BOSSBULLETS=[]
class GUN:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.state='on'
def UpdateBossBullet():
    global BOSSBULLET
    for bullet in BOSSBULLET:
        bullet.update()
    return 0
def UpdateBossBulletS():
    global BOSSBULLETS
    for bullet in BOSSBULLETS:
        bullet.update()
class Boss:
    def __init__(self,a,b,c,d,e,f):
        self.gun1=GUN(a,b)
        self.gun2=GUN(c,d)
        self.gun3=GUN(e,f)
        self.health1=100
        self.health2=100
        self.health3=10
        self.onact='invalid'
BOSS=Boss(3216,125,3240,125,3224,168)
# '''--DEF Func--'''
def UpdateHeight(people):
    people.inair=people.inair+0.01
    people.height=-0.5*648*(0.5-people.inair)*(0.5-people.inair)+81
    return 0
def ScrollPage():
    global PAGE
    global HERO
    if HERO.x>PAGE+200 and (HERO.x<3070):
        PAGE=HERO.x-200
    return 0
def Drop(people):
    people.inair=people.inair+0.01
    people.height=-0.5*648*(people.inair)*(people.inair)
    return 0
def Checkbar(array):
    global HERO
    for i in range(len(array)):
            if HERO.x>array[i].x1-10:
                if HERO.x<array[i].x2:
                    if ((HERO.y+HERO.height)-array[i].y)<5and((HERO.y+HERO.height)-array[i].y)>-5:
                        return True
    return False
# --DEF DISPALY FUNC--
WELCOMECOUNT=0
pMODE=0
def WelcomeDisplay():
    global screen,WELCOMECOUNT,pMODE
    text_surface=[]
    my_font=pygame.font.Font(r"MMM.ttf",16) 
    # my_font = pygame.font.SysFont('arial',20)
    font_height = my_font.get_linesize()
    txt=[u'操作说明:',u'开始/跳跃:空格',u'移动方向:←↓→↑ 攻击:F']
    for i in range(len(txt)):
        text_surface.append(my_font.render(txt[i],True,(12,12,12)))
    screen.blit(back,(0,0))
    if (WELCOMECOUNT<200):
        screen.blit(WelcomeLogo,((400-(WELCOMECOUNT*1.6)),10))
        screen.blit(WelcomeChar,((600-(WELCOMECOUNT*1.6)),80))
        y=100
        for i in range(len(txt)):
            screen.blit(text_surface[i],(400-(WELCOMECOUNT*1.6),y))
            y+=font_height
        WELCOMECOUNT=WELCOMECOUNT+1
    else:
        screen.blit(WelcomeLogo,((400-(WELCOMECOUNT*1.6)),10))
        screen.blit(WelcomeChar,((600-(WELCOMECOUNT*1.6)),80))
        y=100
        for i in range(len(txt)):
            screen.blit(text_surface[i],(400-(WELCOMECOUNT*1.6),y))
            y+=font_height
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                if (WELCOMECOUNT>150):
                    pMODE=1
        elif event.type==QUIT:
            exit()
    return 0
OVERCOUNT,SOMECOUNT=0,0
def GameOverDisplay():
    global screen,OVERCOUNT,SOMECOUNT
    text_surface=[]
    my_font=pygame.font.Font(r"MMM.ttf",40)
    font_height = my_font.get_linesize()
    txt=["GAME OVER",u"游戏结束"]
    for i in range(len(txt)):
        text_surface.append(my_font.render(txt[i],True,(255,255,255)))
    screen.blit(back,(0,0))
    if (OVERCOUNT<200):
        y=80
        for i in range(len(txt)):
            screen.blit(text_surface[i],(440-(OVERCOUNT*1.6),y))
            y+=font_height
        OVERCOUNT=OVERCOUNT+1
    else:
        y=80
        for i in range(len(txt)):
            screen.blit(text_surface[i],(440-(OVERCOUNT*1.6),y))
            y+=font_height
        SOMECOUNT=SOMECOUNT+1
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    if SOMECOUNT==100:
        exit()
    return 0
def DrawBullet():
    global BULLET
    global HeroBullet
    global ENERMYBULLET
    global screen
    global PAGE
    for bullet in BULLET:
        screen.blit(HeroBullet,((bullet.x-PAGE),(224-bullet.y)))
    for bullet in ENERMYBULLET:
        screen.blit(HeroBullet,((bullet.x-PAGE),(224-bullet.y)))
    return 0
def DrawEnermyType1():
    global ENERMYTYPE1
    global PAGE
    global screen
    global STEPINTERVAL
    global EnermyType1ImageLeft
    global EnermyType1ImageRight
    for i in ENERMYTYPE1:
      if i.d<0:
        if i.state=='run':
            if (i.runstate>=0*STEPINTERVAL)and(i.runstate<=1*STEPINTERVAL):
                screen.blit(EnermyType1ImageLeft[0],((i.x-PAGE),(224-i.y-32)))
            elif (i.runstate>=1*STEPINTERVAL)and(i.runstate<=2*STEPINTERVAL):
                screen.blit(EnermyType1ImageLeft[1],((i.x-PAGE),(224-i.y-32)))
            elif (i.runstate>=2*STEPINTERVAL)and(i.runstate<=3*STEPINTERVAL):
                screen.blit(EnermyType1ImageLeft[2],((i.x-PAGE),(224-i.y-32)))
            elif (i.runstate>=3*STEPINTERVAL)and(i.runstate<=4*STEPINTERVAL):
                screen.blit(EnermyType1ImageLeft[3],((i.x-PAGE),(224-i.y-32)))
            elif (i.runstate>=4*STEPINTERVAL)and(i.runstate<=5*STEPINTERVAL):
                screen.blit(EnermyType1ImageLeft[1],((i.x-PAGE),(224-i.y-32)))
        if i.state=='inair':
            screen.blit(EnermyType1ImageLeft[0],((i.x-PAGE),(224-i.y-i.height-25)))
      elif i.d>0:
        if i.state=='run':
            if (i.runstate>=0*STEPINTERVAL)and(i.runstate<=1*STEPINTERVAL):
                screen.blit(EnermyType1ImageRight[0],((i.x-PAGE),(224-i.y-32)))
            elif (i.runstate>=1*STEPINTERVAL)and(i.runstate<=2*STEPINTERVAL):
                screen.blit(EnermyType1ImageRight[1],((i.x-PAGE),(224-i.y-32)))
            elif (i.runstate>=2*STEPINTERVAL)and(i.runstate<=3*STEPINTERVAL):
                screen.blit(EnermyType1ImageRight[2],((i.x-PAGE),(224-i.y-32)))
            elif (i.runstate>=3*STEPINTERVAL)and(i.runstate<=4*STEPINTERVAL):
                screen.blit(EnermyType1ImageRight[3],((i.x-PAGE),(224-i.y-32)))
            elif (i.runstate>=4*STEPINTERVAL)and(i.runstate<=5*STEPINTERVAL):
                screen.blit(EnermyType1ImageRight[1],((i.x-PAGE),(224-i.y-32)))
        if i.state=='inair':
            screen.blit(EnermyType1ImageRight[0],((i.x-PAGE),(224-i.y-i.height-15)))
    return 0
def DrawMark():
    global DeathCount,MarkImage,screen
    for i in range(DeathCount):
        screen.blit(MarkImage,((380-20*(i+1)),10))
def DrawHero():
    global PAGE
    global HERO
    global screen
    global JumpLeft
    global JumpRight
    global DieOnGround
    global LieShootLeft
    global LieShootRight
    global RunLeft
    global RunRIght
    global RunShootLeft
    global RunShootRight
    global ShootLeftDown
    global ShootLeftUp
    global ShootRightDown
    global ShootRightUp
    global ShootUpLeft
    global ShootUpRight
    global STEPINTERVAl
    if HERO.ondeath=='alive':
        if HERO.state=='stand':
            if HERO.d==0:
                screen.blit(RunShootLeft[1],((HERO.x-PAGE),(224-HERO.y-30)))
            else:
                screen.blit(RunShootRight[1],((HERO.x-PAGE),(224-HERO.y-30)))   
        elif HERO.state=='inair':
            if HERO.d==1:
                if (HERO.statestep>=0)and(HERO.statestep<=1*STEPINTERVAL):
                    screen.blit(JumpRight[0],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
                elif (HERO.statestep>=1*STEPINTERVAL)and(HERO.statestep<=2*STEPINTERVAL):
                    screen.blit(JumpRight[1],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
                elif (HERO.statestep>=2*STEPINTERVAL)and(HERO.statestep<=3*STEPINTERVAL):
                    screen.blit(JumpRight[2],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
                elif (HERO.statestep>=3)and(HERO.statestep<=4*STEPINTERVAL):
                    screen.blit(JumpRight[3],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
            elif HERO.d==0:
                if (HERO.statestep>=0)and(HERO.statestep<=1*STEPINTERVAL):
                    screen.blit(JumpLeft[0],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
                elif (HERO.statestep>=1*STEPINTERVAL)and(HERO.statestep<=2*STEPINTERVAL):
                    screen.blit(JumpLeft[1],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
                elif (HERO.statestep>=2*STEPINTERVAL)and(HERO.statestep<=3*STEPINTERVAL):
                    screen.blit(JumpLeft[2],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
                elif (HERO.statestep>=3)and(HERO.statestep<=4*STEPINTERVAL):
                    screen.blit(JumpLeft[3],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
        elif HERO.state=='lieshoot':
            if HERO.d==1:
                screen.blit(LieShootRight,((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
            if HERO.d==0:
                screen.blit(LieShootLeft,((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
        elif HERO.state=='run':
            if HERO.d==1:
                if (HERO.statestep>=0*STEPINTERVAL)and(HERO.statestep<=1*STEPINTERVAL):
                    screen.blit(RunRight[0],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=1*STEPINTERVAL)and(HERO.statestep<=2*STEPINTERVAL):
                    screen.blit(RunRight[1],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=2*STEPINTERVAL)and(HERO.statestep<=3*STEPINTERVAL):
                    screen.blit(RunRight[2],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=3*STEPINTERVAL)and(HERO.statestep<=4*STEPINTERVAL):
                    screen.blit(RunRight[3],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=4*STEPINTERVAL)and(HERO.statestep<=5*STEPINTERVAL):
                    screen.blit(RunRight[4],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=5*STEPINTERVAL)and(HERO.statestep<=6*STEPINTERVAL):
                    screen.blit(RunRight[3],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=6*STEPINTERVAL)and(HERO.statestep<=7*STEPINTERVAL):
                    screen.blit(RunRight[2],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=7*STEPINTERVAL)and(HERO.statestep<=8*STEPINTERVAL):
                    screen.blit(RunRight[1],((HERO.x-PAGE),(224-HERO.y-30)))
            elif HERO.d==0:
                if (HERO.statestep>=0*STEPINTERVAL)and(HERO.statestep<=1*STEPINTERVAL):
                    screen.blit(RunLeft[0],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=1*STEPINTERVAL)and(HERO.statestep<=2*STEPINTERVAL):
                    screen.blit(RunLeft[1],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=2*STEPINTERVAL)and(HERO.statestep<=3*STEPINTERVAL):
                    screen.blit(RunLeft[2],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=3*STEPINTERVAL)and(HERO.statestep<=4*STEPINTERVAL):
                    screen.blit(RunLeft[3],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=4*STEPINTERVAL)and(HERO.statestep<=5*STEPINTERVAL):
                    screen.blit(RunLeft[4],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=5*STEPINTERVAL)and(HERO.statestep<=6*STEPINTERVAL):
                    screen.blit(RunLeft[3],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=6*STEPINTERVAL)and(HERO.statestep<=7*STEPINTERVAL):
                    screen.blit(RunLeft[2],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=7*STEPINTERVAL)and(HERO.statestep<=8*STEPINTERVAL):
                    screen.blit(RunLeft[1],((HERO.x-PAGE),(224-HERO.y-30)))
        elif HERO.state=='runshoot':
            if HERO.d==1:
                if (HERO.statestep>=0*STEPINTERVAL)and(HERO.statestep<=1*STEPINTERVAL):
                    screen.blit(RunShootRight[0],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=1*STEPINTERVAL)and(HERO.statestep<=2*STEPINTERVAL):
                    screen.blit(RunShootRight[1],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=2*STEPINTERVAL)and(HERO.statestep<=3*STEPINTERVAL):
                    screen.blit(RunShootRight[2],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=3*STEPINTERVAL)and(HERO.statestep<=4*STEPINTERVAL):
                    screen.blit(RunShootRight[1],((HERO.x-PAGE),(224-HERO.y-30)))
            elif HERO.d==0:
                if (HERO.statestep>=0*STEPINTERVAL)and(HERO.statestep<=1*STEPINTERVAL):
                    screen.blit(RunShootLeft[0],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=1*STEPINTERVAL)and(HERO.statestep<=2*STEPINTERVAL):
                    screen.blit(RunShootLeft[1],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=2*STEPINTERVAL)and(HERO.statestep<=3*STEPINTERVAL):
                    screen.blit(RunShootLeft[2],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=3*STEPINTERVAL)and(HERO.statestep<=4*STEPINTERVAL):
                    screen.blit(RunShootLeft[1],((HERO.x-PAGE),(224-HERO.y-30)))
        elif HERO.state=='shootdown':
            if HERO.d==1:
                if (HERO.statestep>=0*STEPINTERVAL)and(HERO.statestep<=1*STEPINTERVAL):
                    screen.blit(ShootRightDown[0],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=1*STEPINTERVAL)and(HERO.statestep<=2*STEPINTERVAL):
                    screen.blit(ShootRightDown[1],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=2*STEPINTERVAL)and(HERO.statestep<=3*STEPINTERVAL):
                    screen.blit(ShootRightDown[2],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=3*STEPINTERVAL)and(HERO.statestep<=4*STEPINTERVAL):
                    screen.blit(ShootRightDown[1],((HERO.x-PAGE),(224-HERO.y-30)))
            if HERO.d==0:
                if (HERO.statestep>=0*STEPINTERVAL)and(HERO.statestep<=1*STEPINTERVAL):
                    screen.blit(ShootLeftDown[0],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=1*STEPINTERVAL)and(HERO.statestep<=2*STEPINTERVAL):
                    screen.blit(ShootLeftDown[1],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=2*STEPINTERVAL)and(HERO.statestep<=3*STEPINTERVAL):
                    screen.blit(ShootLeftDown[2],((HERO.x-PAGE),(224-HERO.y-30)))
                elif (HERO.statestep>=3*STEPINTERVAL)and(HERO.statestep<=4*STEPINTERVAL):
                    screen.blit(ShootLeftDown[1],((HERO.x-PAGE),(224-HERO.y-30)))
        elif HERO.state=='shootleftup':
            screen.blit(ShootLeftUp,((HERO.x-PAGE),(224-HERO.y-30)))
        elif HERO.state=='shootrightup':
            screen.blit(ShootRightUp,((HERO.x-PAGE),(224-HERO.y-30)))
        elif HERO.state=='shootupleft':
            screen.blit(ShootUpLeft,((HERO.x-PAGE),(224-HERO.y-35)))
        elif HERO.state=='shootupright':
            screen.blit(ShootUpRight,((HERO.x-PAGE),(224-HERO.y-35)))
        elif HERO.state=='right':
            screen.blit(RunShootRight[0],((HERO.x-PAGE),(224-HERO.y-HERO.height-30)))
        elif HERO.state=='left':
            screen.blit(RunShootLeft[0],((HERO.x-PAGE),(224-HERO.y-HERO.height-30)))
        elif HERO.state=='up':
            if HERO.d==0:
                screen.blit(ShootUpLeft,((HERO.x-PAGE),(224-HERO.y-HERO.height-30)))
            elif HERO.d==1:
                screen.blit(ShootUpRight,((HERO.x-PAGE),(224-HERO.y-HERO.height-30)))
        elif HERO.state=='rightup':
            screen.blit(ShootRightUp,((HERO.x-PAGE),(224-HERO.y-HERO.height-30)))
        elif HERO.state=='leftup':
            screen.blit(ShootLeftUp,((HERO.x-PAGE),(224-HERO.y-HERO.height-30)))
        elif HERO.state=='rightdown':
            screen.blit(ShootRightDown[1],((HERO.x-PAGE),(224-HERO.y-HERO.height-30)))
        elif HERO.state=='leftdown':
            screen.blit(ShootLeftDown[1],((HERO.x-PAGE),(224-HERO.y-HERO.height-30)))
        else :
            print('Do Ur Sister,TYPO!')
    if HERO.ondeath=='dead':
        if HERO.state=='inair':
            if HERO.d==1:
                if (HERO.statestep>=0)and(HERO.statestep<=1*STEPINTERVAL):
                    screen.blit(JumpRight[0],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
                elif (HERO.statestep>=1*STEPINTERVAL)and(HERO.statestep<=2*STEPINTERVAL):
                    screen.blit(JumpRight[1],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
                elif (HERO.statestep>=2*STEPINTERVAL)and(HERO.statestep<=3*STEPINTERVAL):
                    screen.blit(JumpRight[2],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
                elif (HERO.statestep>=3)and(HERO.statestep<=4*STEPINTERVAL):
                    screen.blit(JumpRight[3],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
            elif HERO.d==0:
                if (HERO.statestep>=0)and(HERO.statestep<=1*STEPINTERVAL):
                    screen.blit(JumpLeft[0],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
                elif (HERO.statestep>=1*STEPINTERVAL)and(HERO.statestep<=2*STEPINTERVAL):
                    screen.blit(JumpLeft[1],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
                elif (HERO.statestep>=2*STEPINTERVAL)and(HERO.statestep<=3*STEPINTERVAL):
                    screen.blit(JumpLeft[2],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
                elif (HERO.statestep>=3)and(HERO.statestep<=4*STEPINTERVAL):
                    screen.blit(JumpLeft[3],((HERO.x-PAGE),(224-HERO.y-HERO.height-15)))
            screen.blit(DieOnGround,(HERO.x-PAGE,224-HERO.y-10))
    return 0
def DrawBar():
        elif HERO.state=='dieonground':
    global VisualBar1,VisualBar2
    global PAGE
    if len(VisualBar1)==4:
        screen.blit(outBar1,(VisualBar1[0].x1-PAGE,VisualBar1[0].y-11))
        screen.blit(inBar,(VisualBar1[1].x1-PAGE,VisualBar1[1].y-13))
        screen.blit(inBar,(VisualBar1[2].x1-PAGE,VisualBar1[2].y-13))
        screen.blit(outBar2,(VisualBar1[3].x1-PAGE,VisualBar1[3].y-11))
    if len(VisualBar1)==3:
        screen.blit(inBar,(VisualBar1[0].x1-PAGE,VisualBar1[0].y-13))
        screen.blit(inBar,(VisualBar1[1].x1-PAGE,VisualBar1[1].y-13))
        screen.blit(outBar2,(VisualBar1[2].x1-PAGE,VisualBar1[2].y-11))
    if len(VisualBar1)==2:
        screen.blit(inBar,(VisualBar1[0].x1-PAGE,VisualBar1[0].y-13))
        screen.blit(outBar2,(VisualBar1[1].x1-PAGE,VisualBar1[1].y-11))
    if len(VisualBar1)==1:
        screen.blit(outBar2,(VisualBar1[0].x1-PAGE,VisualBar1[0].y-11))
    if len(VisualBar2)==4:
        screen.blit(outBar1,(VisualBar2[0].x1-PAGE,VisualBar2[0].y-11))
        screen.blit(inBar,(VisualBar2[1].x1-PAGE,VisualBar2[1].y-13))
        screen.blit(inBar,(VisualBar2[2].x1-PAGE,VisualBar2[2].y-13))
        screen.blit(outBar2,(VisualBar2[3].x1-PAGE,VisualBar2[3].y-11))
    if len(VisualBar2)==3:
        screen.blit(inBar,(VisualBar2[0].x1-PAGE,VisualBar2[0].y-13))
        screen.blit(inBar,(VisualBar2[1].x1-PAGE,VisualBar2[1].y-13))
        screen.blit(outBar2,(VisualBar2[2].x1-PAGE,VisualBar2[2].y-11))
    if len(VisualBar2)==2:
        screen.blit(inBar,(VisualBar2[0].x1-PAGE,VisualBar2[0].y-13))
        screen.blit(outBar2,(VisualBar2[1].x1-PAGE,VisualBar2[1].y-11))
    if len(VisualBar2)==1:
        screen.blit(outBar2,(VisualBar2[0].x1-PAGE,VisualBar2[0].y-11))
    return 0
def DrawBomb():
    global BombArray
    global BombImage
    global screen
    global PAGE
    for bomb in BombArray:
        if bomb.state==3:
            screen.blit(BombImage[0],(bomb.x-PAGE-40,bomb.y-10))
        if bomb.state==2:
            screen.blit(BombImage[1],(bomb.x-PAGE-40,bomb.y-10))
        if bomb.state==1:
            screen.blit(BombImage[2],(bomb.x-PAGE-40,bomb.y-10))
    return 0
def DrawEnermyType2():
    global ENERMYTYPE2
    global EnermyType20,EnermyType21
    global screen,PAGE
    for i in ENERMYTYPE2:
        if i.d==0:
            screen.blit(EnermyType20,(i.x-PAGE,224-i.y-32))
        if i.d==4:
            screen.blit(EnermyType21,(i.x-PAGE,224-i.y-32))
    return 0
def DrawBossBullet():
    global BOSSBULLET,BOSSBULLETS,BossBulletS,BossBulletSImage,BossBulletImageS
    for bullet in BOSSBULLET:
        screen.blit(BossBulletImageS,((bullet.x-PAGE),(224-bullet.y)))
    for bullet in BOSSBULLETS:
        screen.blit(BossBulletSImage,((bullet.x-PAGE),(224-bullet.y-bullet.height)))
def DrawBoss():
    global BOSS,screen,PAGE,Boss1,Boss2,Boss3,Boss1s,Boss2s,Boss3s
    if BOSS.health1!=0:
        if BOSS.gun1.state=='on':
            screen.blit(Boss1,(3216-PAGE,53))
        elif BOSS.gun1.state=='off':
            screen.blit(Boss1s,(3216-PAGE,53))
    if BOSS.health2!=0:
        if BOSS.gun2.state=='on':
            screen.blit(Boss2,(3238-PAGE,40))
        elif BOSS.gun2.state=='off':
            screen.blit(Boss2s,(3238-PAGE,40))
    if BOSS.health3!=0:
        if BOSS.gun3.state=='on':
            screen.blit(Boss3,(3216-PAGE,136))
        elif BOSS.gun3.state=='off':
            screen.blit(Boss3s,(3216-PAGE,136))
# --init AI--
FLAG1=0
def addPattern(page1,page2,x,y,d,flag,inter):
    global ENERMYTYPE1
    global PAGE
    if (PAGE>=page1)and(PAGE<=page2):
        
        if flag<0:
            flag=inter
        if flag==inter:
            ENERMYTYPE1.append(Enermytype1(x,y,d))
        flag=flag-1
    return flag
def CheckEnermy1():
    global ENERMYTYPE1
    global PAGE
    global BULLET
    for i in range(len(ENERMYTYPE1)):
        try:
            if ENERMYTYPE1[i].d<0:
                if (ENERMYTYPE1[i].x-PAGE<0)or((ENERMYTYPE1[i].y+ENERMYTYPE1[i].height)>=224)or((ENERMYTYPE1[i].y+ENERMYTYPE1[i].height)<=0):
                        ENERMYTYPE1.remove(ENERMYTYPE1[i])
            elif ENERMYTYPE1[i].d>0:
                if (ENERMYTYPE1[i].x-PAGE>400)or((ENERMYTYPE1[i].y+ENERMYTYPE1[i].height)>=224)or((ENERMYTYPE1[i].y+ENERMYTYPE1[i].height)<=0):
                    ENERMYTYPE1.remove(ENERMYTYPE1[i])
        except:
            pass
    for i in range(len(ENERMYTYPE1)):
        if ENERMYTYPE1[i].ondeath=='alive':
            for bullet in BULLET:
                if ((bullet.x-ENERMYTYPE1[i].x)>-10) and((bullet.x-ENERMYTYPE1[i].x)<15)and((bullet.y-ENERMYTYPE1[i].y-ENERMYTYPE1[i].height)>0)and((bullet.y-ENERMYTYPE1[i].y-ENERMYTYPE1[i].height)<40):
                    ENERMYTYPE1[i].ondeath='dead'
                    BULLET.remove(bullet)
    return 0
def CheckEnermy2():
    global ENERMYTYPE2,PAGE,BULLET
    for i in range(len(ENERMYTYPE2)):
        if ENERMYTYPE2[i].ondeath=='alive':
            for bullet in BULLET:
                if ((bullet.x-ENERMYTYPE2[i].x)>-10) and((bullet.x-ENERMYTYPE2[i].x)<15)and((bullet.y-ENERMYTYPE2[i].y)>0)and((bullet.y-ENERMYTYPE2[i].y)<40):
                    ENERMYTYPE2[i].ondeath='dead'
                    ENERMYTYPE2[i].onfire=0
                    BULLET.remove(bullet)
        
def CheckBullet():
    global BULLET
    global ENERMYBULLET
    global PAGE
    global BOSSBULLET,BOSSBULLETS
    for bullet in BULLET:
        if (bullet.x<PAGE)or(bullet.x>(PAGE+400))or(bullet.y>224)or (bullet.y<0):
            BULLET.remove(bullet)
    for bullet in ENERMYBULLET:
        if (bullet.x<PAGE)or(bullet.x>(PAGE+400))or(bullet.y>224)or (bullet.y<0):
            ENERMYBULLET.remove(bullet)
    for bullet in BOSSBULLET:
        if (bullet.x<PAGE)or(bullet.x>(PAGE+400))or(bullet.y>224)or (bullet.y<0):
            BOSSBULLET.remove(bullet)
    for bullet in BOSSBULLETS:
        if (bullet.x<PAGE)or(bullet.x>(PAGE+400))or(bullet.y>224)or (bullet.y<0):
            BOSSBULLETS.remove(bullet)
    return 0
BOMBINTERVAL=200
BOMBFLAG=1
def UpdateBomb(BombArray):
    global BOMBINTERVAL,BOMBFLAG
    global VisualBar1,VisualBar2,PAGE
    if BOMBFLAG==1:
        if BOMBINTERVAL==150 or BOMBINTERVAL==100 or BOMBINTERVAL==50 or BOMBINTERVAL==0:
            BombArray.append(Bomb(VisualBar1[0].x1,VisualBar1[0].y))
            BombSound2.play()
            VisualBar1.remove(VisualBar1[0])
        if BOMBINTERVAL>-10:
            BOMBINTERVAL=BOMBINTERVAL-1
        else:
            BOMBFLAG=0
            BombArray=[]
    if PAGE>850and PAGE<1200:
        if BOMBINTERVAL<0:
            BOMBINTERVAL=200
        if BOMBINTERVAL==150 or BOMBINTERVAL==100 or BOMBINTERVAL==50 or BOMBINTERVAL==0:
            try:
                BombArray.append(Bomb(VisualBar2[0].x1,VisualBar2[0].y))
                BombSound2.play()
  
                VisualBar2.remove(VisualBar2[0])
            except:
                pass
        if BOMBINTERVAL>-10:
            BOMBINTERVAL=BOMBINTERVAL-1
    for bomb in BombArray:
        bomb.update()   
    return 0
def UpdateEnermyType2():
    global ENERMYTYPE2
    for i in ENERMYTYPE2:
        i.update()
    return 0
def CheckHeroForBullet():
    global ENERMYBULLET,HERO
    for bullet in ENERMYBULLET:
       if HERO.state!='lieshoot':
         if ((bullet.x-HERO.x)>-10) and((bullet.x-HERO.x)<15)and((bullet.y-HERO.y-HERO.height)>0)and((bullet.y-HERO.y-HERO.height)<40):
            HERO.ondeath='dead'
            ENERMYBULLET.remove(bullet)
       else:
         if ((bullet.x-HERO.x)>-10) and((bullet.x-HERO.x)<15)and((bullet.y-HERO.y-HERO.height)>0)and((bullet.y-HERO.y-HERO.height)<10):
            HERO.ondeath='dead'
            ENERMYBULLET.remove(bullet)
def CheckHero():
    global HERO,ENERMYTYPE1
    CheckHeroForBullet()
    for enermy in ENERMYTYPE1:
        if ((HERO.x-enermy.x)>-5)and((HERO.x-enermy.x)<20)and((HERO.y+HERO.height-enermy.y-enermy.height)>-10)and((HERO.y+HERO.height-enermy.y-enermy.height)<10):
            if enermy.ondeath=='alive':
                HERO.ondeath='dead'
    if ((HERO.y+HERO.height)<-5):
        if HERO.ondeath=='alive':
            HERO.y=10
            
            HERO.height=0
            HERO.ondeath='dead'
        elif HERO.ondeath=='dead':
            HERO.y=10
            HERO.height=0
            HERO.state='dieonground'
    return 0
GUN1STEP,GUN2STEP,GUN3STEP=0,0,0
def BossAI():
    global BOSS,HERO,BOSSBULLET,BOSSBULETS,GUN1STEP,GUN2STEP,GUN3STEP
    if BOSS.onact=='valid':
        if GUN1STEP==2000:
            GUN1STEP=0
        if GUN2STEP==2500:
            GUN2STEP=0
        if GUN3STEP==3000:
            GUN3STEP=0
        GUN1STEP=GUN1STEP+1
        GUN2STEP=GUN2STEP+1
        GUN3STEP=GUN3STEP+1
        for i in range(5):
          if BOSS.health1>0:
            if GUN1STEP==(200+20*i):
                if HERO.y>112:
                    BOSSBULLET.append(BossBullet(BOSS.gun1.x,BOSS.gun1.y-20,-3*cos(pi*i/(20)),3*sin(pi*i/20)))
                    BombSound2.play()
                else:
                    BOSSBULLET.append(BossBullet(BOSS.gun1.x,BOSS.gun1.y-20,-3*cos(pi*i/(20)),-3*sin(pi*i/20)))
                    BombSound2.play()
        for i in range(5):
          if BOSS.health2>0:
            if GUN2STEP==(400+20*i):
                if HERO.y<=112:
                    BOSSBULLET.append(BossBullet(BOSS.gun2.x,BOSS.gun2.y-20,-3*cos(pi*i/(20)),3*sin(pi*i/20)))
                    BombSound2.play()
                else:
                    BOSSBULLET.append(BossBullet(BOSS.gun2.x,BOSS.gun2.y-20,-3*cos(pi*i/(20)),-3*sin(pi*i/20)))
                    BombSound2.play()
        for i in range(8):
          if BOSS.health2>0:
            if GUN2STEP==(1000+10*i):
                BOSSBULLET.append(BossBullet(BOSS.gun2.x,BOSS.gun2.y-20,-3*cos(pi*i/(20)),3*sin(pi*(i-4)/20)))
                BombSound2.play()
        for i in range(5):
          if BOSS.health1>0:
            if GUN1STEP==(1400+20*i):
                if HERO.y>112:
                    BOSSBULLET.append(BossBullet(BOSS.gun1.x,BOSS.gun1.y-20,-3*cos(pi*i/(20)),3*sin(pi*i/20)))
                    BombSound2.play()
                else:
                    BOSSBULLET.append(BossBullet(BOSS.gun1.x,BOSS.gun1.y-20,-3*cos(pi*i/(20)),-3*sin(pi*i/20)))
                    BombSound2.play()
        for i in range(5):
          if BOSS.health2>0:
            if GUN2STEP==(1200+20*i):
                if HERO.y<=112:
                    BOSSBULLET.append(BossBullet(BOSS.gun2.x,BOSS.gun2.y-20,-3*cos(pi*i/(20)),3*sin(pi*i/20)))
                    BombSound2.play()
                else:
                    BOSSBULLET.append(BossBullet(BOSS.gun2.x,BOSS.gun2.y-20,-3*cos(pi*i/(20)),-3*sin(pi*i/20)))
                    BombSound2.play()
        
        if (GUN3STEP-(GUN3STEP/400)*400)==0:
            if BOSS.health3!=0:
                BOSSBULLETS.append(BossBulletS(BOSS.gun3.x,224-160))
        
            
    return 0 
def CheckBoss():
    global BULLET,BOSS
    for bullet in BULLET:
        if bullet.x>3210 and bullet.x<3237 and bullet.y<(224-81) and bullet.y>(224-138):
          if BOSS.health1!=0:
            BULLET.remove(bullet)
            BOSS.gun1.state='off'
            BOSS.health1=BOSS.health1-1
        if bullet.x>3237 and bullet.x<3270 and bullet.y<(224-69) and bullet.y>(224-138):
          if BOSS.health2!=0:
            BULLET.remove(bullet)
            BOSS.gun2.state='off'
            BOSS.health2=BOSS.health2-1
        if bullet.x>3222 and bullet.x<3248 and bullet.y<(224-142) and bullet.y>(224-197):
          if BOSS.health3!=0:
            BULLET.remove(bullet)
            BOSS.gun3.state='off'
            BOSS.health3=BOSS.health3-1
    return 0
def ResetBoss():
    BOSS.gun1.state='on'
    BOSS.gun2.state='on'
    BOSS.gun3.state='on'
    return 0
def BossHero():
    global HERO,BOSSBULLET,BOSSBULLETS
    for bullet in BOSSBULLET:
        if HERO.state=='stand' or HERO.state=='run':
            if (HERO.x-bullet.x)>-2 and (HERO.x-bullet.x)<20 and (HERO.y-bullet.y)>-4 and (HERO.y-bullet.y)<30:
                BOSSBULLET.remove(bullet)
                HERO.ondeath='dead'
        elif HERO.state=='inair':
            if (HERO.x-bullet.x)>-2 and (HERO.x-bullet.x)<20 and (HERO.y+HERO.height-bullet.y)>-4 and (HERO.y+HERO.height-bullet.y)<10:
                BOSSBULLET.remove(bullet)
                HERO.ondeath='dead'
        elif HERO.state=='lieshoot':
            if (HERO.x-bullet.x)>-2 and (HERO.x-bullet.x)<30 and (HERO.y-bullet.y)>-4 and (HERO.y-bullet.y)<10:
                BOSSBULLET.remove(bullet)
                HERO.ondeath='dead'
        else:
            if (HERO.x-bullet.x)>-2 and (HERO.x-bullet.x)<20 and (HERO.y-bullet.y)>-4 and (HERO.y-bullet.y)<20:
                BOSSBULLET.remove(bullet)
                HERO.ondeath='dead'
    for bullet in BOSSBULLETS:
        if (HERO.x-bullet.x)>-10 and (HERO.x-bullet.x)<20 and (HERO.y-bullet.y-bullet.height)>-10 and (HERO.y-bullet.y-bullet.height)<10:
                BOSSBULLETS.remove(bullet)
                HERO.ondeath='dead'
FLAG2,FLAG3,FLAG4,FLAG5,FLAG7,FLAG6,FLAG7,FLAG8,FLAG9=0,0,0,0,0,0,0,0,0
def AI():
    global FLAG1,FLAG2,FLAG3,FLAG4,FLAG5,FLAG6,FLAG7,FLAG8,FLAG9
    global ENERMYTYPE1,ENERMYTYPE2
    global PAGE,BombArray,BOSSBULLET,BOSSBULLETS,BossFlag,pygame
    CheckEnermy1()
    CheckEnermy2()
    CheckBullet()
    UpdateBullet(BULLET)#根据值变动子弹位置
    UpdateBullet(ENERMYBULLET)#根据值变动子弹位置
    UpdateBossBullet()
    UpdateBossBulletS()
    UpdateEnermyType1()
    FLAG1=addPattern(10,50,400,116,-0.5,FLAG1,500)
    FLAG2=addPattern(0,40,340,224-209,-0.5,FLAG2,500)
    FLAG3=addPattern(50,100,100,116,0.5,FLAG3,500)
    FLAG4=addPattern(300,350,705,224-157,-0.5,FLAG4,300)
    FLAG5=addPattern(900,1000,1478,224-78,-0.5,FLAG5,300)
    FLAG6=addPattern(1200,1300,1500,224-140,-0.5,FLAG6,300)
    FLAG7=addPattern(1414,1500,2001,224-171,-0.5,FLAG7,300)
    FLAG8=addPattern(1324,1499,1869,224-200,-0.5,FLAG8,300)
    FLAG9=addPattern(1717,1800,1800,224-204,0.5,FLAG9,300)
    if PAGE>550:
        UpdateBomb(BombArray)
    if PAGE>10:
        if ENERMYTYPE2[0].ondeath=='alive':
             ENERMYTYPE2[0].onfire=1
    UpdateEnermyType2()
    CheckHero()
    BossAI()
    if BossFlag==0:
        if PAGE>2860:
            BossFlag=1
            BOSS.onact='valid'
            pygame.mixer.music.load('music/Fight.ogg')
    CheckBoss()
    BossHero()
    return 0        
            
# --Main--
DELTAX=0
DELTAF=0
leftFLAG=0
rightFLAG=0
downFLAG=0
upFLAG=0
fireFLAG=0
inairFLAG=0
jumpFLAG=0
DieCount=350
MusicFlag=1
BossFlag=0
DeathCount=3
initMusic=0
while True:
    if pMODE==0:
        WelcomeDisplay()
        sleep(0.007)
    if (pMODE==1):
        if MusicFlag==1:
            MusicFlag=0
            pygame.mixer.music.play(100,0)
        if initMusic==0 and BossFlag==1:
            initMusic=1
            pygame.mixer.music.play(100,0)
        
        sleep(0.007)
        '''
        map part
        '''
        screen.blit(Map1,(-PAGE,0))
        
        
        '''
        event driver
        make event flag
        '''
        if HERO.ondeath=='dead':
            DieCount=DieCount-1
        if DieCount==0:
            HERO.ondeath='alive'
            DieCount=350
            HERO.y=224
            HERO.inair=0
            HERO.height=0
            HERO.x=PAGE+50
            DeathCount=DeathCount-1
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    inairFLAG=1
                elif event.key==K_LEFT:
                  
                    DELTAX=-0.6
                    leftFLAG=1
                    if HERO.ondeath=='alive':
                        HERO.d=0
                    rightFLAG=0
                elif event.key==K_RIGHT:
                  
                    DELTAX=0.6
                    rightFLAG=1
                    if HERO.ondeath=='alive':
                        HERO.d=1
                    leftFLAG=0
                elif event.key==K_f:
                    HERO.onfire=1
                    fireFLAG=1
                    if DELTAF==0:
                        DELTAF=51
                elif event.key==K_DOWN:
                  if upFLAG==0:
                    downFLAG=1
                elif event.key==K_UP:
                  if downFLAG==0:
                    upFLAG=1
                    
            elif event.type==KEYUP:
                if event.key==K_LEFT:
                  if rightFLAG==0:
                    DELTAX=0
                  leftFLAG=0
                elif event.key==K_RIGHT:
                  if leftFLAG==0:
                    DELTAX=0 
                  rightFLAG=0  
                elif event.key==K_f:
                    HERO.onfire=0
                    fireFLAG=0
                    DELTAF=55
                  
                elif event.key==K_DOWN:
                    downFLAG=0    
                elif event.key==K_UP:
                    upFLAG=0   
            elif event.type==QUIT:
              exit()
        if HERO.ondeath=='alive':
            if ((HERO.x-PAGE+DELTAX)<0)or(HERO.x-PAGE+DELTAX)>300:
                pass
            elif(((leftFLAG==1)or(rightFLAG==1))and(upFLAG==1)and(downFLAG==0)and(inairFLAG==0))==False:
                HERO.x=HERO.x+DELTAX
        '''
        fire or something
        '''
        if HERO.onfire==1:
            DELTAF=DELTAF-1
            if DELTAF==0:
                DELTAF=51
        
        '''
        state
        and Bullet Create
        '''
        if(HERO.ondrop==0)and(HERO.ondeath=='alive'):
         if (inairFLAG==1):
            
            if HERO.statestep>=4*STEPINTERVAL:
                HERO.statestep=0
            if fireFLAG==1:
             if DELTAF==50 or DELTAF==35:
              GunSound2.play()
              if HERO.d==0:
                  BULLET.append(Bullet(HERO.x,HERO.y+HERO.height+10,0))
              elif HERO.d==1:
                  BULLET.append(Bullet(HERO.x,HERO.y+HERO.height+10,1))
         elif (leftFLAG==0)and(rightFLAG==0)and(upFLAG==0)and(downFLAG==0)and(inairFLAG==0):
          HERO.state='stand'
          if fireFLAG==1:
            if DELTAF==50 or DELTAF==35:
              GunSound2.play()
              if HERO.d==0:
                  BULLET.append(Bullet(HERO.x,HERO.y+25,0))
              elif HERO.d==1:
                  BULLET.append(Bullet(HERO.x,HERO.y+25,1))
        
         elif(leftFLAG==0)and(rightFLAG==0)and(upFLAG==0)and(downFLAG==1)and(inairFLAG==0):
            HERO.state='lieshoot'
            if HERO.statestep>=4*STEPINTERVAL:
                HERO.statestep=0
            if fireFLAG==1:
             if DELTAF==50 or DELTAF==35:
              GunSound2.play()
              if HERO.d==0:
                  BULLET.append(Bullet(HERO.x-5,HERO.y+10,0))
              elif HERO.d==1:
                  BULLET.append(Bullet(HERO.x+30,HERO.y+10,1))
         elif((leftFLAG==1)or(rightFLAG==1))and(upFLAG==0)and(downFLAG==0)and(inairFLAG==0)and(fireFLAG==0):
            HERO.state='run'
         elif((leftFLAG==0)or(rightFLAG==0))and(upFLAG==0)and(downFLAG==0)and(inairFLAG==0)and(fireFLAG==1):
            HERO.state='runshoot'
            if HERO.statestep>=4*STEPINTERVAL:
                HERO.statestep=0
            if fireFLAG==1:
             if DELTAF==50 or DELTAF==35:
              GunSound2.play()
              if HERO.d==0:
                  BULLET.append(Bullet(HERO.x,HERO.y+25,0))
              elif HERO.d==1:
                  BULLET.append(Bullet(HERO.x,HERO.y+25,1))
         elif((leftFLAG==1)or(rightFLAG==1))and(upFLAG==0)and(downFLAG==1)and(inairFLAG==0):
            HERO.state='shootdown'
            if HERO.statestep>=3*STEPINTERVAL:
                HERO.statestep=0
            if fireFLAG==1:
             if DELTAF==50 or DELTAF==35:
              GunSound2.play()
              if HERO.d==0:
                  BULLET.append(Bullet(HERO.x-15,HERO.y+20,5))
              elif HERO.d==1:
                  BULLET.append(Bullet(HERO.x+20,HERO.y+20,7))
         elif(leftFLAG==1)and(rightFLAG==0)and(upFLAG==1)and(downFLAG==0)and(inairFLAG==0):
            HERO.state='shootleftup'
            if fireFLAG==1:
                if DELTAF==50 or DELTAF==35:
                  BULLET.append(Bullet(HERO.x,HERO.y+30,4))
                  GunSound2.play()
         elif(leftFLAG==0)and(rightFLAG==1)and(upFLAG==1)and(downFLAG==0)and(inairFLAG==0):
            HERO.state='shootrightup'
            if fireFLAG==1:
                if DELTAF==50 or DELTAF==35:
                  BULLET.append(Bullet(HERO.x,HERO.y+30,6))
                  GunSound2.play()
         elif(leftFLAG==0)and(rightFLAG==0)and(upFLAG==1)and(downFLAG==0)and(inairFLAG==0):
            if fireFLAG==1:
                if DELTAF==50 or DELTAF==35:
                  BULLET.append(Bullet(HERO.x,HERO.y+35,2))
                  GunSound2.play()
            if HERO.d==0:
                HERO.state='shootupleft'
            elif HERO.d==1:
                HERO.state='shootupright'
         if(leftFLAG==0)and(rightFLAG==0)and(upFLAG==0)and(downFLAG==1)and(inairFLAG==1):
            if(HERO.state!='inair'):
                HERO.ondrop=1
                if HERO.d==1:
                    HERO.state='right'
                else:
                    HERO.state='left'
                inairFLAG=0
         elif (inairFLAG==1):
            HERO.state='inair'
        elif HERO.ondrop==1 and HERO.ondeath=='alive':
            if(leftFLAG==1)and(rightFLAG==0)and(upFLAG==0)and(downFLAG==0):
                HERO.state='left'
            if(leftFLAG==0)and(rightFLAG==1)and(upFLAG==0)and(downFLAG==0):
                HERO.state='right'
            if(leftFLAG==0)and(rightFLAG==0)and(upFLAG==1)and(downFLAG==0):
                HERO.state='up'
            if(leftFLAG==1)and(rightFLAG==0)and(upFLAG==1)and(downFLAG==0):
                HERO.state='leftup'
            if(leftFLAG==1)and(rightFLAG==0)and(upFLAG==0)and(downFLAG==1):
                HERO.state='leftdown'
            if(leftFLAG==0)and(rightFLAG==1)and(upFLAG==1)and(downFLAG==0):
                HERO.state='rightup'
            if(leftFLAG==0)and(rightFLAG==1)and(upFLAG==0)and(downFLAG==1):
                HERO.state='rightdown'
        
        if (HERO.state=='inair'):
            
            if HERO.statestep>=4*STEPINTERVAL:
                HERO.statestep=0
            else:
                HERO.statestep=HERO.statestep+1
        elif(HERO.state=='run'):
            if HERO.statestep==8*STEPINTERVAL:
                HERO.statestep=0
            else:
                HERO.statestep=HERO.statestep+1
        elif(HERO.state=='runshoot'):
            if HERO.statestep==4*STEPINTERVAL:
                HERO.statestep=0
            else:
                HERO.statestep=HERO.statestep+1
        elif(HERO.state=='shootdown'):
            if HERO.statestep==4*STEPINTERVAL:
                HERO.statestep=0
            else:
                HERO.statestep=HERO.statestep+1
      
            
        if(HERO.CheckOnBoard(CheckBarArray)):
                jumpFLAG=0
               
                HERO.state='stand'
                HERO.ondrop=0
            
                inairFLAG=0
        
        if ((Checkbar(CheckBarArray)==False )and (Checkbar(VisualBar1)==False)and (Checkbar(VisualBar2)==False)):
            if (HERO.state!='inair'):
                  HERO.ondrop=1
                  HERO.state='right'
        
        
        if(HERO.ondrop==1)and(HERO.ondeath=='alive'):
            Drop(HERO)
        
        if (HERO.state=='inair'and HERO.ondeath=='alive'):
            UpdateHeight(HERO)
        
        if HERO.ondeath=='dead':
            if HERO.state!='dieonground':
                HERO.state='inair'
            if HERO.state=='inair':
                UpdateHeight(HERO)
        
        if(HERO.CheckOnBoard(CheckBarArray)or HERO.CheckOnBoard(VisualBar1)or HERO.CheckOnBoard(VisualBar2)):
            if HERO.ondeath=='alive':
                jumpFLAG=0
                HERO.state='stand'
                HERO.ondrop=0
            
                inairFLAG=0
            elif HERO.ondeath=='dead':
                HERO.state='dieonground'
        
        AI()
        DrawBullet()
        DrawEnermyType1()
        DrawEnermyType2()
        DrawBar()
        DrawHero()
        DrawBomb()
       
        DrawBoss()
        DrawBossBullet()
        ResetBoss()   
        
        if DeathCount==0:
            pMODE=2
        DrawMark()
        ScrollPage()
    if pMODE==2:
        sleep(0.01)
        
        pygame.mixer.music.stop()
        GameOverDisplay()
        
    pygame.display.update()