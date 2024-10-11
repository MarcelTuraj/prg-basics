###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
temp_celsius = float(input("Enter temperature in Celsius : "))   # ask user to input a temp value in Celsius
temp_kelvin = temp_celsius + 273.15    # program counts a given value in terms of Kelvin's unit
temp_fahrenheit = temp_celsius * (9/5) + 32  # program counts a given value in terms of Fahreneheit's unit
print(f'For a given temperature in Celsius ({temp_celsius: .2f}), its value in Fahrenheit is {temp_fahrenheit: .2f} and in Kelvin {temp_kelvin: .2f}.') # program output: displaying a sentence containing all values rounded to 2 decimal places