# '?'
#{max},{min,max}{min,}{,max}
import re
#pat1 = re.compile('^(-)?(\+91)?[0-9]{8,10} +$')
pat1 = re.compile('^(-)?(\+91|\*44)?[0-9]{8,10}$')
pat2 = re.compile('[brewrewrwerrw]a?b' , re.IGNORECASE) #case insensitive

cell = input("enter the string")
if pat1.search(cell):
    print("it matched")
else:
    print("it is not matched")

if pat2.search('BA'):
    print("it matched")
else:
    print("it is not matched")

country = re.compile('(in|jp|uk)$')

if country.search('in'):
    print("it matched")
else:
    print("it is not matched")

#\d
p = re.compile('\d+')
print(p.findall('12 drrummers drumming, 11 pipers piping, 10 lords a-leaping')) # returns the digits in a list

#match and ignore the  new line
greet = "hello\nworld"
pat3 = re.compile('hello$',re.MULTILINE)
print(pat3.search(greet))
pat4 = re.compile(".+",re.DOTALL)# .+ matches everything in a string
print(pat4.search(greet))

#split using '\w'

p1 = re.compile(r'\W+') #meant for white space

lis = p1.split('this is a test, short and sweet, of split() . ')

print(lis)

#split with max count of words

lis1 = p1.split('this is a test, short and sweet, of split() . ',3)

print(lis1)

p2 = re.compile('blue|white|red')
print(p2.sub('colour', 'blue socks and red shoes'))
print(p2.sub('colour','blue socks and red shoes',count = 1))