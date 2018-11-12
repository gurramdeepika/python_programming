import signal
import time

def handler(a,b):
    print("signal number",a,"frame",b)
    signal.signal(signal.SIGINT,signal.SIG_DFL) #terminate the process
signal.signal(signal.SIGINT,handler)

while True:
    print("not afraid od C-c")
    time.sleep(1)