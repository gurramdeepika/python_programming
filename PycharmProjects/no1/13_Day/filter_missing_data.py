import pandas as pd

data = pd.Series([1,None,3.5,None,7])
print(data.dropna())

print(data[data.notnull()])

data = pd.DataFrame([[1.0,6.5,3.0],[1.0,None,None],[None,None,None],[None,6.5,3.0]])

print(data.dropna()) # delete wherever none is present
print(data.dropna(how='all')) # delete only if the complete row in none