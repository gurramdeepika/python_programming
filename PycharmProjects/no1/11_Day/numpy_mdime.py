import numpy as np

a34 = np.array([[12,10,-21,7],[-17,18,19,16],[13,-7,-18,10]])

print(a34)
print(a34.size)# no.of values
print(a34.shape)#n*m
print("second row is",a34[1])
print("second column is",a34[:,1])
print(a34[1,2])
print(a34[1,1:3])
