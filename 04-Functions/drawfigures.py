
# Save the program in the file draw_figures.py. Then, run the program. Next, change the program so that the square is drawn using the draw_square(length) function with the only parameter being the length of the square's side. Place the defined function in a separate module figures.py. Finally, run the program again.

###
# Draw a square
#
def draw_square(t, length) :
    import turtle

 # Set up the screen
   
 # Create the turtle
   

 # Side length
    side_length = length
    
 # Draw a square
    for i in range(4):
      t.forward(side_length)
      t.right(90)

 # Hide the turtle and finish
  
    
def draw_triangle(t, length) :
   import turtle
   import math

   
   base_length = length
   sideslength = base_length/math.sqrt(2)
   t.forward(base_length)
   t.left(135)
   t.forward(sideslength)
   t.left(90)
   t.forward(sideslength)
   

def draw_rectangle(t, length_a, lenght_b) :
   import turtle

   longerside = length_a
   shoreterside = lenght_b
   for i in range(2) :
     t.forward(longerside)
     t.left(90)
     t.forward(shoreterside)
     t.left(90)
   

    
