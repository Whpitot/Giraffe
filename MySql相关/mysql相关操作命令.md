* 编写人：黄永超
* 编写时间：2018-08-25    

## MySql相关命令
---
### 1、登陆服务模块
mysql登陆  
`mysql -u root -p `

带有地址和端口的登陆  
`mysql -h 127.0.0.1 -P 3308 -u root -p`

还原数据库  
`mysql -h 127.0.0.1 -P 3308 -u root -p123456 [database_name] <  backupfile.sql`

指定字符集还原数据库  
`mysql -h 127.0.0.1 -P 3308 -u root -p --default-character-set=utf8 app_dev < D:\Database\dev_master_9807_1771421_all_sql\1771421_all.sql`

查询数据库文件编码格式  
`use [database]`  
`show variables like character_set_database'`   //显示如utf8、latin1等


### 2、数据操作模块

显示所有数据库  
`show databases;`

创建一个数据库  
`create database [database_name]` 

创建utf8格式的数据库  
`create database [database_name] default character set utf8 collate utf8_general_ci;`

切换到某一数据库  
`use [database_name]`   

显示所有表    
`show tables` 

### 3、mysql服务相关

查看服务状态  
`service mysql status`

停止服务  
`service mysql stop`

启动服务  
`service mysql start`

windows下重启服务  
`services.msc` 然后找到对应的服务
