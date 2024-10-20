###
# Dog's age
#
dogs_age_human = float(input("Enter the dogs age in human years: "))
dog_year = 0
if dogs_age_human <= 10.5 :
    dog_year = dogs_age_human / 5.25
elif dogs_age_human > 10.5 :
    dog_year = dogs_age_human / 4

print(f"{dogs_age_human} in human years means {dog_year: .2f} in dog years. ")