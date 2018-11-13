from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

df_wine = pd.read_csv('wine.data',header=None)
y = df_wine.iloc[:,0].values
x = df_wine.iloc[:,1:].values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

lr = LogisticRegression(penalty='l1',C=10.0)
print(lr.fit(x_train,y_train))

y_pred = lr.predict(x_test)
y_train_pred = lr.predict(x_train)

print("misclassified in testing",(y_test-y_pred).sum())
print("misclassified in training",(y_train-y_train_pred).sum())

