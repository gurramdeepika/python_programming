class delete:
    # def __init__(self):
    #     print('entered in to  the init method')

    def hello( self ):
        print("helloworld")
    def __del__(self):
        print('destructor entered')

# d = delete()
# df = d.hello
# del d it will hold and  not delete
#del d1 it will delete the object

#del d automatic call for __del__ after execute complete

#weakref