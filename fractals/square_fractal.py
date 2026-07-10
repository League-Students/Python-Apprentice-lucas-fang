import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(700, 700)
tina.hideturtle()
tina.speed('fastest')

def fractal_hexagon(size, depth):
    # Base case: When depth reaches 0, stop recursing and 
    # draw exactly ONE single filled hexagon.
    if depth == 0:  
        tina.begin_fill()
        for i in range(6):
            tina.forward(size)
            tina.left(60)
        tina.end_fill()
    else:  
        # Recursive case: Ring of 6 positions. 
        # Each position will either break down further or draw a single hexagon.
        for i in range(6):
            fractal_hexagon(size / 3, depth - 1)
            tina.forward(size * 2 / 3)
            tina.left(60)

# Position the turtle to center the final shape
tina.penup()
tina.goto(-150, -220)
tina.pendown()

# Running with Depth 2 or 3 ensures the final tiny elements are single solid blocks
fractal_hexagon(450, 3)

turtle.exitonclick()
