# Minelist=[1,22,12,6,32]
# print(Minelist)
# print(type(Minelist))
# print(len(Minelist))
# print(Minelist[3])
# Minelist.append(4)
# print(Minelist)
# Minelist.remove(22)
# print(Minelist)
# Minelist.pop(2)
# print(Minelist)
# Minelist.reverse()
# print(Minelist)
# Minelist[2]=10
# print(Minelist)
# elist=[]
# for i in range(1,6):
#     num=int(input())
#     elist.append(num)
# print(elist)
#
# clist = [[1,'Hello',143,'Bye'],[2,'hleeww',3,'by']]
# print(clist)
# print(len(clist))
#
# print(clist[0])
# print()
#
#
# print(clist[1])
# print()
#
# for i in clist[0]:
#     print(i)
#
# print()
#
# for i in clist[1]:
#     print(i)
#
#
# mylist = [10,20,30,40]
#
# print(mylist)
#
# mylist.append(90)
# mylist.insert(2,"welcome")
#
# print(mylist)

# mylist = [10,"hello",4.5,False,'A']
#
# print(mylist)
#
# var = -1
# while var >= -5:
#     print(mylist[var])
#     var -= 1
#
#
# mylist = [23,12,6,8,11,9,13]
# # print(mylist)
# # mylist.sort()
# # print(mylist)
# # mylist.sort(reverse=True)
# # print(mylist)
# for i in mylist:
#     print(i)


# how to extend the list without append
# x = [10, 20, 30]
# y = [40, 50, 60]
# # x+=y
# print(x)

# x[:0]=y    # from begining to 0th index
# print(x)
#
# x[3:]=y     #from 3rd to last
# print(x)


############################## FUNCTION #################################

# def myfun1():
#     print("First")
#     print("Second")
#     print("Third")
# myfun1()
#
# print(type(myfun1()))
# print(id(myfun1()))


# String concatenation

# def myfun():
#     num1=100
#     print("Value of Num is\t"+str(num1))
#     print("Value of Num is\t",num1)
# myfun()
# print("Done")
#
# print(type(print))
# print(id(print))



# global and local variable
# var=500
#
# def disp():
#     print("value of var is\t",var)
#
# def myfun():
#     var=100
#     print("value of var is\t",var)
#     disp()
# myfun()




# Global Variable and Local variable
# var=500  # global variable
#
# def disp():
#    return var  # global var
#
# def myfun():
#     var=100  # local variable
#     print("var inside main\t",var) # by default local is given precedence
#     print("global var is\t",disp())
# myfun()


# Global Variable and Local variable
# var=500  # global variable
#
# print("Value of global var is\t",var)
# def myfun():
#     global var     #  try commenting this line
#     var=300  # changing global variable
#     print("var inside main\t",var) # by default local is given precedence
# myfun()
# print("Value of global var is\t",var)



# global and local variables have same name
#
# var=500
# def fun1():
# 	print("global var is  ",var)
# def fun2():
# 	var=200
# 	print("local var is  ",var)
# def fun3():
# 	global var
# 	var=600
# 	print("global var is   ",var)
#
# fun1()
# fun2()
# fun3()
#
# print("Global variable is    ",var)

# def myfun():
#     return 100 ,200,300
#
# a,b,c=myfun()
# print(a,b,c)
#
#
# def calculation(a, b):
#     return a + b, a - b
#
# # get result in tuple format
# # unpack tuple
# add, sub = calculation(40, 10)
# print(add, sub)



# call by value concept
# def change(var):
#     print("id of var before changing var is\t",id(var))
#     var+=1
#     print("Value of var is\t",var)
#     print("id of var after changing var is\t",id(var))
# num=10
# print("id of num is\t",id(num))
# print("before\t",num)
# change(num)
# print("after\t",num)
#


# call by reference concept
# def change(mylist):
#     print("id of mylist before changing var is\t",id(mylist))
#     mylist.append(5)
#     print("id of mylist after changing var is\t",id(mylist))
#
# mainlist=[1,2,3,4]
# print("Mainlist before calling function\t",mainlist)
# print("id of mainlist is\t",id(mainlist))
#
# change(mainlist)
# print("Mainlist after calling function\t",mainlist)





