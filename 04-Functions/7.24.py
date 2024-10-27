###
#
def ranger(x,y):
    summation = 0
    for i in range(x,y+1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0 :
            summation += i
    return summation

x = 1
y = 20
print(f"{ranger(x,y)}")