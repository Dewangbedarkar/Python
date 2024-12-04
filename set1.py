# myset=set()
#
# for i in range(1,11):
#     num=int(input("Enter Numbers : "))
#     myset.add(num)
#
# print(myset)
#
# num1=int(input("Enter a Value : "))
#
# if num1 in myset:
#     myset.remove(num1)
#     print(myset)
# else:
#     print("Number Not in Set")

myset={1,2,3,4,5}
print(myset)
myset.update([5,8])
print(myset)
myset.update([9])
print(myset)
myset.remove(2)
print(myset)
print(max(myset))








