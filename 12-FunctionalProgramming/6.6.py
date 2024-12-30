data = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

surnames = list(map(lambda x:(x[0].upper(),x[1]),data))
for item in surnames:
    print(f"{item[0]}, {item[1]}")
