
#connectionless server and client communication
#will send and recieve the packets
#as the listen is not present because of connectionless concept
# then the stack in upd will handle the queue of systems request to one udp server
#sockets using are transport layer interface sockets

import socket

#udp server
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("localhost",10000))

while True:

    data , addr = s.recvfrom(20)
    resp = b"get off my lawn"
    s.sendto(resp.upper(),addr)

