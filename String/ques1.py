# Write a Python program to get a string from a given string where all occurrences of its first char
# have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

str="restart"

l=list(str)

for i in range(0, len(l)-1):
    for j in range(0,len(l)-1):
        if l[i]==l[j] and i!=j:
            l[j]='$'

print(l)
