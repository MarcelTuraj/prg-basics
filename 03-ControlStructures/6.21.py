### 1. enter amount  2. open infinte loop  3. floor divide by 5 --> its a number of 5 coins that can fit in our amount
#                                  
#
amount = int(input("enter amount: "))
fcount = 0
tcount = 0
ocount = 0
while True :
    fcount = amount // 5
    if amount%5 == 0 :
        break
    elif amount%5 != 0 :
        amount = amount%5
        tcount = amount // 2
        if amount%2 == 0 :
            break
        elif amount%2 != 0 :
            amount = amount%2
            ocount = amount
            

    break

print(f"{fcount} , {tcount}, {ocount}")