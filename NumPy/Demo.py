import numpy as np
# arr=np.array([[1,2,5],[6,3,8],[2,8,5]])
# arr.shape=(3,3)
#
#
# print(arr)
# print("-------------------------------------")
# # print(arr1)
#
# print(np.sum(arr,axis=1))

#
# arr1= np.array([10,20,30])
# arr2=np.array([40,50,60])

# hstack1=np.hstack((arr1,arr2))
# print("Let's print horizontal stack")
# print(hstack1)

# ostack=np.stack((arr1,arr2),axis=1)
# print(ostack)
#
# print("------------------------------------------------------------")
# #
# print(np.sum(ostack,axis=1))
#


# arr1= np.array([[10,20,30],[40,50,60]])
# arr2=np.array([[70,80,90],[100,110,120]])
#
# stack=np.stack((arr1,arr2),axis=2)
# print(stack)
#



#
# arr=np.array([2,7,4,9,1])
# print(arr)
# print("-------------------------------")
# arr.sort()
# print(arr)


# a = np.array([[12, 25], [30, 18]])
# arr1 = np.sort(a, axis=None)
# print("\nAlong None axis : \n", arr1)
#



# myar=np.array([10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])
#
# myar.shape=(2,3,3)
# print(myar)
#
# print(np.sum(myar))
# print("-------------------------------------------")
# print(np.sum(myar,axis=0)) # put 2nd two d array after first 2d array and then sum
# print("--------------------------------------------")
# print("with axis 1")
# print(np.sum(myar,axis=1)) # it's like axis=0 in 2d array , chopping something from top to bottom within each 2d array
# print("--------------------------------------------------")
# print("with axis 2")
# print(np.sum(myar,axis=2)) # it's like axis=1 in 2d array, chopping something from left to right within each 2d array







arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])
arr3=np.array([[13,14,15],[16,17,18]])

hstack=np.hstack((arr1,arr2,arr3))
print("this is hstack")
print(hstack) # each 2d array's individual rows are stacked horizontally




arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])
arr3=np.array([[13,14,15],[16,17,18]])


stack_0=np.stack((arr1,arr2,arr3),axis=0)
print("this is 0 stack")
print(stack_0)  # in 3d array, axis 0 means no. of 2d arrays
# here we have 3 2d arrays , so they are stacked one below other
























