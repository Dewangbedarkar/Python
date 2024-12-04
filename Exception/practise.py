# class Notdivisible_by7(Exception):
#  pass
#
#
# class B:
#     def num(self,num):
#         self.num=num
#         if num%7!=0:
#             raise Notdivisible_by7("No. not Divisible by 7")
#         else:
#             print("Divisible by 7")
#
#
#     def myfun(self):
#         num=int(input("Enter No. : "))
#         try:
#             b.num(num)
#         except Exception as e:
#             print(e)
#         print("Done")
#
#
#
#
#
# b=B()
# b.myfun()






class voting_not_allowed(Exception):
    pass


def vote(age):

    if age <= 18:
        raise voting_not_allowed("You can not Vote")
    else:
        print("You can Vote")



age=int(input("Enter your Age : "))
try:
    vote(age)
except Exception as e:
    print(e)



















































