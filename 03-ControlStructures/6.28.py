### 
#
#
fibbonacci = "01"
for i in range(0,6):
    x = int(fibbonacci[i])
    z = int(fibbonacci[i+1])
    y = x + z
    fibbonacci = fibbonacci + f"{y}"

print(fibbonacci)
####

# 0 + 1
# 1 + 1
# 