# !/usr/bin/env python
# -*- codeing: utf-8 -*-

"""数据库连接模块
	__init__：初始化连接信息
	select(select_sql)：查找字段方法
	sql(insert_sql)：增、删、改数据
"""

import sqlite3#导入数据库模块
db='sb.db3'
class sql_conn:
	def __init__(self):
		try:
			self.db = sqlite3.connect(db)#打开数据库
			self.cursor = self.db.cursor()#创建游标
			print("数据库：%s"%(db))
		except:
			return '失败'
			print("错误：连接失败")

	def select(self, select_sql):#查询数据
		try:
			# 执行SQL语句
			self.cursor.execute(select_sql)
			# 获取所有记录列表
			results = self.cursor.fetchall()
			print(results)
			return results
		except:
			print("错误：查询失败")

	def sql(self, sql):#增、删、改数据
		try:
			self.cursor.execute(sql)# 执行sql语句
			self.db.commit()# 提交到数据库执行
		except:
			self.db.rollback()# 如果发生错误则回滚
			print("错误：操作失败")

	def close(self):
		self.db.close()

# 测试代码
test1 = sql_conn()

# 查找测试
# sql = "SELECT * FROM starbound"
# test1.select(sql)

# 增添测试
sql = "INSERT INTO starbound VALUES ('Mac', 'Mohan', 20, 'A','M', 2000,23)"
# 删除测试
#sql = "DELETE FROM starbound WHERE name = '%s'" % ('Mac')
# 更新测试
#sql = "UPDATE starbound SET synthesis =synthesis+1 WHERE name = '%s'" % ('Mac')
test1.sql(sql)

test1.close()