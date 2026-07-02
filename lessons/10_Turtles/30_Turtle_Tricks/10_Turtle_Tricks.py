"""
# 10_Turtle_Tricks.py

In this exercise, you will use Tina the Turtle to draw an equilateral triangle.

- Use the commands: tina.forward() and tina.left() to draw the three sides of the triangle.
- Change the pen color before drawing each side using tina.pencolor(), so each side is a different color.

Refer to previous turtle programs for examples of how to use these commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
import random
turtle.setup(600, 600, 0, 0)            # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
#tina.hideturtle()
tina.speed('fastest')
he = 10
rad = 100
angle = 2
angle1 = random.uniform(0, 360)
# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

... # Your code here
window = turtle.Screen()
window.bgcolor('black')
for i in range(0, 0 ):
  tina.circle( rad , steps= 3)
  tina.left( angle1 )
  tina.circle(- rad , steps = 3)
  tina.left( angle1 )
  tina.circle(rad, steps = 3)
  tina.right( angle )
  i = i + 1
  print(i)

n = 0 
tina.color('white')
for n in range(0, he ):
    tina.circle( rad , steps= 3)
    tina.left( angle1 )
    tina.circle(- rad , steps = 3)
    tina.left( angle1 )
    tina.circle( rad , steps = 3)
    tina.right( angle )
    n = n + 1
    print(n)
    
n = 0 
tina.color('red')
for n in range(0, he ):
    tina.circle( rad , steps= 3)
    tina.left( angle1 )
    tina.circle(- rad , steps = 3)
    tina.left( angle1 )
    tina.circle( rad , steps = 3)
    tina.right( angle )
    n = n + 1
    print(n)
    
n = 0 
tina.color('orange')
for n in range(0, he ):
    tina.circle( rad , steps= 3)
    tina.left( angle1 )
    tina.circle(- rad , steps = 3)
    tina.left( angle1 )
    tina.circle( rad , steps = 3)
    tina.right( angle )
    n = n + 1
    print(n)
    
n = 0 
tina.color('yellow')
for n in range(0, he ):
    tina.circle( rad , steps= 3)
    tina.left( angle1 )
    tina.circle(- rad , steps = 3)
    tina.left( angle1 )
    tina.circle( rad , steps = 3)
    tina.right( angle )
    n = n + 1
    print(n)
    
n = 0 
tina.color('green')
for n in range(0, he ):
    tina.circle( rad , steps= 3)
    tina.left( angle1 )
    tina.circle(- rad , steps = 3)
    tina.left( angle1 )
    tina.circle( rad , steps = 3)
    tina.right( angle )
    n = n + 1
    print(n)
    
n = 0 
tina.color('blue')
for n in range(0, he ):
    tina.circle( rad , steps= 3)
    tina.left( angle1 )
    tina.circle(- rad , steps = 3)
    tina.left( angle1 )
    tina.circle( rad , steps = 3)
    tina.right( angle )
    n = n + 1
    print(n)
    
n = 0 
tina.color('purple')
for n in range(0, he ):
    tina.circle( rad , steps= 3)
    tina.left( angle1 )
    tina.circle(- rad , steps = 3)
    tina.left( angle1 )
    tina.circle( rad , steps = 3)
    tina.right( angle )
    n = n + 1
    print(n)
tina.speed(1)  
radius = 50

tina.color("black", "lightblue")  # Outline and Fill colors
tina.begin_fill()

tina.setheading(0)
tina.backward(radius)  # Shift to place center at origin
tina.circle(radius)    # Draw circle
tina.forward(radius)   # Return to the starting center point

tina.end_fill()

turtle.exitonclick()                    # Close the window when we click on it