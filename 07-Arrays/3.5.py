arr = [15, 8, 31, 47, 2, 19]
def arithmetic_mean(numbers) :
    sum = 0
    for item in numbers :
        sum += item
    mean = sum/len(numbers)
    return mean

print(arithmetic_mean(arr))
