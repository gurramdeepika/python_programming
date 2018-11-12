#list comprehensions
li = [1,2,3,4]
li = [ele/2 for ele in li]
print(li)

li = [(3,2),(2,3),(2,1),(1,2)]
lis = [(n * 3,x*n,x*2) for (x,n) in li]
print(lis)
lis = [[n * 3,x*n,x*2] for (x,n) in li]
print(lis)
lis = [{n * 3,x*n,x*2} for (x,n) in li]
print(lis)

#passing functions in list comprehensions
def subtract(a,b):
    return a-b
print("funtion in list comprehensions ",[subtract(y,x) for (x,y) in li])

#filtered list comprehensions
li1 = [1,2,3,4]
lis1 = [ele*2 for ele in li1 if ele > 2] # priority is from right to left
print('flitered list comprehensions ',lis1)

#nested list comprehensions

print('nested list comprehensions ',
      [ele*2 for ele in
                       [item+1 for item in li1]]
      )

#assignment sequence

x,y = 2,3
(x,y,(a,b)) = (1,2,(3,4))
print(x,y,a,b)