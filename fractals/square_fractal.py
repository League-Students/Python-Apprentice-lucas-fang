import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(700, 700)
tina.hideturtle()

# This makes the turtle draw instantly so you don't have to wait!
screen.tracer(0)

def fractal_hexagon(size, depth):
    if depth == 0:  # Base case: draw a single solid hexagon
        tina.begin_fill()
        for i in range(6):
            tina.forward(size)
            tina.left(60)
        tina.end_fill()
    else:  # Recursive case: 6 smaller hexagons arranged in a perfect ring
        for i in range(6):
            fractal_hexagon(size / 3, depth - 1)
            tina.forward(size * 2 / 3)  # Move to the next position cleanly
            tina.left(60)

# Move tina to a good starting spot to center the drawing
tina.penup()
tina.goto(-150, -220)
tina.pendown()

# Run the fractal (Size 450, Depth 3 matches your image perfectly)
fractal_hexagon(450, 3)

# Refresh the screen to display the completed masterpiece
screen.update()
turtle.exitonclick()
