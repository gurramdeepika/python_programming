import socket
s = socket.socket ( socket.AF_INET , socket.SOCK_STREAM )
s.bind ( ("localhost" , 10000) )
s.listen ( 5 )
while True:
    c , a = s.accept ( )
    data = c.recv(10000)
    print ( "Received connection from" , a )
    c.send ( data.upper()  + bytes ( a[ 0 ] , "utf-8" ) )
    c.close ( )