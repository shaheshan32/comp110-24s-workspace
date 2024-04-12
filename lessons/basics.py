from turtle import Turtle, colormode, done

# Function to draw a square
def draw_square(turtle, size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

# Function to draw a stoplight
def draw_stoplight(turtle, box_size, light_size, colors):
    # Draw the black box
    turtle.penup()
    turtle.goto(-box_size/2, -box_size/2)
    turtle.pendown()
    draw_square(turtle, box_size, "black")

    # Draw the three lights
    for i, color in enumerate(colors):
        turtle.penup()
        turtle.goto(-box_size/2 + light_size, box_size/2 - (i+1)*light_size*2)
        turtle.pendown()
        draw_square(turtle, light_size, color)

# Main function
def main():
    # Create Turtle object
    t = Turtle()

    # Set up the canvas
    colormode(255)

    # Define colors for the stoplight
    colors = ["red", "yellow", "green"]

    # Draw the stoplight with all lights on
    draw_stoplight(t, 100, 30, colors)

    # Hide the turtle and display the drawing
    t.hideturtle()
    done()

# Call main function
if __name__ == "__main__":
    main()
