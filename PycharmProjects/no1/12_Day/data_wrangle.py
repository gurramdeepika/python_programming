import pandas as pd
df1 = pd.DataFrame({'lkey':['a','d','b'],'data1':range(3)})
df2 = pd.DataFrame({'rkey':['a','c','a','b','c','c','b'],'data2':range(7)})

#print(pd.merge(df1,df2,left_on='lkey',right_on='rkey',how='outer'))# by default inner join,rigth--df2,left-df1

left = pd.DataFrame({'st':['ka','ka','kl','tl'],
                     'fg':['pd','wh','pd','re'],
                     'lqty':[12,11,14,13]})

right = pd.DataFrame({'st':['ka','ka','kl','kl','ka'],
                     'fg':['pd','pd','pd','cn','wh'],
                     'lqty':[5,7,6,4,3]})

#print(pd.merge(left,right,on='st')) left will select
#print(pd.merge(left,right,on=['st','fg'],suffixes=('_left','_right'))) #common values

print(pd.merge(left,right,on='st',how='outer',suffixes=('_left','_right')))
