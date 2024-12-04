
dict={'soap':100,'deo':300,'perfume':400}
print(dict.keys())

prod=input("Enter Any Product : ").lower()

if prod in dict:
    print(dict[prod])
else:
    print("Product not Available")

    