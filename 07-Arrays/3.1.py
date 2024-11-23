arr = [34,7,19,4,21,8]
n = 0
even_sum = 0
while n < len(arr):
    if arr[n] % 2 == 0 :
        even_sum += 1
    n += 1

print(even_sum)