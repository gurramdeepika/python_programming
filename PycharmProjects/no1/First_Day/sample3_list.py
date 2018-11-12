#changing the object

tul = (12,9.12,'lu',[18,'ty'],(34,23))

lis = [19,60,'ff',(45,"gfd"),'li',89,90]

lis[0] = 90 # not allowed in tuple

print(lis)

#tul[0] = 33

print(tul) # exception as TypeError: 'tuple' object does not support item assignment

#accessing the tuple and changing the list in a tuple

tul[3][0] = 31
print (tul)

#lis[3][0] = 46
lis[3] = (46,54)
print(lis)

# to know the methods used by list
print(dir(lis))

# to know the description of a particular method
print(lis.count.__doc__)

#string methods
print(dir(str))

# list funtions
lis.append('a')
lis.insert(0,23) # add at 0 index and push the others elements to its next index
print(lis)

lis.extend([19,30]) # added two elements in a list
print(lis)
lis.append([19,30]) # added one element in  a list
print(lis)
print(id(lis))

lis = lis + [19,30] # appended a new list with old lis ref and assigned to the new lis ref
print(id(lis))

print(lis.index(90,2))
print(lis.index(90))
print(lis.index(90,1,8)) # not in a list range from 2 - 4, 8 is excluded , 1 is included
lis4 = [34,90,78,90]
print(lis4.index(90,-1))

print(lis.count(30))
print(lis)
lis.remove(30) # removes first occurence of 30 in a list
print(lis)


#lis.pop(-2) # removes the element in index -2
lis.pop() # removes last element of a list
print(lis)

del lis[1] # del is  keyword
print(lis)

# del lis  delete the whole list from memory
# print(lis)  - throws exception

'''lis.reverse()
print(lis)'''

lis4 = [90,89,67]
lis4.sort()
lis4.reverse()
print(lis4)

# tuple and int difference
tupx = (9,) # tuple identifies with a comma operator
tupy = (9) #int
tupyz = 9 # int
print(tupx , tupx[0], tupy)

'''a = [3,4]
b=a != b=a[:]'''


print(list(range(10,20,2)))
print(list(enumerate((lis)))) # same as below
print(list(enumerate(lis)))
