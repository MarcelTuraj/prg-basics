def asterisks(n) :
    number_of = n
    string = ""
    string += f"*/"*n
    string = string[0:n*2-1]
    return string

n = 1
print(f"{asterisks(n)}")
