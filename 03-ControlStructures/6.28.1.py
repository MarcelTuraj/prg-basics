a = 0 
b = 1
fibb = ''
for i in range(0,20):
    a = a + b
    b = a + b
    fibb += f"{a},{b},"

print(f"0,1,{fibb}")