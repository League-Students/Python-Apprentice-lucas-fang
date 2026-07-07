"""
# 30_Loop_with_Turtle.py

In this program, use a loop to draw a regular pentagon (5-sided shape) with Tina the Turtle.

- Review your previous program, 20_Loop_with_Turtle.py, which uses a loop to draw a shape with the turtle module.
- Make sure your code is clear and well-commented.
- Run your program to verify that Tina the Turtle draws a pentagon.

(Hint: You can copy and modify your previous code!)

uid: BpGnQq64
name: Loop With Turtle
"""

... # Your code here
import turtle #Tells Python we want turtle
turtle.setup(600 , 600 , 0 , 0) #Creates the drawing area
tina = turtle.Turtle() #Creates a turtle named tina
for side in range(1 , 6): #Loop to make all 5 sides
    tina.forward(100) #make the side
    tina.left(72) #turn so the next side is in the correct angle