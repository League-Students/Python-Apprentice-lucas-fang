import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()

# 1. RE-ENABLE ANIMATION: Tell the screen to update on every single movement
screen.tracer(1)
tina.speed('fastest')

def hexaflake(size, depth):
    if depth == 0: # base case: draws the hexagon lines
        tina.begin_fill()
        for i in range(6):
            tina.forward(size)
            tina.left(60)
        tina.end_fill()
    else: # recursive case
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

tina.color("black", "royalblue")

# 2. LOWER DEPTH: Set to depth 2 so you can watch it draw without waiting forever
hexaflake(350, 2)

turtle.exitonclick()
