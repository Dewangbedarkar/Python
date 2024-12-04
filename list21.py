

color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

# Converting lists to a list of dictionaries
result = [{"color_name": name, "color_code": code} for name, code in zip(color_names, color_codes)]

print(result)
