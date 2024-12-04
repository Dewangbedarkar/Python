# 5) Write a Python program to create a dictionary from two lists without losing duplicate values.
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})



lists= ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
lists1= [1, 2, 2, 4]
dic={i:j for i,j in zip(lists,lists1)}
# for i,j in zip(lists,lists1):
#     dic[i]=j
print(dic)


