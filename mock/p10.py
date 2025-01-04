def f(array):
    def minimum(array):
        return min(min(item) for item in array)
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == minimum(array):
                if i == j:
                    return True
                else: 
                    return False
                


def column_access(array):
    new_arr = []
    for i in range(len(array[0])):
        value = list(array[j][i] for j in range(len(array)))
    new_arr = value
        
    return new_arr
print(column_access([[7,8,5,3],[9,4,2,6]]))
    