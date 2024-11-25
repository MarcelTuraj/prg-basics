import re
def file_analyzer(anyfile):
    with open(anyfile, "r") as file:
        content = file.read()
    line_container = content.splitlines()
    line_counter = 0
    word_container = content.split()
    for item in line_container:
        line_counter+= 1
    pattern = r"."
    characters = re.findall(pattern, content)
    character_counter = len(characters)
    word_counter = len(word_container)
    result = f"Number of lines : {line_counter}, Number of words: {word_counter}, number of characters: {character_counter}"
    return result
    

print(file_analyzer("countries.txt"))




