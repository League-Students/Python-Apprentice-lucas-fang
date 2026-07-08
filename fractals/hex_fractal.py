import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600,600)
tina.hideturtle()
tina.speed('fastest')
# Tell python to work with turtles, make tina, set screen size, hide tina, set tinas speed. 
def fractal_square(size, depth):
    if depth == 0: # base case
        tina.begin_fill()
        for i in range(6):
            tina.forward(size)
            tina.left(60)
        tina.end_fill()
    else: #recursive case
        for i in range(6):
            fractal_square(size / 6, depth - 1)
            tina.forward(size / 6)            
            tina.left(60)
            fractal_square(size / 6, depth - 1)
            tina.forward(size * 2 / 6)
            tina.left(60)

#move tina to a good spot
tina.penup()
tina.goto(-250 , -250)
tina.pendown()
fractal_square(400, 3)
turtle.exitonclick()