###
#Tree cutter
#
import math
circ = float(input("Enter a circumference in cm: "))
diameter = circ / math.pi >= 50
print('A tree may be cut down :', diameter)