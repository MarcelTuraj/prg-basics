import queue

def evaluate_rpn(input_expression):
    stack = queue.LifoQueue()
    operators1 = ["-", "/"]
    operators2 = ["+", "*"]
    
    for char in input_expression.split():  # Split the input expression into tokens
        if char.isnumeric():
            stack.put(int(char))  # Store numbers as integers
        elif char in operators1 or char in operators2:
            if stack.qsize() < 2:
                raise ValueError("Insufficient values in the expression.")
            b = stack.get()  # Get the second operand
            a = stack.get()  # Get the first operand
            
            if char == "+":
                stack.put(a + b)
            elif char == "-":
                stack.put(a - b)
            elif char == "*":
                stack.put(a * b)
            elif char == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero.")
                stack.put(a / b)
        elif char == "=":
            return stack.get()  # Return the final result

    