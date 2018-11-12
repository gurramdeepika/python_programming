import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(10,4).cumsum(0),columns=['A','B','C','D'],index=np.arange(0,100,10)) #cum means prev,prev+pres
df.plot()