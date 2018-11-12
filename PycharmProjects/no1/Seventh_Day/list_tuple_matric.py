class MatrixList:
    def __init__(self,tup):
        self.tup = tuple(tup)
    def validateSize( self ):
        innertup = self.tup[1]
        if len(self.tup[0]) != (innertup[0] * innertup[1]):
            input("please enter the valid size in the second index of a tuple")
            self.validateSize()
        return innertup

    def matrixtup( self ):

        sizeMatrix = self.validateSize()
        col = sizeMatrix[1]
        lis = self.tup[0]
        lis1=[ ]
        totallis = []
        i = 0
        for var in lis:
            if i == col and lis:
                lis1=[ ]
                i = 0
            if i<col:
                lis1.append(var)
            i+=1
            if len(lis1) == col:
                totallis.append(lis1)
        print(totallis)

if __name__ == '__main__':
   # tup = input("please enter the tuple")
    tup = ([2,3,4,5,6,7],(3,2))
    MatrixList(tup).matrixtup()





