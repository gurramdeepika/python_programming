import socket
import pickle



def send_to_client():
    s = socket.socket ( socket.AF_INET , socket.SOCK_STREAM )
    s.bind ( ("localhost" , 10000) )
    s.listen ( 5 )
    while True:
        c , a = s.accept ( )
        print ( "Received connection from" , a )
        data = c.recv(10000)
        stu5=pickle.loads ( data )
        name = stu5.name.upper()
        c.send ( bytes(name,'utf-8') )
        c.close ( )

if __name__ == '__main__':
    send_to_client()