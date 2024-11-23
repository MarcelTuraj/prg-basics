import math
def greater(array) :
    number = float(input("Enter float value :"))
    counter = 0
    for item in array:
        if item > number :
            counter += 1
    return counter 

array = [5,7,9,2,45, 5.321, math.pi, math.sqrt(3)]

print(greater(array))