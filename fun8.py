def fun(str):
    if len(str) < 3:
        print("String is too short. Minimum 3 characters required.")
    elif len(str)> 5:
        print("String is too long. Maximum 5 characters allowed.")
    else:
        print("Accepted string  \t"+str)







str = input("Enter a String : ")
fun(str)