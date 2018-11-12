import _thread
x = 0
def inc_x(inc):
    global x
    x = x + inc

def print_x(val):
    global x
    print( x + val)

_thread.start_new_thread(print_x,(5,))
print(_thread.start_new_thread(inc_x,(8,)))


while 1:
    pass