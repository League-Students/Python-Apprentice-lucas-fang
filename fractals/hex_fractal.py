import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()

# Live line-by-line drawing
screen.tracer(1)
tina.speed('fastest')

def draw_clean_hexagon(size):
    """Draws one single, solid green hexagon with a clean black outline."""
    tina.color("black", "#5CFF42")
    tina.begin_fill()
    for _ in range(6):
        tina.forward(size)
        tina.left(60)
    tina.end_fill()

def hexaflake(size, depth):
    if depth == 0:
        # Base case: Just draw ONE solid hexagon unit
        draw_clean_hexagon(size)
    else:
        # Recursive case
        for _ in range(6):
            hexaflake(size / 3, depth - 1)
            
            # FIX: Lift the pen completely before moving to the next spot!
            # This prevents the turtle from slicing through the hexagon with black lines.
            tina.penup()
            tina.forward(size * 2 / 3)
            tina.left(60)
            tina.pendown() # Put it down only when ready to draw the next unit

# Center the drawing on the canvas
tina.penup()
tina.goto(-100, -150) 
tina.pendown()
tina.pensize(2)

# depth=1 gives exactly 6 clean hexagons in a ring with a hollow star center!
hexaflake(300, 1)

turtle.exitonclick()
