import matplotlib.pyplot as plt
slice = [7,3,2,4,5,24]
activity = ['Eating','Sleeping','Running','Playing','Other','Working']
colr=['m','c','r','k','g','l']
plt.title('Pie Plot')
plt.pie(slice,labels=activity,colors=colr,shadow=True,explode=(0,0.1,0,0,0),autopct='%1.1f%%')
plt.show()