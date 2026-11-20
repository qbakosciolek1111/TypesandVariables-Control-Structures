###
# Draws the function y = sin(x) for an angle in the range 0-360 degrees
#
import math  # potrzebny do sin() i radians()
import matplotlib.pyplot as plt  # as plt to skrót nazwy modułu; wymaga wcześniejszej instalacji: python -m pip install matplotlib

x = []  # typ: pusta list; trafią do niej kąty w stopniach
y = []  # typ: pusta list; trafią do niej wartości sinusa

for angle in range(0, 361):  # range() to funkcja wbudowana; 361, bo górna granica nie wchodzi do zakresu, a 360 ma się znaleźć na wykresie; angle jest typu int
    x.append(angle)  # append() to metoda listy; dopisuje kąt na koniec
    y.append(math.sin(math.radians(angle)))  # math.sin() przyjmuje kąt w RADIANACH, a nie w stopniach, więc math.radians() najpierw zamienia stopnie na radiany; bez tego dostałbyś zły wykres; sin zwraca float z zakresu od -1 do 1

plt.plot(x, y)  # plot() rysuje linię przez punkty złożone z kolejnych par (x, y); obie listy mają po 361 elementów
plt.show()  # show() otwiera okno z wykresem; bez tego nic się nie wyświetli