import pandas as pd
import numpy as np

ages = [20,22,25,27,21,23,37,31,61,45,41,32]
bins = [18,25,35,60,100] # bins should be in increased monotonically

cats = pd.cut(ages,bins)

# print(cats.codes)
# print(pd.value_counts(cats))

group_names = ['youth','young adult','middle aged','senior']

print(pd.cut(ages,bins,labels=group_names))

data = np.random.rand(20)

print(pd.cut(data,4,precision=2)) #bins = 4, after decimanl is precision=2

