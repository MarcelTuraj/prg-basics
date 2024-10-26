def n_numbers(n):
    string = ""
    for i in range(1,n+1):
        string = string + f"{i}"
    return string
        
n = 12
print(f"{n_numbers(n)}")
