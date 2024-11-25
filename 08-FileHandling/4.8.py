import re
with open("files.txt", "r") as file:
    content = file.read()

pattern = r"(.*\..{4})"
file_names = re.findall(pattern, content)
print(file_names)
