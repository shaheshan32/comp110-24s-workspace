"""TODO: This program draws a christmas tree with two gifts underneath with a star on top."""

__author__ = "730396719"

from turtle import Turtle, colormode, done


def draw_triangle(turtle_a: Turtle, x: int, y: int, size: int, color: str) -> None:
    """Draws triangle with the given parameters."""
    turtle_a.penup()
    turtle_a.goto(x, y)
    turtle_a.pendown()
    turtle_a.begin_fill()
    turtle_a.color(color)
    for edge in range(3):
        turtle_a.forward(size)
        turtle_a.left(120)
    turtle_a.end_fill()


def draw_rectangle(turtle_b: Turtle, x: int, y: int, width: int, height: int, color: str) -> None:
    """Draws rectangle with the given parameters."""
    turtle_b.penup()
    turtle_b.goto(x, y)
    turtle_b.pendown()
    turtle_b.begin_fill()
    turtle_b.color(color)
    for edge in range(2):
        turtle_b.forward(width)
        turtle_b.left(90)
        turtle_b.forward(height)
        turtle_b.left(90)
    turtle_b.end_fill()


def draw_star(turtle_c: Turtle, x: int, y: int, size: int, color: str) -> None:
    """Draws star with the given parameters."""
    turtle_c.penup()
    turtle_c.goto(x, y)
    turtle_c.pendown()
    turtle_c.color(color)
    turtle_c.begin_fill()
    for edge in range(5):
        turtle_c.forward(size)
        turtle_c.right(144)
    turtle_c.end_fill()


def draw_trunk(turtle_d: Turtle, x: int, y: int, width: int, height: int, color: str) -> None:
    """Draws trunk of the tree with the given parameters."""
    turtle_d.penup()
    turtle_d.goto(x, y)
    turtle_d.pendown()
    turtle_d.color(color)
    turtle_d.begin_fill()
    for edge in range(2):
        turtle_d.forward(width)
        turtle_d.right(90)
        turtle_d.forward(height)
        turtle_d.right(90)
    turtle_d.end_fill()


def make_tree_segment(turtle_e: Turtle, size: int, top_position: int, color: str) -> None:
    """Draws tree segment recursively."""
    if size < 5:
        return
    turtle_e.begin_fill()
    turtle_e.setposition(0, top_position)
    turtle_e.setposition(size, top_position - size)
    turtle_e.setposition(-size, top_position - size)
    turtle_e.setposition(0, top_position)
    turtle_e.end_fill()

    # Recursively draw smaller tree segments
    make_tree_segment(turtle_e, int(size / 2), int(top_position - size / 2), color)


def draw_gift(turtle_f: Turtle, x: int, y: int, size: int, color: str) -> None:
    """Draws gift with the given parameters."""
    turtle_f.penup()
    turtle_f.goto(x, y)
    turtle_f.pendown()
    turtle_f.color(color)
    turtle_f.begin_fill()
    for edge in range(4):
        turtle_f.forward(size)
        turtle_f.right(90)
    turtle_f.end_fill()


def draw_tree() -> None:
    """Draws Christmas tree with gifts and a star."""
    # Set color mode to use the RGB values
    colormode(255)

    # Create the background blue
    window = Turtle().screen
    window.bgcolor("sky blue")

    # Create the Turtle for drawing the scene
    my_turtle = Turtle()
    my_turtle.color("forest green")

    # Drawing tree segments
    tree_segments = ((50, 20, "forest green"), (80, 0, "forest green"), (120, -30, "forest green"), (150, -60, "forest green"))
    for size, top_position, color in tree_segments:
        make_tree_segment(my_turtle, size, top_position, color)

    # Drawing the trunk of the tree
    trunk = tree_segments[-1][1] - tree_segments[-1][0] 
    draw_trunk(my_turtle, -10, trunk - 10, 20, 50, "brown")  

    # Drawing gifts next to the trunk
    draw_gift(my_turtle, -45, trunk - 10, 20, "red")
    draw_gift(my_turtle, 35, trunk - 10, 20, "blue")

    # Drawing a star on top of the tree
    star_peak_x = -10  
    star_peak_y = tree_segments[0][1] + 5  
    draw_star(my_turtle, star_peak_x, star_peak_y, 25, "yellow")
    done()


if __name__ == "__main__":
    draw_tree()