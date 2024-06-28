import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("op.csv",engine="python")

x=df['Year']
y=df['Sales']

plt.plot(x,y)
plt.show()

