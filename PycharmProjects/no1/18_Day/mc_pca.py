from numpy import array
from sklearn.decomposition import PCA

a = array([[1,4],[3,2],[5,9]])
print(a)

pca =PCA(2) #creating two features(columns)

pca.fit(a)

#acess values and vectors
print(pca.components_)
print(pca.explained_variance_)

#transform data
b = pca.transform(a)
print(b)

