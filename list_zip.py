# 12) Write a Python program to convert list to list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
#  """

# list=["Black", "Red", "Maroon", "Yellow"]
# list1=["#000000", "#FF0000", "#800000", "#FFFF00"]
# dict=[{"color_name":name,"color_code":code} for name,code in zip(list,list1)]
# print(dict)

# list1=[1,2,3,4,5]
# list2=['dewang','tushar','saurabh','kartik','kaushik']
# dict={x:y for x,y in zip(list1,list2)}
# print(dict)

# list=[x for x in range(1,11)]
# list1=[y for y in list if y%2 != 0]
# print(list1)