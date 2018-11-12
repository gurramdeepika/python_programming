class qsequence(object):
    def __init__(self,s):
        self.s = s

    def __next__(self):
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except:
            raise StopIteration()

    def __iter__(self):
        return self

    def current_state(self):
        return self.s

q = qsequence([1,1])

print([next(q) for __ in range(10)])

