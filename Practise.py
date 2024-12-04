# import numpy as np
#
# list=[]
# print("Enter elements : ")
# for i in range(1,6):
#     num=int(input())
#     list.append(num)
# print(list)
# print("-------------------------------")
# arr=np.array(list)
# print(arr)


# import numpy as np
# sum=0
# arr=np.array([2,5,1,5,7])
# for i in arr:
#     sum+=i
#
# print("Sum = ",sum)


# import numpy as np
# from numpy import random
#
# random.seed(18)
# arr=np.random.randint(1,10,9).reshape(3,3)
# print(arr)


#
# import numpy as np
#
# arr=np.arange(12)
#
# print("Enter Elements : ")
# for i in range(0,arr.__len__()):
#     arr[i]=int(input())
#
# print("One-D Array : ",arr)
#
# print("-----------------------------------------")
#
# print(arr.reshape(4,3))


# import numpy as np
# from numpy import random
#
# random.seed(18)
# arr=np.random.randint(1,10,18).reshape(2,3,3)
# print(arr)
# print("----------------------------------------------------")
# arr1=np.stack((arr),axis=0)
# print(arr1)
# print("----------------------------------------------------")
# arr2=np.stack((arr),axis=1)
# print(arr2)
# print("----------------------------------------------------")
# arr3=np.stack((arr),axis=2)
# print(arr3)


# import numpy as np
# arr=np.array([1,6,3,5,7,6,9])
# arr1=np.array([3,6,7,2,5,1,0])
#
# print("common elements of both the array")
#
# com=np.intersect1d(arr,arr1)
# print(com)
#
# print("-----------------------------------------------")
#
# print("unique elements of first array")
#
# uni=np.setdiff1d(arr,arr1)
# print(uni)
#
# print("-----------------------------------------------")
#
# print("unique elements of second array")
#
# uni1=np.setdiff1d(arr1,arr)
#
# print(uni1)


# import numpy as np
#
# list=[]
# rows=int(input("Enter No. Rows : "))
# column=int(input("Enter No. of Columns : "))
#
#
#
# for i in range(1,(rows*column)+1):
#     num=int(input("Enter Element : "))
#     list.append(num)
#
# arr=np.array(list)
# arr1=arr.reshape(rows,column)
# print(arr1)
# print("--------------------------------------------------")
# sum=np.sum(arr1,axis=0)
# print(sum)
# print("--------------------------------------------------")
# sum1=np.sum(arr1,axis=1)
# print(sum1)


#
# import numpy as np
# from numpy import random
#
# arr=np.random.randint(1,20,18).reshape(2,3,3)
# print(arr)
#
# print("-----------------------------------------------------")
#
# sum=np.sum(arr,axis=0)
# print(sum)
#
# print("------------------------------------------------------")
#
# sum1=np.sum(arr,axis=1)
# print(sum1)
#
# print("------------------------------------------------------")
#
#
# sum2=np.sum(arr,axis=2)
# print(sum2)


# import numpy as np
# from numpy import random
#
# arr=np.random.randint(1,10,9).reshape(3,3)
# print(arr)
#
# num=int(input("Enter Any No. : "))
#
# add=arr+num
# print(add)
#
# print("---------------------------------------")
#
# sub=arr-num
# print(sub)
#
# print("----------------------------------------")
#
# mul=arr*num
# print(mul)
#
# print("----------------------------------------")
#
# divi=arr/num
# print(divi)


# import numpy as np
#
# arr=np.array([1,3,7,2,6,8,3,7])
# print(arr)
#
# print("--------------------------------------------")
#
# print(arr[1:5])
# print("-------------------------------")
# print(arr[2::])
# print("-------------------------------")
# print(arr[:-4:-1])


# import numpy as np
#
# arr=np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
# print(arr[1])
#
#
# print(arr[2,1:3])
#
# print("---------------------------------")
#
# print(arr[0:3,2:3])
#
# print("------------------------------------")
#
# print(arr[1:3,0:2])


# class Student:
#     def __init__(self):
#         self.name="Dewang"
#         print("in Student Init")
#     def disp(self):
#         print(self.name)
#     class python:
#         def __init__(self,ref):
#             self.name="Debu"
#             self.ref=ref
#             print("in python init")
#         def show(self):
#             print("In python show ")
#
#         def __str__(self):
#             return self.ref.name
#
# s1=Student()
# s1.disp()
# print("------------------------------")
# s2=Student.python(s1)
# s2.show()
# print(s2)


