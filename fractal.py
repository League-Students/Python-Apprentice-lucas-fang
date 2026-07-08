import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600,600)
tina.hideturtle()
tina.speed('fastest')

def fractal_triangle(size, depth):
    if depth == 0: # base case
        for i in range(3):
            tina.forward(size)
            tina.left(120)
    else: #recursive case
        for i in range(3):
            fractal_triangle(size / 2, depth - 1)
            tina.forward(size)
            tina.left(120)

#move tina to a good spot
tina.penup()
tina.goto(-250 , -250)
tina.pendown()
fractal_triangle(200, 5)
turtle.exitonclick()