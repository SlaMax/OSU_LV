import numpy as np
import matplotlib.pyplot as plt

img=plt.imread("road.jpg")

posvjetljena=img+10
plt.imshow(posvjetljena)
plt.show()