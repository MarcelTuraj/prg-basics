def f(array):
    suma = 0
    for i in range(0,len(array)):
        suma += array[i][len(array[0])-1]
    return suma


    

def create_2d_array(x,y):
    return [[0]*y for i in range(x)]



def table(n,x):
    arr = []
    for i in range(1,n+1):
        step_arr = []
        for j in range(1,x+1):
            step = i*j
            step_arr.append(step)
        arr.append(step_arr)
    return arr



def fa(array):
    data = {}
    maximum = max(max(array[i]) for i in range(len(array)))
    minimum = min(min(array[j]) for j in range(len(array)))
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == minimum:
                data["minimum"] = f"{minimum}, cords: {i},{j}"
            elif array[i][j] == maximum:
                data["maximum"] = f"{maximum}, cords: {i},{j}"
    return data


            
def switch_cols(array):
    for i in range(len(array)):
        array[i][0], array[i][len(array[0])-1] = array[i][len(array[0])-1], array[i][0]
    return array




def switch_rows(array):
    array[0],array[len(array)-1] = array[len(array)-1],array[0]
    return array


def identity_m(n):
    matrix = [[0]*n for x in range(n)]
    for i in range(len(matrix)):
        matrix[i][i] = 1
    return matrix
    
def transposer(matrix):
    new_matrix = [[0]*len(matrix)for i in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            new_matrix[i][j] = matrix[j][i]
    return new_matrix


def f(arr2D):
    sums_of_cols = []
    for i in range(len(arr2D[0])):
        sums_of_cols.append(sum(arr2D[j][i] for j in range(len(arr2D))))
    return sums_of_cols


def whole(arr):
    whole = []

    for i in range(len(arr[0])):
        col = []
        for j in range(len(arr)):
            col.append((arr[j][i]))
        whole.append(col)
    return whole



def min_of_cols(arr):
    mins = []
    for i in range(len(arr[0])):
        mins.append(min(arr[j][i] for j in range(len(arr))))
        

    return mins


print(min_of_cols([[3,4,2],[5,1,6]]))

    