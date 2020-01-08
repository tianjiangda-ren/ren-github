import tkinter as tk  # 使用Tkinter前需要先导入
import sqlite3#导入数据库模块

# 第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('星界边际查询工具')
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

 # 第4步，在图形界面上设定输入框控件entry框并放置
e = tk.Entry(window, show = None,font=('华文新魏', 16))#显示成明文形式
e.pack()
 
# 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def select_sbdb(): 
    var = e.get()#获取输入框中输入的内容
    # t1.insert('insert', var)# 在鼠标焦点处插入输入内容
    path1=sys.path[0]+r"\sb.db3"#当前目录创建数据库路径
    # print("默认路径文件:\n",path1,"\n")#打印数据库文件路径
#    con=sqlite3.connect(path1)#打开数据库
    con=sqlite3.connect(r'.\sb.db3')#打开数据库
    c=con.cursor()#创建游标
    c.execute('select * from starbound where name like "%'+ var +'%" ')
    # c.execute('select * from starbound')
    res = c.fetchall()  # 从游标中取出所有记录放到一个序列中
    # print (result)
    t1.insert('insert', res[0][0])
    t2.insert('insert', res[0][1])
    t3.insert('insert', res[0][2])
    t4.insert('insert', res[0][3])
    t5.insert('insert', res[0][4])
    t6.insert('insert', res[0][5])
    t7.insert('insert', res[0][6])


# 第6步，创建并放置两个按钮分别触发两种情况
b = tk.Button(window, text='查询', width=10,
               height=1, command=select_sbdb)

b.pack()

# 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
t1 = tk.Text(window, height=2)
t1.pack()
t2 = tk.Text(window, height=2)
t2.pack()
t3 = tk.Text(window, height=2)
t3.pack()
t4 = tk.Text(window, height=2)
t4.pack()
t5 = tk.Text(window, height=2)
t5.pack()
t6 = tk.Text(window, height=2)
t6.pack()
t7 = tk.Text(window, height=2)
t7.pack()

# 第8步，主窗口循环显示
window.mainloop()