###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
washing_product = ''
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
if program == ("j") : 
    washing_product = "Jacket"
    total_washing_time += 40
    extra_rinse = input('Extra rinse? (y/n)')
    if extra_rinse == "y" : 
        extra_rinse = True
        total_washing_time += 15
    else :
        extra_rinse = False
    extra_spin = input('Extra spin? (y/n)')
    if extra_spin == "y" :
        extra_spin = True
        total_washing_time += 9
    else :
        extra_spin = False

elif program == ("u") : 
    washing_product = "Underwear"
    total_washing_time += 70
    extra_rinse = input('Extra rinse? (y/n)')
    if extra_rinse == "y" : 
        extra_rinse = True
        total_washing_time += 15
    else :
        extra_rinse = False
    extra_spin = input('Extra spin? (y/n)')
    if extra_spin == "y" :
        total_washing_time += 9
    else :
        extra_spin = False

elif program == ("s") : 
    washing_product = "Shoes"
    total_washing_time += 20
    extra_rinse = input('Extra rinse? (y/n)')
    if extra_rinse == "y" : 
        extra_rinse = True
        total_washing_time += 15
    else :
        extra_rinse = False
    extra_spin = input('Extra spin? (y/n)')
    if extra_spin == "y" :
        extra_spin = True
        total_washing_time += 9
    else :
        extra_spin = False

print(f"Washing product: {washing_product}, rinse = {extra_rinse}, spin = {extra_spin}, time : {total_washing_time}")
    