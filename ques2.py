# using switch ….case   display whether accepted character is vowel or not.
#
# char=input("Enter Character = ")
# match char:
#        case 'a':
#             print("vowel")
#        case 'e':
#             print("vowel")
#        case 'e':
#             print("vowel")
#        case 'e':
#             print("vowel")
#        case 'e':
#             print("vowel")
#        case _:
#             print("Not a vowel")

# print("Hello Sir ")

# Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.

from collections import Counter

str=input("Enter the string : ")
print(str)

l1=list(str)
print(l1)

print(Counter(l1))