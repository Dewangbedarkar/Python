# 2) create numpy array of 5 numbers and print their sum
import numpy as np
arr=np.array([2,4,1,5,8])
sum=0
print("Array",arr)
for i in arr:
    sum=sum+i

print("Sum = ",sum)