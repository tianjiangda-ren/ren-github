#测试
# -*- coding: utf-8 -*-
'''
a=input('输入命令\n')
print(a)
print(eval(a))#输入内容当做命令执行
'''  
import time #导入时间模块
time1=time.time() #计算当前时间
'''
算法根据马青公式计算圆周率

'''
number = int(input('请输入想要计算到小数点后的位数n:'))
number1 = number+10 # 多计算10位，防止尾数取舍的影响
b = 10**number1 # 算到小数点后number1位

x1 = b*4//5 # 求含4/5的首项
x2 = b// -239 # 求含1/239的首项

he = x1+x2 # 求第一大项
number *= 2 #设置下面循环的终点，即共计算n项

for i in range(3,number,2): #循环初值=3，末值2n,步长=2
    x1 //= -25 # 求每个含1/5的项及符号
    x2 //= -57121 # 求每个含1/239的项及符号
    x = (x1+x2) // i     # 求两项之和
    he += x # 求总和

pai = he*4  # 求出π
pai //= 10**10 #舍掉后十位

paistring=str(pai) ############ 输出圆周率π的值
result=paistring[0]+str('.')+paistring[1:len(paistring)]
print (result)

time2=time.time()
print (u'总共耗时：' + str(time2 - time1) + 's')
