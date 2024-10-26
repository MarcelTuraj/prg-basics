### negative even numbers
x = -5
y = 2
def my_function(x,y):
    counter = 0
    n = x
    while n < y :
        number = n
        if number < 0 and number%2 == 0 :
            counter += 1
            n += 1
        else :
            n += 1
            
    return counter

print(f"negative even numbers : {my_function(x,y)}")