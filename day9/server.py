#_*_coding:utf-8 _*_
__author__ = 'sylar'

import socket

def handle_request(client):
    buf = client.recv(1024)
    client.send('http/1.1 200 OK\r\n')
    client.send('content-Type:text/html\r\n\r\n')
    client.send(u'<h2> Hello Sylar')
def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8080))
    sock.listen(5)
    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()