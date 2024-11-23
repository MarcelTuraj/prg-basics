numbers = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5], ]
summ = 0
for row in numbers:
    summ += row[len(row)-1]
print(summ)