
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#upd client

msg = b"Hello world"
s.sendto(msg,("localhost",10000))
data,addr = s.recvfrom(20)
print(data)
