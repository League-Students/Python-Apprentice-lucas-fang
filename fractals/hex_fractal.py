import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()

# Animate line-by-line visually
screen.tracer(1)
tina.speed('fastest')

def draw_single_small_hexagon(size):
    """Draws exactly one standalone small hexagon unit."""
    tina.color("black", "#5CFF42")
    tina.begin_fill()
    for _ in range(6):
        tina.forward(size)
        tina.left(60)
    tina.end_fill()

def hexaflake_small_units(size, depth):
    # When depth reaches 0, we draw a single independent small hexagon
    if depth == 0:
        draw_single_small_hexagon(size)
    else:
        # Move through the fractal tree to position the small units
        for _ in range(6):
            hexaflake_small_units(size / 3, depth - 1)
            
            # Step to the next cluster node without dragging internal lines
            tina.penup()
            tina.forward(size * 2 / 3)
            tina.left(60)
            tina.pendown()

# Center the setup nicely on the canvas
tina.penup()
tina.goto(-80, -150) 
tina.pendown()
tina.pensize(2)

# depth=2 creates exactly the 36 individual small hexagons seen in your image
hexaflake_small_units(260, 2)

turtle.exitonclick()
