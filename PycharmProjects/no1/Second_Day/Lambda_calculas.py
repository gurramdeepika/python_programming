def applier(q,x):
   return q(x)

def applier1(q, x,y):
    return q(x,y)

print(applier(lambda x:x*x,5))
print(applier1(lambda x,y:x+y,4,5))
print(applier.__code__.co_argcount)
print(applier.__code__.co_nlocals)
print(applier.__code__.co_varnames)

def myfun(n):
    return lambda x:n+x
f1 = myfun(5)
f2 = myfun(40)
print(f1(6), f2(0))
ie = myfun('http://')
cr = myfun('https://')
print(ie('www.google.com') ,'\n',cr('www.google.com'))

#map and filter -- which reduces the use of loops

def square(x):
    return x * x
def even(x):
    return 0 == x%2

print('list of a map',list(map(square,range(10,20))))
print('list of a filter', list(filter(even,range(10,20)))) # int's subclass in bool

print('map with filter', list(map(square,filter(even,range(10,20)))))

#bool is the subclass of int
print(issubclass(bool,int))

#adding three list using lambda

sem1 = [12,13,14,15,16]
sem2 = [10,9,8,7,6]
sem3 = [10,11,12,13,14]
print('sum of three matrices ',list(map(lambda x,y,z:x+y+z,sem1,sem2,sem3)))

#reduce function fron funtools

from functools import reduce

print('using reduce',reduce(lambda x,y:x+y,sem1))

#conctenation of string using list and reduce
url='http://www.google.com'
url = list(url)
url.insert(4,'s')
print(reduce(lambda x,y:x+y,url))

#zip function

print('using zip in list ',list(zip(sem1,sem2))) #tuple format

print('using zip in dict ',dict(zip(sem1,sem2))) # dictionary format

print(list(reversed(sem1))) # will not change sem1
print(sem1)
sem1.reverse()
print(sem1) # will change sem1