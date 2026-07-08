"""import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600,600)
#tina.hideturtle()
#tina.speed('fastest')
# Tell python to work with turtles, make tina, set screen size, hide tina, set tinas speed. 
def fractal_triangle(size, depth):
    if depth == 0: # base case
        for i in range(4):
            tina.forward(size)
            tina.left(90)
    else: #recursive case
        for i in range(4):
            fractal_triangle(size / 2, depth - 1)
            tina.forward(size)
            tina.left(90)

#move tina to a good spot
tina.penup()
tina.goto(-250 , -250)
tina.pendown()
fractal_triangle(400, 4)
turtle.exitonclick()"""
import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()
tina.speed('fastest')

def fractal_square(size, depth):
    if depth == 0:  # base case: draw a standard square
        for i in range(4):
            tina.forward(size)
            tina.left(90)
    else:  # recursive case: draw smaller squares at each corner
        for i in range(4):
            fractal_square(size / 2, depth - 1)
            tina.forward(size)
            tina.left(90)

# Move tina to a good starting spot to center the image
tina.penup()
tina.goto(-200, -200)
tina.pendown()

# Draw the fractal (depth 4 or 5 looks best and runs quickly)
fractal_square(400, 4)
turtle.exitonclick()