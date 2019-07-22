* 编写时间：2018-08-25
* 编写人：黄永超

## MySql安装及基本使用
---
### 1、Installing MySQL with APT
Install MySQL by the following command:  
`sudo apt-get install mysql-server`  

This installs the package for the MySQL server, as well as the packages for the client and for the database common files.  

During the installation, you are asked to supply a password for the root user for your MySQL installation.

### 2、Starting and Stopping the MySQL Server
The MySQL server is started automatically after installation. You can check the status of the MySQL server with the following command:  
`sudo service mysql status`

Stop the MySQL server with the following command:  
`sudo service mysql stop`

To restart the MySQL server, use the following command:  
`sudo service mysql start`