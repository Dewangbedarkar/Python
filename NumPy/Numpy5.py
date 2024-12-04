#5) create two double dimension array and arrange (stack) them using "axis=0" "axis=1" and  "axis=2".

import numpy as np
from numpy import random
random.seed(18)
arr=np.random.randint(10,50,18).reshape(2,3,3)
print(arr)

stack1=np.stack((arr),axis=0)
print("---------------- Axis=0 -----------------------")
print(stack1)
stack2=np.stack((arr),axis=1)
print("---------------- Axis=1 -----------------------")
print(stack2)
stack3=np.stack((arr),axis=2)
print("---------------- Axis=2 -----------------------")
print(stack3)
