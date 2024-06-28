import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([1,8])
ypoints=np.array([3,10])

xpoints1=[1,3,5,5,7,4];
ypoints1=[5,3,2,8,10,3];

plt.grid(axis='x',color='blue',linestyle='--',linewidth=0.5)

# plt.plot(xpoints,ypoints,xpoints1,ypoints1)

plt.plot(xpoints,ypoints,'c',label='Sales Adipur',linewidth=2,marker='o')
plt.plot(xpoints1,ypoints1,'b',label='Sales Anjar',linewidth=2,marker='*')

plt.title("My Salse Chart",loc='center')
plt.xlabel("Days")
plt.ylabel("Month")
plt.legend()
plt.show()