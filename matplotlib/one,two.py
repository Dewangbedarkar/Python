# from MyPackage import one,two
# one.disp1()
# two.disp()

# from multipledispatch import dispatch
#
# class A:
#     @dispatch(str)
#     def display(self,str):
#         print("hello",str)
#     @dispatch(int)
#     def display(self,num):
#         print("hello ",num)
#
# a=A()
# a.display('Dewang')
# a.display(18)


class A():
    def disp(self):
        print("In A ")
class B(A):
    def disp(self):
        print("In B ")
class C(A):
    def disp(self):
        print("In C ")
    def print(self):
        print("Oyeeeee!!!!")


def perform(ref):
    ref.disp()
    if isinstance(ref,C):
        ref.print()



perform(A())
perform(B())
perform(C())








