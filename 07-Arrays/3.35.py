matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]

]

def transposition(m):
   transposed = [[0]*len(matrix) for i in range(len(matrix[0]))]
   for i in range(len(matrix)):
      for k in range(len(matrix[0])):
         transposed[i][k] = m[k][i]
   return transposed

array = [[0]*4 for i in range(9)]


print(array)
print(transposition(matrix))
