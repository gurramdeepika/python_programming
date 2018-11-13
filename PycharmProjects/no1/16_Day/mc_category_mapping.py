import pandas as pd

df = pd.DataFrame([['green','M',10.1,'class1'],['red','L',13.5,'class2'],['blue','XL',15.3,'class1']])

print(df)

df.columns = ['color','size','price','classlabel']

size_mapping = {'XL':3,'L':2,'M':1}

df['size'] = df['size'].map(size_mapping)

print(df)

inv_size_mapping = {v: k for k,v in size_mapping.items()}

print(inv_size_mapping)

#label mapping

import numpy as np

class_mapping = {label:idx for idx,label in enumerate(np.unique(df['classlabel']))}

print(class_mapping)

df['classlabel'] = df['classlabel'].map(class_mapping)

print(df)

#label encoder

# color in digit -- based on alphabetical order
from sklearn.preprocessing import LabelEncoder

x = df[['color','size','price']].values
color_le = LabelEncoder()
x[:,0] = color_le.fit_transform(x[:,0])
print(x)

#one-hot encoder

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(categorical_features=[0]) #0 -- column, 1 -- row
print(ohe.fit_transform(x).toarray())