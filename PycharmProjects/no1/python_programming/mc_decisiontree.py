from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.preprocessing import StandardScaler
df_wine = pd.read_csv('wine.data',header=None)
y = df_wine.iloc[:,0].values
x = df_wine.iloc[:,1:].values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

sc = StandardScaler()
x_train_std = sc.fit_transform(x_train)
x_test_std = sc.transform(x_test)

lr = DecisionTreeClassifier(max_depth=15)
lr.fit(x_train_std,y_train)

y_pred = lr.predict(x_test_std)
#y_train_pred = lr.predict(x_train)

print("misclassified in testing",(y_test-y_pred).sum())
#print("misclassified in training",(y_train-y_train_pred).sum())

