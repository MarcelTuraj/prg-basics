###
# Functions to read any data type from the keyboard
#
def input_string(message):
    text = str(input(message))
    return text
    

def input_integer(message):
    integer = int(input(message))
    return integer

def input_real(message):
    floater = float(input(message))
    return floater

def input_boolean(message):
    true_or_false = input(message)
    if true_or_false == "y" :
        true_or_false = True
    elif true_or_false == "n":
        true_or_false = False
    return bool(true_or_false)