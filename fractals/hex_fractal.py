import turtle
import math

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()
tina.speed('fastest')

def draw_hexagon(x, y, size):
    tina.penup()
    tina.goto(x, y)
    tina.setheading(0)
    tina.pendown()
    tina.begin_fill()
    for i in range(6):
        tina.forward(size)
        tina.left(60)
    tina.end_fill()

def sierpinski_hexagon(x, y, size, depth):
    if depth == 0:
        draw_hexagon(x, y, size)
    else:
        new_size = size / 2
        for i in range(6):
            angle_deg = 60 * i
            angle_rad = math.radians(angle_deg)
            offset_x = new_size * math.cos(angle_rad)
            offset_y = new_size * math.sin(angle_rad)
            sierpinski_hexagon(x + offset_x, y + offset_y, new_size, depth - 1)

# move to a good starting spot (centered-ish)
sierpinski_hexagon(0, -150, 200, 3)
turtle.exitonclick()