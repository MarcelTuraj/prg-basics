def counter(tuple, value):
    counter = tuple.count(value)
    return counter

mytuple = (50,20,40,50,30,50)
value = 50
print(counter(mytuple, value))