# from multipledispatch import dispatch
#
# class A:
#
#     def __init__(self):
#         print("in init")
#
#     @dispatch(int)
#     def show(self,num):
#         print(num)
#
#     @dispatch(str)
#     def show(self,str):
#         print(str)
#
#
# a=A()
# a.show('dewang')


# Write three functions start(), stop(), and pause() that simply print a message. Accept input from the user:
# if 1 is entered, call start(),
# if 2 is entered, call stop(),
# if 3 is entered, call pause(). Use match...case for the implementation.


#
# def start():
#     print("START")
#
#
# def stop():
#     print("STOP")
#
#
# def pause():
#     print("PAUSE")
#
#
#
#
# num=int(input("Enter 1,2,3(start,stop,pause) :  "))
#
# match num:
#     case 1 :
#         start()
#
#     case 2 :
#         stop()
#
#     case 3 :
#         pause()
#
#     case _:
#         print("Invalid Entry !!!!!!!! ")


# Define a function that accepts a number and returns if the number is:
# Even
# Odd Use match...case to return appropriate strings.


# def Accpt(num):
#     match num%2 :
#         case 0:
#             return 'Even'
#         case 1:
#             return 'Odd'
#
#
#
#
# a=Accpt(11)
# print(a)


# Write a function that accepts a list of numbers and returns the largest number using:
# A normal function
# A lambda function

#
# list=[x for x in range(1,6)]
#
#
# def Large(l1):
#     return max(l1)
#
#
# l=Large(list)
# print(l)

#
# -----------------------------------------------------------
# list=[x for x in range(1,7)]
# (lambda list: [print(max(list)) ])(list)

# larg=lambda list: [print(max(list))]
# larg(list)


# Create three functions: task1(), task2(), and task3(). Now, define a function execute(func) that accepts any function as
# an argument and invokes it. Call the execute() function, passing each of the three functions in turn.


# def task1():
#     print("Task1")
#
# def task2():
#     print("Task2")
#
# def task3():
#     print("Task3")
#
#
#
#
# def execute(func):
#     func()


# execute(task1)
# execute(task2)
# execute(task3)


# Write a function that accepts a dictionary using variable keyword arguments (**kwargs) and print the key-value pairs.


# dict={str(x):x*2 for x in range(1,6)}
#
# def Accpt(**kwargs):
#     for i,j in kwargs.items():
#         print(f"{i}:{j}")
#
# Accpt(**dict)


# Define a function that accepts a string and returns a list of consonants from the string using both:
# A normal function
# A lambda function

# list=[]
# def Accpt(str):
#     st='aeiouAEIOU'
#     for i in str:
#         if i not in st:
#             list.append(i)
#     print(list)
#
# Accpt('dewang')


# Accpt=lambda str:[i for i in str if i not in 'aeiouAEIOU']
# print(Accpt('dewang'))


# Define a nested function where the outer function accepts two numbers and the inner function multiplies them.
# Invoke the nested function correctly.


# def outer(num1,num2):
#     print(f"num1={num1},num2={num2}")
#
#     def inner():
#         mul=num1*num2
#         print("multiplication = ",mul)
#     inner()
#
#
# outer(2,4)

#
# class base1:
#     def __init__(self):
#         print("Base1")
#     def disp(self):
#         print("Base1 disp")
#
# class base2:
#     def __init__(self):
#         print("Base2")
#     def disp1(self):
#         print("Base2 disp")
#
#
# class sub(base1,base2):
#
#     def __init__(self):
#         base1.__init__(self)
#         base2.__init__(self)
#         print("in Sub")
#
#
# s=sub()
# s.disp()
# s.disp1()


