### 
#
#
fibbonacci = "01"
for i in range(0,6):
    x = int(fibbonacci[i])
    z = int(fibbonacci[i+1])
    y = x + z
    fibbonacci = fibbonacci + f"{y}"
for k in range(6,20):
    x = int(fibbonacci[k:k+1])
    z = int(fibbonacci[k+2:k+3])
   
    fibbonacci = fibbonacci + f"{y}"
print(fibbonacci)

####

# 0 + 1
# 1 + 1
# 