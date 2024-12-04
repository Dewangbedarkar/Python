# # Converting tsv of title.akas.tsv
# import pandas as pd
#
# file_path = r"A:\CDAC_SM_VITA\7_Big_Data_Engineering\Day3\title.akas.tsv\title.akas.tsv"  # Replace with the path to your TSV file
# df = pd.read_csv(file_path, sep="\t")
# df.head()



# Write a Python program to find the value of n where n degrees of number 2 are written sequentially in a line without spaces.



degree=int(input("Enter no. of dgrees :- "))
str1=""
n=0
while degree>0:
    str1+=str(2 ** n)
    n+=1
    degree-=1

print(str1)


# Write a Python program to find the median among three given numbers


# num=input("Enter three digit number = ")
# l1 = list(map(int, num))
# l1.sort()
#
#
# median=int(( (l1[2]) + (l1[0]) ) / 2)
#
# print(median)








