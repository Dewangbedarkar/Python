
str=input("Enter String : ")
str1=str[::-1]
print(str1)
if str.casefold()==str1.casefold():
    print("Palindrome")
else:
    print("Not Palindrome")

