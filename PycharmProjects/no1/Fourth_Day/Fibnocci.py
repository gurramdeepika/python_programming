class fibnum:
    def __init__(self):
        self.f1 = 0
        self.f2 = 1
    def __next__(self):
        self.f1,self.f2,olff2 = self.f1+self.f2,self.f1,self.f2
        return olff2

    def __iter__(self):
        return self
def main():
    f = fibnum()
    for i in f:
        print(i)
        if i > 20: break

if __name__ == '__main__':
    main()