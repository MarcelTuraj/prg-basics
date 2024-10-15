###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
fraction = float
for i in range(2,11):
    fraction = 1 / i
    print(f'1/{i} = {fraction}')