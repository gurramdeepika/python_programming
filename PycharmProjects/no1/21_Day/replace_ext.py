import glob, os

folder = '/home/cisco/Downloads/'
for filename in glob.iglob(os.path.join(folder, '*.txt')):
    os.rename(filename, filename[:-4] + 'data') #rename(oldname, newname)


import os
folder = '/home/cisco/PycharmProjects/no1/20_Day'
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)#o/p - tuple- (one, .csv)
    print(oldbase)
    newname = infilename.replace('.csv', '.txt')
    output = os.rename(infilename, newname)

import glob
# for name in glob.glob('/home/cisco/PycharmProjects/no1/*/*'):#print files in dir and sub dir
for name in glob.glob('/home/cisco/PycharmProjects/no1/20_Day/?*.txt'): # ? for files
    print(name)