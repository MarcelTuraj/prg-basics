price = input("Enter price: ")
discount = input("Enter discount %: ")
price = float(price)
discount = float(discount)
discount_value = price * (discount * 1/100)
price_after = price - discount_value
result = f"""Price : {price: .2f}
Discount : {discount: .2f}%
Final price : {price_after: .2f}
Reduction : {discount_value :.2f}"""
print(result)
