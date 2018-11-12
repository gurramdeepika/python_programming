#if-else

wage = int(input('enter the wage'))
print('daily wage is',wage*8)
print("high" if wage > 2500 else "moderate")

time = input('enter the time')
print('the time now is', time)

thr = time.split(':')

print(time + "AM" if int(thr[0]) < 12 else str(int(thr[0])-12) +'thr[1]' + "PM")

print("multiple statements")

x=3

if x == 3:
    print('x = 3')
elif x == 2:
    print('x = 2')
else:
    print('x is different')
print("bye ifelse")

