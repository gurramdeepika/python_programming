import pickle
import socket
# import Student_Details as picstu
#
# name = input('enter the name of the student')
# rollno = input('enter the rollno of the student')
#
# stu = picstu.Student(name,rollno)

def pickle_data(obj):
    puckdump = pickle.dumps ( obj)
    return puckdump

def receive_from_server(obj ):
    p = pickle_data(obj)
    sock = socket.socket ( socket.AF_INET , socket.SOCK_STREAM )
    server_address = ('localhost' , 10000)
    sock.connect ( server_address )
    sock.send(p)
    data,addr = sock.recvfrom ( 200 )
    data = data.decode('utf-8')
    return data



# if __name__ == '__main__':
#
#     name = receive_from_server()
#
#     print('Recived the capitalized name from the server',name)