### coin counter
def amount_to_pay(price) :
    number = price
    five_count = number // 5
    container1 = number%5
    two_count = container1//2
    container2 = container1%2
    if container2 != 0 :
        one_count = container2
    else :
        one_count = 0 
    total_coin = five_count + two_count + one_count
    return total_coin

amount = int(input("Enter selected price : "))
print(f"{amount_to_pay(amount)}")