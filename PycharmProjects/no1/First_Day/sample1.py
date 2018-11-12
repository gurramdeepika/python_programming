#First Day Training-1

print("hello world to deepika!!!")
x = 20
y = 23.4
z="hello"

if x==20:
    print("Welcome X !!")
    print("z is from ", type(z), "family")
print("Bye")

# string representation in print

print('"hey !!! hi"')
print("hey id's")
print('''"hello id's", bye''')
print("hello \n world")
print(r"hello \n world")

#comparing types
if type(x) is int:
    print("x is from integer family")
else:
    print("something else")

#assigning to other variable
w = x
x = "world"
w = x
print(x,w)

#to know the id's
print(id(x) , id(w))

print(id(x))
print(id(w))

#help to get all the keywords
#help('keywords')

#swap two variables
a,b = 5,10
print(a,b)

b,a = a,b
print(a,b)