def occurence(array, number):
    if number in array :
        return True
    else :
        return False
    
array = [15, 38, 7, 23, 14]
number = int(input("Enter number"))
print(occurence(array, number))