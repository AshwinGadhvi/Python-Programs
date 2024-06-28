import matplotlib.pyplot as plt
import numpy as np


days = [1,2,3,4,5]
s=[7,8,6,11,7]
r=[2,3,4,3,2]
w=[7,8,7,2,2]
p=[8,5,7,8,13]

plt.plot([],[],color='m',label='Sleeping')
plt.plot([],[],color='c',label='Working')
plt.plot([],[],color='r',label='Eating')
plt.plot([],[],color='k',label='Playing')

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title('Stack Plot')
clr=['m','c','r','k']
plt.stackplot(days,s,r,w,p)
plt.show()