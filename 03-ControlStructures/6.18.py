###
# 1. let x,y be variables - define them in program
# 2. build if-condition for first quadrant, determine x,y > 0
# ... build if conditions for three remianing quadrants 
# define position (0,0) and axis points
#
x = float(input("Enter X coordinate : "))
y = float(input("Enter Y coordinate : "))
P = f"P({x:.0f},{y:.0f})"
if x > 0 and y > 0 : 
    print(f"Point {P} is located in the first quadrant.")
elif x == 0 and y == 0 :
    print(f"Point {P} is located in the starting point of the coordinate system. ")
elif x == 0 and y != 0 :
    print(f"Point {P} is on the Y axis. ")
elif x != 0 and y == 0 :
    print(f"Point {P} is on the X axis. ")
elif x < 0 and y > 0 : 
    print(f"Point {P} is in the second quadrant. ")
elif x < 0 and y < 0 :
    print(f"Point {P} is in the third quadrant. ")
elif x > 0 and y < 0 :
    print(f"Point {P} is in the fourth quadrant. ")
