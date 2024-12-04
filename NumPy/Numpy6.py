#
# 6) create two one-d arrays and then find out:
# 	a) common elements of both the array
# 	b) unique elements of first array
# 	c) unique elements of second array

import numpy as np

arr=np.array([1,2,5,3,6,7])
arr1=np.array([4,5,2,6,7,2])

common=np.intersect1d(arr,arr1)

print("a) -> ",common)
print("-----------------------------------------")

unique=np.setdiff1d(arr,arr1)

print("b) -> ",unique)
print("-----------------------------------------")

unique1=np.setdiff1d(arr1,arr)

print("c) -> ",unique1)

