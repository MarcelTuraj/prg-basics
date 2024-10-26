###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import drawfigures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)   

## Draw figures
square1 = drawfigures.draw_square(pen, 100)
pen.penup()
pen.goto(67,85)
pen.down()
square2 = drawfigures.draw_square(pen, 100)
pen.penup()
pen.goto(70,85)
pen.down()
rectangle1 = drawfigures.draw_rectangle(pen, 50,70)
pen.penup()
pen.goto(-90,-56)
pen.down()
rectangle2 = drawfigures.draw_rectangle(pen, 60,90)
pen.penup()
pen.goto(56,-56)
pen.down()
triangle1 = drawfigures.draw_triangle(pen, 45)
pen.penup()
pen.goto(-100,100)
pen.down()
triangle2 = drawfigures.draw_triangle(pen, 50)



# Hide the turtle and finish
pen.hideturtle()
window.mainloop()