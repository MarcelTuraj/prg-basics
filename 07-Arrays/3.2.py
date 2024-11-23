arr = [15, 8, 31, 47, 2, 19]

newarr = []
for i in range(1,len(arr) + 1):
    newarr.append(arr[len(arr) - i])
print(newarr)