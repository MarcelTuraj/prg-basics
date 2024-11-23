### negative even numbers
x = -7
y = 8
def my_function(x,y):
    counter = 0
    while x < y :
        number = x
        if number < 0 and number%2 == 0 :
            counter += 1
            x += 1
        else :
            x += 1
            
    return counter

print(f"negative even numbers : {my_function(x,y)}")