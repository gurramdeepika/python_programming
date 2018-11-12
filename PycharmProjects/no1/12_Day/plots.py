import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi,np.pi,256)#256 is smoothness of the curve
y00 = np.sin(x)
y01 = np.cos(x)
y1 = np.sinh(x)
y2 = np.cosh(x)
y3 = np.tan(x)
# plt.plot(x,y00)
# x = np.linspace(-1,1,256)
# y4 = np.sqrt(1-x*x)
plt.figure(figsize=(6,4),dpi=100)#dpi - dots per inch(resolution-results the how big the sixe of a figure) # 6->x-axis,4->y-axis
plt.plot(x,y00,color='blue',linewidth=2.5,linestyle='--',label='sin')# -. , :
plt.plot(x,y01,color='red',linewidth=2.5,linestyle=':',label='cos')
# plt.xlim(x.min()*1.5) # to move the graph in the x-axis with that range
#plt.ylim(y1.min())
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$\pi/2$',r'$\pi$'],rotation=30)
plt.yticks([-1,0,1])
ax = plt.gca() # to get the axes of current figure
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
#ax.xaxis.set_ticks_position('bottom')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
for labels in ax.get_xticklabels() + ax.get_yticklabels():
    labels.set_fontsize(16)
    labels.set_bbox(dict(facecolor='pink',edgecolor='blue',alpha=0.35))#alpha is the transperancy of the box
#plt.legend(loc='righttop')#shows warning and gives all the possiblities
plt.legend(loc='best')
plt.show()