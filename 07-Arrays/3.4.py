arr = [-15, 8, -31, 47, -2,]
maxnum = arr[0]
minnum = arr[0]
for numbers in arr:
    if numbers > maxnum:
        maxnum = numbers
    if numbers < minnum:
        minnum = numbers

print(maxnum, minnum)
