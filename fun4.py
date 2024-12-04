def myfun1():
    print(" myfun1 ")

def mufun2():
    print("In myfun2 invoking ")
    myfun1()
mufun2()