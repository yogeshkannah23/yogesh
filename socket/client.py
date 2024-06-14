import socket

c = socket.socket()

c.connect(('localhost',9999))
print(c.recv(1024).decode())
print("connected")

c.send(bytes("hi server",'utf-8'))