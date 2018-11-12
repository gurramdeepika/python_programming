#files
import os
def f_diclist_w():
    mydict = {'png': [12,13,14],
            'maa':[34,35,36]}
    f = open("dci_lis_data.csv","w")
    f.write(','.join(mydict.keys())+'\n')
    i=0
    while i<len(mydict['png']):
        f.write(str(mydict['png'][i])+',' + str(mydict['maa'][i]) + '\n')
        i+=1
    f.close()

import numpy as np

def f_diclist_r():
    f =open("dci_lis_data.csv")
    rlis = list(map(lambda x:x.strip().split(','),f.readlines()))
    print(rlis)
    rlis_arr = np.array(rlis[1:])
    rlis_lis = list(rlis_arr.T)
    rlis_lis = list(map(lambda x:list(x),rlis_arr))
    data = dict(zip(rlis[0],rlis_lis))

if __name__ == '__main__':
    f_diclist_w()
    f_diclist_r()

#To delete the file
print(list(os.stat('dci_lis_data.csv'))[0])
os.unlink('dci_lis_data.csv')

#builtins
map = 8
print(list(__builtins__.map(lambda x:x*2,[2,1,4])))
print(map)