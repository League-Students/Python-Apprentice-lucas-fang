import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(700, 700)
tina.hideturtle()
tina.speed('fastest')

def fractal_hexagon(size, depth):
    if depth == 0:  # Base case: draw a solid hexagon
        tina.begin_fill()
        for i in range(6):
            tina.forward(size)
            tina.left(60)
        tina.end_fill()
    else:  # Recursive case: place smaller hexagons along the perimeter
        for i in range(6):
            fractal_hexagon(size / 3, depth - 1)
            tina.forward(size / 3)
            fractal_hexagon(size / 3, depth - 1)
            tina.forward(size * 2 / 3)
            tina.left(60)

# Move tina to a centered starting spot
tina.penup()
tina.goto(-100, -200)
tina.pendown()

# Run the fractal (size 350, depth 3 looks best without lagging)
fractal_hexagon(350, 3)

turtle.exitonclick()
