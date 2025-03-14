import numpy as np
import matplotlib . pyplot as plt

data=np.loadtxt('data.csv', delimiter=",", dtype="str")
data=data[1::]
data=np.array(data,np.float32)
print(data.len())