def converter(array):
    onedimension = []
    for row in array :
        for item in row:
            onedimension.append(item)
    return onedimension

array = [[2,1],[3,5],[7,4],[2,6]]
print(converter(array))