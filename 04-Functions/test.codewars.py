def digital_root(n):
    string_ = str(n)
    summation = 0
    while True :
        for digit in string_:
            summation += int(digit)
        if summation >= 10 :
            string_ = str(summation)
            summation = 0
        elif summation < 10 :
            return int(summation)
            
    
    
    
    
    
print(digital_root(132189))