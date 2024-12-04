# 8) declare two 2d arrays and calculate the sum as per "axis=0" "axis=1" and "axis=2"
import numpy as np

arr=np.array([[1,4,2],[5,3,8],[2,9,1]])
arr1=np.array([[3,6,1],[8,2,9],[6,4,1]])
print(arr)
print()
print(arr1)
print("--------- Sum as axis=0 -----------")
print(np.sum((arr,arr1),axis=0))
print("--------- Sum as axis=1 -----------")
print(np.sum((arr,arr1),axis=1))
print("--------- Sum as axis=1 -----------")
print(np.sum((arr,arr1),axis=2))