import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(500 , 500)
tina.shape("turtle")
tinapath = [1, 2, 3, 4, 5]
tinaprogress = 0
camcolors = ["red", "black", "white","green","blue"]

def showanimes(cam_num):
    if(cam_num == tinapath[tinaprogress]):
        tina.showturtle()
    else:
        tina.hideturtle()

def opencam1():
    print("cam 1 open")
    screen.bgcolor(camcolors[0])

def opencam2():
    print("cam 2 open")
    screen.bgcolor(camcolors[1])

def opencam3():
    print("cam 3 open")
    screen.bgcolor(camcolors[2])

def opencam4():
    print("cam 4 open")
    screen.bgcolor(camcolors[3])

def opencam5():
    print("cam 5 open")
    screen.bgcolor(camcolors[4])

def exitcam():
    print("cam exited")
    screen.bgcolor("yellow")

exitcam()

screen.listen()
screen.onkey(opencam1, "1")
screen.onkey(opencam2, "2")
screen.onkey(opencam3, "3")
screen.onkey(opencam4, "4")
screen.onkey(opencam5, "5")
screen.onkey(exitcam, "0")

turtle.exitonclick()