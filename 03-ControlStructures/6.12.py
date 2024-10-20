###
# online store
#
amount = int(input("Enter amount of products purchased: "))
price = float(input("Enter price of the product: "))
to_pay = 0
if amount > 2 : 
    to_pay += (2 * price) + ((amount - 2)*(0.75*price))
    print(f"""Number of products purchased: {amount}
               Product price: {price}
               Amount to pay: {to_pay}""")
else :
    to_pay += amount * price
    print(f"""Number of products purchased: {amount}
               Product price: {price}
               Amount to pay: {to_pay}""")
