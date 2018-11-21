from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import  Pipeline
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('wdbc.data',header=None)

x = df.loc[:,2:].values #all rows and from second column to end column

print(x)

y = df.loc[:,1].values

print(y)

le = LabelEncoder()

y = le.fit_transform(y)


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=1)

pipe_lr = Pipeline([('scl',StandardScaler()),
                    ('pca',PCA(n_components=4)),
                    ('clf',LogisticRegression(random_state=1,penalty='l1'))])

pipe_lr.fit(x_train,y_train)

print('Train Accuracy: %.3f'%pipe_lr.score(x_train,y_train))
print('Test Accuracy: %.3f'%pipe_lr.score(x_test,y_test))

y_pred = pipe_lr.predict(x_test)
print("Missclassified",(y_pred!=y_test).sum())
print('confusion matrix')

