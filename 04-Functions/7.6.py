def binary_checker(binary_number) :
    string = str(binary_number)
    is_binary = True
    for char in string :
        if (char != "0" and char != "1") :
            is_binary = False
    return is_binary

            
            
sequence = str(input("Enter a number to check if it is binary or not: "))
if binary_checker(sequence) == True :
    print("It is correct. ")
else :
    print("Not correct. ")
    