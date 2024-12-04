# for i in range(1,6):
#     for j in range(0,i):
#         print("*",end="")
#     print()




# for i in range(1,6):
#     for j in range(0,6-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print(chr(64+i),end=" ")
#     print()
#
#
# for i in range(6-2,0,-1):
#     for j in range(0,6-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print(chr(64+i),end=" ")
#     print()




#
#
# n=int(input("Enter range : "))
# for i in range(1,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(1,i*2):
#         print(chr(64+k),end=" ")
#     print()
#
# for i in range(n-2,0,-1):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(1,i*2):
#         print(chr(64+k),end=" ")
#     print()




# str="restartr"
# list=list(str)
# temp=list[0]
#
# for i in range(1,len(list)):
#     if list[i]==temp:
#         list[i]='$'
#
# print("".join(list))



# class Outer:
#     def __init__(self,num):
#         self.num=num
#         print("Num = ",self.num)
#     def disp(self):
#         print("In Outer disp Num = ",self.num)
#     class Inner:
#         def __init__(self,num1,ref):
#             print("Num = ",ref.num)
#             self.num1=num1
#         def disp(self):
#             print("In Inner disp Num1 = ",self.num1)
#
# s1=Outer(2)
# s1.disp()
#
# print("----------------------------------------------------------")
#
# s2=Outer.Inner(4,s1)
# s2.disp()



#
# import pandas as pd
#
# name=[]
# desig=[]
# salary=[]
#
# for i in range(5):
#     names=input("Enter Name : ")
#     desigs=input("Enter Designation : ")
#     salarys=float(input("Enter Salaary : "))
#
#     name.append(names)
#     desig.append(desigs)
#     salary.append(salarys)
#
# mydict={'Name':name," Designation":desig,"Salary":salary}
# mydataframe=pd.DataFrame(mydict)
# print(mydataframe)



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

# a1=Army()
# a1.show()
# g1=Army.Gun(a1)
# print("\n")
# print(g1)







#
#
# n=int(input("Enter range : "))
# for i in range(1,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(1,i*2):
#         print(chr(64+k),end=" ")
#     print()
#
# for i in range(n-2,0,-1):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(1,i*2):
#         print(chr(64+k),end=" ")
#     print()

#
# for i in range(1, 6):
#     for j in range(0, 6-i):
#         print(" ", end=" ")
#     for k in range(1, i * 2):
#         print(k, end=" ")
#     print()
#
# for i in range(6-2,0,-1):
#     for j in range(0,6-i):
#         print(" ",end=" ")
#     for k in range(1,i*2):
#         print(k,end=" ")
#     print()
# #
#
#
# for i in range(1,6):
#     for j in range(0,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     for l in range(i-1,0,-1):
#         print(l,end="")
#     print()
#
#




# for i in range(1,6):
#     for j in range(0,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     for l in range(i-1,0,-1):
#         print(l,end="")
#     print()





# for i in range(1,6):
#     for j in range(0,6-i):
#         print(" ",end=" ")
#     for k in range(1,i*2):
#         print(k,end=" ")
#     print()
#
# for i in range(6-2,0,-1):
#     for j in range(0,6-i):
#         print(" ",end=" ")
#     for k in range(1,i*2):
#         print(k,end=" ")
#     print()





# for i in range(0,5):
#     print(("*")*(i+1) + (" ")*(5-i))


# for i in range(0,5):
#     print((" ")*(5-i) + ("* ")*(i+1))


# for i in range(0,5):
#     print((" ")*(i+1) + ("*")*(5-i))


# for i in range(0,5):
#     print(("*")*(5-i) + (" ")*(i+1))




























































