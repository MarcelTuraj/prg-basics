def fibonacci(n):
    if n == 1 :
        return 0
    elif n == 2 : 
        return 1
    elif n == 3 :
        return 1
    elif n > 3 :
        return fibonacci(n - 1) + fibonacci(n - 2)


def n_leading_fibos(N):
    if N == 1 :
        return f"{fibonacci(1)}"
    fibostring = ""
    counter = 1
    while counter < N + 1:
        fibostring += f"{fibonacci(counter)}, "
        counter += 1
    return fibostring

print(n_leading_fibos(6))
print(fibonacci(5))