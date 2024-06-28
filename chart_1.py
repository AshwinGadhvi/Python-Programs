import matplotlib.pyplot as plt


xpoint=[2016-10-1,2016-10-2,2016-10-3,2016-10-4]
ypoint=[772.5,773.0,773.5,774.0]

plt.grid(axis='x',color='blue',linestyle='solid',linewidth='1')
plt.grid(axis='y',color='blue',linestyle='solid',linewidth='1')
plt.plot(xpoint,ypoint,color='red',marker='o')
plt.title("Closing Stock Value of Alphabet",loc="center")
plt.xlabel("date")
plt.ylabel("closing value")
plt.show()