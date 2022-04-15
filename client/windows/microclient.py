from socket import *
import time

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.bind(('127.0.0.1',55002))
tcpCliSock.connect(('127.0.0.1',55001))

while True:
    data1 = '111111'

    tcpCliSock.send(data1.encode("utf-8"))
            
    data1 = tcpCliSock.recv(1024)
            

    print(data1.decode('utf-8'))

    time.sleep(1)