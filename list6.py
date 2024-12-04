mylist=[]

for i in range(1,6):
    num=int(input("Enter 5 no. = "))
    mylist.append(num)
print(mylist)
rem=int(input("Enter Position to be removed : "))
mylist.remove(mylist[rem])
print(mylist)