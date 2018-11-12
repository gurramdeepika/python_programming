import os
import time
import signal
# os.fork() #which is a system call which is creating the one more process in the memory
# print("hello world")
# os.fork()
# print(os.stat('factory.py'))
def handler(a,b):
    print("signal number",a,"frame",b)

x = 9
pid=os.fork() # which is a system call which is creating the one more process in the memory
# pwho =  os.getpid()

if pid==0:

    #os.execlp("ls","ls") #it replaces the correct process and  add the next process
    #os.execl("/bin/ls",'ls')
    time.sleep(2)
    print("hello world from child")  # child is second ,as a backup it will copy the process first and will load the parent process
    print("my parent pid is",os.getppid())
    parent = os.getppid()
    print("i am child my pid is",os.getpid())
    child = os.getpid ( )# getpid is used to get the current process pid
    x = x+1
    f = open("comm.txt",'w')
    f.write(str(x))
    f.close()
    print('x is',x)
    print("child is done")
else:
    os.wait()
    #os.system("notepad")opens the external command
    #signal.signal(signal.SIGINT,handler)
    print("hello world from parent pid is",os.getpid())  # parent will execute first
    print("child pid is",pid)
    f = open("comm.txt")
    x = f.read()
    x = int(x)
    print('x is',x)
