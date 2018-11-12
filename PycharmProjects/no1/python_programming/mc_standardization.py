import pandas as pd

ex = pd.DataFrame([0,1,2,3,4,5])
ex[1]=(ex[0]-ex[0].mean())/ex[0].std(ddof=0)
ex[2]=(ex[0]-ex[0].min())/(ex[0].max()-ex[0].min())
ex.columns = ['input','standardized','normalized']
print(ex)

