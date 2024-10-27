def function(number) :
    string = str(number)
    
    summ = 0
    for i in range(1,10):
        counter = string.count(f"{i}")
        if counter > 1 :
            summ += counter*i
    return summ

number = 1222011
print(f"sum of repeated numbers is {function(number)}")