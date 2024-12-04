# Write a Python program to get the largest number from a list.

# mylist=[12,35,20,45,98]
#
# print(max(mylist))

# num=max(mylist)
# print(num)


mylist=[1,4,7,23,8]

i=float('-inf')
for j in mylist:
    if j>i:
       i=j


print(i)
