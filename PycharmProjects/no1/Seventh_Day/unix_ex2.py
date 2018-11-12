#stderr

import sys
import os

divisor = int(input(" "))
dividend = int(input(" "))
fd = os.open("allers.txt",os.O_CREAT|os.O_WRONLY)
os.dup2(fd,2)

if divisor == 0:
    sys.stderr.write("can't divide by zero")

os.close(fd)