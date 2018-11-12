import numpy as np

arrange = np.arange(0,10,1) #start,stop,step
print('arrange is',arrange)

linearspace = np.linspace(0,10,25)
print('linearspace is',linearspace)

#linear space calculation
#start + sum i=1 from step((stop-start)/step-1) 10/24*1,10/23*2...10/2*24

logspace = np.logspace(0,10,10,base = np.e)
print("logspace is",logspace)