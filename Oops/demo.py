# from multipledispatch import dispatch
#
# class A:
#     @dispatch(int)
#     def disp(self,val):
#         print(val)
#     @dispatch(str)
#     def disp(self,val):
#         print(val)
#     @dispatch(int,str)
#     def disp(self,val,val1):
#         print(val,val1)
#
# a=A()
# a.disp(5)
# a.disp('Dewang')
# a.disp(7,'Debu')

#
# class Bird:
#     def fly(self):
#         print("Bird is flying")
# class SuperMan:
#     def fly(self):
#         print("Superman is flying")
# class Person:
#     def talk(self):
#         print("Person is flying")
#
# def perform(obj):
#     print("Type of obj is\t",type(obj))
#     obj.fly()
#
# b1=Bird()
# perform(b1)
# s1=SuperMan()
# perform(s1)
# p1=Person()
# perform(p1)   #  AttributeError: 'Person' object has no attribute 'fly'

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
# class student:
#
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __str__(self):
#         return self.name+"\t"+str(self.age)
#
#     def getname(self):
#         return self.name
#
#     def getage(self):
#         return self.age
#
# s1=student("Dewang",22)
# s2=student("Vipul",21)
# s3=student("Tushar",21)
# s4=student("Saurabh",23)
#
#
# mylist=[s1,s2,s3,s4]
#
# for i in mylist:
#     print(i)
#
#
# mylist.sort(key=student.getage)
# print("----------------------------------------------------")
# for i in mylist:
#     print(i)

# print("----------------------------------------------------")
# mylist.sort(key=student.getname)
# for i in mylist:
#     print(i)
#
# print("----------------------------------------------------")
# mylist.sort(key=student.getname,reverse=True)
# for i in mylist:
#     print(i)
#
#
#



#
#
# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
#     def __str__(self):
#         return "Name : "+self.name+"\t"+"Age : "+str(self.age)
#
#     def getname(self):
#         return self.name
#
#     def getage(self):
#         return self.age
#
# s1=A("dewang",22)
# s2=A("Tushar",21)
# s3=A("Vipul",23)
#
# li=[s1,s2,s3]
#
# li.sort(key=A.getage)
#
# for i in li:
#     print(i)






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
# m2 = m1
# print(hex(id(m1)))
# print(m1.getvar())
# del m1     # it will not delete the object as m2 reference is also referring to the same object
# print("After deleting m1  ", m2.getvar())
# print("done")




#
# class bird:
#     def fly(self):
#         print("Bird fly")
# class krrish:
#     def fly(self):
#         print("Krrish fly")
# class person:
#     def swim(self):
#         print("Swim person")
#
# def perform(ref):
#     if(hasattr(ref,"fly")):
#         ref.fly()
#     else:
#         ref.swim()
#
# perform(bird())
# perform(krrish())
# perform(person())


#
# class A:
#     var=11
#     def __init__(self,num,num1):
#         self.num=num
#         self.num1=num1
#         print("Instance Variable",self.num,self.num1)
#
# a=A
# a1=A(10,20)
#
# print("Class Variable",a.var)


#
# class a:
#     def __init__(self):
#         print("a")
#
# class b:
#     def __init__(self):
#         print("b")
# class c(a,b):
#     def __init__(self):
#         a.__init__(self)
#         b.__init__(self)
#         print("c")
#
#
# c=c()


# class a:
#     def __init__(self):
#         print("In A")
# class b(a):
#     def __init__(self):
#         super().__init__()
#         print("In B")
#
# class c(b):
#     def __init__(self):
#         super().__init__()
#         print("In C")
#
# c=c()






# class a:
#     def __init__(self):
#         print("In A")
#
#
# class b(a):
#     def __init__(self):
#         super().__init__()
#         print("In B")
#
#
# class c(a):
#     def __init__(self):
#         super().__init__()
#         print("In C")
#
#
# c=c()
# print()
# b=b()


#
#
# class a:
#     def __init__(self):
#         print("In A")
#
#
# class b(a):
#     def __init__(self):
#         super().__init__()
#         print("In B")
#
#
#
#
# b = b()
#
#
#
#






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
#





# from dataclasses import dataclass
# @dataclass
# class A:
#     name : str
#     age : int
#     height : float
#
# a=A("Tushar",22,5.9)
# print(a)
#

#
# mylist1 = [10,20,30,40]
# mylist2 = [100,200,300,400]
#
# print(mylist1)
# print(mylist2)
#
# result = map(lambda x,y:x+y,mylist1,mylist2)
# print(result)
# print(list(result))
#




# l = ['sat', 'bat', 'cat', 'mat']
#
# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)

# what does map(list,l) do ?
    # map(list,l) returns  [['s','a','t'],['b','a','t'],['c','a','t'],['m','a','t']]

# for i in map(list,l):
#     print(i)
#
# for i in map(list,l):
#     for j in i:
#         print(j,end="     ")
#     print("\n")
#
















