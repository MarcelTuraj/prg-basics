import re
def f(first_letter, last_letter):

    regex = fr"^{first_letter}.*{last_letter}[\.,;:?]?$"
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()
    box = content.split()
    
    counter = 0 
    for word in box :
        if re.match(regex, word) :
            counter += 1
    return box

print(f("p","o"))