#circle stuff
import math
radius = float(input("Determine value of the radius: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f'For a given radius, area of considered circle is equal to {area: .2f} and its circumference is {circumference: .2f}.')