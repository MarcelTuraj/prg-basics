def fibonacci(n):
    if n == 1 :
        return 0
    elif n == 2 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibo_range_sum(x,y):
    return sum(fibonacci(n) for n in range(x,y+1))

import queue
def f(detector):
    stack = queue.LifoQueue()
    for char in detector:
        if char == "+" :
            stack.put(char)
        elif char == "-":
            stack.get()
        if stack.qsize() >= 3:
            return True
    return False
        

def exponential(x,n):
    if x == 0 :
        return 0
    if n == 0 :
        return 1
    elif x == 1 :
        return 1 
    elif n == 1 :
        return x
    elif n > 1 :
        return x*exponential(x,n-1)
    
def fa(dice):
    data = {}
    for char in dice:
        if char not in data.keys():
            data[char] = 1
        else :
            data[char] += 1
    for key, value in data.items():
        if data[key] == max(data.values()):
            return int(key)

print(fa("5233165554211")) # returns 5
print(fa("2133")) # returns 3


print(f"{231.2342:.2f}")