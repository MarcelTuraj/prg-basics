import random
def rand_elem(array):
    random_item = array[random.randint(0,len(array)-1)]
    return random_item

array = [1,2,3,4,5,6]
print(rand_elem(array))
