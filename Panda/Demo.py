import pandas as pd

# series=pd.Series([1,'Dewang','True',18,7],index=[i for i in range(1,6)])
# print(series)
# print("------------------------------------------")
# print(series.values)

mylist=[]
print("Enter Values : ")
for i in range(1,6):
    values=input()
    mylist.append(values)

series=pd.Series(mylist)
print(series)