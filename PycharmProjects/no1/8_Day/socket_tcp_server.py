import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.bind(("",9000))
s.bind(("localhost",9001))
s.listen(5) # s is only used to listen and bind ,
# 5 is nothing but the waiting state in a queue by systems to socket and the remaining are rejected
print(socket.gethostbyname("www.google.com"))
while True:
    c, a = s.accept() # a is a tuple ,c is duplicate socket
    print("Received connection from",a)
    c.send(b"Hello"+bytes(a[0],"utf-8"))
    c.close()
