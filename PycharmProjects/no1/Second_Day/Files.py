#files
import os
import sys
def file_wr(filename):
    if os.path.exists(filename):
        sys.stderr.write("File exists\n")
        sys.exit(2)
    f = open(filename,"w")
    f.write("good morning\n")
    f.write("good evening\n")
    f.write("good night")
    f.close()

def file_rd(filename):
    if not os.path.exists(filename):
        sys.stderr.write("No such file")
        sys.exit(3)
    f =open(filename)#by default the second argument is r
    #print(f.read())
    #print(f.readline()) #current point means after first execution done in the same file
    #f.seek(-15,1) error will not allow the negative values in the first argument
    f.seek(15,0) # should be 0 in the second argument but theoriticall it can be 1 or 2
    print(f.readlines())
    f.close()

#convert list and dictionary as a string
def file_w_int():
    x,y,z = 43,44,45
    s="spam"
    d={'a':1,'b':2}
    l=[1,2,3]
    f=open("sample.txt","w")
    f.write(s+'\n')
    f.write('%s,%s,%s\n'%(x,y,z))
    f.write(str(l)+'$'+str(d)+'$'+'\n')
    f.close()

#list of type integer
def file_w_lst(filename, lst):
    f=open(filename,"w")
    lst = list(map(lambda x:str(x)+'\n',lst))
    f.writelines(lst)
    f.close()

#read the list of type interger
def file_r_lst(filename):
    f=open(filename)
    rlist = f.readlines()
    rn = list(map(lambda x:int(x.strip('\n')),rlist))
    print(rn)

def file_w_dict(dic,filename):
    f=open(filename,'w')
    dic1=""
    for (k,v) in dic.items():
     f.write(str(k) + ',' + str(v) + '\n')
    f.close()

def file_r_dic(filename):
    f=open(filename)
    rlis = list(map(lambda x:x.strip().split(','),f.readlines()))
    dic = dict(map(lambda x:(x[0],int(x[1])),rlis))
    print(dic)

lst = [1,2,3,4,5]
dic = {'w':6,'e':2,'i':3}
if __name__ == '__main__':
    file_wr("output.txt")
    file_rd("output.txt")
    file_w_int()
    file_w_lst("output.txt",lst)
    file_r_lst("output.txt")
    file_w_dict(dic,'output_dic.txt')
    file_r_dic('output_dic.txt')