def subset(arr1,arr2):
    for item in arr1:
        if item not in arr2:
            return False
    return True

superior_array = [1,2,3,5,6,7,23,234]
subarr = [2,23,234]
subarr2 = [2,23,234,46]
print(subset(subarr,superior_array))
print(subset(subarr2, superior_array))