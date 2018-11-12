class Counter:
    overall_total = 0 #static variables
    def __init__(self):
        self.my_total = 0
    def increment(self):
       # Counter.overall_total = Counter.overall_total +1
        __class__.overall_total = Counter.overall_total +1
        self.my_total = self.my_total + 1

a = Counter()
b = Counter()
a.increment()
b.increment()
b.increment()
print(a.my_total)
print(b.my_total)
print(b.overall_total , a.overall_total)