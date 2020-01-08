#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk  # 使用Tkinter前需要先导入
创建可视化窗口
'''创建可视化窗口
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
# 第3步，设定窗口的大小(长 * 宽)
 
window.geometry('500x300')  # 这里的乘是小x
'''
添加部件
-'''Label（标签）
# 第4步，在图形界面上设定标签
l = tk.Label(window, text='你好！this is Tkinter', bg='green', fg='white', font=('华文新魏', 12), width=30, height=2)
# 说明：bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
 
# 第5步，放置标签
l.pack()    # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();
'''
-'''Button（按钮）
# 第4步，在图形界面上设定标签
var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('华文新魏', 12), width=30, height=2)
l.pack()
 
# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')
 
# 第5步，在窗口界面设置放置Button按键
b = tk.Button(window, text='hit me', font=('华文新魏', 12), width=10, height=1, command=hit_me)
b.pack()

'''
#
'''
'''
