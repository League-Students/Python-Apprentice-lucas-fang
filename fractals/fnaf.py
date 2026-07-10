import turtle
import time

tina = turtle.Turtle()

screen = turtle.Screen()
screen.setup(500 , 500)

tina.shape("turtle")
tinapath = [1, 2, 3, 4, 5]
tinaprogress = 0
camnum = 0
camcolors = ["red", "black", "white","green","blue"]

def movetina():
    global tinaprogress
    tinaprogress += 1
    if tinaprogress == len(tina_path):
        print("game over :((((")
    showanimes()
    screen.ontimer(movetina,2000)

def showanimes():
    global camnum
    if(camnum == tinapath[tinaprogress]):
        tina.showturtle()
    else:
        tina.hideturtle()

def opencam1():
    global camnum
    camnum = 1
    print("cam 1 open")
    screen.bgcolor(camcolors[0])
    showanimes()

def opencam2():
    global camnum
    camnum = 2
    print("cam 2 open")
    screen.bgcolor(camcolors[1])
    showanimes()

def opencam3():
    global camnum
    camnum = 3
    print("cam 3 open")
    screen.bgcolor(camcolors[2])
    showanimes()

def opencam4():
    global camnum
    camnum = 4
    print("cam 4 open")
    screen.bgcolor(camcolors[3])
    showanimes()

def opencam5():
    global camnum
    camnum = 5
    print("cam 5 open")
    screen.bgcolor(camcolors[4])
    showanimes()

def exitcam():
    print("cam exited")
    screen.bgcolor("yellow")
    showanimes()

exitcam()

screen.listen()
screen.onkey(opencam1, "1")
screen.onkey(opencam2, "2")
screen.onkey(opencam3, "3")
screen.onkey(opencam4, "4")
screen.onkey(opencam5, "5")
screen.onkey(exitcam, "0")

screen.ontimer(movetina, 2000)

turtle.exitonclick()