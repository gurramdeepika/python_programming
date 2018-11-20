st = 'A man, a plan, a canal; panama'

lis1 = list(st.lower())

lis1.reverse()
print(lis1)

lis3 =[]

for var in lis1:
    if var.isalpha():
        lis3.append(var)

print(lis3)
lis2 = list(st.lower().replace(' ','').replace(';','').replace(',',''))

print(lis2)

if(lis2 == lis3):
    print("the given string is a palindrome")

else:
    print('the given string is not a palindrome')









