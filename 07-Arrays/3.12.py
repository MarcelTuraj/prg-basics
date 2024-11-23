def unique(arr):
    unique = []
    for item in arr:
        if arr.count(item) <= 1 :
            unique.append(item)
    return unique

arr = [2, 3, 2, 5, 8, 1, 9, 8]
print(unique(arr))