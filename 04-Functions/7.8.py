###
# sum of digits function
number = "10000"
even = True
def summ(number, even) :
    suma = 0
    if even == True :
        for char in number :
            container_even = int(char)
            if container_even%2 == 0:
                suma = suma + container_even
    elif even == False :
        for char in number :
            container_odd = int(char)
            if container_odd%2 != 0:
                suma = suma + container_odd
    return suma

print(f"Sum of digits: {summ(number, even)}")


