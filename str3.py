str=input("Enter a String : ")
vow="aeiouAEIOU"
count=0
for i in str:
    if i in vow:
        count+=1

print(count)

