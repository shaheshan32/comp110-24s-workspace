"""Turtle tutorial."""

from turtle import Turtle, colormode, done

leo: Turtle = Turtle()

# Color picker
colormode(255)

# Change color of turtle
leo.color("blue")

# Color RGB values like mixing paint
leo.color(99, 204, 250)

# Moving the turtle
leo.forward(100)
leo.left(90)
leo.right(90)
done()

# Square
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
done()

# Square short hand
i: int = 0
while i < 4:
    leo.forward(300)
    leo.left(90)
    i = i + 1
done()

# Triangle
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i = i + 1

# Move to new position and penup means lift turtle, and pendown means put down on paper
leo.penup()
leo.goto(50, 50)
leo.pendown()

i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i = i + 1

# For coloring in a square shape
leo.begin_fill()
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.end_fill()

leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green, yellow")

# Max and min values to get colors, pure white all 255, min is 0 pure black in RGB space
leo.begin_fill()
leo.fillcolor(128, 128, 128)  # Grey color
# Draw triangle
i: int = 0
while i < 3:
    leo.forward(100)
    leo.left(120)
    i = i + 1
leo.end_fill()

# Now we have all of the basic commands needed for creating interesting patterns:

# After your first triangle is created, we will set up a new turtle to do the rest of the work. Name this one bob.
bob: Turtle = Turtle()

# Changing bob’s color to black or a darker version of your triangle color
bob.color("black")

# Using the goto, penup, and pendown commands to position bob in the same spot that leo started.
bob.penup()
bob.goto(50, 50)
bob.pendown()

# Set bob’s speed to a higher value
bob.speed(50)

# Create an outline of leo’s filled-in triangle by having bob add another triangle without filling it in with the same size specifications as the original.
side_length: int = 300

i: int = 0
while i < 3:
    bob.forward(side_length)
    bob.left(120)
    i = i + 1

# Duplicate the code you created to have bob create an outline. We will use this second loop to add some more exciting linework. Turn the side length of the triangle into a variable and use it for both triangles.
# Inside the second outline triangle loop, multiply the side length variable by a number from 0.95 to 0.98. This will decrease the length of the side each time it is drawn.
i = 0
while i < 3:
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(120.5)  # Adjusted degrees
    i = i + 1

# Right now this will look like it is not changing much. Try increasing the number of loops of the second outline triangle to a much higher number. Mess around with this until it seems to fully recede!
# For one last magic touch, try changing the degrees of the second outline loop to just over 120. Mess around with a range of 120.5 to 123 until you get a result you like!