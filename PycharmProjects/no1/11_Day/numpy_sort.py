import numpy as np

arr = np.array([4.5,2.3,6.7,1.2,1.8,5,5])
arr.sort()
print('sorted array',arr)

x = np.array([4.5,2.3,6.7,1.2,1.8,5,5])
s = x.argsort()
print('before sort',s)
np.sort(x)
print(np.sort(x))
print(x)

s = x.argsort()
print('after sort',s)
print('x[s]',x[s])

#singular matrix error ad-bc = 0
# arr = np.array([[3,2],[6,4]])
# print('inv',np.linalg.inv(arr))

#idempotent matric-- a*a = a
g = np.eye(2)
print("idempotent",g)

print("transpose",g.transpose())