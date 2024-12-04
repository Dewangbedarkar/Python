def add():
    print("Add")
def modify():
    print("Modify")
def delete():
    print("delete")

num=int(input("Enter number : "))

match num:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
    case _:
        print("Invalid")


