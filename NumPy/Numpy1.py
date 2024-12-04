# 1) create a list, accept 5 numbers , store them in the list and finally convert that list to numpy array.
import numpy as np
mylist=[]
for i in range(1,6):
    num=int(input("Enter Element : "))
    mylist.append(num)
print("List = ",mylist)
print("----------------------------------------------------------")
arr=np.array(mylist)
print("Array = ",arr)
    