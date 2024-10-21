###
# multiplication table
#
number = int(input("Enter your number : "))
result = 0
for i in range(1,11) :
    result = number*i
    print(f"{number} x {i} = {result}" )