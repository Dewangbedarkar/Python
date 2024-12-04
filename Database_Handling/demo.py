# # how to create database using Python
#
# import mysql.connector as m
#
# mydatabase = m.connect(host="localhost", user="root", password="Dew@ng123")
# cursor = mydatabase.cursor()
# cursor.execute("create database pythondb1")  # go and check inside MySQL whether database has been created or not

#
# import mysql.connector as m
# mydatabase=m.connect(host="localhost",user="root",password="Dew@ng123",database="pythondb1")
#
# cursor=mydatabase.cursor()
#
# cursor.execute("create table dept(deptno int primary key auto_increment,dname varchar(20),loc varchar(30))")


# import mysql.connector as m
# mydatabase=m.connect(host="localhost",user="root",password="Dew@ng123",database="pythondb1")
#
# cursor=mydatabase.cursor()
#
# query1="insert into dept(dname,loc) values(%s,%s)"    # it has to be "s"
# mydata1=('accounts','delhi')
# cursor.execute(query1,mydata1)
# mydatabase.commit()                    #   commit() is compulsory




# accept values from user and then insert the record
# run this program on "terminal"

# import mysql.connector as m
# mydatabase=m.connect(host="localhost",user="root",password="Dew@ng123",database="pythondb1")
# query="insert into dept(dname,loc) values(%s,%s)"         #  must be "s"
# dname=input("enter department name")
# loc=input("enter location")
# cursor=mydatabase.cursor()
# cursor.execute(query,[dname,loc])       #  second argument has to be list or tuple or dictionary
# mydatabase.commit()      #   commit() is must here
#

#
# import mysql.connector as m
# mydatabase=m.connect(host="localhost",user="root",password="Dew@ng123",database="pythondb1")
# cursor=mydatabase.cursor()
# query="insert into dept(dname,loc) values(%s,%s)"
# cursor.execute(query,['admin','Banglore'])
# cursor.execute(query,['RnD','Chennai'])
# mydatabase.commit()
#
#
#
#
#
# import mysql.connector as m
# mydatabase=m.connect(host="localhost",user="root",password="Dew@ng123",database="pythondb1")
# cursor=mydatabase.cursor()
# query="insert into dept(dname,loc) values(%s,%s)"
# while True:
#     dname=input("Enter dname")
#     loc=input("Enter location")
#     cursor.execute(query,[dname,loc])
#     ans=input("Do you wish to continue")
#     if(ans=="no"):
#         break
# mydatabase.commit()




# import mysql.connector as m
# mydatabase=m.connect(host="localhost",user="root",password="Dew@ng123",database="pythondb1")
# cursor=mydatabase.cursor()
#
# query="update dept set loc=%s where deptno=%s"
# loc=input("Enter location")
# deptno=input("Enter deptno")
# cursor.execute(query,[loc,deptno])
# mydatabase.commit()







# import mysql.connector as m
# mydatabase=m.connect(host="localhost",user="root",password="Dew@ng123",database="pythondb1")
# cursor=mydatabase.cursor()
# query="delete from dept where dname=%s"
#
# dname=input("Enter department to delete the record")
# cursor.execute(query,(dname,))     # passing tuple as second argument   comma(,)  is mandatory here as we just have only one value inside the tuple
#
# mydatabase.commit();
#
#



# executemany function  if we pass list of list to the "execute()" method

# from dataclasses import dataclass
# import mysql.connector as m
# mydatabase=m.connect(host="localhost",user="root",password="Dew@ng123",database="pythondb1")
# cursor=mydatabase.cursor()
# query="insert into dept(dname,loc) values(%s,%s)"
# mylist=[['accounts','Mumbai'],['placement','Hyderabad']]      # list of list
# # cursor.execute(query,mylist)    #  won't work as it is list of list
# cursor.executemany(query,mylist)
# mydatabase.commit()



#
# import mysql.connector as m
# mydatabase=m.connect(host="localhost",user="root",password="Dew@ng123",database="pythondb1")
# cursor=mydatabase.cursor()
# query="select * from dept"
# cursor.execute(query)
# result=cursor.fetchall()     # here we get tuples equivalent to the number of records
# for record in result:
#     print(record)


# import mysql.connector as m
# mydatabase=m.connect(host="localhost",user="root",password="Dew@ng123",database="pythondb1")
# cursor=mydatabase.cursor()
# query="select * from dept"
# cursor.execute(query)
# result=cursor.fetchall()     # here we get tuples equivalent to the number of records
# for record in result:
#     for i in range(0,len(record)):    # traversing through each and every column of respective record
#         print(record[i])





import mysql.connector as m
mydatabase=m.connect(host="localhost",user="root",password="Dew@ng123",database="pythondb1")
cursor=mydatabase.cursor()

query="insert into dept(dname,loc) values(%s,%s)"
try:
    cursor.execute(query,['training','Pune'])
    cursor.execute(query,['cleaning','Banglore'])
    mydatabase.commit()
except Exception as e:
    print("exception occured\t",e)
    mydatabase.rollback()
print("done")




























