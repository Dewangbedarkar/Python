mylist=[]
num=int(input("Enter number : "))
mylist.append(num)
str=input("Enter Name : ")
mylist.append(str)
float=float(input("Enter float value : "))
mylist.append(float)
bool=bool(input("Enter Boolean Value : "))
mylist.append(bool)
char=input("Enter Character : ")
mylist.append(char)

print(mylist)
print(mylist[::-1])