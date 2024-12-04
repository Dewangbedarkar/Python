 # 7) accept no.of rows and no. of cols from the user , create two-d array accordingly. Now calculate the sum as per "axis=0" and "axis=1"
import numpy as np

mylist=[]

row=int(input("Enter No. of Rows : "))
column=int(input("Enter No. of Column : "))

print("Enter values of Rows and Column")
for i in range(1,(row*column)+1):
    num=int(input())
    mylist.append(num)

arr=np.array(mylist)
print("--------------------------------------------------------------")
arr=arr.reshape(row,column)
print(arr)
print("--------------------------------------------------------------")
print("axis 0 sum")
print(np.sum(arr,axis=0))
print("--------------------------------------------------------------")
print("axis 1 sum")
print(np.sum(arr,axis=1))
