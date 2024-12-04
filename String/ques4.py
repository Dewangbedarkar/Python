# 4) Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'

# from collections import Counter
#
# str=input("Enter String : ")
#
# print(Counter(str))

#
# str=input("Enter String : ")
# dict={}
# for i in str:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)


class bird:
    def fly(self):
        print("bird fly")
class superman:
    def fly(self):
        print("Superman fly")
class person:
    def swim(self):
        print("person swim")


def perform(ref):
    if hasattr(ref,"swim"):
        ref.swim()
    else:
        ref.fly()


perform(bird())
perform(superman())
perform(person())