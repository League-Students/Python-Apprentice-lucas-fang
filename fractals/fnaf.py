import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(500 , 500)

camcolors = ["red", "black", "white","green","blue"]

def opencam1():
    print("cam 1 open")
    screen.bgcolor(camcolors[0])
def opencam2():
    print("cam 2 open")
    screen.bgcolor(camcolors[1])
def opencam3():
    print("cam 3 open")
    screen.bgcolor(camcolors[2])


screen.listen()
screen.onkey(opencam1, "1")
screen.onkey(opencam2, "2")
screen.onkey(opencam2, "3")

turtle.exitonclick()