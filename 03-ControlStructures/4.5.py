###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())   # add one to the character's code
    char = ord(char)
    char += 1
    char = chr(char)
    # replace new character code with its
    # corresponding character (use chr())
    encrypted_text += char
    # add encrypted character to encrypted text
    

print(encrypted_text, end="")