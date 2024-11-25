import csv
with open("clothing.csv", "r") as file:
    clothing_dict = csv.DictReader(file)
    
    for row in clothing_dict:
       if float(row['Price']) < 60 and float(row['Stock_Quantity']) < 40 :
          print(row)