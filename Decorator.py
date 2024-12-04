# def decorator(fun):
#     def modify():
#         print("modify")
#         fun()
#     return modify
#
#
#
#
# @decorator
# def Add():
#     print("add")
# def Multi():
#     print("Multi")
# def Sub():
#     print("Sub")
#
#
# Add()



# def decorator(fun):
#     def modify():
#         print("Modify")
#         fun()
#     return modify
#
#
#
# def A():
#     print("A")
#
# def B():
#     print("B")
#
# def C():
#     print("C")
#
#
# var=decorator(A)
# var()
# var=decorator(B)
# var()
# C()


def division(a,b):
    print(a/b)


def division1(fun):
    def modify(a,b):
        if a<b:
            a,b=b,a
        fun(a,b)
    return modify


var=division1(division)
var(4,8)
















































