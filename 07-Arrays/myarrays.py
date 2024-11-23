def second_largest(array):
    maxnum = array[0]
    for number in array :
        if number > maxnum:
            maxnum = number
    newarray = []
    for item in array :
        if item != maxnum :
            newarray.append(item)
    maxnum2 = 0
    for item in newarray :
        if item > maxnum2:
            maxnum2 = item
    return maxnum2


array = [7,3,8,5,2]



def difference(array):
    maxnum = array[0]
    minnum = array[0]
    for number in array :
        if number > maxnum:
            maxnum = number
        if number < minnum :
            minnum = number
    difer = maxnum - minnum
    return difer

def bubblesort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def median(array):
    array = bubblesort(array)
    if len(array) % 2 != 0 :
        median = array[int((len(array)-1)/2)]
    else : 
        median = (array[int(len(array)/2)] + array[int((len(array)/2))-1])/2
    return median



       



def extreme_array(array):
    maxnum = array[0]
    minnum = array[0]
    for number in array :
        if number > maxnum:
            maxnum = number
        if number < minnum :
            minnum = number
    newarr = []
    newarr.append(maxnum)
    newarr.append(minnum)
    return newarr
    
def string_array(array):
    string = ""
    for item in array:
        string += f"{item}-"
    string = string[:-1]    
    return string

print(median(array))
