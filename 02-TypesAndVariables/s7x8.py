###
# A program that displays results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
dice_roll_3 = random.randint(1,6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print("First roll result: ", dice_roll_1)
print('Second result:', dice_roll_2)
print("Third result: ", dice_roll_3)
print("Sum of three dice rolls equals to: ", total) 