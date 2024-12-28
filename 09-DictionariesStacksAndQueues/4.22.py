import json
product = {}
file_name = "product.json"
prod_name = str(input("Enter product name: "))
prod_price = float(input("Enter price: "))
prod_price = round(prod_price)
ispaid = input("paid? yes/no")
if ispaid == "yes":
    ispaid = True
else :
    ispaid = False
product["name"] = prod_name
product["price"] = prod_price
product["paid"] = ispaid
with open(file_name, "w") as file :
    json.dump(product, file, indent=4)
                   