import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()
tina.speed('fastest')

def sierpinski_hexagon(size, depth):
    if depth == 0:  # base case
        tina.begin_fill()
        for i in range(6):
            tina.forward(size)
            tina.left(60)
        tina.end_fill()
    else:  # recursive case
        start_x, start_y = tina.position()
        start_heading = tina.heading()
        for i in range(6):
            tina.penup()
            tina.setheading(start_heading + 60 * i)
            tina.forward(size)
            tina.pendown()
            sierpinski_hexagon(size / 3, depth - 1)
            tina.penup()
            tina.goto(start_x, start_y)
            tina.setheading(start_heading)
            tina.pendown()

tina.penup()
tina.goto(0, -0)
tina.pendown()
sierpinski_hexagon(50, 3)
turtle.exitonclick()