""" Python provides a built-in function, to determine which objects are callable. The function is callable().
If the object passed as a parameter to the callable() prints TRUE then that object is callable.
If it displays FALSE then it is not callable in Python.
 """
#
# def main(fun):
#     if callable(fun):
#         fun()
#     else:
#         print("You passed non-callable argument to main function")
#     print("inside caller function")
#
# def disp():
#     print("inside disp function")
#
# main(disp)    # works
# temp=100
# main(temp)    # you won't get TypeError
#

"""
Closure in Python is an inner function object, a function that behaves like an object, that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing.
"""
#
# def outer():
#     def inner():     # it's a closure
#         print("inside inner function")
#     print("inside outer function")
#     return inner
#
# var1=outer()
# var1()

# place the breakpoint at both the print statements,debug and check the call stack


# When a function decorated with @dispatch is called,
# the library inspects the arguments passed to the function
# and dispatches the call to the appropriate implementation
# based on the type and number of arguments.
#
# from multipledispatch import dispatch
#
#
# # passing two parameters
# @dispatch(int, int)
# def product(first, second):
#     result = first * second
#     print(result)
#
#
# # passing three parameters
# @dispatch(int, int, int)
# def product(first, second, third):
#     result = first * second * third
#     print(result)
#
#
# # you can also pass data type of any value as per requirement
# @dispatch(float, float, float)
# def product(first, second, third):
#     result = first * second * third
#     print(result)


# calling product method with 2 arguments
# product(20, 4)
# product(2, 3, 2)
# product(2.2, 3.4, 2.3)
#

#
# mystring = "Hello dewang"
# print(mystring)
# mylist = mystring.split()
# print(mylist)
# print(mylist[1])

# mystr="Hello"
# mystr1="hello"
#
# if mystr==mystr1 :
#     print("true")
# else:
#     print("false")
#
# if mystr.casefold()==mystr1.casefold():
#     print("true")
# else:
#     print("false")


#
# def myfun():
#     num1=100
#     print("Value of Num is\t"+str(num1))
#     print("Value of Num is\t",num1)
# myfun()
# print("Done")
#
# print(type(print))
# print(id(print))


# var=500
#
# def disp():
#     print("value of var is\t",var)
#
# def myfun():
#     var=100
#     print("value of var is\t",var)
#     disp()
# myfun()
#
# call by reference concept
# def change(mylist):
#     print("id of mylist before changing var is\t",id(mylist))
#     mylist.append(5)
#     print("id of mylist after changing var is\t",id(mylist))
#
# mainlist=[1,2,3,4]
# print("Mainlist before calling function\t",mainlist)
# print("id of mainlist is\t",id(mainlist))
#
# change(mainlist)
# print("Mainlist after calling function\t",mainlist)




# call by value concept
# def change(var):
#     print("id of var before changing var is\t",id(var))
#     var+=1
#     print("Value of var is\t",var)
#     print("id of var after changing var is\t",id(var))
# num=10
# print("id of num is\t",id(num))
# print("before\t",num)
# change(num)
# print("after\t",num)

#
# print(dir(__builtins__))        #   built-in namespace
# print("\n\n")
# print("Type of builtins namespace is\t",type(__builtins__))
#
# k=100
# def disp():
#     def inner():
#         print("inside inner")
#     var=40
#     print("hello")
#     print(locals())
#     print("\n")
#     print("Type of local namespace is\t",type(locals()))
#
# num1=200
# print("\n\n\n")
# print(globals())
# print("\n\n")
# print("Type of global namespace is\t",type(globals()))
# print("\n\n")
# disp()



# print(dir(__builtins__))        #   built-in namespace
# print("\n\n")
# print("Type of builtins namespace is\t",type(__builtins__))
#
# k=100           # global for everyone
# def disp():
#     k=30        # local for disp but enclosing for inner
#     def inner():
#         k=60    # local for inner
#         print("inside inner")
#         print("local namespace for inner\t",locals())
#     print("hello")
#     print("local namespace for disp\t",locals())
#     print("\n")
#     print("Type of local namespace is\t",type(locals()))
#     inner()
#
# num1=200
# print("\n\n\n")
# print(globals())
# print("\n\n")
# print("Type of global namespace is\t",type(globals()))
# print("\n\n")
# disp()



