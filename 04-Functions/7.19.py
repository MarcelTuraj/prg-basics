def primeflag(num) :
    flag = True
    if num < 2 : 
        flag = False
    if num == 2 :
        flag = True
    for i in range(2,num):
        if num%i == 0 :
            flag = False
    return flag
        
    
    
def nprime(n):
    counter = 0
    number = 2
    while counter < n :
        if primeflag(number) == True :
            counter += 1
            last_found = number
        number += 1
    return last_found

n = 4
print(f"nth prime: {nprime(n)}")


