import numpy as np
import matplotlib.pyplot as plt

n=12

x=np.arange(n)


y1=(1-x/float(n))*np.random.uniform(0.5,1.0,n)

y2 = (1-x/float(n))*np.random.uniform(0.5,1.0,n)


plt.bar(x,+y1,facecolor = '#9999ff',edgecolor='white')

plt.bar(x,-y1,facecolor = '#ff9999',edgecolor='white')

for x,y in zip(x,y1):
    plt.text(x+0.4,y+0.05,'%2f'%y,ha='center',va='bottom')
    plt.ylim(-1.25,+1.25)
