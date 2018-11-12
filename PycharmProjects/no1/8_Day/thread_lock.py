import time
import _thread

def myfunction(string,sleeptime,lock,*args):
    while 1:
        #entering critical section
        lock.acquire()
        print(string,"now sleeping after lock acquired for",sleeptime)
        time.sleep(sleeptime)
        print(string)
        lock.release()
        #exiting critical section
        time.sleep(sleeptime)
if __name__ == '__main__':
    lock = _thread.allocate_lock()
    _thread.start_new_thread(myfunction,("thread no:1",2,lock))
    _thread.start_new_thread(myfunction,("thread no:2",2,lock))

    while 1:
        pass