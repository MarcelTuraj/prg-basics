price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for key, value in price_list.items():
    value = round(value*0.9, 2)

for key, value in price_list.items():
    print(key, value)