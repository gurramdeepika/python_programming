
import matplotlib.pyplot as plt
import numpy as np

#subplot returns the numpy array object
fig = plt.figure(figsize=(8, 6))
fig.add_subplot(231).hist(np.random.randn(100),bins=20,color='k',alpha=0.3)#bins -- no.of histograms
fig.add_subplot(233).scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
fig.add_subplot(235).plot(np.arange(10))
fig.add_subplot(236).plot(np.sin(np.linspace(-np.pi,np.pi,256)))


