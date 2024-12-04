def Accept():
    char=input("Enter Character = ")
    if char.islower():
        return char.upper()
    else:
        return char.lower()
acc=Accept()
print(acc)