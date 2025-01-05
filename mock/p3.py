def f(array2D):
    for i in range(len(array2D)):
        sum_of_rows = sum(array2D[i])
        sum_of_columns = sum(array2D[j][i] for j in range(len(array2D)))
        if sum_of_rows != sum_of_columns:
            return False
    return True



































def f(array2D):
    for i in range(len(array2D)):
        if sum(array2D[i]) != sum(array2D[j][i] for j in range(len(array2D))) :
            return False
    return True