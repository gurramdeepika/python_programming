import pandas as pd

data = pd.read_csv("data.csv",header= None) #if not none by default it will take the first row as a header

print(data.head) #no header is mentioned in the file

data.columns = ['first','second','third','fourth','fivth']

print(data)

data1 = data.set_index("fivth")  # this column will come at the firstc

print(data1)

data2 = data.iloc[:,1:].values

print(data2) #matrix form