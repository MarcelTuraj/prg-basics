### 
# Program that calculates VAT for any given amount
#
amount = input('Enter an amount ')
amount = float(amount)
value_after_tax = amount * 0.23
result = f"""Amount : {amount: .2f} 
VAT : {value_after_tax: .2f}"""
print(result)