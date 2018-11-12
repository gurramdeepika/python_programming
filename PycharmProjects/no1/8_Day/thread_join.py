import threading
import time

loops = [4,2]
def loop(nloop,nsec):
    print('start loop',nloop,'at:',time.ctime(time.time()))
    time.sleep(nsec)
    print('loop',nloop,'done at:',time.ctime(time.time()))

def main():
    print('starting threads....')
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t=threading.Thread(target=loop,args=(1,loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()        #start threads

    for i in nloops:              #wait for all
        threads[i].join()         #threads to finish
    print("all done at:", time.ctime(time.time()))

if __name__ == '__main__':
    main()

