###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import turtle

def draw_square(length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)  # cztery razy bok i skręt o 90 stopni, co daje kwadrat

def draw_triangle(length):
    for i in range(3):
        pen.forward(length)
        pen.right(120)  # trzy razy bok i skręt o 120 stopni; trzy skręty dają razem 360, więc żółw wraca do kierunku, w którym zaczął, i kolejna figura nie jest obrócona

def draw_rectangle(length_a, length_b):
    for i in range(2):  # dwie pary boków: a, b, a, b
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)

def go_to(x, y):  # skraca trzy linie z polecenia (podnieś pisak, idź, opuść pisak), które trzeba powtórzyć przed każdą figurą
    pen.penup()  # bez podniesienia pisaka żółw zostawiłby linię po drodze do nowego miejsca
    pen.goto(x, y)
    pen.pendown()

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

## Draw figures
go_to(-150, 80)  # współrzędne (0, 0) to środek okna; x rośnie w prawo, y w górę
draw_square(60)
go_to(-150, -80)
draw_square(60)

go_to(-30, 80)
draw_triangle(70)
go_to(-30, -80)
draw_triangle(70)

go_to(80, 80)
draw_rectangle(100, 50)
go_to(80, -80)
draw_rectangle(100, 50)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()