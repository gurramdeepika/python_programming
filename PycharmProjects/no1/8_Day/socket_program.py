import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #adressname-net/net6,type -- tcp/upd
s.connect(("www.python.org",443)) #connect
s.send(b"GET /index.html HTTPS\1.0\n\n") # send request
data = s.recv(10000)#get response, 10000---no.of bytes
print(data)
s.close()

# http-tcp
# https-udp
#for all website - 80
#for security,the port is 443
