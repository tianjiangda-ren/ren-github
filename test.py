#!/usr/bin/env python
# _*_ coding:utf-8 _*_
s=int(input('我的数字：'))

for i in range(-s+1,s):
    print((' *'*(s-abs(i))).center(s*2))

for i in range(-s+1,s):
    if i<0:i=-i
    print(' '*i+'*'*(2*(s-i)-1))
    
    