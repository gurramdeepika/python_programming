#find the number in the list

lis = [1,19,89,23,34,19,78,19]
i=0
for var in lis:
    if var == 19: print('index of 19 is', i)
    i = i + 1

# delete the duplicate one number

#if we use set the list wil be unordered and it will not be the list anymore

print(lis)
i=0
s1 = set(lis)
lis1 = lis

# getting keys from values
adict = {'i':'mine','we':'us','they':'them'}
lis=[]
print(lis)
for x in adict.items():
    lis.append(x)
print(lis)
val = input("enter the value")
for x1 in lis:
    if x1[1] == val:
        print(x1[0])
        break











