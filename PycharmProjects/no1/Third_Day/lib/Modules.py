#importing a module

#import Second_Day.Files as f

# from Second_Day.Files import file_wr
# file_wr("NewWrite.txt")

def myadd(x,y):
    return x+y
def mysub(x,y):
    return x-y

if __name__ == '__main__':

    lis = [1, 2, 3, 4]
    lis1 = lis[:]

    from copy import deepcopy
    dic = {1: 2, 3: 4}
    dic1 = deepcopy(dic)
    print(dic1)

    print("from module",myadd(9,8))
    print("from module",mysub(8,3))