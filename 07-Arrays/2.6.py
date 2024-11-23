matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def diagonal(matrices) :
    n = 0
    while n < len(matrices):
        row = matrices[n]
        row[n] = 1
        n += 1
    return matrices

def diagonal_print(matrices):
    matrixx = ""
    for item in diagonal(matrices):
        for num in item :
            matrixx += f"{num} "
        matrixx += "\n"
    return matrixx

print(diagonal_print(matrix))


    
