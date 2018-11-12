import pandas as pd
import numpy as np

# df1 = pd.DataFrame({'key1':['mh','mh','mh','tn','tn'],
#                     'key2':[2000,2001,2002,2001,2002],
#                     'data':[3,4,5,6,9]})

df2 = pd.DataFrame(np.arange(12).reshape((6,2)),
                   index = [['tn','tn','mh','mh','mh','mh'],[2000,2000,2000,2000,2001,2002]],
                   columns=[['event1','event2'],['event3','event4']])


#print(df2)

df2.index.names = ['key1','key2']
df2.columns.names = ['state','year']

#print(df2.swaplevel('key1','key2'))
print(df2.sort_index(level=1)) # second index , default = 0
#print(df2.sum(level='key1'))

