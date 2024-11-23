arr = [
    [1,2,3,4],
    [4,5,6,7]
]
strarray = ""
for row in arr :
    for item in row:
        string_element = str(item)
        strarray += f"{string_element} "
    strarray += "\n"
print(strarray)