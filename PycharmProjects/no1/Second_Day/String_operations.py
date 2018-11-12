#string operations

greet = "deepika is a good girl:)"
print(greet.title())
print(greet.upper())
print(greet.lower())
print(greet.capitalize())
print(greet.casefold())
print(greet.swapcase())

def yesorno(str1,str2):
    if str2 == '1':
       return str1.upper()
    if str2 == '2':
        return str1.lower()
    if str2 == '3':
        return str1.capitalize()
    else:
        print("no")
str1 = input("please enter the string")
str2 = input('please enter the type of function to covert the string, \n 1.uppercase \n 2.lowercase \n 3.capital')
str3 = yesorno(str1,str2)
print("your string is converted as" , str3 ,'\n Thank you ')

def yesono(str1):
    while(str1 != 'YES'):
        if(str1 == 'yes'):
              return str1.upper()
        else:
            print("invalid string")
            break
str4 = input("print yes or no").strip(' ')
print(yesono(str4))

#isdigit

wage = input("enter the daily wage")
if wage.isdigit():
    wage = int(wage)
else:
    wage = 121313131312323131231231
print("your daily wage is ", wage)

#print statement

print("hello",end=' ')
print("world")
print("hello "," world", sep=":")

#format specifiers

x = 34545*343.5565
str5 = 'hi world'
fname,lname = 'gj' , 'jaji'
print("float format specifier is %.f" %x) # .f / .0f
print("float format specifier is %.2f" %x)
print('string and float is %.2f:%.2s:%-.7s' %(x,str5,str5))
print("string format specifier is :%-10s:%10s" %(fname,lname))

print('join() for joining the strings using seperator \n',':'.join(['abcdef','ghijk','lnmop','qrstu','vwxyz']))
lis1 = ':'.join(['abcdef','ghijk','lnmop','qrstu','vwxyz']).split(':')
tup1 = tuple(lis1)
print(lis1)
print(tup1)

