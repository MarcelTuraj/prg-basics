def calc(expression) :
    expression = str(expression)
    result = 0
    current = 0
    for i in range(len(expression)):
        char = expression[i]
        if char.isdigit() :
           current = int(char)
        if char == "-" or i == len(expression) - 1:
            result -= current
        elif char == "+" or i == len(expression) - 1 :
            result += current

    
        
           
           
           

    return result

expression = "7-2+3"
print(f"{calc(expression)}")