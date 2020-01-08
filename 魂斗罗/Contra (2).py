PAGE=0
STEPINTERVAL=15
'''
import CheckBarArray &
       pygame
! PAGE >=0
'''


import pygame
from pygame.locals import*
from sys import exit
from time import sleep
from math import sin
from math import cos
from math import pi





'''
init pygame
'''
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
pygame.init()
pygame.mixer.set_num_channels(8)
screen=pygame.display.set_mode((400,224),1,32)
pygame.display.set_caption("CONTRA")
Map1=pygame.image.load(r'Map1.png')
pygame.mixer.music.load('BackMusic2.ogg')
GunSound2=pygame.mixer.Sound('GunSound2.ogg')
BombSound2=pygame.mixer.Sound('BombSound2.ogg')
BombSound2.set_volume(0.20)



'''
init CONTRA image
'''
back=pygame.image.load('back.png')
JumpLeft=[]
JumpRight=[]
DieOnGround=pygame.image.load('DieOnGround.png')
for i in range(4):
    JumpLeft.append(pygame.image.load('JumpLeft'+str(i+1)+'.png').convert_alpha())
for i in range(4):
    JumpRight.append(pygame.image.load('JumpRight'+str(i+1)+'.png').convert_alpha())
LieShootLeft=pygame.image.load('LieShootLeft.png').convert_alpha()
LieShootRight=pygame.image.load('LieShootRight.png').convert_alpha()
RunLeft=[]
RunRight=[]
for i in range(5):
    RunLeft.append(pygame.image.load('RunLeft'+str(i+1)+'.png').convert_alpha())
for i in range(5):
    RunRight.append(pygame.image.load('RunRight'+str(i+1)+'.png').convert_alpha())
RunShootLeft=[]
RunShootRight=[]
for i in range(3):
    RunShootLeft.append(pygame.image.load('RunShootLeft'+str(i+1)+'.png').convert_alpha())
for i in range(3):
    RunShootRight.append(pygame.image.load('RunShootRight'+str(i+1)+'.png').convert_alpha())
ShootLeftDown=[]
ShootRightDown=[]
ShootLeftUp=pygame.image.load('ShootLeftUp.png').convert_alpha()
ShootRightUp=pygame.image.load('SHootRightUp.png').convert_alpha()
for i in range(3):
    ShootLeftDown.append(pygame.image.load('ShootLeftDown'+str(i+1)+'.png').convert_alpha())
for i in range(3):
    ShootRightDown.append(pygame.image.load('ShootRightDown'+str(i+1)+'.png').convert_alpha())
ShootUpLeft=pygame.image.load('ShootUpLeft.png').convert_alpha()
ShootUpRight=pygame.image.load('ShootUpRight.png').convert_alpha()
WelcomeChar=pygame.image.load('WelcomeChar.png').convert_alpha()
WelcomeLogo=pygame.image.load('WelcomeLogo.png').convert_alpha()
HeroBullet=pygame.image.load('HeroBullet.png').convert_alpha()
EnermyType1ImageLeft=[]
EnermyType1ImageRight=[]
for i in range(4):
    EnermyType1ImageLeft.append(pygame.image.load('EnermyType1ImageLeft'+str(i+1)+'.png').convert_alpha())
    EnermyType1ImageRight.append(pygame.image.load('EnermyType1ImageRight'+str(i+1)+'.png').convert_alpha())
inBar=pygame.image.load('inBar.png')
outBar1=pygame.image.load('outBar1.png')
outBar2=pygame.image.load('outBar2.png')
BombImage=[]
for i in range(3):
    BombImage.append(pygame.image.load('Bomb'+str(i+1)+'.png'))
EnermyType20=pygame.image.load('EnermyType20.png').convert_alpha()
EnermyType21=pygame.image.load('EnermyType21.png').convert_alpha()
Boss1=pygame.image.load('Boss1.png').convert_alpha()
Boss2=pygame.image.load('Boss2.png').convert_alpha()
Boss3=pygame.image.load('Boss3.png').convert_alpha()
Boss4=pygame.image.load('Boss4.png').convert_alpha()
Boss1s=pygame.image.load('Boss1s.png').convert_alpha()
Boss2s=pygame.image.load('Boss2s.png').convert_alpha()
Boss3s=pygame.image.load('Boss3s.png').convert_alpha()
BossBulletSImage=pygame.image.load('BossBulletS.png').convert_alpha()
'''
init
CheckBarArray
'''
class Bar:
    def __init__(self,x,y,z):
        self.x1=x
        self.x2=y
        self.y=z
CheckBarArray=[]
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
'''
visual bar
'''
VisualBar1=[]
VisualBar1.append(Bar(736,767,224-108))
VisualBar1.append(Bar(767,799,224-108))
VisualBar1.append(Bar(799,831,224-108))
VisualBar1.append(Bar(831,867,224-108))
VisualBar2=[]
VisualBar2.append(Bar(736+289,767+289,224-108))
VisualBar2.append(Bar(767+289,799+289,224-108))
VisualBar2.append(Bar(799+289,831+289,224-108))
VisualBar2.append(Bar(831+289,867+289,224-108))





