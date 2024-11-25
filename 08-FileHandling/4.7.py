import re

with open("oblawa.txt", encoding="utf-8") as file:
    content = file.read()



pattern = r"[aeiouyAEIOUY]"
arr = re.findall(pattern, content)
vowel_number = len(arr)
print(vowel_number)

