import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(6),index=pd.date_range('1/1/2000',periods=6,freq="D")) #d - daily, m-monthly,y-yearly

print(ts)
print(ts.shift(2))
print(ts/(ts.shift(1)-1))

ts_local = ts.tz_localize('UTC')
print(ts_local)
print(ts_local.tz_convert('US/Eastern'))

st_price = pd.read_csv("/home/cisco/Downloads/stock_px.csv",parse_dates=True,index_col=0)

st_imp = st_price[['AAPL','MSFT']]

st_imp[['AAPL','MSFT']].plot()

#range
st_imp.loc['13-02-2003':'20-06-2003'].plot()

close_px = st_price[['AAPL','MSFT','XOM']]
close_px.AAPL.rolling(250).mean().plot()