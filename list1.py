mylist=[]
num=int(input("Enter number : "))
mylist.append(num)
str=input("Enter Name : ")
mylist.append(str)
float=float(input("Enter float value"))
mylist.append(float)

print(mylist)

name=input("Enter one more Name : ")
mylist.insert(1,name)

print(mylist)
