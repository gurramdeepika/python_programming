#class 1
#iterator the class using iter
class Repeater:
    def __init__(self,value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)

#class 2

class RepeaterIterator:
    def __init__(self,source):
        self.source = source
    def __next__(self):
        return self.source.value

r1 = Repeater([12,11])
#r2 = RepeaterIterator(r1)
iter1 = r1.__iter__()

#print(dir(r2.source))
#print(r1)

count =0
for var in r1:
    if count < 2:
        print(var)
        count+=1

item = iter1.__next__()
print(next(item))

