-- SQLite
select name from sqlite_master where type='table' order by name
select * from starbound 
alter table 测试 add 性别 varchar(30) 
alter table tableName delete 性别
alter table 测试 alter column 年龄 char(5)
select * from 测试 where 时间>'2019-07-19'
CREATE TABLE 测试 (
自增长主键 INTEGER primary key AUTOINCREMENT,
姓名 char,年龄 int,时间 date
)
insert into 测试  values(null,'上海','松江','2019-07-19')
,(null,'上海','松江','2019-07-19')
,(null,'上海','松江','2019-07-19')
,(null,'上海','松江','2019-07-19')
,(null,'上海','松江','2019-07-19')
,(null,'上海','松江','2019-07-19')
,(null,'上海','松江','2019-07-19')
,(null,'上海','松江','2019-07-19')
,(null,'上海','松江','2019-07-19');
