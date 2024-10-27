def f(text):
    new_string = ""
    for char in text :
        new_string += f"{char}-"
    new_string = new_string[:-1]
    return new_string

text = "university"

print(f'{f(text)}')