import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 17000)
sock.connect(addr)
for x in range(0,100):
    msg = "hello " + str(x)
    try:
        sock.sendall(msg.encode())
        ans = sock.recv(1024).decode()
        print("The reply is: " + ans)
    except:
        print("client closed")
        sock.close()
print("client closed")
sock.close()