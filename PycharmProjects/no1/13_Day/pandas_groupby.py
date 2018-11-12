import pandas as pd
import numpy as np

stocks = pd.DataFrame({'spice':['mirchi','pepper','salt','turmeric','tamarind','onion','salt','mirchi'],
                       'brand':['aachi','mtr','asirvad','aachi','ntr','aachi','mtr','asirvad'],
                       'price':[200,201,202,200,201,202,203,201],'qtg':[200,400,600,300,200,400,600,800]})



#print(stocks.groupby('spice').mean())

# print(stocks['price'].groupby([stocks['brand'],stocks['spice']]).mean())
#
# print(stocks.groupby('spice').size())

# for name,group in stocks.groupby('spice'):
#     print(name)
#     print(group)

print(stocks.groupby('spice')['price'])
print(stocks.groupby('spice')['qtg'])

pieces = dict(list(stocks.groupby('spice')))
print(pieces)