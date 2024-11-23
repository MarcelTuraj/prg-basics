table = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(1,6):
    for j in range(1,6) :
        table[i-1][j-1] = i*j
display = ""
for row in table:
    for item in row :
        if item < 10 :
            display += f"{item}  "
        elif item >= 10 :
            display += f"{item} "
    display += "\n"
print(display)