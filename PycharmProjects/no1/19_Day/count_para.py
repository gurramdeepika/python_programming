lis = list(map(lambda x: x ,open('count.txt').readlines() ))
lis1 =0
i =0
count=0

while i<len(lis):
    count=0
    if i+2  < len ( lis ) and lis[i]!='\n' and lis[i+2]!='\n' :
        lis1+=1
    elif  i+2  > len ( lis ) and lis[ i ]:
        lis1+=1
    i+=1

print(lis1)






