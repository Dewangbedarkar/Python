# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221'] """


mylist=['abc', 'xyz', 'aba', '1221']

count=0

for i in mylist:
    if len(i)>= 2 and i[0] == i[-1]:
        print(i)
        count+=1

print("Count = "+str(count))



