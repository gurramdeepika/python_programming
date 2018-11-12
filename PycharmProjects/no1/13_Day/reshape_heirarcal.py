import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key1':['mh','mh','mh','tn','tn'],
                    'key2':[2000,2001,2002,2001,2002],
                    'data':[3,2,5,6,9]})

df2 = pd.DataFrame(np.arange(12).reshape((6,2)),
                    index= pd.Index(['KL','tn','ka','ts','ap','mh'],name='state'),
                   columns=pd.Index(['event1','event2'],name='event'))

print(df2)

sdf2 = df2.stack()

print(sdf2)

print(sdf2.unstack(0))
print(sdf2.unstack('event')) #original way - sfd2 - unstack(1)
print(sdf2.unstack('state')) # unstack(0) is same as this statement

df3 = pd.Series([0,1,2,3,4,5], index= ['KL','tn','ka','ts','ap','mh'])
df4 = pd.Series([6,7,8,9], index=['KL','tn','ts','mh'])

data = pd.concat([df3,df4],keys=['one','two'])

print(data)

#print(data.stack()) # no stack and unstack for series
print('rename',df2.rename(index=str.lower,columns=str.title))
