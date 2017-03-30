#_*_coding:utf-8 _*_
__author__ = 'sylar'


import SocketServer
import os

class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        base_path = 'temp'
        conn = self.request
        print 'connected...'
        while True:
            pre_data = conn.recv(1024)
            cmd,file_name,file_size = pre_data.split('|')#获取请求方法
            recv_size = 0 #已接收文件大小
            file_dir = os.path.join(base_path,file_name) #上传文件路径拼接
            f = file(file_dir,'wb')
            flag = True
            while flag:
                if int(file_size) > recv_size:#未上传完
                    data = conn.recv(1024)  #每次最大接收1024
                    recv_size+=len(data)
                    f.write(data)
                else:#上传完成就清除标记
                    recv_size = 0
                    flag = False
            print 'upload successed.'
            f.close()

instance = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
instance.serve_forever()