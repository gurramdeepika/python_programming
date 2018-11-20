st = 'A man, a plan, a canal; panama'

st = st.lower()

st = st.split(' ')

print(st)

st1 = []

i=len(st)-1
while i>=0:
    st1.append(st[i])
    i-=1

print(st1)

