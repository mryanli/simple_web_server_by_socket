#!/usr/bin/python
# -*- coding:UTF-8 -*-

from socket import *
import os



class MyServer():
    base_dir = os.path.dirname(__file__)

    def __init__(self,host_port):
        self.head='HTTP/1.1 200 OK\r\n\r\n'.encode()
        self.sc = sc = socket()
        sc.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        sc.bind(host_port)
        sc.listen(1)


    def serve_forever(self):
        while True:
            print('listenning..')
            self.conn,self.addr = self.sc.accept()
            request =self.conn.recv(1024).decode()
            if not request: #若请求为空，则不处理，继续监听
                continue
                self.conn.close()
            self.handle_request(request)  #处理请求
            self.conn.close() #关闭连接

    def handle_request(self,request):
        first_line = request.splitlines()[0] #拿到HTTP请求报文的第一行
        first_line = first_line.rstrip('\r\n') #去掉第一行末尾的换行符
        print('first_line:',first_line)
        #保存请求的方法、路径、版本
        self.req_method,self.req_path,self.req_version = first_line.split()
        #针对请求路径进行响应
        self.response(self.req_path)

    #响应请求函数
    def response(self,path):
        if path == '/':
            path = '/js1.html'
        self.file_response(path)

    #针对不同的请求文件，响应不同的请求内容
    def file_response(self,path):
        file_path = self.base_dir + path
        print('file_path:',file_path)
        try:
            with open(file_path,'rb') as f:
                file = f.read()
            self.conn.sendall(self.head+file)
        except:
            file = 'file wrong'.encode()
            self.conn.sendall(self.head + file)


if __name__ == '__main__':
    myserver = MyServer(('127.0.0.1',8080))
    myserver.serve_forever()

