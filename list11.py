mylist=[]
mylist1=[]

for i in range(1,6):
    num=int(input("Enter Values Of List : "))
    mylist.append(num)


print(mylist)

num1=int(input("Enter value : "))

for i in mylist:
    if i > num1:
        mylist1.append(i)


print(mylist1)

