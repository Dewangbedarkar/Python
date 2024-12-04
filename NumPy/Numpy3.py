# 3) create numpy double dimension array of 3*3 to store your initial and display them in a tabular form.
import numpy as np
from numpy import random


arr=np.random.randint(1,50,9).reshape(3,3)
print(arr)
