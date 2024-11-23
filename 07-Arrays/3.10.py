num1 = [4,36,12,28,9,44,5]
num2 = [5,1,36]

unique = []
for item in num1 :
    if item not in num2 :
        unique.append(item)

print(unique)