# print(dir(__builtins__))        #   built-in namespace
# print("\n\n")
# print("Type of builtins namespace is\t",type(__builtins__))
#
# k=100           # global for everyone
# def disp():
#     k=30        # local for disp but enclosing for inner
#     r=60
#     def inner():
#         k=60    # local for inner
#         print("inside inner")
#         print("local namespace for inner\t",locals())
#     print("hello")
#     print("local namespace for disp\t",locals())
#     print("\n")
#     print("Type of local namespace is\t",type(locals()))
#     inner()
#
# num1=200
# print("\n\n\n")
# print(globals())
# print("\n\n")
# print("Type of global namespace is\t",type(globals()))
# print("\n\n")
# disp()

#
#
#
# print(dir(__builtins__))        #   built-in namespace
# print("\n\n")
# print("Type of builtins namespace is\t",type(__builtins__))
#
# k=100           # global for everyone
# def disp():
#     k=30        # local for disp but enclosing for inner
#     r=60
#     def inner():
#         k=60    # local for inner
#         print("inside inner")
#         print("let's access 'r' from enclosing scope\t",r)
#         print("let's access 's' from enclosing scope\t",s) # no problem even if 's' is defined below
#         print("local namespace for inner\t",locals())    # not only "k" but "r" also
#     print("hello")
#     print("local namespace for disp\t",locals())
#     print("\n")
#     print("Type of local namespace is\t",type(locals()))
#     s=800
#     inner()
#
# num1=200
# print("\n\n\n")
# print(globals())
# print("\n\n")
# print("Type of global namespace is\t",type(globals()))
# print("\n\n")
# disp()
# import time
# i=0
# start=time.time()
# name=input("enter your name")
# age=int(input("enter your age"))
# message="Name is {} and Age is {}"
# print(message.format(name,age))
# print("This program took\t",time.time()-start,"\tseconds")



#
#
# add=lambda x,y:x+y
# print("add is the reference to the object of type\t",type(add))
# print("address of the object where add refers to is\t", id(add))
# print(add(5,6))

#
#
# class First:
#     def mainfunction(self):
#         print("address of self is\t",id(self))
#         print("type of self is\t",type(self))
#         print("inside main function")
# f1=First()
# print("address of f1 is\t",id(f1))
# f1.mainfunction()
#
# f2=First()
# print("address of f2 is\t",id(f2))
# print("let's invoke mainfunction with f2")
# f2.mainfunction()
#

#
# class MyClass:
#     var=0
#     def __init__(self,var):
#         self.var=var
#     def getvar(self):
#         return self.var
#     def __del__(self):
#         print("No Reference is left for {}".format(self))
#
# m1 = MyClass(10)
# print(hex(id(m1)))
# print(m1.getvar())
# m1 = MyClass(10)
# print(hex(id(m1)))
# print(m1.getvar())
# del m1     # use of del statement to delete the object
# print("done")
#
#
#

#
# class Base:
#     def __init__(self,num):
#        self.num=num
#     def disp(self):
#         print(self.num)
# s1=Base(10)
# print(s1)
# print(hasattr(s1,'disp'))
# print(hasattr(s1,'__init__'))

#
#
# print(dir(__builtins__))        #   built-in namespace
# print("\n\n")
# print("Type of builtins namespace is\t",type(__builtins__))
#
# k=100           # global for everyone
# def disp():
#     k=30        # local for disp but enclosing for inner
#     r=60
#     def inner():
#         k=60    # local for inner
#         print("inside inner")
#         print("let's access 'r' from enclosing scope\t",r)
#         print("let's access 's' from enclosing scope\t",s) # NameError: free variable 's' referenced before assignment in enclosing scope
#         print("local namespace for inner\t",locals())    # not only "k" but "r" also
#     print("hello")
#     print("local namespace for disp\t",locals())
#     print("\n")
#     print("Type of local namespace is\t",type(locals()))
#     inner()
#     s=800
#
# num1=200
# print("\n\n\n")
# print(globals())
# print("\n\n")
# print("Type of global namespace is\t",type(globals()))
# print("\n\n")
# disp()


