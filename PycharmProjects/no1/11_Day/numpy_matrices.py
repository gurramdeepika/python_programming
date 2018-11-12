import numpy as np


a = np.array([[1,2],[3,4]])

m = np.mat(a) # convert 2-d np.array to np.matrix
m = np.matrix([[1, 2], [3, 4]])
print(a[0])

# result is 1-dimensional
np.array([1, 2])
print(m[0])

# result is 2-dimensional
np.matrix([[1, 2]])
print(a*a)

# element-by-element multiplication
np.array([[ 1, 4], [ 9, 16]])
print(m*m)

# (algebraic) np.matrix multiplication
np.matrix([[ 7, 10], [15, 22]])
print(a**3)

# element-wise power
np.array([[ 1, 8], [27, 64]])
print(m**3)

# np.matrix multiplication m*m*m
np.matrix([[ 37, 54], [ 81, 118]])
print(m.T)

# transpose of the np.matrix
np.matrix([[1, 3], [2, 4]])
print(m.H)

# conjugate transpose (differs from .T for complex matrices)
np.matrix([[1, 3], [2, 4]])
print(m.I)

# inverse np.matrix
np.matrix([[-2. , 1. ], [ 1.5, -0.5]])