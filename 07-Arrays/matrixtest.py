matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]

]

for i in range(len(matrix)):
    for k in range(len(matrix[0])):
        matrix[i][k] = matrix[k][i]

print(matrix)
        