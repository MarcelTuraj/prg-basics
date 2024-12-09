import queue
def binary_converter(natural):
    string = ""
    num = natural
    remainders = queue.LifoQueue()
    while True:
        item = num%2
        remainders.put(item)
        num = num//2
        if num == 0 :
            break
    while not remainders.empty():
        string += f"{remainders.get()}"
    result = int(string)
    return result

    
print(binary_converter(18))