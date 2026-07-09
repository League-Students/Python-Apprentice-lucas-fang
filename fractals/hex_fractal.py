import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()

# Keep it drawing line-by-line visually
screen.tracer(1)
tina.speed('fastest')

def draw_single_hexagon(size):
    """Draws exactly one solid green hexagon with a clean black outline."""
    tina.color("black", "#5CFF42")
    tina.begin_fill()
    for _ in range(6):
        tina.forward(size)
        tina.left(60)
    tina.end_fill()

def hexaflake(size, depth):
    # BASE CASE: Stop everything immediately and draw ONE solitary hexagon
    if depth == 0:
        draw_single_hexagon(size)
        return  # This prevents the loop below from ever running at depth 0
        
    # RECURSIVE CASE: Only position the sub-clusters if we haven't hit the base depth
    for _ in range(6):
        hexaflake(size / 3, depth - 1)
        
        # Move cleanly around the outer perimeter to the next node position
        tina.penup()
        tina.forward(size * 2 / 3)
        tina.left(60)
        tina.pendown()

# Center the setup nicely on the canvas
tina.penup()
tina.goto(-150, -200) 
tina.pendown()
tina.pensize(2)

# Run at depth 1 to see the perfect solid ring structure
hexaflake(350, 1)

turtle.exitonclick()
