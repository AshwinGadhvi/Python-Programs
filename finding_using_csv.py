import matplotlib.pyplot as plt
import pandas as pd
import math

df = pd.read_csv('op.csv');
slice1 = df['Year']
slice2 = df['Sales']
max=max(slice2)

slice3=df['Year']
slice4=df['Sales']

exp=[]
for s in slice2:
    if max==s:
        exp.append(0.1)
    else:
        exp.append(0)

plt.subplot(1,2,1)
plt.title('Sales repot Yearly')
plt.pie(slice2,labels=slice1,explode=exp,autopct='%1.1f%%')

plt.title('Bar Chart')
plt.subplot(1,2,2)
plt.bar(slice3,slice4,label="BAr Chart",width=0.1)
plt.show()