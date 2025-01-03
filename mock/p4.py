def f(subject):
    current_max = 0
    current_average = 0
    for key, value in subject.items():
        current_average = sum(subject[key])/len(subject[key]) 
        if current_average > current_max:
            current_max = current_average
            max_key = key
    return max_key
    
    
    





dict = {"comp":[1,2,3],
        "wf":[2,4,5],
        "przyroda":[0,0,0],
        "tpi":[5,5,5]}

print(f(dict))