'''
init bullet
about direction:
      0:left
      1:right:
      2:up
      3:down
      4:leftup
      5:leftdown
      6:rightup
      7:rightdown
'''
BULLETSPEED=3
class Bullet:
    def __init__(self,x,y,d):
        self.x=x
        self.y=y
        self.d=d
    def CheckIfOut(self,page):
        if (self.x<page)or(self.x>page+400)or(self.y>224)or(self.y<0):
            return True
        else:
            return False

BULLET=[]
ENERMYBULLET=[]
def UpdateBullet(array):
    global BULLETSPEED
    for bullet in array:
        if bullet.d==0:
            bullet.x=bullet.x-BULLETSPEED
        elif bullet.d==1:
            bullet.x=bullet.x+BULLETSPEED
        elif bullet.d==2:
            bullet.y=bullet.y+BULLETSPEED
        elif bullet.d==3:
            bullet.y=bullet.y-BULLETSPEED
        elif bullet.d==4:
            bullet.y=bullet.y+BULLETSPEED
            bullet.x=bullet.x-BULLETSPEED
        elif bullet.d==5:
            bullet.y=bullet.y-BULLETSPEED
            bullet.x=bullet.x-BULLETSPEED
        elif bullet.d==6:
            bullet.y=bullet.y+BULLETSPEED
            bullet.x=bullet.x+BULLETSPEED
        elif bullet.d==7:
            bullet.y=bullet.y-BULLETSPEED
            bullet.x=bullet.x+BULLETSPEED
    
'''
init PEOPLE
state:
      RunLeft:1 2 3 4 5 4 3 2
      RunShoot:1 2 3 2
'''
class People:
    def __init__(self,a,b):
        self.x=a
        self.y=b
        self.height=0
        self.state='stand'
        self.inair=0
        self.statestep=0
        self.onfire=0
        self.d=1
        self.ondrop=0
        self.ondeath='alive'
    def CheckOnBoard(self,array):
     global HERO
     if HERO.state=='inair':
      if HERO.inair>0.76:

        for i in range(len(array)):
            if self.x>array[i].x1-10:
                if self.x<array[i].x2:
                    if ((self.y+self.height)-array[i].y)<5and((self.y+self.height)-array[i].y)>-5:
                        self.y=array[i].y
                        self.inair=0
                        self.height=0
                        return True
     elif HERO.ondrop==1:
       if HERO.inair>0.2:
         for i in range(len(array)):
            if self.x>array[i].x1-10:
                if self.x<array[i].x2:
                    if ((self.y+self.height)-array[i].y)<4and((self.y+self.height)-array[i].y)>-4:
                        self.y=array[i].y
                        self.inair=0
                        self.height=0
                        self.ondrop=0
                        
                        return True
         return False

     return False
HERO=People(2888,224)
'''
init enermy
'''
class Enermytype1():
    def __init__(self,a,b,c):
        self.x=a
        self.y=b
        self.d=c
        self.height=0
        self.state='run'
        self.inair=0
        self.runstate=0
        self.ondeath='alive'
    def CheckOnBoard(self,array):
      if self.inair>0.5and self.state=='inair':
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
    
ENERMYTYPE1=[]
class Enermytype2():
    def __init__(self,x,y,d):
        self.x=x
        self.y=y
        self.d=d
        self.onfire=0
        self.step=100
        self.ondeath='alive'
    def update(self):
        global ENERMYBULLET
        if self.onfire==1:
            if self.step==0:
                ENERMYBULLET.append(Bullet(self.x-10,self.y+38,self.d))
                self.step=100
            self.step=self.step-1
        return 0
ENERMYTYPE2=[]
ENERMYTYPE2.append(Enermytype2(328,224-207,4))


def UpdateEnermyType1():
    global ENERMYTYPE1
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
'''
init Bomb
'''
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
'''
init Boss
'''
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
        self.health3=200
        self.onact='invalid'
BOSS=Boss(3216,125,3240,125,3224,168)



'''
DEF Func
'''
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
    
    

    

'''
DEF DISPALY FUNC

'''

WELCOMECOUNT=0
pMODE=1 
def WelcomeDisplay():
    global screen
    global WELCOMECOUNT
    global pMODE
    my_font=pygame.font.Font(r"MMM.ttf",20) 
    text_surface=my_font.render("PRESS SPACE",True,(255,255,255))
    screen.blit(back,(0,0))
    if (WELCOMECOUNT<200):
        screen.blit(WelcomeLogo,((400-(WELCOMECOUNT*1.6)),10))
        screen.blit(WelcomeChar,((600-(WELCOMECOUNT*1.6)),80))
        screen.blit(text_surface,(440-(WELCOMECOUNT*1.6),150))
        WELCOMECOUNT=WELCOMECOUNT+1
    else:
        screen.blit(WelcomeLogo,((400-(WELCOMECOUNT*1.6)),10))
        screen.blit(WelcomeChar,((600-(WELCOMECOUNT*1.6)),80))
        screen.blit(text_surface,(440-(WELCOMECOUNT*1.6),150))
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                if (WELCOMECOUNT>150):
                    pMODE=1
        elif event.type==QUIT:
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
        elif HERO.state=='dieonground':
            screen.blit(DieOnGround,(HERO.x-PAGE,224-HERO.y-10))

    return 0
