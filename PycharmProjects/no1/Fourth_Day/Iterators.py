# iterating from a file
f = open("output.txt")
for line in f:
    print(line)

#iterating from list , set and string
ilis = iter(['some','list'])
print(next(ilis))
print(next(ilis))

iset = iter({'some','set'})
print(next(iset))
print(next(iset))

istring = iter('some string')
print(next(istring))

#using while to iterate the values from an object

def iter_each(iterable):
    while True:
        try:
            item = next(iterable)
        except:
            break
        else:
            print(item)
iter_each(istring)

