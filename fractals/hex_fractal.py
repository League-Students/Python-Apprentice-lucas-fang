import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()

# Set up live drawing animations
screen.tracer(1)
tina.speed('fastest')

def hexaflake_precise(size, depth):
    if depth == 0:
        # Base case: draw one of the small, solid green hexagons
        tina.begin_fill()
        for _ in range(6):
            tina.forward(size)
            tina.left(60)
        tina.end_fill()
    else:
        # Recursive case: position 6 smaller flakes in a ring matching the image
        for _ in range(6):
            hexaflake_precise(size / 3, depth - 1)
            
            # Move along the geometric outline to the next cluster node
            tina.forward(size * 2 / 3)
            tina.left(60)

# Center the drawing on screen
tina.penup()
tina.goto(-100, -150) 
tina.pendown()

# Set pen thickness and matching bright green color
tina.pensize(2)
tina.color("black", "#5CFF42")

# Draw the exact depth 2 pattern line-by-line
hexaflake_precise(300, 2)

turtle.exitonclick()
