# create one-d numpy array of 12 elements , accept 12 numbers and display them. Now convert this one-d array into (4*3) two-d array and display it in a tabular form.

import numpy as np

arr=np.arange(12)
print("Enter 12 Numbers : ")
for i in range(0,arr.__len__()):
    arr[i]=int(input())

print("One-D Array = ",arr)

arr1=arr.reshape(4,3)
print("--------------------------------------------------------------------------------------")
print(arr1)
