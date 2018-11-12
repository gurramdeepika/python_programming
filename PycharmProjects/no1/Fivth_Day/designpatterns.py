#singleton
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton,cls).__new__(cls)
        return cls.instance

s1 = Singleton()
s2 = Singleton()

print(s1, s2)

#singleton as a Monostate design
class Borg:
    __shared_state = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass
b = Borg()
b1 = Borg()
b.x = 4
b1.x  = 6
print(b)
print(b1)
print(b.__dict__)
print(b1.__dict__)