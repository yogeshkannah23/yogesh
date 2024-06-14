import socket

s = socket.socket()

print("socket created")
s.bind(('localhost',9999))

s.listen(3)
print("waiting for the connections: ")

while True:
    c,addr = s.accept()
    print("connected with ",addr )
    c.send(bytes("welcome to the server",'utf-8'))
    print("Message recived from client " ,c.recv(1024).decode())
    c.close()

