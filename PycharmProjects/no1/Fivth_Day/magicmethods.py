class A(object):  # -> don't forget the object specified as base

    def __new__(cls):
        print("A.__new__ called")
        return super(A, cls).__new__(cls)

    def __init__(self):
        print( "A.__init__ called" )

A()

class Test(object):
    def __getitem__(self, items):
        print('%-15s  %s' % (type(items), items))

t = Test()
t[1]
t['hello world']
t[1, 'b', 3.0]
t[5:200:10]
t['a':'z':3]
t[object()]