###
# DICE ROLL 9
#
import random
dice_roll = random.randint(1,6)
print(f"The result of the roll is {dice_roll}.")
dice_roll_special =  dice_roll == 1 or dice_roll == 6
print("Special number 1 or 6: ", dice_roll_special)
