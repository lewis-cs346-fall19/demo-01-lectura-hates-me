sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 17000)
sock.connect(addr)
for x in range(0,100):
    msg = "hello " + x
    sock.sendall(msg.encode())
    try:
        ans = sock.recv(1024).decode()
        print("The reply is: " + ans)
    except:
        sock.close()

