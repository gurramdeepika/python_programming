import numpy as np
x,y = np.mgrid[1:6,10:14]
print(x)
print(y)
print(x.shape)
print(y.shape)

rand = np.random.rand(5,5)# between 0 and 1
print(rand)