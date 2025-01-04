import queue
def f(n):
    stack = queue.LifoQueue()
    box = []
    for char in str(n):
        if int(char) % 2 != 0 :
            stack.put(str(char))
    if stack.empty():
        return -1
    else :
        while not stack.empty():
            box.append(int(stack.get()))
    return max(box) - min(box)

print(f(10852))
print(f(723597))
print(f(4388))
print(f(846206))

            