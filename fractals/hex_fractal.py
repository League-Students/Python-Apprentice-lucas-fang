import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.hideturtle()

# Keep it drawing line-by-line visually
screen.tracer(1)
tina.speed('fastest')

# Exact matching vibrant green color
HEX_GREEN = "#5CFF42"

def hexaflake_clean(size, depth):
    if depth == 0:
        # Base case: draw a solid green hexagon with NO black outline lines
        tina.color(HEX_GREEN, HEX_GREEN)  
        tina.begin_fill()
        for _ in range(6):
            tina.forward(size)
            tina.left(60)
        tina.end_fill()
        
        # Optional: Add a black edge only to the outer border of this hexagon
        tina.color("black", HEX_GREEN)
        for _ in range(6):
            tina.forward(size)
            tina.left(60)
    else:
        # Recursive case
        for _ in range(6):
            hexaflake_clean(size / 3, depth - 1)
            
            # Move along the geometric outline with pen hidden to avoid stray cross-lines
            tina.color(HEX_GREEN) 
            tina.forward(size * 2 / 3)
            tina.left(60)

# Center the drawing on screen
tina.penup()
tina.goto(-100, -150) 
tina.pendown()
tina.pensize(2)

# Draw the clean depth 2 pattern line-by-line
hexaflake_clean(300, 2)

turtle.exitonclick()

