import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(700, 700)
tina.hideturtle()

# 'fastest' is highly recommended so you don't have to wait too long!
tina.speed('fastest')

def fractal_hexagon(size, depth):
    if depth == 0:  # Base case: draw and fill each individual hexagon line-by-line
        tina.begin_fill()
        for i in range(6):
            tina.forward(size)
            tina.left(60)
        tina.end_fill()
    else:  # Recursive case: follow the perimeter path to place the sub-hexagons
        for i in range(6):
            fractal_hexagon(size / 3, depth - 1)
            tina.forward(size * 2 / 3)
            tina.left(60)

# Move tina to a good starting spot to center the drawing
tina.penup()
tina.goto(-150, -220)
tina.pendown()

# Run the fractal (Size 450, Depth 3)
fractal_hexagon(450, 3)

turtle.exitonclick()
