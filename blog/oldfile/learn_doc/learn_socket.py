#_*_coding:utf-8 _*_
__author__ = 'sylar'

import socket
'''
常用方法
###bind 绑定套接字和地址,
###listen 挂起的最大连接数
###accpet 等待接受连接并返回客户端对象和套接字(conn,address),conn是新建立连接的对象,
可以用来接收和发送数据,address是连接的客户端地址.accpet接收一个连接后会阻塞
###connect(address) 连接到address处的套接字,address格式为元组(hostname,port),如果连接出错,返回socket.error错误
###connect_ex(address) 通商,只不过会有返回值,连接成功返回0.连接失败返回编码,
###close 关闭套接字
###recv(bufsize,[flag]) 接受套接字的数据,数据以字符串形式返回,bufsize指定要接受的最大数据量,flag提供有关消息的其它信息,可以忽略
###recvfrom(bufsize,[flag])与recv()类似,但返回值是(data,address).data是包含接收数据的字符串,address是发送方的套接字地址
###send(string,[flag])将string数据发送到连接的套接字,返回值是要发送的字节数量,该数量可能小雨string的字节大小
###sendall(string,[flag]) 同send,但返回之前会尝试发送所有数据,成功返回none,失败则抛出异常
###sendto(string,[flag],address) 将数据发送到套接字,address为元组(ip,port)指定地址,返回值是发送的字节数,主要用于UDP协议
###settimeout(timeout)设置套接字操作的超时时间,timeout是个浮点数,单位是秒.none表示没有超时时间,超时应该在刚创建套接字时设置
因为他们可能用于连接的操作(如connection())
###getpeername() 返回连接套接字的远程地址,返回值通常是元组(ip,port),客户端
###getsockname() 返回套接字自己的地址.通常是一个元组(ip,port),服务端的
###fileno() 套接字的文件描述符
'''

def handle_request(client):#将客户端对象传入
    buf = client.recv(1024)  #接收客户端数据
    client.send('HTTP/1.1 200 OK\r\n\r\n')#返回的数据
    client.send('Hello,world')#返回数据
def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建socket对象
    '''
    参数一:地址簇
    socket.AF_INET IPv4  默认
    socket.AF_INET6 IPv6
    socket.AF_UNIX 只能够用于单一的Unix系统进程间通信
    参数二:常用数据类型
    socket.SOCK_STREAM  流式数据,for TCP  默认
    socket.SOCK_DGRAM  数据报式socket for UDP
    参数三:协议:
    0 (默认)与特定地址家族相关的协议,如果是0系统会根据地址格式和套接类别,自动选择合适的协议
    '''
    sock.bind(('localhost',8080))  #监听地址端口
    sock.listen(5)  #最大接收连接数
    while True:
        connection,address = sock.accept() #等待请求,有请求就阻塞
        handle_request(connection)  #调用handle处理,connection是客户端对象
        connection.close()#发送完成就关闭连接

'''
if __name__ == '__main__':
    main()
'''

'''
异步和多线程模块SocketServer



'''
import SocketServer
class MyServer(SocketServer.BaseRequestHandler):
    def setup(self):
        pass
    def handle(self):
        print self.request,self.client_address,self.server
        #self.request = socket

    def finish(self):
        pass
if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    server.serve_forever()








