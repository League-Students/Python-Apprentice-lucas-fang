import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(700, 700)
tina.hideturtle()

# Turn off tracer for instant rendering
screen.tracer(0) 
tina.pensize(1)

def draw_single_hexagon(size):
    """The absolute smallest unit: exactly one solid hexagon."""
    tina.color("black", "#5CFF42")
    tina.begin_fill()
    for _ in range(6):
        tina.forward(size)
        tina.left(60)
    tina.end_fill()

def sierpinski_hexagon(size, depth):
    # BASE CASE: The smallest hexagons are just one single hexagon
    if depth == 0:
        draw_single_hexagon(size)
        return

    # RECURSIVE CASE: Arrange 6 smaller hexagons in a ring
    for _ in range(6):
        # Draw the smaller sub-hexagon/cluster at this corner
        sierpinski_hexagon(size / 3, depth - 1)
        
        # Move perfectly along the imaginary parent edge to the next corner
        tina.penup()
        tina.forward(size * 2 / 3) 
        tina.left(60)
        tina.pendown()

# Position the turtle to center the fractal nicely
tina.penup()
tina.goto(-150, -220)
tina.pendown()

# Depth 3 or 4 shows the beautiful structure clearly
sierpinski_hexagon(400, 3)

screen.update()
turtle.exitonclick()
