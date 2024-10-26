def negative(n1,n2,n3): 
    negative_flag = False
    if n1 < 0 or n2 < 0 or n3 < 0 :
        negative_flag = True
    return bool(negative_flag)
    
n1 = 0
n2 = 0
n3 = 0
print(f"negative : {negative(n1,n2,n3)}")