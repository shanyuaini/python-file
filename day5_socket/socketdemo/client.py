#_*_coding:utf-8 _*_
__author__ = 'sylar'


import socket
client = socket.socket()
ip_port = ('127.0.0.1',9999)
client.connect(ip_port)
while True:
    data = client.recv(1024)
    print data
    inp = raw_input('发送信息:')
    client.send(inp)
    if inp == 'exit':
        break