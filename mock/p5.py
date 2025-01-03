import re
def f(first_letter, last_letter):

    regex = fr"^{first_letter}.*{last_letter}$"
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()
    counter = 0 
    for word in content.split():
        if re.match(regex, word) :
            counter += 1
    return counter

print(f("p","o"))