###
# A program that displays your height both in cm and in feet and inches.
#
cm = int(input("Enter your height in cm: "))
feet = cm // 30.48
z = cm % 30.48
inches = z / 2.54
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches: .1f} inches. ')