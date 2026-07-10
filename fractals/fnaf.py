import turtle
import time

tina = turtle.Turtle()

screen = turtle.Screen()
screen.setup(500 , 500)

tina.shape("turtle")
tinapath = [1, 2, 3, 4, 5]
tinaprogress = 0

camcolors = ["red", "black", "white","green","blue"]

def movetina():
    
def showanimes(cam_num):
    if(cam_num == tinapath[tinaprogress]):
        tina.showturtle()
    else:
        tina.hideturtle()

def opencam1():
    print("cam 1 open")
    screen.bgcolor(camcolors[0])
    showanimes(1)

def opencam2():
    print("cam 2 open")
    screen.bgcolor(camcolors[1])
    showanimes(2)

def opencam3():
    print("cam 3 open")
    screen.bgcolor(camcolors[2])
    showanimes(3)

def opencam4():
    print("cam 4 open")
    screen.bgcolor(camcolors[3])
    showanimes(4)

def opencam5():
    print("cam 5 open")
    screen.bgcolor(camcolors[4])
    showanimes(5)

def exitcam():
    print("cam exited")
    screen.bgcolor("yellow")
    showanimes(-1)

exitcam()

screen.listen()
screen.onkey(opencam1, "1")
screen.onkey(opencam2, "2")
screen.onkey(opencam3, "3")
screen.onkey(opencam4, "4")
screen.onkey(opencam5, "5")
screen.onkey(exitcam, "0")

screen.ontimer(movetina, 1000)

turtle.exitonclick()