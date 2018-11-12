#loop
x=3
while x<5:
    print("x is still in the loop")
    x=x+1
print(x)

i=0
while i<10:
    i+= 1
    if i<=4:
        print("continue")
        continue
    print('i is', i)

    if i>=8:
        print('break')
        break

lis1 = [1,2,3,4,5]
for var in lis1:
    print(var)

for var in range(len(lis1)):
    print(lis1[var])

