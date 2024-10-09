###
#Distance to the horizon - calculator
#
import math
height = input("Enter your height in meters ")
height = float(height)
distance = 3.57 * math.sqrt(height)
print(distance)