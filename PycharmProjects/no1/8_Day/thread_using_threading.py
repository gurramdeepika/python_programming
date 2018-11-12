import threading
import time

class PrintTime(threading.Thread):
    def __init__(self,interval):
        threading.Thread.__init__(self)
        self.interval = interval
    def run( self ):
        while True:
            time.sleep(5)
            print(time.ctime(time.time()))
p1 = PrintTime(5)
p1.start()

while 1:
    pass

