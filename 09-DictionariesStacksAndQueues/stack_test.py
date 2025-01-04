import queue
def brackets_ok(expression):
    data = {"{":"}",
            "[":"]",
            '(':")",
            }
    stack = queue.LifoQueue()
    for char in expression:
        if char in data.keys():
            stack.put(char)
        elif char in data.values():
            if data[stack.get()] != char :
                return False
    if not stack.empty():
        return False
    else :
        return True

print(brackets_ok("[(2+3)*4+5]/6-{(7*8)+[4]}"))
print(brackets_ok("[(2+3]/4)"))
print(brackets_ok("(2-3*4+(5/6)"))
    
            