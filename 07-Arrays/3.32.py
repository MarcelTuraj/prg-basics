array = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [6,7,8,9,10]
]
stringbefore = ""
for row in array:
    for item in row:
        stringbefore += f"{item} "
    stringbefore += f"\n"
print(stringbefore)
print("new array: ")
for i in range(0,len(array[0])):
    array[0][i] , array[2][i] = array[2][i], array[0][i]

stringafter = ""
for item in array:
    for element in item :
        stringafter += f"{element} "
    stringafter += "\n"
print(stringafter)



    
    