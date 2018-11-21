#
# f = open('space.txt')
# f_r = f.readlines()
# lis= []
# length = 7
# i=1
# for var in f_r:
#     var2=''
#     var=var.strip ( )
#     for var1 in var:
#         if i<=length:
#             var2+=var1
#             i+=1
#             if length>len(var) and i == len(var):
#                 i = length + 1
#
#         if i > length:
#             var2=' '*4+var2+'\n'
#             lis.append ( var2 )
#             i=0
#             var2=''
#
# print(lis)
#
# f = open('space.txt','w')
# f.writelines(lis)

lis = list(map(lambda x: x.strip('\n').strip().replace(' ',''),open('space.txt').readlines()))

length = 5

def sp_gen(lis):
    for var in lis:
        yield var
lis1=[]
for var in sp_gen(lis):
    i,j=0,5
    while i<len(var):
        var2 =' '*4+var[i:j]+'\n'
        lis1.append(var2)
        i , j=j , j+5

print(lis1)

open('space.txt','w').writelines(lis1)




