def f(uid):
    for item in uid:
        if uid.count(item) != 1:
            return False
    return True
        
print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"])) 
print(f(["bob2","bob2"]))
print(f(["bob2","BOB2"]))

 