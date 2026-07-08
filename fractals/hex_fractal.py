import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600,600)
tina.hideturtle()
tina.speed('fastest')
# Tell python to work with turtles, make tina, set screen size, hide tina, set tinas speed. 
def fractal_square(size, depth):
    if depth == 0: # base case

        for i in range(6):
            tina.left(30)
            tina.forward(size)
            tina.right(120)

        for i in range(6):
            tina.forward(size)
            tina.right(120)
        tina.right(60)
        tina.forward(size)
        tina.left(150)
    else: #recursive case
        
#move tina to a good spot
tina.penup()
tina.goto(0 , 0)
tina.pendown()
fractal_square(200, 0)
turtle.exitonclick()