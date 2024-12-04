# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black'] """

mylist=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

mylist.pop(5)
mylist.pop(4)
mylist.pop(0)

print(mylist)