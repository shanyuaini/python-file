#_*_coding:utf-8 _*_
__author__ = 'sylar'
import SocketServer
import os

class MyServer(SocketServer.BaseRequestHandler):
    def setup(self):
        pass
    def handle(self):
        base_path = 'temp'
        conn = self.request
        print 'connected...'


        while True:
            pre_data = conn.recv(1024)#获取请求方法,文件名,文件大小
            cmd,file_name,file_size = pre_data.split('|')
            recv_size = 0 #已接收文件的大小
            file_dir = os.path.join(base_path,file_name)#上传文件路径拼接
            f =file(file_dir,'wb')
            flag = False
            while flag:
                if int(file_size)>recv_size:#未上传完成
                    data = conn.recv(1024)
                    recv_size+=len(data)
                else:#上传完毕退出循环
                    recv_size = 0
                    flag = False
                f.write(data) #写入文件
            print 'upload successed'
            f.close()
        conn.close()


    def finish(self):
        pass
if __name__ == '__main__':
    instance = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    instance.serve_forever()