def exponential(x,n):
    if x == 0 :
        return 0
    if n == 0 :
        return 1
    elif n == 1 :
        return x
    elif n < 0 :
        return 1/x**-n
    elif n > 0 :
        return x*x**(n-1)

x = 5
n = 3
print(f"{exponential(x,n)}")