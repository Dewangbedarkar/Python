# Write a Python program to find the list of words that are longer than n from a given list of words.

mylist=['dewang','tushar','saurish','saurabh']
mylist1=[]

print(mylist)

n=int(input("enter a no. "))

for i in mylist:
    if len(i)>n:
        mylist1.append(i)

print(mylist1)