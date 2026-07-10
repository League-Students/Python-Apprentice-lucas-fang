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
        b = 150  # Static blue value to keep colors vibrant
        
        # Apply the unique coordinate-based color
        tina.fillcolor(r, g, b)
        
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

# Move tina to a good spot
tina.penup()
tina.goto(-200, -200) # Slightly adjusted to center a 400px shape on a 600x600 screen
tina.pendown()

fractal_square(400, 3) # Lowered depth to 3 so it runs much faster, change to 4 if desired
turtle.exitonclick()