# age=int(input(" enter age "))
# print("Hii Myself dewang I'm {} year old".format(age))
#
# mess="I'm  {} year Old "
# age=int(input(" enter age "))
# print(mess.format(age))

# print("Myself {} I'm {} year old".format("Dewang",22))
# name=input("Name : ")
# print(f"Hello {name} , how are you")


# creating and accessing "docstring" for user defined functions

# def square(num):
#     ''' this function accepts a number and return its square '''
#     return num*num
#
# print(square(10))
# # print(int.__doc__)
#
# help(print())

# sum=lambda x,y:print(x+y)
# sum(4,5)

# print((lambda x,y:x+y)(23,45))




# class A:
#     def __init__(self,a,c,b):
#         print("Inside init")
#         self.a=a
#         self._b=b
#         self.__c=c
#
#     def disp(self,Num):
#         print(Num)
#
# ref=A(1,2,3);
#
# ref.disp(4)
# print(ref.a)
# print(ref._b)
# print(ref._A__c)
#







#
# # We do not have method overloading in Python
#
# class Base:
#     def __init__(self,num1):
#         self.num1=num1
#         print("Base class constructor ",self.num1)
#     def disp1(self):
#         print("Base class disp1 method")
#
#
# class Sub(Base):
#     def __init__(self):
#         super().__init__(100)    # invoking Base class parameterized constructor explicitly
#         print("Sub class constructor")
#     def disp1(self,val1):      # method hiding
#         print("Sub class disp1 method ",val1)
#
#
# s1 = Sub()
# print(id(s1))
#
# s1.disp1(200)







# from abc import ABC, abstractmethod
#
# class Person(ABC):
#     def __init__(self):
#         print("inside Person default constructor")
#     def walk(self):
#         print("I can walk")
#     def talk(self):
#         print("I can talk")
#     def eat(self):
#         print("I can eat")
#     def sleep(self):
#         print("I can sleep")
#     @abstractmethod
#     def performduties(self):
#         pass
#
# class Teacher(Person):
#     def __init__(self):
#         super().__init__()
#         print("Teacher default constructor")
#     def performduties(self):
#         print("Perform teacher's duties")
#
#
# class HouseWife(Person):
#     def __init__(self):
#         super().__init__()
#         print("HouseWife default constructor")
#     def performduties(self):
#         print("Perform HouseWife's duties")
#
#
# class Soldier(Person):
#     def __init__(self):
#         super().__init__()
#         print("Soldier default constructor")
#     def performduties(self):
#         print("Perform Soldier's duties")
#
#
# def perform(ref):
#     ref.walk()
#     ref.talk()
#     ref.eat()
#     ref.sleep()
#     ref.performduties()
#
#
# perform(Teacher())
# perform(Soldier())
# perform(HouseWife())

# ob = Person()   #  TypeError: Can't instantiate abstract class Person with abstract method performduties


#
# import re
#
# pattern1="Vidya"
# mystring1="Vidyanidhi"
# print(re.match(pattern1, mystring1))
# mystring2="vidyanidhi"
# print(re.match(pattern1,mystring2))
# print(re.match(pattern1, mystring2,re.IGNORECASE))

# using map() function with tuple by passing lambda


#
# mytuple = (10,20,30,40)
# print(mytuple)
# print(type(mytuple))
#
# result = map(lambda x:x+2,mytuple)
# print(list(result))

#
# list=[1,34,2,45]
# list1=[3,6,32,78]
#
# dict={}
#
# for i,j in zip(list,list1):
#     dict[i]=j
#
# print(dict)
#
#

# dict={1:3,2:8,3:4,4:9}
# disct1={5:2,6:4,7:1,8:3}
#
# dict.update(disct1)
# print(dict)

# Players={'Rohit':{'runs':10000,'centuries':15},'Virat':{'runs':12000,'centuries':18}}
#
# for i,j in Players.items():
#     print(i)
#     for k,l in j.items():
#         print(k,l)


#
# dict={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
#
# for i in dict:
#     print(dict[i][4])




# 12) Write a Python program to convert list to list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
#  """
#
# lists=["Black", "Red", "Maroon", "Yellow"]
# lists1=["#000000", "#FF0000", "#800000", "#FFFF00"]
#
# dict=[{"color_name":name,"color_code":code}for name,code in zip(lists,lists1)]
# print(dict)


