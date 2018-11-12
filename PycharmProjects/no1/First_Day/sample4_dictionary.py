# dictionary

user={'we':'us', 'i':'me','they':'them'}

print(user['we'])

user['it'] = 'it'
user['i'] = 'mine'
print(user)

#print(dir(dict))

print(user.setdefault.__doc__)

print(user.keys(), user.values())
print(user.items())

user.pop('i') #need atleast one argument not like list

user.setdefault('i','me')
print(user)

dict1 = {'hi','hey'}
dict2 = {'hello','aa'}
dict1.update(dict2)
print(type(dict1)) #set

#k1 = input() this will also work for stdin
k1 = input("enter the key")
if k1 in user:
    print(k1,"has value",user[k1])
else:
    print("no such value")

for mykey in user.keys():
    print(mykey, "=>", user[mykey])

for (k,v) in user.items():
    print(k , '=>', v)

print("dictionaray with list and tuples")
for x in user.items():
    print(x[0] , '=>' , x[1])
#set

lis1 = [1,23,445,5556]
lis2=[11,223,4455,6677,1]
s1=set(lis1)
s2=set(lis2)

print(s1, '\n', s2, type(s1),type(s2))

#print(s1[0]) does't support indexing

print(s1.union(s2))

print(s1.issubset(s2))

print(s2.issuperset(s1))

print(s2.isdisjoint(s1))

print(s1.difference(s2) , '\n' , s1.difference_update(s2))

print(s1)




