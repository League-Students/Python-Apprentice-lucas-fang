import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(700, 700)
tina.hideturtle()

# Turn off tracer for instant drawing of complex fractals
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

def hexaflake(size, depth):
    # BASE CASE
    if depth == 0:
        draw_single_hexagon(size)
        return

    # RECURSIVE CASE
    # 1. Draw the central sub-flake
    hexaflake(size / 3, depth - 1)
    
    # 2. Draw the 6 surrounding sub-flakes
    for _ in range(6):
        tina.penup()
        tina.forward(size * 2 / 3)
        tina.pendown()
        
        # Recursively call the next depth
        hexaflake(size / 3, depth - 1)
        
        # Return to center and turn to the next position
        tina.penup()
        tina.backward(size * 2 / 3)
        tina.left(60)
        tina.pendown()

# Center the setup nicely on the canvas
tina.penup()
tina.goto(-100, -150)
tina.pendown()

# Depth 3 or 4 will show a beautiful, intricate fractal structure
hexaflake(300, 3)

screen.update()
turtle.exitonclick()
