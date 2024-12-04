# import threading
#
# import time
#
#
# def disp(thread_name):
#     for i in range(6):
#         t1=threading.current_thread()
#         time.sleep(0.5)
#         print(t1.name)
#         print(f"{thread_name} - {i}")
#
# thread1=threading.Thread(target=disp,args=("1st thread",))
# thread2=threading.Thread(target=disp,args=("2nd thread",))
#
# thread1.start()
# thread2.start()
#
#
# thread1.join()
# thread2.join()
#
# t1=threading.current_thread()
# print(t1.name)

#

#
# import threading
#
# import time
#
#
# # class A:
# #
# #     def disp(self):
# #         with self.lock:
# #             for i in  range(5):
# #                 print(f"Hey \t{i}")
# #                 time.sleep(0.5)
# #
# #     def __init__(self):
# #         self.lock = threading.Lock()
# #
# # def main():
# #     a=A()
# #
# #
# #     thread1=threading.Thread(target=a.disp())
# #     thread2=threading.Thread(target=a.disp())
# #
# #     thread1.start()
# #     thread2.start()
# #
# # main()
#
#
#
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
#
# class Linklist:
#     def __init__(self):
#         self.head=None
#         self.last=None
#
#     def add(self,data):
#         ref=node(data)
#         if self.head==None:
#             self.head=ref
#             self.last=ref
#         else:
#             self.last.next=ref
#             self.last=ref
#
#     def disp(self):
#         temp=self.head
#         while temp is not None:
#             print(temp.data)
#             temp=temp.next
#
#     def sort(self):
#         temp=0
#         perv=self.head
#         cur=perv.next
#         while perv is not self.last:
#             while cur is not None:
#                 if perv.data > cur.data:
#                     temp=perv.data
#                     perv.data=cur.data
#                     cur.data=temp
#                 cur=cur.next
#             perv=perv.next
#             cur=perv.next
#
#     def insert(self,data):
#         ref=node(data)
#         if ref.data < self.head.data:
#             ref.next=self.head
#             self.head=ref
#         elif ref.data > self.last.data:
#             self.last.next=ref
#             self.last=ref
#
#
#
#
#
#
#
#
# mylist=Linklist()
# mylist.add(45)
# mylist.add(35)
# mylist.add(63)
# mylist.add(5)
#
# mylist.sort()
#
# mylist.insert(3)
# mylist.insert(90)
# mylist.disp()
#



class node:
    def __init__(self):
        self.data=None
        self


class linklist:
    def __init__(self):
        self.head = None
        self.last = None


























