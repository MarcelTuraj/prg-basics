###
# barcode checker
#
barcode = str(input("Enter EAN-13 article number: "))
is_polish = barcode[0:3]
is_correct = len(barcode)
if is_polish == "590" and is_correct == 13 :
    print("""             Article number correct.
             Manufactured in Poland.""")
elif is_polish != "590" and is_correct == 13 :
    print("""Article number correct.
             But not in Poland.""" )
else :
    print("Article number incorrect. ")