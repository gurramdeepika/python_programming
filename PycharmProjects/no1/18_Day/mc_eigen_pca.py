#principle component analysis

from numpy import array,mean,cov
from numpy.linalg import eig

a = array([[1,2],[3,4],[5,6]])

print('a is')
print(a)

m = mean(a.T,axis=1) #calculate mean of each column

print(' m is')

print(m)

c = a-m #center columns by subtracting colum means

print(c)
print('c.T is')
print(c.T)

v = cov(c.T) #calculate covariance matrix of centered matrix

print(' v is')
print(v)

values, vectors = eig(v) #eigen decomposition of covariance matrix

print('vectors are')
print(vectors)

print('values are')
print(values)

p = vectors.T.dot(c.T)

print(' p.T is')
print(p.T)

