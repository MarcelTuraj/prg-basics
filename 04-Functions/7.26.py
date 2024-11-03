def f(product_code) :
    string = product_code
    summ = 0
    for i in range(3) :
        summ = summ + int(string[i])
    if int(string[3]) == summ%7 :
        return True
    else :
        return False
    
product_code = "1114"

print(f(product_code))