# from abc import ABC,abstractmethod
#
# class Person(ABC):
#     def walk(self):
#         print("Walk")
#     def eat(self):
#         print("Eat")
#     def sleep(self):
#         print("Sleep")
#     @abstractmethod
#     def perform_duties(self):
#         pass
#
# class Teacher(Person):
#     def perform_duties(self):
#         print("Teacher")
#
# class Housewife(Person):
#     def perform_duties(self):
#         print("Housewife")
#
# class Solider(Person):
#     def perform_duties(self):
#         print("Soldier")
#
# def Perform(ref):
#         ref.walk()
#         ref.eat()
#         ref.sleep()
#         ref.perform_duties()
#         print("------------------------------")
#
#
#
# Perform(Teacher())
# Perform(Housewife())
# Perform(Solider())


# class VotingNotAllowedException(Exception):
#     pass
#
# class Voter():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         if (self.age) < 18:
#             raise VotingNotAllowedException("You Cannot Vote !!!!")
#         else:
#             print("You can Vote ")
#
# age=int(input("Enter Your Age : "))
#
# try:
#     v=Voter("Dewang",age)
# except Exception as e:
#     print(e)


#
# class Students:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def getname(self):
#         return self.name
#
#     def getage(self):
#         return self.age
#
#     def __str__(self):
#         return (f"Name={self.name}\tAge={self.age}")
#
#
# s1=Students("dewang",22)
# s2=Students("Tushar",21)
# s3=Students("Vipul",23)
# s4=Students("Saurabh",25)
#
# list=[s1,s2,s3,s4]
#
# for i in list:
#     print(i)
# print("--------------------------------------")
#
# list.sort(key=Students.getage)
#
# for i in list:
#     print(i)


from pandas import *

# first=Series([1,3,6,2,7],index=[1,2,3,4,5])
# print(first)


# mydict={1:'de',2:'yus',3:'aswdx',4:'hkj',5:'adb'}
# print(mydict)
# first=Series(mydict)
# print(first)

#
# first=Series([1,4,5,3,6,8,9,2])
# print(first)
# first.index=['a','b','c','d','e','f','g','h']
# print(first)
# print(first[1])
# first[1]=65
# print(first)


#
# mylist=[]
# mylist1=[]
#
# for i in range(1,6):
#     subj = input("Enter Subject :")
#     num = int(input("Enter marks : "))
#
#     mylist.append(num)
#     mylist1.append(subj)
#
# first=Series(mylist,index=mylist1)
# print(first)


# mydict={'Virat':35000,'Rohit':25000,'Rishabh':8900,'Shubman':20000,'Siraj':500}
#
# first=Series(mydict)
# print(first)


# list=[x for x in range(1,11)]
# first=Series(list)
# print(first)
# print(first[2])
# print(first[3:7])
# print(first[:3])
# print(first[6:])


# from pandas import *
#
# mydict={"Name":['Sachin','Rahul','Anil'],"Age":[30,35,38]}
# print(mydict)
# mydataframe=DataFrame(mydict)
# print(mydataframe)
# print("\n")
# print(type(mydataframe))

#
#
#
# from pandas import *
#
# mydataframe=DataFrame({"proid":range(1,5),"proname":['soap','perfume','deo','powder']})
# print(mydataframe)
# mylist=mydataframe["proid"].values.tolist()       # extract values of "proid" only and convert them to list
# print(mylist)
# mylist=mydataframe[["proname","proid"]].values.tolist() # extract values of "proname and proid" and convert them to list
# print(mylist)
# mylist1=mydataframe[["proid","proname"]].values.tolist()
# print(mylist1)


# def myfun(*args):
#
#     total=sum(args)
#     return total
#
# s=myfun(2,3,5)
# print(s)


# from pandas import *
#
# mydataframe=DataFrame({"proid":[1,2,3,4,5],"proname":['abc','asd','wfe','wfasc','acacs'],"price":[234,45,233,456,123]},index=[1,2,3,4,5])
# print(mydataframe)
#
#
# print("---------------------------------------")
#
# list=mydataframe.values.tolist()
# print(list)
#
# list=mydataframe.iloc[[1,3],[0,1]].values.tolist()
# print(list)
#
# print("--------------------------------------------------")
# print(mydataframe.loc[2:4])


# import pandas as pd
#
# #
# df1 = pd.DataFrame({1: 'A', 2: 'B'},index=[3,4])
# df2 = pd.DataFrame({2: 'B', 3: 'C'},index=[5,5])
# with pd.ExcelWriter("vita1.xlsx") as s:
#     df1.to_excel(s, sheet_name="abc", index=False)
#     df2.to_excel(s, sheet_name="ABCS", index=False)



