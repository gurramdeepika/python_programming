import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key1':['mh','mh','mh','tn','tn'],
                    'key2':[2000,2001,2002,2001,2002],
                    'data':[3,4,5,6,9]})

df2 = pd.DataFrame(np.arange(12).reshape((6,2)),
                   index = [['tn','tn','mh','mh','mh','mh'],[2000,2000,2000,2000,2001,2002]],
                   columns=['event1','event2'])


print(df2)

print(df2.loc['mh'].loc[2000])

print(pd.merge(df1,df2,left_on=['key1','key2'],right_index=True))