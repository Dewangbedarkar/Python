str2 = input("Enter a string: ")
count={}
for i in str2:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

for i,count1 in count.items():
    if count1>1:
        print(i)

# str2 = input("Enter a string: ")
#
# for i in range(len(str2)):
#     for j in range(len(str2)):
#         if str2[i]==str2[j] and i!=j:
#             print(str2[i])
#             break
#
# else:
#     print  ("nocommon")