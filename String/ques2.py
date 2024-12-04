# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3,
# leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


str=input("Enter String ")
l=list(str)
# print(l)
if len(l)<=3 and l[-3::]!=["i","n","g"]:
    l.append("i")
    l.append("n")
    l.append("g")
    # print(str(l))
elif len(l)>=3 and l[-3::]==["i","n","g"]:
    l.append("l")
    l.append("y")
    # print(str(l))
else:
    print(str)

s="".join(l)
print(s)






