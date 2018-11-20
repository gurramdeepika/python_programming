st = 'A man, a plan, a canal; panama'

st = st.split(' ')
lis2=[]
print(st)

for var in st:
    i =len(var)-1
    var1=''
    while(i>=0):
        var1 += var[i]
        i-=1
    lis2.append ( var1 )

print(lis2)
