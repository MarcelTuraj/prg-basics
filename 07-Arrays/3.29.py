def create_2d_array(x,y):
    d_array = []
    subset = []
    for i in range(y):
        subset.append(0)
    for j in range(x):
        d_array.append(subset)
    return d_array

print(create_2d_array(3,5))


    
    

    
    
