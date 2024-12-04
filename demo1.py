# mylist=[1,2,3,4,1,3,4,5,6,3,4]
# print(mylist)
#
# myset=set(mylist)
# print(myset)

# "update()" function to add two or more elements into set
#
# myset = {1,2,3,4,5}
#
# print(myset)
# print(type(myset))
#
# # adding a tuple
# myset.update((10,20,30))
#
# print(myset)
#
# # adding list and tuple
# myset.update(['A','B','C'],("hello","welcome"))
# print(myset)



# ________________________________________________________________________________________________

# mytupple=(1,'Dewang',True,100,'A')
#
# print(mytupple)
# print(mytupple[1])
# print(len(mytupple))



# def outer():
#     def inner():     # it's a closure
#         print("inside inner function")
#     print("inside outer function")
#     return inner
#
# var1=outer()
# var1()


# """
#
# The inner function maintains a reference to the variables in the scope of "outer" through closure, allowing it to access "num" even after outer has finished executing.
#
# The closure mechanism keeps the environment of "outer" function alive in memory as long as there's a reference to the "inner" function.
#
# """
#
#
# def outer():
#     num=100
#     def inner():     # it's a closure
#         print("inside inner function\t",num)
#     num=400
#     print("inside outer function")
#     return inner
#
# var1=outer()
# var1()


# class Account:
#     rate = 9  # class variable
#
#     def __init__(self, accid, name, balance):
#         self.accid = accid
#         self.name = name
#         self.balance = balance
#
#     def getAccid(self):  # instance method
#         return self.accid
#
#     def getName(self):  # instance method
#         return self.name
#
#     def getBalance(self):  # instance method
#         return self.balance
#
#     @classmethod
#     def getRate(cls):
#         return cls.rate
#
#     @staticmethod
#     def calculateEMI(no_of_years, load_amt):
#         return "calculated EMI per month"
#
#
# c1 = Account(1, "Abc", 40000)  # instance object
# c2 = Account(2, "Xyz", 70000)  # instance object
#
# print(c1.getAccid(), "\t", c1.getName(), "\t", c1.getBalance())
# print(c2.getAccid(), "\t", c2.getName(), "\t", c2.getBalance())
#
# print(Account.getRate())
#
# print(Account.calculateEMI(10, 200000))
# print(c1.__dict__)
# temp = Account  # class object
# print(temp.__dict__)
#








#
# class Bird:
#     def fly(self):
#         print("Bird is flying")
# class SuperMan:
#     def fly(self):
#         print("Superman is flying")
# class Person:
#     def talk(self):
#         print("Person is talking")
#
# def perform(obj):
#     print("Type of obj is\t",type(obj))
#     obj.fly()
#
# b1=Bird()
# perform(b1)
# s1=SuperMan()
# perform(s1)







# class Army:
#     def __init__(self):
#         self.name="Rahul"
#     def show(self):
#         print(self.name)
#     class Gun:
#         def __init__(self):
#             self.name="AK47"
#             self.capacity="75 Rounds"
#             self.length="34.3 in"
#         def __str__(self):
#             return self.name+"\t"+self.capacity+"\t"+self.length
#
# a1=Army()
# a1.show()
# g1=Army.Gun()
# print("\n")
# print(g1)








# class Army:
#     def __init__(self):
#         self.name="Rahul"
#     def show(self):
#         print(self.name)
#     class Gun:
#         def __init__(self,ref):
#             self.name="AK47"
#             self.capacity="75 Rounds"
#             self.length="34.3 in"
#             self.ref=ref
#         def __str__(self):
#             return self.ref.name+"\t"+self.name+"\t"+self.capacity+"\t"+self.length
#
# a1=Army()
# a1.show()
# g1=Army.Gun(a1)
# print("\n")
# print(g1)











# class First:
#     def __new__(cls):
#         print("inside __new__ dunder method")
#         instance=object.__new__(cls)
#         print("id of instance is\t",id(instance))
#         return instance
#     def __init__(self):
#         print("inside __init__ dunder method")
#
# f1=First()
# print("id of f1 is\t",id(f1))
# print("\n")
# print("done")


#
# from dataclasses import dataclass
#
# @dataclass
# class Person:
#     name: str ="Rohit"
#     age: int  = 35
#     height: float =5.8
#     email: str = "Rohit@gmail.com"
#
#
# p=Person() # now there is __init__() methods with default values which are provided in the class
#
# p1=Person("Sachin",50,5.1,"sachin@gmail.com")  # you can pass also explicitly
# print(p)
# print(p1)



# mylist=[1,5,3,7,2,8]
#
# print(mylist[2:5])
# print(mylist[-1:-3:-1])
#
# print(mylist[-2:2:-1])
#
#


# mylist=[num**2 for num in range(1,15,2)]
# print(mylist)


