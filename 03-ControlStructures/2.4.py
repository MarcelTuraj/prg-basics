###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = float(input("Enter number 1 : "))
number2 = float(input("Enter number 2 : "))
operator = input("Enter an operator : ")
if operator == '+' :
    print(f'{number1} + {number2} = {number1 + number2}')
    
elif operator == '-' :
    print(f'{number1} - {number2} = {number1 - number2}')
elif operator == '*' :
    print(f'{number1} * {number2} = {number1*number2}')
elif operator == "/" and number2 != 0 :
    print(f'{number1} / {number2} = {number1/number2}')
else :
    print("Error")