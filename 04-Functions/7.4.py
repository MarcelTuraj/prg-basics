import ranger
left_end = int(input("Enter left end of the range: "))
right_end = int(input("Enter right end of the range: "))
number = int(input("Enter to check if desired number is within selected range: "))
if ranger.rangechecker(left_end, right_end, number) == True :
    print(f"The number {number} lies within the range <{left_end},{right_end}>. ")
elif ranger.rangechecker(left_end, right_end, number) == False :
    print("The number is not within the selected range. ")