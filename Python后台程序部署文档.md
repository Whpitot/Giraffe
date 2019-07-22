* 编写人：黄永超
* 编写时间：2018-08-25
  
## Python后台程序部署文档
---
### 1、构建虚拟环境
新建项目文件夹giraffe, 进入文件夹中安装虚拟环境venv  
    `mkdir giraffe`  
    `virtualenv venv`  

在giraffe中会自动建立一个venv的文件，进入当前虚拟环境  
`source venv/bin/activate`

### 2、安装uwsgi并配置
在虚拟环境中安装uwsgi  
`pip install uwsgi`

创建配置uwsgi配置文件  
`vim uwsgi.ini`

编辑配置文件uwsgi.ini  
```
[uwsgi]
# uwsgi 启动时所使用的地址与端口
socket = 127.0.0.1:8001 

# 指向网站目录
chdir = /home/girafee/ 

# python 启动程序文件
wsgi-file = run.py 

# python 程序内用以启动的 application 变量名
callable = app 

# 处理器数
processes = 4

# 线程数
threads = 2

#状态检测地址
stats = 127.0.0.1:9191
```