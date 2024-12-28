import queue
stack = queue.LifoQueue()
input_expression = str(input("Enter expression: "))
operators1 = ["-", "/"]
operators2 = ["+", "*"]
step_result = ""
for char in input_expression: 
    if char.isnumeric() :
        stack.put(char)
    elif char in operators1:
        step_result = str(stack.get()) + char + str(stack.get())
        step_result = step_result[::-1]
        stack.put(eval(step_result))
    elif char in operators2:
        step_result = str(stack.get()) + char + str(stack.get())
        stack.put(eval(step_result))
    elif char == "=":
        result = stack.get()

print(result)



    