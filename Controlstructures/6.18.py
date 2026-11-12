###
# Determines in which quadrant of the coordinate system the point P(x, y)
# is located, or on which axis, or that it is the origin (0,0)
#
x = int(input('x = '))
y = int(input('y = '))

if x == 0 and y == 0:  # ten przypadek sprawdzam NA POCZĄTKU, bo punkt (0,0) leży jednocześnie na obu osiach; gdyby sprawdzanie osi było wcześniej, nigdy by do niego nie doszło
    print('Point P(0,0) is at the origin of the coordinate system')
elif x == 0:  # x równe 0 (a y różne od 0, bo zero już obsłużone) oznacza punkt na osi pionowej
    print(f'Point P({x},{y}) is on the Y axis')
elif y == 0:  # tak samo: y równe 0 oznacza punkt na osi poziomej
    print(f'Point P({x},{y}) is on the X axis')
elif x > 0 and y > 0:  # dopiero tutaj wiadomo, że żadna współrzędna nie jest zerem, więc można ustalać ćwiartkę po znakach
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
else:  # zostaje ostatnia kombinacja: x > 0 i y < 0
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')