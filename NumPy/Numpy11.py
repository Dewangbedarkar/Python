# 11) create one-d array of 8 numbers and then using "slicing" concept,
# 	a) print numbers from 1 to 4
# 	b) print all the numbers from 3rd position
# 	c) print last 3 numbers

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8])
print(arr)

print("----- a) print numbers from 1 to 4 -----")
arr1=arr[:4]
print(arr1)

print("----- b) print all the numbers from 3rd position -----")
arr2=arr[2:]
print(arr2)

print("----- c) print last 3 numbers -----")
arr3=arr[:-4:-1]
print(arr3)