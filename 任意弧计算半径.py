#测试
# -*- coding: utf-8 -*-
while 1:
	print("任意弧求半径\n两端直线距离为长\n中点与宽垂线为宽")
	a=int(input("长:"))
	b=int(input("宽:"))
	'''
	r**2=(r-b)**2+(a/2)**2 #勾股定理
	r**2=r**2-2rb+b**2+(a/2)**2 #同时减r**2加2rb
	2rb=b**2+(a/2)**2
	r=(b**2+(a/2)**2)/b/2
	r=(b**2+a**2/4)/2/b
	r=a*a/8/b+b/2
	'''
	r=a*a/8/b+b/2
	print(r,"\n")