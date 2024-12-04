# l=[i for i in range(1,5)]
# print(l)



# n=int(input("enter n "))
# fab=[0,1]
# [fab.append(fab[-2]+fab[-1]) for i in range(n-2)]
# print(fab)


#
# for i in range(0,5):
#     print(" "*(i+1)+(str(i+1)+" ")*(5-i))



# n=int(input("Enter no. of fabi series : "))
# fab=[0,1]
# [fab.append(fab[-1]+fab[-2]) for i in range(n-2)]
# print(fab)



# n=input("enter No = ")
#
# if n==n[::-1]:
#     print("Palindrome No. ")
# else:
#     print("Not a Palindrome No. ")



# n=int(input("Enter n = "))
# for i in range(0,n):
#     print(" "*(n-i+1)+"* "*(i+1))


# 1. Write a Python function that takes a sequence of numbers and determines whether all the numbers are different
# from each other.

# l1=[1,3,2,1]
# l1=[1,4,5,9]
#
# def fun(l1):
#     return (len(l1) == len(set(l1)))
#
# a=fun(l1)
#
# print(a)



# 3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

# l1=[1,2,3,4,5,6]
# l2=[]
#
# for i in range(len(l1)):
#     l2.append(l1[2])
#     l1.pop(2)

#
# print(l2)
#



# l1 = [1, 2, 3, 4, 5, 6]
# l2 = []
# index = 0  # Start with the 3rd element (0-based index)
#
# while l1 :
#     index =index+2
#     index=index %len(l1)
#     print(l1[index])
#     l1.pop(index)
#
# print(l1)


# 25. Write a Python program to find the digits which are absent in a given mobile number.

# a=set("0123456789")
# b=set(input("Enter the number: "))
# print(a-b)

# a='0123456789'
# b=input("Enter teh num: ")
# for i in a:
#     if i not in b:
#         print(i)




# 6. Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.

# from collections import Counter
#
# text="hello how are you"
#
# l1=list(text.replace(" ",""))
#
# print(Counter(l1))


# 7. Write a Python program to count the number of each character of a given text of a text file.


# with open(r"C:\Users\dewang\PycharmProjects\pythonProject5.py\Hello World.txt", 'r') as file:
#     count={}
#
#     for i in file:
#         for j in i:
#             if j not in count:
#                 count[j]=1
#             else:
#                 count[j]+=1
#
# print(count)



# str="hello world"
# dict={}
#
# for i in str:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
# print(dict)








