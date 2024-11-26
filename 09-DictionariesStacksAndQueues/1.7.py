products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

product_list = []
for name, value in products.items():
    product_list.append([name, value])


for i in range(0,len(product_list)):
    print(i+1, product_list[i] )
total = 0
for quantity in products.values():
    total += quantity

print(total)