# Keyworded args (**vargs)
# Prime or not
# Reverse triangle
# Dispatch overloading
# Outer inner
# String slicing
# Switch case
# *vargs print sum



# def dis(fun):
#     print("In Display")
#     fun(name="Dewang",age=22,location="SMvita")
#
# def info(**kwargs):
#     print(kwargs)
#
# dis(info)


#
# prime=int(input("Enter no. : "))
# count=0
# for i in range(1,prime+1):
#     if prime%i==0 :
#         count+=1
#
#
# if count==2:
#     print("Prime")
# else:
#     print("Not Prime")

#
#
# from multipledispatch import dispatch
#
# class A:
#     @dispatch(int)
#     def disp(self,int):
#         print("In display of Int")
#         print(int)
#
#     @dispatch(str)
#     def disp(self,str):
#         print("In display of Int")
#         print(str)
#
#
# a=A()
# a.disp(7)
# a.disp('Dewang')

# str="Dewang"
# print(str[1:4])

# multiple inheritance , multiple parents have same method name

# class Base1:
#     def __init__(self,num1):
#         self.num1=num1
#         print("Base1 class constructor  ",self.num1)
#     def disp2(self):
#         print("Base1 disp2")
#
# class Base2:
#     def __init__(self,num2):
#         self.num2=num2
#         print("Base2 class constructor   ",self.num2)
#     def disp2(self):
#         print("Base2 disp2")
#
# class Sub(Base1,Base2):
#     def __init__(self):
#        Base1.__init__(self,100)
#        Base2.__init__(self,300)
#        print("Sub class constructor")
#     def disp3(self):
#         print("Sub disp3")
#
#
# s1 = Sub()
# s1.disp2()
# s1.disp3()

# class Base:
#     def __init__(self,num1):
#         self.num1=num1
#         print("base")
# class Sub(Base):
#     def __init__(self,num3,num2):
#         super().__init__(num3)
#         self.num2=num2
#         self.num3=num3
#         print("sub")
#     def show(self):
#         print(self.num3,"\t",self.num2)
#
# s1=Sub(100,200)
# s1.show()

#
#
# class A :
#     def __init__(self,num2):
#         self.num2=num2
#         print("in class A constructor")
#         print(num2)
#
#
# class B(A):
#     def __init__(self,num1):
#         super().__init__(num1+10)
#         print("in class B constructor")
#         print(num1)
#
#
#
# b=B(3)

#
# class weapon:
#     def attack(self):
#         print("Weapon Attack ")
# class gun(weapon):
#     def attack(self):
#         print("gun Attack ")
# class sword(weapon):
#     def attack(self):
#         print("Sword Attack ")
#
#
# def perform(ref):
#     ref.attack()
#
#
# perform(weapon())
# perform(sword())
#


#
# class Course:
#     def start(self):
#         print("Starting course")
#     def end(self):
#         print("Ending course")
#
# class MsCit(Course):
#     def start(self):
#         print("Starting Mscit course")
#
#     def end(self):
#         print("Ending Mscit course")
#
#
# class Basic(Course):
#     def start(self):
#         print("Starting Basic course")
#
#     def end(self):
#         print("Ending Basic course")
#
#
# class Dbda(Course):
#     def start(self):
#         print("Starting Dbda course")
#
#     def orientation(self):
#         print("\t Orientation of Dbda")
#
#     def end(self):
#         print("Ending Dbda course")
#
#
#
# def perform(ref):
#
#     ref.start()
#     print()
#
#     if isinstance(ref,Dbda):
#         ref.orientation()
#         print()
#
#     ref.end()
#     print("---------------------------------------")
#
#
# perform(MsCit())
# perform(Basic())
# perform(Dbda())


# num=int(input("Enter any Number : "))
#
# match(num):
#     case 1:
#         print("oyeeeeeee")
#     case 2:
#         print("Hlewwwwwwwwww")
#     case 3:
#         print("Byeeeeeeee")
#     case _:
#         print("Invalid no. ")




# disp=lambda x:[print(i) for i in range(1,x)]
# disp(6)
#


# var=lambda *args:print(args)
# var(1,3,5)

var=lambda:[print(i) for i in range(1,7)]
var()







