import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()
tina.speed('fastest')
# Tell python to work with turtles, make tina, set screen size, hide tina, set tina's speed.

def sierpinski_hexagon(size, depth):
    if depth == 0:  # base case
        tina.begin_fill()
        for i in range(6):
            tina.forward(size)
            tina.left(60)
        tina.end_fill()
    else:  # recursive case
        for i in range(6):
            sierpinski_hexagon(size / 2, depth - 1)
            tina.forward(size)
            tina.left(60)

# move tina to a good spot
tina.penup()
tina.goto(-200, -150)
tina.pendown()
sierpinski_hexagon(200, 3)
turtle.exitonclick()