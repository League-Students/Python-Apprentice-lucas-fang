import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(700, 700)
tina.hideturtle()

# Turn off tracer for instant rendering of deep recursive layers
screen.tracer(0) 
tina.pensize(1)

def draw_single_hexagon(size):
    """Draws exactly one solid green hexagon with a clean black outline."""
    tina.color("black", "#5CFF42")
    tina.begin_fill()
    for _ in range(6):
        tina.forward(size)
        tina.left(60)
    tina.end_fill()

def corner_hexaflake(size, depth):
    # BASE CASE: Draw a solid hexagon at the lowest depth
    if depth == 0:
        draw_single_hexagon(size)
        return

    # RECURSIVE CASE: Place smaller flakes exactly on the 6 outer corners
    for _ in range(6):
        # Draw the smaller sub-flake at the current vertex
        corner_hexaflake(size / 3, depth - 1)
        
        # Move along the perimeter of the parent hexagon to the next corner
        tina.penup()
        tina.forward(size * 2 / 3) 
        tina.left(60)
        tina.pendown()

# Center the starting point on the screen
tina.penup()
tina.goto(-150, -200)
tina.pendown()

# Depth 4 or 5 looks incredible with this specific pattern
corner_hexaflake(350, 4)

screen.update()
turtle.exitonclick()
