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
        x = int(tina.xcor() + 300)
        y = int(tina.ycor() + 300)
        
        # Map coordinates to 0-255 RGB range
        r = max(0, min(255, int((x / 600) * 255)))
        g = max(0, min(255, int((y / 600) * 255)))
        b = 150  
        
        # Set BOTH the edge/pen color and the fill color
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

# Move tina to a good spot
tina.penup()
tina.goto(-200, -200) 
tina.pendown()

fractal_square(400, 4) 
turtle.exitonclick()
