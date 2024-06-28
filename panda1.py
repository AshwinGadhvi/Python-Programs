import pandas as pd
import matplotlib.pyplot as plt

mydataset={
    'cars':["AUDI","VOLVO","FORD"],
    'passing':[3,5,1]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
print("----------------------------")

#x=myvar.loc[:,[1]]


df=pd.read_csv('op.csv')
a=pd.DataFrame(df)
print(a)

x=myvar['cars']
y=myvar['passing']

# plt.plot(x,y) done hei 
# plt.show()

df = pd.read_csv('op.csv')
pd.options.display.max_rows=9999

x1=df['Year']
y2=df['Sales']

plt.plot(x1,y2)
plt.show()


