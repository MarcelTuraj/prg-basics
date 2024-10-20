###
# price analyser
#
first_price = 200
new_price = 140
reduction = ((first_price - new_price) / (first_price)) * 100
message = f"""              Current price: {new_price} 
              Previous price : {first_price} 
              Buy the product!!! 
              Product price reducted by {reduction}% ."""
if reduction >= 10 :
    print(message)
else : 
    print("wtf")