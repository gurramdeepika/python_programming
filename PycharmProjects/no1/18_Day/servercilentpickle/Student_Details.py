import file_client as cl

class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def stu( self ):
        return cl.receive_from_server ( self )

