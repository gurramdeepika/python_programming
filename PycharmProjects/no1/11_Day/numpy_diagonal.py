import numpy as np

daigonal = np.diag([1,2,3])
print("daigonal is",daigonal)

b = np.zeros(5)
print('b is',b)
print(b.dtype)

n = 10
my_int_array = np.zeros(n,dtype=np.int)# by default float
print("my int array is", my_int_array)
print(my_int_array.dtype)

c = np.ones((3,3))#or ([3,3])
print('c is',c)

print(c * 4.0)