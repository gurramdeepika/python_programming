import pandas as pd
import numpy as np

# arr = np.arange(12).reshape((3,4))
# print(np.concatenate([arr,arr],axis=1))

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
print(pd.concat([s1, s2, s3],sort=True))
print(pd.concat([s1, s2, s3], axis=1,sort=True))#<Default axis 0>, default - outer
s4 = pd.concat([s1 * 5, s3])
print(s4)
print(pd.concat([s1, s4], axis=1,sort=True)) #<Default outer>
print(pd.concat([s1, s4], axis=1, join='inner',sort=True))
print(pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']],sort=True))
