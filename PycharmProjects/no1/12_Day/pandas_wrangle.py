import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key':['a','a','b','c','c','b','c'],'value':range(7)})

df2 = pd.DataFrame({'val':[12,7,9]},index=['a','b','d'])

print(pd.merge(df1,df2,left_on='key',right_index=True))