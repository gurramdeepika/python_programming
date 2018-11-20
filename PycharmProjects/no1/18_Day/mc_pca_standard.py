from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# df_wine = pd.read_csv('/home/cisco/PycharmProjects/no1/17_Day/wine.data',header=None)
# y = df_wine.iloc[:,0].values
# x = df_wine.iloc[:,1:].values

iris = load_iris()
x = iris.data[:150]
y = iris.target[:150]

print(x)
print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

sc = StandardScaler()
x_train_std = sc.fit_transform(x_train)
x_test_std = sc.transform(x_test)

pca = PCA(n_components=2)
print('Standardised data',x_train_std)

x_train_pca = pca.fit_transform(x_train_std)
x_test_pca = pca.transform(x_test_std)

print('principal data',x_train_pca)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(penalty='l1',C=1.0)
lr.fit(x_train_pca,y_train)

y_pred = lr.predict(x_test_pca)

y_train_pred = lr.predict(x_train_pca)

print("misclassified in testing",(y_test-y_pred).sum())
print("misclassified in training",(y_train-y_train_pred).sum())




