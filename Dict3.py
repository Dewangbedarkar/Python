# 3) Write a Python script to check whether a given key already exists in a dictionary.

dict={0: 10, 1: 20, 2: 30}

key=int(input("Enter any Key : "))

if key in dict.keys():
    print("Exists")
else:
    print("Not Exists")

