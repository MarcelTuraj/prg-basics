arr = [15, 8, 31, 47, 2, 19]
n = 0
sum = 0
while n < len(arr) :
    sum += arr[n]
    n += 1

mean = sum/len(arr)
print(mean)