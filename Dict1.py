# 1) Write a Python program to create a dictionary of keys x, y, and z
# where each key has as value a list from 11-20, 21-30, and 31-40 respectively.
# Access the fifth value of each key from the dictionary.
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
#
# dict={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
#
# for i in dict.keys():
#     print(dict[i][4])
#
# # print(dict['x'][4])
# # print(dict['y'][4])
# # print(dict['z'][4])
# #
#
# print(dict['y'][0])
#
# print(dict['y'][0])

Players={'Rohit':{'runs':10000,'centuries':15},'Virat':{'runs':12000,'centuries':18}}
# for i,j in Players.items():
#     print(i)
#     for k,l in j.items():
#         print(k,l)

for i,j in Players.items():
    print(i)
    for k,l in j.items():
        print(k,l)