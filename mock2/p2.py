def f(x,y,digit):
    counter = 0
    mylist = []
    for i in range(x,y+1):
        mylist.append(str(i))
    for item in mylist:
        if str(digit) in item:
            counter += item.count(str(digit))
    return counter

print(f(100,105,6))