def DrawBar():
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
            screen.blit(BombImage[0],(bomb.x-PAGE,bomb.y-20))
            
        if bomb.state==2:
            screen.blit(BombImage[1],(bomb.x-PAGE,bomb.y-20))
           
        if bomb.state==1:
            screen.blit(BombImage[2],(bomb.x-PAGE,bomb.y-20))
            
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
    global BOSSBULLET,BOSSBULLETS,BossBulletS
    for bullet in BOSSBULLET:
        screen.blit(HeroBullet,((bullet.x-PAGE),(224-bullet.y)))
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



'''
init AI
'''
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
        if ENERMYTYPE2[i].d<0:
            if (ENERMYTYPE2[i].x-PAGE<0)and(ENERMYTYPE2[i].y>=224)and(ENERMYTYPE2[i].y<=0):
                    ENERMYTYPE2.remove(ENERMYTYPE2[i])
        elif ENERMYTYPE2[i].d>0:
            if (ENERMYTYPE2[i].x-PAGE>400)and(ENERMYTYPE2[i].y>=224)and(ENERMYTYPE2[i].y<=0):
                ENERMYTYPE2.remove(ENERMYTYPE1[i])

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
        if ((bullet.x-HERO.x)>-10) and((bullet.x-HERO.x)<15)and((bullet.y-HERO.y-HERO.height)>0)and((bullet.y-HERO.y-HERO.height)<40):
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
                    BOSSBULLET.append(BossBullet(BOSS.gun1.x,BOSS.gun1.y,-3*cos(pi*i/(20)),3*sin(pi*i/20)))
                else:
                    BOSSBULLET.append(BossBullet(BOSS.gun1.x,BOSS.gun1.y,-3*cos(pi*i/(20)),-3*sin(pi*i/20)))
        for i in range(5):
          if BOSS.health2>0:
            if GUN2STEP==(400+20*i):
                if HERO.y<=112:
                    BOSSBULLET.append(BossBullet(BOSS.gun2.x,BOSS.gun2.y,-3*cos(pi*i/(20)),3*sin(pi*i/20)))
                else:
                    BOSSBULLET.append(BossBullet(BOSS.gun2.x,BOSS.gun2.y,-3*cos(pi*i/(20)),-3*sin(pi*i/20)))
        for i in range(8):
          if BOSS.health2>0:
            if GUN2STEP==(1000+10*i):
                BOSSBULLET.append(BossBullet(BOSS.gun2.x,BOSS.gun2.y,-3*cos(pi*i/(20)),3*sin(pi*(i-4)/20)))

        for i in range(5):
          if BOSS.health1>0:
            if GUN1STEP==(1400+20*i):
                if HERO.y>112:
                    BOSSBULLET.append(BossBullet(BOSS.gun1.x,BOSS.gun1.y,-3*cos(pi*i/(20)),3*sin(pi*i/20)))
                else:
                    BOSSBULLET.append(BossBullet(BOSS.gun1.x,BOSS.gun1.y,-3*cos(pi*i/(20)),-3*sin(pi*i/20)))
        for i in range(5):
          if BOSS.health2>0:
            if GUN2STEP==(1200+20*i):
                if HERO.y<=112:
                    BOSSBULLET.append(BossBullet(BOSS.gun2.x,BOSS.gun2.y,-3*cos(pi*i/(20)),3*sin(pi*i/20)))
                else:
                    BOSSBULLET.append(BossBullet(BOSS.gun2.x,BOSS.gun2.y,-3*cos(pi*i/(20)),-3*sin(pi*i/20)))
        
        if (GUN3STEP-(GUN3STEP/400)*400)==0:
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
    






    






    
FLAG2,FLAG3,FLAG4,FLAG5,FLAG7,FLAG6,FLAG7,FLAG8,FLAG9=0,0,0,0,0,0,0,0,0
def AI():
    global FLAG1,FLAG2,FLAG3,FLAG4,FLAG5,FLAG6,FLAG7,FLAG8,FLAG9
    global ENERMYTYPE1,ENERMYTYPE2
    global PAGE,BombArray,BOSSBULLET,BOSSBULLETS,BossFlag

    CheckEnermy1()
    CheckEnermy2()
    CheckBullet()
    UpdateBullet(BULLET)
    UpdateBullet(ENERMYBULLET)
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
    CheckBoss()


    return 0        
            
'''
Main
'''
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
while True:
    if (pMODE==1):
        if MusicFlag==1:
            MusicFlag=0
            pygame.mixer.music.play(100,0)
        
        sleep(0.008)
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
                  BULLET.append(Bullet(HERO.x,HERO.y+5,0))
              elif HERO.d==1:
                  BULLET.append(Bullet(HERO.x,HERO.y+5,1))
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
        try:
            print BOSSBULLETS[0].x
        except:
            pass







        ScrollPage()
        

    pygame.display.update()

    
    
    
