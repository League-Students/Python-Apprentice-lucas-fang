import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()
tina.speed('fastest')

# Enable RGB color mode up to 255
screen.colormode(255)

def fractal_square(size, depth):
    if depth == 0:  # base case
        # Get coordinates and convert negative values to positive
        # Screen is 600x600, so coords range roughly from -300 to 300
        x = int(tina.xcor() + 300)
        y = int(tina.ycor() + 300)
        
        # Map coordinates to 0-255 RGB range (clamped to prevent errors)
        r = max(0, min(255, int((x / 600) * 255)))
        g = max(0, min(255, int((y / 600) * 255)))
        
        # Calculate Blue using a mix of X and Y for a smooth diagonal gradient
        b = max(0, min(255, int(((x + y) / 1200) * 255)))
        
        # Set BOTH the edge/pen color and the fill color to match
        tina.color(r, g, b)
        
        tina.begin_fill()
        for i in range(4):
            tina.forward(size)
            tina.left(90)
        tina.end_fill()
    else:  # recursive case
        for i in range(4):
            fractal_square(size / 3, depth - 1)
            tina.forward(size / 3)            
            fractal_square(size / 3, depth - 1)
            tina.forward(size * 2 / 3)
            tina.left(90)

# Move tina to a good spot to center the 400px fractal on a 600x600 screen
tina.penup()
tina.goto(-200, -200) 
tina.pendown()

# Set depth to 3 for fast rendering. Increase to 4 if you want higher detail!
fractal_square(400, 4) 
turtle.exitonclick()
