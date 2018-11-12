import socket

s = socket.socket(socket.AF_PACKET,socket.SOCK_DGRAM)
s.bind(("eth0",0x0800))
while True:
    msg,addr = s.recvfrom(4096)