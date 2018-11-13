from sklearn.preprocessing import Imputer
import pandas as pd

df = pd.read_csv('sample.csv',header=None)
imr = Imputer(missing_values='NaN',strategy='mean',axis=0) # 0 - depends on column, 1- depends on row
imr = imr.fit(df)
imputed_data = imr.transform(df.values)

print(imputed_data) # will not consider the missing number in the total count