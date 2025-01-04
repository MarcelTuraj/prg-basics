res = [95,90,20,50,70]  
fnc1 = lambda x: x>50 

def f(fnc, res) :
    return max(list(filter(fnc, res))) - min(list(filter(fnc, res)))

print(f(fnc1, res))
fnc2 = lambda x: x>30 and x<90 
print(f(fnc2,res))