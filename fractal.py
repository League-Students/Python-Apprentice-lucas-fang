import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600,600)
#tina.hideturtle()

def fractal_triangle(size, depth):
    if depth == 0: # base case
        for i in range(3):
            tina.forward(size)
            tina.left(120)
    else: #recursive case
        for i in range(3):
            fractal_triangle(size/2, depth - 1)


fractal_triangle(200, 2)
turtle.exitonclick()