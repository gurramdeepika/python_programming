import _thread
import time

def print_time(delay):
    while 1:
        time.sleep(delay)
        print(time.ctime(time.time()))
#start the thread
_thread.start_new_thread(print_time(5,))
while(1):pass