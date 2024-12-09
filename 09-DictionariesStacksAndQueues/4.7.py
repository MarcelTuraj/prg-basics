hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]


hotel_names_krakow = ""
for item in hotels_in_Krakow:
    hotel_names_krakow += f"{item["name"]}, "
hotel_names_krakow = hotel_names_krakow[:-2]

average_krakow_price = 0
sum_prices_krakow = 0
for item in hotels_in_Krakow:
    sum_prices_krakow += item["price"]
average_krakow_price = sum_prices_krakow/len(hotels_in_Krakow)

hotel_names_sopot = ""
for item in hotels_in_Sopot:
    hotel_names_sopot += f"{item["name"]}, "
hotel_names_sopot = hotel_names_sopot[:-2]

average_sopot_price = 0
sum_prices_sopot = 0
for item in hotels_in_Sopot:
    sum_prices_sopot += item["price"]
average_sopot_price = sum_prices_sopot/len(hotels_in_Sopot)

if average_krakow_price < average_sopot_price :
    cheaper_name = "Kraków"
elif average_sopot_price < average_krakow_price :
    cheaper_name = "Sopot"





print(f"Hotels in Krakow: {hotel_names_krakow}")
print(f"Average hotel price in Krakow: {average_krakow_price}")
print(f"Hotels in Sopot: {hotel_names_sopot}")
print(f"Average hotel price in Sopot: {average_sopot_price}")
print(f"Cheaper hotels in: {cheaper_name}")