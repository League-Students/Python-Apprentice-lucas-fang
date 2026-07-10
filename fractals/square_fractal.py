import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(700, 700)
tina.hideturtle()

# CRITICAL: Tracer speeds up the rendering so you don't have to wait!
screen.tracer(0) 

def draw_solid_hexagon(size):
    tina.begin_fill()
    for _ in range(6):
        tina.forward(size)
        tina.left(60)
    tina.end_fill()

def hexflake(x, y, size, depth):
    if depth == 0:
        # Move to position and draw the base shape
        tina.penup()
        tina.goto(x, y)
        tina.pendown()
        draw_solid_hexagon(size)
    else:
        # Calculate the size of the smaller hexagons (1/3 of original)
        new_size = size / 3
        
        # Draw 7 smaller hexagons: 1 in the center, 6 at the corners
        # Center hexagon
        hexflake(x, y, new_size, depth - 1)
        
        # 6 Corner hexagons
        tina.penup()
        tina.goto(x, y)
        for i in range(6):
            # Move to a vertex position
            tina.forward(size * 2 / 3) 
            current_pos = tina.position()
            
            # Recursively draw the smaller hexagon at this vertex
            hexflake(current_pos[0], current_pos[1], new_size, depth - 1)
            
            # Reset to center and turn to the next vertex angle
            tina.penup()
            tina.goto(x, y)
            tina.left(60)

# Run the fractal (Centered at 0,0, Size 250, Depth 3)
hexflake(0, -120, 250, 3)

# Refresh the screen to show the finished drawing instantly
screen.update() 
turtle.exitonclick()
