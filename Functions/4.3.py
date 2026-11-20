###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math  # potrzebne do pierwiastka, bo wzór Herona go wymaga

def triangle_area(a, b, c):
    s = (a + b + c) / 2  # s to połowa obwodu; wzór Herona liczy pole na podstawie samych boków, bez wysokości
    return math.sqrt(s * (s - a) * (s - b) * (s - c))  # wzór Herona: pierwiastek z iloczynu s i różnic między s a każdym bokiem

# Reads sides from the keyboard
a = float(input('Enter side a: '))  # float, bo boki mogą być ułamkami
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))
print(f'The area of a triangle with sides {a}, {b}, {c} is {triangle_area(a, b, c)}')

# Tests for the sides from the task
print(f'The area of a triangle with sides 3, 4, 5 is {triangle_area(3, 4, 5)}')
print(f'The area of a triangle with sides 5, 12, 13 is {triangle_area(5, 12, 13)}')
print(f'The area of a triangle with sides 7, 24, 25 is {triangle_area(7, 24, 25)}')