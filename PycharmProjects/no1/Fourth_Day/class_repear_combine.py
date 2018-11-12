class Repeater:
    def __init__(self,value,upLim):
        self.value = value
        self.upLim = upLim
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.upLim:
            raise StopIteration
        self.count += 1
        return self.value

r1 = Repeater({'hello',12},4)

# print(next(r1))
# print(next(r1))
# print(next(r1))
# try:
#     for var in r1:
#         print("inside loop",var)
# except:
#     print("Done")

while True:
    try:
        print(next(r1))
    except:
        print("Done")
        break

