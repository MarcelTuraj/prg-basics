arr = [7,9,2,4,5,6]

even_arr = []
odd_arr = []

for item in arr:
    if item % 2 == 0 :
        even_arr.append(item)
    else :
        odd_arr.append(item)

final_arr = even_arr + odd_arr
print(final_arr)