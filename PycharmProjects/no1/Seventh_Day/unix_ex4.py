import os
import sys


r,w = os.pipe()
pid=os.fork()  # which is a system call which is creating the one more process in the memory
if pid:
    os.wait()
    #this is the parent process
    #closes file descriptor
    os.close(w)
    r= os.fdopen(r)
    print("parent reading")
    mstr = r.read()
    print("text =",mstr)
    sys.exit(0)
else:
    #this is the child process
    os.close(r)
    w = os.fdopen(w,'w')
    print('child writing')
    w.write("text written by child")
    w.close()
    print("child closing")
    sys.exit(0)






