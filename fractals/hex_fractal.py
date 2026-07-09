import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()
tina.speed('fastest')

# CRITICAL OPTIMIZATION: Turns off instant animation so depth 4 doesn't freeze your PC.
screen.tracer(0, 0)

def hexaflake(size, depth):
    if depth == 0: # base case: draw a filled hexagon
        tina.begin_fill()
        for i in range(6):
            tina.forward(size)
            tina.left(60)
        tina.end_fill()
    else: # recursive case: arrange smaller hexaflakes in a hexagonal ring
        for i in range(6):
            hexaflake(size / 3, depth - 1)
            tina.forward(size / 3)            
            hexaflake(size / 3, depth - 1)
            tina.forward(size * 2 / 3)
            tina.left(60)

# Move tina to a good starting spot to center the flake
tina.penup()
tina.goto(-100, -200) 
tina.pendown()

# Set colors (optional, makes the geometry pop)
tina.color("black", "royalblue")

# Draw the fractal
hexaflake(350, 4)

# Force the screen to display the fully generated image
screen.update()
turtle.exitonclick()
