###
# Calculates the sum of the digits in a number
#
###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = abs(number)
    number = str(number)
    summ = 0
    for char in number:
        char = int(char)
        summ += char
        
    result = summ
    return  result



    

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')