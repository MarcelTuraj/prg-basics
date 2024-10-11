###
# binary and hexadecimal numbers converter
#
decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)
hexadecimal = hex(decimal)
print(f"For a {decimal} number, its binary representation is {binary}, hexadecimal is {hexadecimal}. ")