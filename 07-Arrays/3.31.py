numbers = [[-38, 19], [5,40],[-7,11],[29,16]]
maximum_value = numbers[0][0]
minimum_value = numbers[0][0]
max_coords = []
min_coords = []
for i in range(0,len(numbers)):
    for j in range(0,len(numbers[i])):
        if numbers[i][j] > maximum_value :
            maximum_value = numbers[i][j]
        if numbers[i][j] < minimum_value :
            minimum_value = numbers[i][j]
    
for i in range(0,len(numbers)):
    for j in range(0,len(numbers[i])):
        if numbers[i][j] == maximum_value :
            max_coords = [i+1,j+1]
        if numbers[i][j] == minimum_value:
            min_coords = [i+1,j+1]

print(maximum_value,max_coords)
print(minimum_value,min_coords)