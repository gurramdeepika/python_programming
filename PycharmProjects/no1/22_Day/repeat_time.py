from datetime import datetime,timedelta
from threading import Timer
import time

x = datetime.now()
# y=datetime.now()+timedelta(minutes=1)
# y_delta = y-x


def hello_world():
    print ("hello world")

# t = Timer(y_delta, hello_world)
# t.start()

print ("started timer at", x)
while x:
    # Sleep for a minute
    time.sleep(60)
    hello_world()
    print ( "processing...." , datetime.now() )
