import numpy as np

a1 = np.array([12,-9,10,60.6,-13])
a2 = np.array([-6,17,5,12,-9])
print(a1)
print(type(a1))
print(a1.dtype)

if type(a1) is np.ndarray:
    print("An array")

if a1.dtype == np.int64:
    print('an array of numbers')

print('mul',a1*4)
print('div',a1/4)
print('add',a1+4)
print('mod',a1%4)
