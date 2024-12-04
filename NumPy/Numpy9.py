# 9) create two-d array ,display it. Now accept a number from user and perform all arithmetic operations on each and
# every element of the array using that number.

import numpy as np
from numpy import random

random.seed(18)

arr=np.random.randint(1,10,9).reshape(3,3)
print(arr)

num=int(input("Enter any no. : "))

print("---------- Addition -----------")
add=arr+num
print(add)

print("---------- Subtraction -----------")
sub=arr-num
print(sub)

print("---------- Mulitipilcation -----------")
multi=arr*num
print(multi)

print("---------- Division -----------")
div=arr/num
print(div)
