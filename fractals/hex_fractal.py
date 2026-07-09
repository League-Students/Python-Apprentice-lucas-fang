import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()

# Keep it drawing line-by-line visually
screen.tracer(1)
tina.speed('fastest')

def draw_single_hexagon(size):
    """Draws exactly one solid green hexagon with a black border."""
    tina.color("black", "#5CFF42")
    tina.begin_fill()
    for _ in range(6):
        tina.forward(size)
        tina.left(60)
    tina.end_fill()

def hexaflake_direct(size, depth):
    if depth == 0:
        # Base case: Just draw ONE hexagon instead of a cluster of 6
        draw_single_hexagon(size)
    else:
        # Recursive case: Position 6 sub-flakes around a ring
        for _ in range(6):
            # Pass the scaled-down size down the chain
            hexaflake_direct(size / 3, depth - 1)
            
            # Move cleanly along the outer perimeter to the next node position
            tina.penup()
            tina.forward(size * 2 / 3)
            tina.left(60)
            tina.pendown()

# Center the drawing on screen
tina.penup()
tina.goto(-100, -150) 
tina.pendown()
tina.pensize(2)

# Draw the exact image structure cleanly at depth 2
# (At depth 1, this will draw exactly 6 individual hexagons in a ring)
hexaflake_direct(300, 2)

turtle.exitonclick()
