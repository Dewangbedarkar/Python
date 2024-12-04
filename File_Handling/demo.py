# from os import path
#
# print("File Exists\t",path.exists("web.xml"))
# print("Directory Exists\t",path.exists("d:\\new"))
#



# import os
#
# os.rename("iris.csv","temp.txt")
# print("Done")
#
# import shutil
#
# #  Python allows you to quickly create zip/tar archives.
# # Following command will zip entire directory
#
# # here "myzip.zip" will be created of the current working directory (. is given) and that zip file will be stored in the current working directory itself.
#
# shutil.make_archive("myzip","zip","C:\\today")
# print("Done")


# how to read from a file
#
#
# with open("Sample.json","r") as f:
#     data=f.read()
#     print(data)
#
# print("Done")
#




# how to write inside a file
# with open("myfile.txt","w") as f:
# 	print("enter messages, stop to quit\n")
# 	while True:
# 		str=input()
# 		if str=="stop":
# 			break
# 		f.writelines(str+"\n")
#
# print("Done")






#
# with open("myfile.txt","w+") as f:
#     print("enter messages, stop to quit\n")
#     while True:
#         str=input()
#         if str=="stop":
#             break
#         f.writelines(str+"\n")
#     f.seek(0, 0)  # place the file pointer at the beginning
#     data=f.read()
#     print(data)
# print("Done")



#
#
# class MyReader:
#     def __init__(self, filename,mode):
#        self.filename=filename
#        self.mode=mode
#     def __enter__(self):
#         print("in __enter__")
#         # logic to open "filename" in "mode" mode
#         return self
#     def __exit__(self, exception_type, exception_value, traceback):
#         print("in __exit__\t",exception_value)
#         self.close()
#     def close(self):
#         print("closing the stream\n")
#     def read(self):
#         if len(self.filename)<9:
#             raise Exception("not able to read the file")
#         print("successfully read the file")
#
# print("before with")
# with MyReader("abcde.txt","r") as m:
#     # exception successfully pass to __exit__
#     print("before read")
#     m.read()
#     print("after read")
# print("done")

#
# import os
# os.rename("temp.txt","temp1.txt")
# print("Done")



# import shutil
#
# shutil.make_archive("temp","zip","C:\\heyyyy")
# print("Done")
#



# with open("Sample.json","r") as f:
#     read=f.read()
#     print(read)
# print("done")

#
# with open("Sample.json","w")as f:
#     print("Enter message (Stop to Quit) : ")
#     while True:
#         str=input()
#         if str == "stop":
#             break
#         f.writelines(str+"\n")
# print("Done")
#



#
# with open("Sample.json","a+")as f:
#     print("Enter Message : ")
#     while True:
#         str=input()
#         if str == "stop":
#             break
#         f.writelines(str+"\n")
#     f.seek(0,0)
#     read=f.read()
#     print(read)






with open("Sample.json","r+")as f:
    read=f.read()
    print(read)
    f.seek(f.tell())

    print("Enter Message : ")
    while True:
        str=input()
        if str == "stop":
            break
        f.writelines(str+"\n")
    f.seek(0,0)
    read=f.read()
    print(read)
print("Done")










