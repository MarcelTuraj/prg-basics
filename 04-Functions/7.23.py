def calc(expression) :

    # Initialize total and the current number
    total = 0
    current_number = 0
    operation = '+'  # Start with addition for the first number
    
    # Iterate through each character in the expression
    for char in expression:
        if char.isdigit():  # Check if the character is a digit
            current_number = int(char)  # Convert to integer
        else:  # The character is an operator
            if operation == '+':
                total += current_number  # Add the current number to total
            elif operation == '-':
                total -= current_number  # Subtract the current number from total
            
            operation = char  # Update the operation to the current operator
            current_number = 0  # Reset current number for the next number
    
    # Handle the last number in the expression
    if operation == '+':
        total += current_number
    elif operation == '-':
        total -= current_number
    
    return total

expression = "2+3-4+5-0"
print(calc(expression))



