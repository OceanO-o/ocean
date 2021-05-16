show database; ";"分号来语句划分
use 数据库名;   show tables; 查看所有的表
describe table_name; 查看表所有信息
create database name; 创建一个数据库
DDL 数据库 定义 语言
DML 数据库 操作 语言
DQL 数据库 查询 语言
DCL 数据库 控制 语言
1.操作数据库
    操作数据库-->操作数据库中的表-->操作数据库表中的数据
    操作数据库 create database if not exists school;
    删除数据库 drop database if exists school;
    使用数据库 use school;
    查看数据库 show database;
2.数据库列类型
    tinyint 1个字节 smallint 2个字节 int四个字节
    char 字符串0-255   varchar 可变字符串 0-65535  text 文本串,保存大文本
3.表建立
    字符串使用引号括起来，所有语句后加逗号，最后一个不用加
    CREATE TABLE IF NOT EXISTS `表名` (
    `字段名` 列类型 [属性 NOT NULL DEFAULT] [索引] [注释]， 
    `字段名` 列类型 [属性 NOT NULL DEFAULT] [索引] [注释]， 
    `字段名` 列类型 [属性 NOT NULL DEFAULT] [索引] [注释]
    )
    查看创建数据库,表的语句
    show create database school
    show create table student
    查看表结构
    desc student
4.数据库引擎
    innodb
    myisam
4.修改表
    修改表名  alter table old_name rename as new_name alter table teacher rename teacher1
    增加表字段 alter table table add 新字段名 列属性  alter table teacher1 add hobby varchar(20)
    修改表字段 alter table teacher modify hobby int(10) 修改约束
               alter table teacher change hobby hobby1 int(10) 字段重命名
    删除表字段 alter table teacher drop hobby
    删除表     drop table if exists teacher 
     
5.dml
    insert into `student` (`name`) values('zhang'), ('li') 一一对应， 可以多个values
    update 表名 set key1 = value1, key2 = value2  where  条件
    update student name="name1" where id=1
    where 条件 = < >  between and [2,5]在某个范围内 and or 
    删除 delete truncate都能清空一个数据库表，表的结构索引约束不会变
    相同点都能删除数据，都不会删除表结构，不同点，truncate重新设置自增列，不会影响事务。
    delete from 表名 where 条件
    delete from student where id =1
    truncate table student    
6.dql
    1.select查询语句
    简单查询 as 别名    select concat(姓名： name) as new_name from student as st可以这样作为一列最终输出
    去重 distinct 
    select distinct `student_num` from student
    数据库计算表达式
    select `student_score` +1 as '提分后' from student
    2.where 条件子句  逻辑运算 and not between
    3.模糊查询
    is null,  like,  between and, in, 
    like % _                      %（0到任意个字符） _ (一个字符)
    in()                           (里面一个或多个值)
    null 
    4.连表查询
    join(连接的表) on(连接条件)
    where 等值查询
    inner join   left join左表为准，即使右表没有  right join   自连接
    5.分页
    select [all | distinct] table.filed from table_name as table_alias
        [left join table_name1
        [where 
        [group by
        [having 过滤分组必须满足的条件
        [order by 
        [limit offset {row_count}指定查询从哪条记录到哪条     
    order by 通过哪个字段排序，怎么排
    order by name desc降序
    limit语法  limit 起始值，页面大小    (n-1)*pagesize, pagesize   n当前页 pagesize页大小
    6.嵌套查询，子查询
    7.函数
    聚合函数 count() sum() avg() max() min()
    8.索引
    主键索引  唯一索引   常规索引   全文索引    
    show index from student
    创建完表后增加索引 alter table school.student add fulltext index `name`(`name`);  增加全文索引
7.数据库备份
    先登录并进入数据库
    导出数据库表
    mysqldump -h 主机 -u 用户名  -p 密码 数据库 表名1    > 物理磁盘位置/文件名
    mysqldump -hlocalhost -uroot -p123   school student >          D:/a.sql
    导出多张数据库表
    mysqldump -h 主机 -u 用户名  -p 密码 数据库 表名1 表名2 表名3     > 物理磁盘位置/文件名
    导出数据库
    mysqldump -h 主机 -u 用户名  -p 密码 数据库     > 物理磁盘位置/文件名
    导入数据库表,切换到指定数据库中
    source d:/asql
    ui semantic ui      grabient         vue element admin      element    ant design pro 
8.三大范式
    1.列不可分
    2.每张表只做一件事情
    3.每一列数据都和主键直接相关，而不能间接相关
    规范性和性能关系
        关联查询不得超过三张表
        但考虑到商业化的需求，数据库性能更加重要
        故意给某些表增加冗余字段，从多表查询变为单表查询
        故意增加一些计算列，索引
        
        
        
        
        
        
        
        