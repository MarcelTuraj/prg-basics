###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Marcel'   
surname = 'Turaj' 
characters_in_name = len(name)
characters_in_surname = len(surname)
print(f'Your name has {characters_in_name} characters. ')
print(f'Your surname has {len(surname)} characters. ')
print(f'Your full name has {len(name) + len(surname) + 1} characters with space between name and surname.') # with a space between name and surname