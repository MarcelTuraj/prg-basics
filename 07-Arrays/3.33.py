array = [
    [1,2,3,4,5],
    [0,0,0,0,0],
    [6,7,8,9,10]
]
stringbefore = ""
for row in array:
    for item in row:
        stringbefore += f"{item} "
    stringbefore += f"\n"
print(stringbefore)
for i in range(0,len(array)):
    array[i][0] , array[i][4] = array[i][4] , array[i][0]
stringafter = ""
for row in array:
    for item in row:
        stringafter += f"{item} "
    stringafter += "\n"

print(stringafter)