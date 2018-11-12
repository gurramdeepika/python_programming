import pandas as pd

data = pd.DataFrame({'k1':['one']*3+['two']*4,
                     'k2':[1,1,2,3,3,4,4]})

# print(data.duplicated('k1'))
# print(data.drop_duplicates('k1')) # will not change the actual object
data.drop_duplicates('k1',inplace=True) #will change in the actual object

print(data.get('k2'))
print(data.get('k1'))



