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
            
    
def factorial(num):
        if num == 0 :
            return 1
        elif num == 1 :
            return 1
        elif num > 1:
            return num*factorial(num-1)

def zeros(n):
    
    number = factorial(n)
    trailing_zeros = 0
    while True :
        if number%10 == 0 :
            trailing_zeros += 1
            number = number/10
        elif number%10 != 0 :
            return trailing_zeros
        
    


    
            
    
def is_monotone(heights):
    if len(heights) == 1 :
        return True
    
    if heights is None :
        return True
    
    counter = 0 
    
    while counter < len(heights):
        current_number = heights[counter]
        checked_number = heights[counter + 1]
        if checked_number >= current_number :
            return True
        else :
            counter += 1
            current_number = checked_number
        return False


        
    
        
print(is_monotone([3,2,2]))
    
    
