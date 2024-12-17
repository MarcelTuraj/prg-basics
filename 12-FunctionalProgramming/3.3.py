stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

total = sum(map(lambda stock: (stock[0]*stock[1]), stock))
print(total)