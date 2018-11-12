class mydecorator:
    def __init__(self,f):
        print("a logging is about to start")
        f()
    def __call__(self):
        print("Done")

@mydecorator
def myfunct():
    print("the function called")
myfunct()

@mydecorator
def myfunc1():
    print("second funtion called")
myfunc1()

#closure(decorater can act as a closure)
def entryExit(f):
    def new_f():
        print("Entering",f.__name__)
        f()
        print("Exited",f.__name__)
    return new_f

@entryExit
def func1():
    print("inside func1")

func1()
