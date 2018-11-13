from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

df_wine = pd.read_csv('wine.data',header=None)

df_wine.columns = ['class label','alcohol','malic acid','ash','alcalinity of ash','Magnesium',
                   'Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins',
                   'Color intensity','Hue','OD280/OD315 of diluted wines','Proline' ]
print(df_wine)
y = df_wine.iloc[:,0].values
x = df_wine.iloc[:,1:].values
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

lr = LogisticRegression(penalty='l1',C=0.1) # l1 - linear , l2 - quadratic
print(lr.fit(x_train,y_train))

sc = StandardScaler()
x_train_std = sc.fit_transform(x_train)
x_test_std = sc.transform(x_test)

# print('training accuracy:',lr.score(x_train_std,y_train)) #train should be more than test
# print('test accuracy',lr.score(x_test_std,y_test))
cf = lr.coef_

#c = 1/lambda(T) c - increases variance means over fitting, if increses t inncreses bias and under fitting
colors = ['blue','green','red','cyan','magenta','yellow','black','pink',
          'lightgreen','lightblue','gray','indigo','orange']

weights,params = [],[]

for c in np.arange(-4.,6.):
    lr = LogisticRegression(penalty='l1',C=10.**c,random_state=0)
    lr.fit(x_train_std,y_train)
    weights.append(lr.coef_[1])
    params.append(10.**c)

print(weights)
print('training accuracy:',lr.score(x_train_std,y_train)) #train should be more than test
print('test accuracy',lr.score(x_test_std,y_test))

weights = np.array(weights)

for column,color in zip(range(weights.shape[1]),colors):
    plt.plot(params,weights[:,column],
             label = df_wine.columns[column+1],
             color = color)
plt.axhline(0,color= 'black',linestyle='--',linewidth=3)
plt.xlim([10**(-5),10**5])
plt.ylabel('weight coefficient')
plt.xlabel('C')
plt.xscale('log')
plt.legend(loc='upper left')
plt.show()