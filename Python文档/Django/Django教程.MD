参考文献：http://www.cnblogs.com/feixuelove1009/p/5823135.html

# Django快速参考

##  0.MTV模型

![](images\afc7bff9.png)

## 1.安装Django

sudo apt install python3-pip

pip3 install django

添加到系统环境变量中(win)

## 2.创建Django项目

file-->new project-->Django-->mysite

![](images/1_目录结构.png)

templates目录存放html文件，MTV中的T

![](images/2_配置文件.png)

> 命令行：django-admin startproject mysite

## 3.创建APP

python manage.py startapp cmdb

创建了一个叫做cmdb的APP，django自动生成“cmdb”文件夹

> 命令行：django-admin startapp cmdb

## 4.编写路由

![](images/4_路由文件.png)
> urls.py, 将URL关联到views.py

## 5.编写业务处理逻辑

![](images/5_业务处理逻辑.png)
> views.py，让系统响应指定字符串

## 6.运行Web服务

![](images/6_1_编辑配置.png)

![](images/6_2_运行Web服务.png)
> 或 python manage.py runserver 127.0.0.1:8000

![](images/6_3_打开网页.png)

## 7.返回HTML文件

![](images/7_1_添加index.png)
> index.html，用作网页显示

![](images/7_2_修改views.png)
> views.py，让系统响应index.html文件

![](images/7_3_修改settings.png)
> 关联html目录, 默认不修改

## 8.使用静态文件

![](images/8_1_静态目录.png)
> 静态目录static, 用于存放CSS,JS,插件

![](images/8_2_配置settings.png)
> settings.py, 关联静态目录

![](images/8_3_index中引入.png)
> index.html,引入js文件

## 9.接收用户发送的数据

![](images/9_1_index表单.png)
> index.html，加入表单

![](images/9_2_修改views.png)
> views.py，接收网页数据

![](images/9_3_设置settings.png)
> settings.py，关闭保护机制

![](images/9_4_刷新浏览器.png)
> 浏览器

## 10.返回动态页面

![](images/10_1_改造views.png)
> views.py，数据中转站

![](images/10_2_改造index.png)
> index.html，动态显示数据

## 11.使用数据库

![](images/11_1_注册app.png)
> settings.py, 注册app

![](images/11_2_数据库配置.png)
> settings.py, 配置数据库，这里不修改

![](images/11_3_编辑models.png)
> models.py, MTV中的M

![](images/11_4_创建表.png)
> 通过2条命令创建数据库的表

> python manage.py makemigrations

> python manage.py migrate

![](images/11_5_修改views.png)
> views.py, 关联数据库

(完)