#
# 10) create a class "Car" with two instance members i.e. "model(string)" and "isautomatic(boolean)"
# have getter methods also.
# create 5 to 6 objects by passing model name and True or False for "isautomatic".
#
# create a list and store all the objects inside it.
#
# now create one more list and in that list store all the objects from first list where "isautomatic" is True.
# Print both the lists.


# class Car:
#
#     def __init__(self,model,isauto):
#         self.model=model
#         self.isauto=isauto
#
#     def getstring(self):
#         return self.model
#
#     def getboolean(self):
#         return self.isauto
#
#     def __str__(self):
#         return f"{self.model}\t{self.isauto}"
#
#
#
# c1=Car("abc",True)
# c2=Car("bas",False)
# c3=Car("sdc",False)
# c4=Car("nja",True)
# c5=Car("fvb",True)
#
# list=[c1,c2,c3,c4,c5]
#
# l1=[]
#
# for i in list:
#     if i.isauto==True:
#         l1.append(i)
#
# for i in l1:
#     print(i)



# dict1={1:"ghs",2:"jhg",6:"jhg",3:"hjfv",7:"hgj"}
# dct2=dict(sorted(dict1.items(),key= lambda x:x[0]))
# print(dct2)



# str="restart"
# mylist=list(str)
# temp=mylist[0]
#
# for i in range(1,len(mylist)):
#     if mylist[i]==temp:
#         mylist[i]='$'
#
# print("".join(mylist))
#

# n=int(input("Enter the num:"))
#
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(1,i+2):
#         print(k,end=" ")
#     for l in range(i,0,-1):
#         print(l,end=" ")
#
#     print()
#
# set1=set(chr(i) for i in range(97,123))
# str=input("Enter the string:").lower()
# # set2=set(i for i in str if i.isalpha())
# # if (set1==set2):
# #     print("panigram")
# # else:
# #     print("not")
#
# s1=set(str)
# s1==26
#




#
# class Student:
#     def __init__(self,name,age,address,qualification):
#         self.name=name
#         self.age=age
#         self.address=address
#         self.qualification=qualification
#     def __str__(self):
#         return f"Name={self.name}\tAge={self.age}\tAddress={self.address}\tQualification={self.qualification}"
#
#
#
# s1=Student("Dewang",22,"juhu_taj","BE")
# s2=Student("Dsdf",24,"taj","BE")
# s3=Student("fddb",25,"juhu_taj","BE")
# s4=Student("juyt",21,"juhu_taj","BE")
# s5=Student("zxcv",23,"juhu_taj","BE")
#
#
# mydict={1:s1,2:s2,3:s3,4:s4,5:s5}
#
# roll=int(input("Enter Roll no. : "))
#
#
# if roll in mydict:
#     print(mydict[roll])





# import numpy as np
# from numpy import random
#
# random.seed(18)
#
# arr=np.random.randint(1,10,18).reshape(2,3,3)
#
# arr1=np.stack(arr,axis=0)
# print(arr1)
# print("------------------------------")
# arr2=np.stack(arr,axis=1)
# print(arr2)
# print("-------------------------------")
# arr3=np.stack(arr,axis=2)
# print(arr3)
#


#
#
# import numpy as np
# from numpy import random
#
# random.seed(18)
#
# arr=np.random.randint(1,10,18).reshape(2,3,3)
# print(arr)
# print("-----------------------------------------------")
#
#
# arr1=np.sum(arr,axis=0)
# print(arr1)
# print("--------------------------------------------")
# arr2=np.sum(arr,axis=1)
# print(arr2)
# print("--------------------------------------------")
# arr3=np.sum(arr,axis=2)
# print(arr3)


#
#
# import numpy as np
#
# arr=np.array([i for i in range(1,10)])
# print(arr)
#
# mask=(arr>2)&(arr%2==0)
#
# arr1=arr[mask]
#
# print(arr1)



import pandas as pd

list=[]

for i in range(1,11):
    num=int(input("Enter Elements : "))
    list.append(num)

first=pd.Series(list)
print(first)

print(first[2])


print(first[3:7])

print(first[-4::-1])






























