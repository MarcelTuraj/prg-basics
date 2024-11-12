###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]
string = ""
print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print(arr[4])
print(arr[3])
print(arr[0] + arr[4])
print(arr[2])

for item in arr:
    string += f"{item} "
   
print(string)