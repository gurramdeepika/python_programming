import pandas as pd


min_index = pd.read_csv("/home/cisco/Downloads/NIFTY-I.csv",header= None)
min_index.columns = ['data','time','open','high','low','close','volume','OI']

min_index['period'] = min_index['data'].map(str) + \
                      min_index['time']

min_index = min_index.drop(axis=1,columns=['data','time'])

min_index['period'] = pd.to_datetime(min_index['period'],format='%Y%m%d%H:%M')

min_index = min_index.set_index('period')

print(min_index.head())