import numpy as np

a = np.arange(4.0)
print('a is',a)
b = a*23.4
c = b/(a+1)
c+=10
print("c is",c)

arr = np.arange(100,200)
select = [5,25,50,75,-5]
print("arr is",arr[select])

arr = np.arange(10,20)
div_by_3 = arr%3 == 0
print("div_by_3",div_by_3)
print("arr [div_by_3]",arr[div_by_3])

arr = np.arange(10,20).reshape((2,5))
print("reshaped array",arr)

print("arr sum",arr.sum())
print("arr mean",arr.mean())
print("arr std",arr.std())#standard deviation (sigma)
print("arr max",arr.max())
print("arr min",arr.min())
print("div_by_3 all",div_by_3.all())
print("div_by_3 any",div_by_3.any())
print("div_by_3 sum",div_by_3.sum())
print("div_by_3 non-zero",div_by_3.nonzero())