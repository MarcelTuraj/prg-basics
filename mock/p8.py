import queue
def f(expression):
    # Split the expression into tokens
    tokens = expression.split()
    stack = queue.LifoQueue()
    
    for token in tokens:
        if token.isdigit():  # Check if the token is a number
            stack.put(int(token))  # Push the number onto the stack
        else:  # The token is an operator
            # Pop the top two numbers from the stack
            b = stack.get()
            a = stack.get()
            
            if token == '+':
                stack.put(a + b)  # Perform addition
            elif token == '-':
                stack.put(a - b)  # Perform subtraction
    
    # The final result will be the only element left in the stack
    return stack.get()

# Example usage
print(f("2 3 +"))          # Output: 5
print(f("2 6 + 4 5 - +"))  # Output: 7
print(f("11 7 + 15 - 14 +"))  # Output: 11
