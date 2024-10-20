###
# Decimal to binary converter
#
quotient = int(input("Enter decimal number: "))
remainder = 0
binary = ''
while quotient > 0 :
    remainder = quotient % 2
    binary = str(remainder) + binary 
    quotient = quotient // 2
    

print(f"{binary}")
   
