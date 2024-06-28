import matplotlib.pyplot as plt
import numpy as np

x=np.random.normal(140,3,250)
print(len(x))
print(x)
plt.hist(x)
plt.show()