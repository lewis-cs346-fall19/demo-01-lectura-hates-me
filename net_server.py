import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("0.0.0.0", 17000)
sock.bind(addr)
sock.listen(5)
while True:
    (connectedSock, clientAddress)=sock.accept()
    try:
        msg=connectedSock.recv(1024).decode()
        print("Here's the data: " +msg)
        sock.sendall(msg.encode())
    except ConnectionAbortedError:
        sock.close()