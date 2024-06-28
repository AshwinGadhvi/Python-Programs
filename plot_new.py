import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([1,2,3,4,5])

plt.subplot(2,2,1)
plt.plot(x,y)


#plot

x1=np.array([1,3,2,4,5])
x2=np.array([1,2,3,4,5])

plt.subplot(2,2,2)
plt.plot(x1,x2)

x3=np.array([1,2,3,4,5])
y4=np.array([1,2,3,4,5])

plt.subplot(2,2,3)
plt.plot(x3,y4)


#plot

x5=np.array([1,3,2,4,5])
x6=np.array([1,2,3,4,5])

plt.subplot(2,2,4)
plt.plot(x5,x6)
plt.show()
