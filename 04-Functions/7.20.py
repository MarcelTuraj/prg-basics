def difference(n1,n2,n3):
    maximum = max(n1,n2,n3)
    minimum = min(n1,n2,n3)
    result = maximum - minimum
    return result

n1 = 2
n2 = -3
n3 = 5
print(f"difference is {difference(n1,n2,n3)}")