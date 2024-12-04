# from Temp1 import MyModule
# from Temp1.MyModule import Person
#
# p=Person("Dewang",22)
# print(p)




# class A:
#     def disp(self):
#         print("In A ")
# class B(A):
#     def disp(self):
#         print("In B ")
# class C(B):
#     def disp(self):
#         print("In C ")
#     def print(self):
#         print("In C print ")
#
# def perform(ref):
#     ref.disp()
#     if isinstance(ref,C):
#         ref.print()
#
#
#
# perform(A())
# perform(B())
# perform(C())



# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end=" ")
#     for k in range(1,i*2):
#         print(i,end=" ")
#     print()





# class A:
#     def __init__(self):
#         print("In A ")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('In B ')
# class C(A):
#     def __init__(self):
#         super().__init__()
#         print("In C")
#
# c=C()
# print("-----------------------------------")
# b=B()


# class A:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,obj):
#         return self.x+obj.x
#     def __sub__(self, obj):
#         return self.x-obj.x
#     def __mul__(self, obj):
#         return self.x*obj.x
#
#
# a=A(2)
# a1=A(4)
# a2=A(5)
# a3=(a*a2)+a1
# print(a3)












# mydict={1:'dewang',3:'vipul',2:'aye',4:'om'}
# print(mydict)
#
# mydict[4]='hello'
# print(mydict)
# mydict.pop(4)
# print(mydict)
# print(mydict.keys())
# print(mydict.values())
# print(sorted(mydict))
# for i in mydict.values():
#     print(i)


# mydict={x:x**2 for x in range(1,10)}
# print(mydict)


#
# name=['Dewang','vipul','om','tushar']
# age=[22,24,21,25]
#
# mydict={name:age for (name,age) in zip(name,age)}
# print(mydict)
# print(sorted(mydict))



# mydict={}
# print("Enter Names : ")
# for i in range (1,6):
#     name=input()
#     mydict[i]=name
#
# print(mydict)





# mydict={'soap':100,'deo':300,'perfume':400}
#
# print(mydict)
#
# pname=input("Enter Product Name : ")
# if pname in mydict:
#     print(mydict[pname])
# else:
#     print("Prodct Not Present !!!!! ")


# Access the fifth value of each key from the dictionary.

# mydict={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
#
# for i in mydict:
#     print(mydict[i][4])




# 2) Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# mydict={0: 10, 1: 20}
# mydict[2]=30
# print(mydict)



# 3) Write a Python script to check whether a given key already exists in a dictionary.

# mydict={1:43,4:23,2:67,3:69}
# print(mydict)
# key=int(input("Enter key :" ))
#
# if key in mydict.keys():
#     print("Exists ")
# else:
#     print("Not Exists ")



# 4) Write a Python program to count the values associated with key in a dictionary.
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True

# Sampledata = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# count=0
# for i in Sampledata:
#     if i['success']:
#         count+=1
# print(count)



# 5) Write a Python program to create a dictionary from two lists without losing duplicate values.
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})

#
# list=['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# list2=[1, 2, 2, 3]
#
# mydict={list:list2 for (list,list2) in zip(list,list2)}
# print(mydict)





# Write a Python program to check a dictionary is empty or not.

# mydict={}
#
# if not mydict:
#     print("Empty")
# else:
#     print(mydict)

#
# 7) Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


# from collections import Counter
#
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3=Counter(d1)+Counter(d2)
# print(d3)




mydictionary1={'Names':['Rohit','Ganesh','SRK','Akshay'],'age':40,'addresses':['Mumbai','Delhi','Kolkara','Banglore'],'emails':['actor.gmail.com','movie.gmail.com']}
count=0
for i in mydictionary1.values():
    if isinstance(i,list):

        for j in i:
            print(j)
        # count+=1

# print(j)









