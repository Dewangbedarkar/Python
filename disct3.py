# class Student :
#         def __init__(self,name,age,address,qualification):
#             self.name=name
#             self.age=age
#             self.address=address
#             self.qualification=qualification
#
#         def __str__(self):
#             return f"Name:{self.name},Age:{self.age},Address:{self.address},Qualification:{self.qualification}"
#
#
# s1=Student('Dewang',22,'Juhu','BE')
# s2=Student('Saurabh',23,'Bandra','MSC')
# s3=Student('Gaurav',21,'Andheri','Bcom')
# s4=Student('Tushar',22,'Thane','PHD')
#
# dict={1:'s1',2:'s2',3:'s3',4:'s4'}
# print(dict)
# roll=int(input("Enter roll no."))
# if roll in dict:
#     print(dict[roll])
# else:
#     print("Student Not Found")




# dict={1:'a',2:'b',3:'c',4:'d'}
#
# print(dict)
# print(dict[3])
# for i in dict:
#     if i>2 :
#         print(i)
#
# dict[3]='e'
# print(dict)


class Student:
    def __init__(self,name,age,address,qualification):
        self.name=name
        self.age=age
        self.addresss=address
        self.qualification=qualification

    def __str__(self):
        return self.name+'\t'+str(self.age)+'\t'+'\t'+self.addresss+'\t'+self.qualification

s1=Student('Dewang',22,'Juhu','BE')
s2=Student('Saurabh',23,'Bandra','MSC')
s3=Student('Gaurav',21,'Andheri','Bcom')
s4=Student('Tushar',22,'Thane','PHD')


dict={1:s1,2:s2,3:s3,4:s4}

roll=int(input("Enter Roll no. : "))

if roll in dict:
    print(dict[roll])
else:
    print("Error")





















