import matplotlib.pyplot as plt
import numpy as np

xpoints=[2018,2019,2020,2021,2022,2023]
ypoints=[10,20,30,40,50,60]

xpoints1=[2018.5,2019.5,2020.5,2021.5,2022.5,2023.5]
ypoints1=[5,15,25,35,45,55]

plt.bar(xpoints,ypoints,label="Adipur Salse",width=0.5)
plt.bar(xpoints1,ypoints1,label="Anjar Salse",width=0.5)

plt.xlabel("Sales")
plt.ylabel("Year")
plt.legend()
plt.title("Sales Report",loc="center")
plt.show();

