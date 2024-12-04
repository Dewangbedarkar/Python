# accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.

marks = int(input("Enter marks = "))
if marks>85:
            print("Distinction")
elif marks>=65:
            print("First class")
elif marks>=55:
            print("Second class")
elif marks>=35:
            print("pass")
else:
    print("fail")



