import turtle
import math

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

        corners = []
        for i in range(6):
            angle = math.radians(start_heading + 60 * i)
            cx = start_x + size * math.cos(angle)
            cy = start_y + size * math.sin(angle)
            corners.append((cx, cy, start_heading + 60 * i + 30))

        tina.goto(corners[0][0], corners[0][1])
        for i in range(6):
            cx, cy, heading = corners[i]
            tina.setheading(heading)
            sierpinski_hexagon(size / 3, depth - 1)
            next_i = (i + 1) % 6
            nx, ny, _ = corners[next_i]
            tina.setheading(tina.towards(nx, ny))
            tina.goto(nx, ny)

        tina.goto(start_x, start_y)
        tina.setheading(start_heading)

tina.penup()
tina.goto(0, -150)
tina.pendown()
sierpinski_hexagon(100, 3)
turtle.exitonclick()