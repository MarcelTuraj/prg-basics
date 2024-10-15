###
# Checking if discount is available
# The discount is available to children under 18,            #72 (discount), 65 (discount), 64, 18, 17 (discount)
# or people 65 or older.
#
age = int(input('Enter your age: '))

if age < 18 or age >= 65 :
    print("Discount is available for you. ")
else:
    print("You cannot get discount. ")