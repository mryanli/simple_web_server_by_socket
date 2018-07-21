# simple_web_server_by_socket
用python的socket模块实现的简单web本地服务器，可实现以文件路径形式的url解析，并返回相应路径下的html文件，若html中含有css，js，image文件的链接，浏览器会自动请求该服务器文件，服务器同样按照路径返回文件，浏览器加载。


运行环境：python 3.6.4

使用方法，在python环境下，运行 myserver.py  默认监听地址：端口是：127.0.0.1：8080

url格式：127.0.0.1:8080/html/***.html



