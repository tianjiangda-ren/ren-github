#数据库练习脚本
#-*- encoding=utf8 -*-
import sqlite3#导入数据库模块
import sys#导入系统模块
path1=sys.path[0]+"测试数据库.db"#当前目录创建数据库路径
print("默认路径文件:\n",path1)#打印数据库文件路径
con=sqlite3.connect(path1)#打开数据库
c=con.cursor()#创建游标

def ll_table(c):#查看表结构
    ll_db()#打印所有表
    table=input("查看哪个表？\n")
    print(r"PRAGMA table_info table")
    for row in c.execute('PRAGMA table_info(%s)'%(table)):
        print(row)
    print("\n")

def ll_db(c):#查看所有表
l=list(c.execute("select name from sqlite_master where type='table' order by name"))
    print("所有表")
    return l
    for ll in l: 
        print (ll)

def create(c):#创建新表
    ll_db()#打印所有表
    table_name=input("\n创建表名为\n")
    new=input("主键列名，字符类型，以空格隔开\n不写创建默认自增主键\n")
    if new:
        new=new+' primary key'
    else:
        new='id INTEGER primary key AUTOINCREMENT'
    table_lie='CREATE TABLE '+table_name+'('+new
    while new:
        new=input("新列名，字符类型，以空格隔开\n")        
        table_lie=table_lie+','+new
    sql_create=table_lie[:-1]+')'
    c.execute(sql_create)
    print('创建成功')
    ll_db()#打印所有表
    
def drop(c):#删除指定表
    ll_db()#打印所有表
    table=input("删除哪个表？\n")#获得要删除的表名
    print(r"DROP TABLE table")#打印删除表语句
    try:
        c.execute("DROP TABLE %s"%(table))#执行删除表语句
        print("删除成功")
    except:
        print("删除失败，请检查该表是否存在")
    ll_db()#打印所有表

def sql_up(c):#修改数据
    print(r"update table set new(列名=列值) where old(列名=列值)")#打印修改语句
    zhi1=input("列名=新值\n")#获得要改成的值
    zhi2=input("修改条件\n")#获得要修改的数据条件
    c.execute('update '+table+' set '+zhi1+' where '+zhi2)#执行修改语句

def sql_sel(c):#查询数据
    print(r'select 列名 from table where 条件')#打印查询语句
    lie=input("查询列名(所有请输入*)\n")#获得显示列名
    zhi3=input("查询条件\n")#获得查询条件
    for row in c.execute('select '+lie+' from '+table+' where '+zhi3):#逐行打印查询到的数据
        print(row)

def sql_ins(c):#插入数据
    print(r'insert into table values(对应值)')#打印插语句
    zhi='null,yu,8'#input("各列对应值，以英文逗号隔开\n")#获得插入值
    c.execute('insert into '+table+' values('+zhi+')')#执行插入语句

def sql_del(c):#删除数据
    print(r'delete from table where 删除条件')#打印删除语句
    zhi=input("删除条件\n")#获得删除语句
    c.execute('delete from '+table+' where '+zhi)#执行删除语句

print("%18s"%("选择要执行的命令："),
    "\n%18s"%("1.查看所有表"),
    "\n%18s"%("2.创建新表"),
    "\n%18s"%("3.删除指定表"),
    "\n%18s"%("4.查看表结构"),
    "\n%18s"%("5.查看表数据"),
    "\n%18s"%("6.插入表数据"),
    "\n%18s"%("7.修改表数据"))
    "\n%18s"%("7.删除表数据"))
xz=input("")

con.commit()#提交数据
con.close()#关闭数据库
'''
括号里内容格式：""

新建表
"create table 表名 #创建新表
id int primary key, #主键列
列名 数据类型, #普通列
foreign key(列名) references 关联表名(关联列名)" #关联列

插入
变量名=[(各列对应值 以,隔开),
       (可添加多个值)] #插入方式三备用
"insert into 表名 values(各列对应值 以,隔开)" #方法一
"insert into 表名 values(?,?)",(各列对应值 以,隔开) #方法二
"insert into 表名 values(?,?)",变量名 #方法三
#使用"?"作为替代符号，并在后面的参数中给出具体值。这里不能用Python的格式化字符串，如"%s"，因为这一用法容易受到SQL注入攻击。

查询结果读取
"select * from 表名 where 条件 排序命令 having 函数条件"
print(c.fetchone())#查看一条
print(c.fetchall())#查看所有
或者循环读取全部
for row in c.execute("select * from 表名 where 条件 排序命令 having 函数条件"):
 print(row)

修改和删除
"update 表名 set 已知列名=新列值 where 已知列名=已知列值"
"delete from 表名 where 列名=列值"

删除整个表
"DROP TABLE book"
'''
'''
实际应用，异常处理
zhi=[(),
     ()
    ]
sql_insert="insert into 表名 values(?,?)"
sql_select="select * from 表名 where 条件 排序命令 having 函数条件"
sql_update="update 表名 set 已知列名=新列值 where 已知列名=已知列值"
sql_delete="delete from 表名 where 列名=列值"
try:
    c.executemany(sql_insert,zhi)
    c.execute(sql_delete)
    c.execute(sql_update)
  
    con.commit()
except Exception as e:
    print(e)
    con.rollback

c.execute(sql_select)
print(c.fetchall())

c.close()
con.close()

for row in c.execute("PRAGMA table_info('Item')"):
    print(row)
#pprint.pprint(c.fetchall())
lie=input("列名\n")
zhi=input("修改为\n")

sql_update='update Item set '+lie+'=\''+zhi+'\' where '+lie+' like \'%_%\''
c.execute(sql_update)#执行sql语句

sql_select='select '+lie+' from Item where '+lie+' like \'%_%\''
#for row in c.execute(sql_select):
# print(row)
#print(sql_update,'\n',sql_select)

--提交

设置自动提交：con.autocommit(true/false)#开/关
正常结束事务：con.commit()
异常结束事务：con.rollback()

string1 = "Now I am here."#文字居中
print string1.center( 50 )
print string1.rjust( 50 )
print string1.ljust( 50 )
'''
'''mysql语法
1、使用SHOW语句找出在服务器上当前存在什么数据库：

mysql> SHOW DATABASES;

2、创建一个数据库MYSQLDATA

mysql> CREATE DATABASE MYSQLDATA;

3、选择你所创建的数据库

mysql> USE MYSQLDATA; (按回车键出现Database changed 时说明操作成功！)

4、查看现在的数据库中存在什么表

mysql> SHOW TABLES;

5、创建一个数据库表

mysql> CREATE TABLE MYTABLE (name VARCHAR(20), sex CHAR(1));

6、显示表的结构：

mysql> DESCRIBE MYTABLE;

7、往表中加入记录

mysql> insert into MYTABLE values (”hyq”,”M”);

8、用文本方式将数据装入数据库表中（例如D:/mysql.txt）

mysql> LOAD DATA LOCAL INFILE “D:/mysql.txt” INTO TABLE MYTABLE;

9、导入.sql文件命令（例如D:/mysql.sql）

mysql>use database;

mysql>source d:/mysql.sql;
'''