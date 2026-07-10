import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(700, 700)
tina.hideturtle()

# Set turtle speed. Use 'fast' or 'fastest' to watch it draw line-by-line.
tina.speed('fastest')

def fractal_hexagon(size, depth):
    if depth == 0:  # Base case: draw a hollow hexagon outline line-by-line
        for i in range(6):
            tina.forward(size)
            tina.left(60)
    else:  # Recursive case: follow the perimeter to arrange the sub-hexagons
        for i in range(6):
            fractal_hexagon(size / 3, depth - 1)
            tina.forward(size * 2 / 3)
            tina.left(60)

# Move tina to a good starting spot to center the drawing
tina.penup()
tina.goto(-150, -220)
tina.pendown()

# Run the fractal (Size 450, Depth 3 looks great line-by-line)
fractal_hexagon(450, 3)

turtle.exitonclick()
