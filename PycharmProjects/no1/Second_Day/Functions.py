def s_math(x,y):
    '''
    hey hi math problem
    '''
    if type(x) is not int or type(x) is not float:
        x=15
    if type(y) is not int or type(y) is not float:
        y=15
    global a #if the variable is not declared globally then it will throw the runtime error

    x = 1.9/x + 8.1*y
    y = 7.6/x + 3.2*(1/2*y)
    a = 2.3 *(9/y + x/7.2)
    b = 5.6*x + 7/8*y
    return a+b
a,b = 4.63, 7.81
if __name__ == '__main__':
    print("Return value is", s_math(a,b))
    print('a is ', a)
    print('b is ', b)

#appending an element in a list
def a_list(lis,ele):

    lis.append(ele)
    print(lis)

lis=[1,2,3,4]
if __name__ == '__main__':
    a_list(lis,5)

#default arguments

def login(name, password, host='asterix'): # declare non-default parameters first and default parameters later
    print("welcome ",name)
    print("your password ",password)
    print("you are tyring with the host ", host)
if __name__ == '__main__':
    login('Deepika', 'i will not tell','my host')

#formal parameters used as actual/keyword parameters
def myfun(a,b,c=10):
    print(a-b+c)
if __name__ == '__main__':
    myfun(1,2,3)
    myfun(c=90,a=1,b=3)
    myfun(2,c=34,b=67)
    myfun(5,b=2)#first values and later the actual parameters

#variable parameter
def varargs(*args):
    print(args[0])
    print(args) # will print as a tuple / print like a raw string
if __name__ =='__main__':
    varargs('s','g')
    varargs(1,2,3)

#keyword with  non-keyword variable arguments
def varnkey(*args, **kwargs):
    print('non-keywords =>',args)#o/p in tuple format
    print('keywords =>',kwargs) #o/p in dictionay format
if __name__ == '__main__':
    varnkey(1,2,3)
    varnkey(c=1,a=1,d=1)
    varnkey(1,6,8,a=3,v=5)

#Functions inside a function / call back functions

def square(x):
    print(x*x)
def applier(q,x):
     q(x)
applier(square,7)

def double(x):
    print(2*x)
applier(double,2)

#higher order function
import inspect
def applier2(q,x,y):

    if '__code__' in dir(q):
        print(inspect.isfunction(q))
        return q(x,y)
def myadd(x,y):
    return x+y
print(applier2(myadd,4,5))



