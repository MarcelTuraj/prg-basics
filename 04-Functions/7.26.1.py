def f(product_code):
    count = 0 
    summ = 0
    while count < len(product_code) - 1 :
          summ += int(product_code[count])
          count += 1
    if summ % 7 != int(product_code[3]) :
         return False
    else : 
         return True
   
product_code = "1114"
print(f(product_code))