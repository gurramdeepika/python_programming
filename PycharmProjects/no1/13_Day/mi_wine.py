import pandas as pd

#other than csv to add the space '/s' is used
df_wine = pd.read_csv(r'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header = None)

df_wine.columns = ['Type','Alcohol','Malic acid','Ash',
                   'Alcalinity of ash','Mg','TOtal Phenols',
                   'Flavnoids','NonFlavanoid Phenols',
                   'Proanthocyanins','color intensity','Hue',
                   'OD280/OD315 of diluted wines','proline']

# print(df_wine.head()) # will return first five rows and 14 columns

# data = df_wine[1:]
# print(data)

data = df_wine.iloc[:,1:].values #index name -- values

print(data)