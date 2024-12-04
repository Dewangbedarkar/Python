

mylist=[]

for i in range(1,6):
    num=int(input("Enter 5 no. = "))
    mylist.append(num)
print(mylist)

mylist.extend([1,3,4])
print(mylist)