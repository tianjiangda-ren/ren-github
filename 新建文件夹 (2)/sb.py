#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  # 使用Tkinter前需要先导入
import sqlite3#导入数据库模块
import pyglet

#创建窗口
window = tk.Tk()#k是小写的 # 第1步，实例化object，建立窗口window
window.title('星界边境查询工具')# 第2步，给窗口的可视化起名字
window.iconbitmap('sb_img/11.ico')#设置窗口图标
window.geometry('510x300')  # 这里的乘是小x# 第3步，设定窗口的大小(长 * 宽)

# 第4步，在图形界面上创建 500 * 300 大小的画布并放置各种元素
canvas1 = tk.Canvas(window, height=1050, width=1920)#下面的图片最好也是相同的分辨率
# 说明图片位置，并导入图片到画布上
image_file1 = tk.PhotoImage(file='sb_img/bg.png')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
image1 = canvas1.create_image(0, 0, anchor='nw',image=image_file1)
canvas1.pack()

T1 = canvas1.create_text(30, 65, text='NAME', fill='darkgreen', font=('MV Boli', 10, "bold"))
T2 = canvas1.create_text(30, 95, text='类型', fill='aqua', font=('Arial', 12, "bold"))
T3 = canvas1.create_text(30, 125, text='像素', fill='aqua', font=('Arial', 12, "bold"))
T4 = canvas1.create_text(30, 155, text='item', fill='aqua', font=('Arial', 12, "bold"))
T5 = canvas1.create_text(30, 195, text='描述', fill='aqua', font=('Arial', 12, "bold"))
T7 = canvas1.create_text(30, 260, text='合成', fill='aqua', font=('Arial', 12, "bold"))

 # 第4步，在图形界面上设定输入框控件entry框并放置
e = tk.Entry(window, show = None,font=('华文新魏', 16), width=12)#显示成明文形式
e.place(x=150, y=12, anchor='nw')
 
# 第5步，定义一个触发事件时的函数（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def select_sbdb(): # 在鼠标焦点处插入输入内容
	var = e.get()#获取输入框中输入的内容
	con=sqlite3.connect(r'.\sb.db3')#打开数据库
	c=con.cursor()#创建游标
	c.execute('select * from starbound where name like "%'+ var +'%" ')
	# c.execute('select * from starbound')
	res = c.fetchall()  # 从游标中取出所有记录放到一个序列中
	# print (result)
	t1.delete('1.0', 'end')#清空内容(Text.delete(1.0,END)代表将文本框从第一行删除至最后一行，即清空)
	t2.delete('1.0', 'end')
	t3.delete('1.0', 'end')
	t4.delete('1.0', 'end')
	t5.delete('1.0', 'end')
	# t6.delete('1.0', 'end')
	t7.delete('1.0', 'end')
	# t8.delete('1.0', 'end')
	t1.insert('insert', res[0][0])
	t2.insert('insert', res[0][1])
	t3.insert('insert', res[0][2])
	t4.insert('insert', res[0][3])
	t5.insert('insert', res[0][4])
	# t6.insert('insert', res[0][5])
	t7.insert('insert', res[0][6])
	# result1 = cursor.execute(sql)  # 返回受影响的行数
	#print result1
	# print(type(res[0][5]))
	# print(res[0][5])
	# global sbbb_picture#使用global来声明变量为全局变量(create_image方法有两个重要的点要注意，一个是格式，第二是要保持持续引用)
	# sbbb_picture = tk.PhotoImage(file=res[0][5])  # 这里对图片的格式也有要求的
	# t8.image_create('end', image=sbbb_picture)
	# some = input("输入关键字：")
	# for row in c.execute('select * from starbound where name like "%'+ some + '%";'):#逐行打印查询到的数据
	#	 print (row)
	#	 print (type(row))

	# sb_picture = res[0][5]
	# print(sb_picture)
	
	#物品图片
	canvas2 = tk.Canvas(window, bg='LightGrey', width=200, height=125)#下面的图片最好也是相同的分辨率
	# 说明图片位置，并导入图片到画布上
	global image_file2#使用global来声明变量为全局变量(create_image方法有两个重要的点要注意，一个是格式，第二是要保持持续引用)
	image_file2 = tk.PhotoImage(file=res[0][5])  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
	# print(image_file2)
	# canvas2.create_image(10, 10, anchor='nw',image=image_file2)
	canvas2.create_image(100, 50, image=image_file2)
	canvas2.place(x=300, y=40, anchor='nw')
	# canvas2.pack()

# 第6步，创建并放置一个按钮触发查询
b = tk.Button(window, text='查询', width=10,
			   height=1, command=select_sbdb)
b.place(x=300, y=10, anchor='nw')

# 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
# t1 = tk.Text(window, bg='green', font=('Comic Sans MS', 10, 'bold'), height=2, width=30)
#名称
# t1 = tk.Text(window, fg="green", font=('幼圆', 10, 'bold italic'), height=2, width=30)
# t1 = tk.Text(window, fg="green", font=('幼圆', 10, 'italic'), height=2, width=30)
t1 = tk.Text(window, fg="green", font=('微软雅黑', 10, 'bold'), height=2, width=30)
# t1.pack()
t1.place(x=50, y=50, anchor='nw')

#类型
t2 = tk.Text(window, font=('微软雅黑', 10, 'bold'), height=2, width=30)
# t2.pack()
t2.place(x=50, y=80, anchor='nw')

#像素
t3 = tk.Text(window, font=('Comic Sans MS', 10, 'bold'), height=2, width=30)
# t3.pack()
t3.place(x=50, y=110, anchor='nw')

#item
t4 = tk.Text(window, font=('Comic Sans MS', 10, 'bold'), height=2, width=30)
# t4.pack()
t4.place(x=50, y=140, anchor='nw')

#描述
t5 = tk.Text(window, font=('微软雅黑', 10, 'bold'), height=3, width=56)
# t5.pack()
t5.place(x=50, y=170, anchor='nw')

# t6 = tk.Text(window, font=('Comic Sans MS', 10, 'bold'), height=2)
# # t6.pack()
# t6.place(x=50, y=210, anchor='nw')

#合成
t7 = tk.Text(window, font=('Comic Sans MS', 10, 'bold'), height=2, width=56)
# t7.pack()
t7.place(x=50, y=240, anchor='nw')

# t8 = tk.Text(window, width=30, height=9)
# # t8.pack(padx=10, pady=10)
# t8.place(x=300, y=50, anchor='nw')
# sbbb_picture = tk.PhotoImage(file="sb_img/Coal_Sample.png")  # 这里对图片的格式也有要求的
# t8.image_create('end', image=sbbb_picture)


# 第8步，主窗口循环显示
window.mainloop()
