import sys
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("0.0.0.0", 17000)
sock.bind(addr)
sock.listen(5)
(connectedSock, clientAddress)=sock.accept()
while True:
    msg=connectedSock.recv(1024).decode()
    if msg!='':
        print("Here's the data: " +msg)
        connectedSock.sendall(msg.encode())
    else:
        print('Server closed')
        connectedSock.close()
        break