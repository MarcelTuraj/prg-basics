

def reverse_string(string):
    import queue
    string_deck = queue.LifoQueue()
    for char in string:
        item = char
        string_deck.put(item)
    reversed_string = ""
    while not string_deck.empty():
        reversed_string += f"{string_deck.get()}"
    return reversed_string

text = input("Enter desired string: ")
print(reverse_string(text))
