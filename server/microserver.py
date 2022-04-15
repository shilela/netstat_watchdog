from socket import *
from threading import Thread

def data_handler(client,addr):
    while True:
        req = client.recv(1024)
        if not req:
            break
        message = req.decode('utf-8')
        resp="Successful!Bye!".encode("ascii") + b'\n'
        client.send(resp)
        print(client)


sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(('127.0.0.1',55001))
sock.listen(5)
while True:
    client, addr = sock.accept()
    print('a')
    Thread(target=data_handler, args=(client, addr,), daemon=True).start()


