###
# checking if number is positive
#                                    
number = int(input("Enter number: "))           #7, 1 ,0 ,-1 , -4
if number > 0 :
    print(f"Number {number} is positive. ")
elif number < 0 :
    print(f"Number {number} is negative. ")
else :
    print("Number must be equal to 0. ")