# var=5
# try:
#     print(var/0)
# except ZeroDivisionError:
#     print("You can't devide any number by 0")
# print("done")



# print("Let's open a file")
# open("d:\\sample1.txt","r")  #file not found exception
# print("done")


# print("Let's open a file")
# try:
#     open("d:\\sample1.txt","r")
# except FileNotFoundError:
#     print("File not found")
# print("done")




# def fun():
#
# 	try:
# 		f=open("d:\\FileDemo1.java","r")
# 	except FileNotFoundError:
# 		print("File not Found")
# 	finally:
# 		print("I will always execute")
# 	print("Done")
# fun()



#
# def fun():
#
# 	try:
# 		f=open("d:\\FileDemo1.java","r")
# 	finally:
# 		print("I will always execute")
# 	print("Done")
# fun()


#
# def fun():
# 	try:
# 		f=open("demo.py","r")
# 		for content in f:
# 			print(content)
# 		var=10/0
# 	except Exception as e:
# 		print("some other error\t",e)
# 	except ZeroDivisionError as z:
# 		print("error is\t",z)
# 	print("Done")
# fun()

#
# def double(var):
# 	if var<=0:
# 		raise Exception("IllegalValue Exception")
# 	return var*var
#
# def fun():
# 	try:
# 		print(double(6))
# 	except Exception as e:
# 		print("error is\t",e.__str__())
# 	print("Done")
# fun()

#
# class IllegalValue(Exception):
# 	pass
#
# def double(var):
# 	if var<=0:
# 		raise IllegalValue("Number cannot be negative or zero")
# 		#raise IllegalValue()
# 	return var*var
#
# def fun():
# 	try:
# 		print(double(-4))
# 	except Exception as e:
# 		print("error is\t",e.__str__())
# 	print("Done")
# fun()



var=5
try:
	print(var/0)
except ZeroDivisionError:
	print("You can't divide any no. with zero")
print("Done")
















