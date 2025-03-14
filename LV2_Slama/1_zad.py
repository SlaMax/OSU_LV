import numpy as np
import matplotlib . pyplot as plt


x=np.array([1,2,3,3,1])
y=np.array([1,2,2,1,1])

plt.plot(x,y,'r', linewidth=1,marker='X', markersize=6)
plt.axis([0,4,0,4])
plt.xlabel("x os")
plt.ylabel("y os")
plt.title("zadatak 1")
plt.show()