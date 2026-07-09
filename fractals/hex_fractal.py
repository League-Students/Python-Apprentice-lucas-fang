import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(700, 700)
tina.hideturtle()

# Instant drawing for crisp rendering
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

def crystal_hexagon(size, depth):
    # BASE CASE: Stop branching when depth hits 0
    if depth == 0:
        return

    # 1. Draw the actual, solid single hexagon for this level
    draw_single_hexagon(size)

    # 2. RECURSIVE CASE: Go to each of the 6 corners and sprout a smaller hexagon
    for _ in range(6):
        tina.penup()
        tina.forward(size)  # Move directly to the outer vertex
        tina.pendown()
        
        # Recursively draw a smaller single hexagon branching off this corner
        # Scaling by 2.5 keeps the branches perfectly separated
        crystal_hexagon(size / 2.5, depth - 1)
        
        tina.penup()
        tina.backward(size) # Return to the starting vertex
        tina.left(60)       # Turn to the next corner
        tina.pendown()

# Center the primary base hexagon on the canvas
tina.penup()
tina.goto(-75, -120)
tina.pendown()

# Depth 4 creates a beautiful, solid geometric crystal flake
crystal_hexagon(150, 4)

screen.update()
turtle.exitonclick()
