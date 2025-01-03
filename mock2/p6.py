import re

def f(password):
    pattern = r"^[A-Za-z_][A-Za-z0-9_]*"
    if re.match(pattern, password):
        return True
    else : 
        return False
    

print(f("abc"))
print(f("Abc"))
print(f("aBC")) 
print(f("_ab_c")) 
print(f("abcdef"))
print(f("8abc"))
print(f("_aB8_")) 
print(f("_4x"))