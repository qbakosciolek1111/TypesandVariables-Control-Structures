###
# Draw a square using the draw_square(length) function
#
import turtle

def draw_square(length): 
    for i in range(4):
        pen.forward(length) 
        pen.right(90)  # cztery razy: bok i skręt o 90 stopni, co daje kwadrat

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length
side_length = 100

# Draw a square
draw_square(side_length)  # jedno wywołanie zastępuje pętlę for z oryginalnego programu

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()  # utrzymuje okno otwarte, dopóki go nie zamkniesz