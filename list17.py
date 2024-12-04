# Write a Python program to print the numbers of a specified list after removing even numbers from it.


mylist=[2,4,9,3,10,5]
mylist1=[]

for i in mylist:
    if i%2==0 :
        mylist.remove(i)
    else:
        mylist1.append(i)
        
print(mylist1)