def Accept():
    num=int(input("Enter a number : "))
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0
Acc=Accept()
print(Acc)
