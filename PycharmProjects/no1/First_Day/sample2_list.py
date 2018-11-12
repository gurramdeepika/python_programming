#First Day Training-2

# string, tuple, list as sequence types

tul = (12,9.12,'lu',[18,'ty'],(34,23))

lis = [19,60,'ff',(45,"gfd"),'li',89,90]

greet = "good morning"

print(lis)

print('first element is' , tul[0])
print('last element is', lis[-1])

lis[-1] = (45,'hh')

print(lis[-1])

#slicing the object list

#m:n
print(lis[1:-1])
print(lis[1:5])

#n:m
print(lis[5:1])

'''index out of range

print(lis[5])'''

#print last three elements

print(lis[-3:])

#print first three elements

print(lis[:3])

#first to last before one

print(lis[0:-1])

#first to last

print(lis[0:])
print(lis[:])
print(lis)

li2 = lis # shallow copy
li3=lis[:] # deep copy

print( 'li2 is ', lis is li2)
print(lis is li3)


print(id(lis))
print(id(li2))
print(id(li3))


# string slicing using alphas()
alphas = 'abcdefghijklmnopqrstuvwxyz'
print(alphas[3:24:2]) #start at 3  stop at 24 increment by 2 factor 3 + 2 / 3 + 4 .....24
print(alphas[24:3:-1]) # start at 24 stop at 3 decrement by -1 means 24-1
print(alphas[::-1])
print(alphas[0::-1])
print(alphas[0::1])

print('palindrome or not')
pal="able was i ere i saw elba"

if pal == pal[::-1]:
    print('pal is a palindrome string')
else:
    print('pal is not a palindrome string')

# in keyword
print('in keyword')
#print(19 in lis[0])
print('li' in lis[4])

# + operator
print('str ' + ' str1')
print(1+2)

# * usage
str1 ='hi'
print(str1*5)



