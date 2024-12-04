# a=0
# b=1
# print(a)
# print(b)
# i=2
# while(i<=10):
#     sum=a+b
#     print(sum)
#
#     a=b
#     b=sum
#
#     i+=1
for i in range(0,5):
    for j in range(0,5-i):
        print(" ", end=" ")
    for k in range(0,i+1):
        print("*", end=" ")
    print()
