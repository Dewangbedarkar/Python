"""12) print the following pattern:
*
* *
* * *
* * * *
* * * * *
"""
"""for i in range (0,5):
    for j in range (0,i+1):
        print("*",end=" ")

    print()


13) print the following pattern:

* * * * * 

* * * * 

* * * 

* * 

* 


for i in range(0,5):
    for j in range(i,5):
        print("* ",end=" ")

    print()


 
 """

for i in range(0,5):
    for j in range(0,5-i):
        print(" ",end=" ")
        for k in range(0,i+1):
            print("*",end=" ")
    print()
