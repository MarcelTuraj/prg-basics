def f(array2D):
    sums = []
    for i in range(len(array2D[0])):
        sum_of_columns = sum(array2D[j][i] for j in range(len(array2D)))
        sums.append(sum_of_columns)
    def check(sums):
        for item in sums:
            if sums.count(item) >= 2:
                return True
            else :
                return False
    return check(sums)
        
    

print(f([[3,4],[5,9],[4,7]]))

