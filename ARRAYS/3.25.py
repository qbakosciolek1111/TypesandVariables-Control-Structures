###
# Draws the graph of the function f(x) = x^2 - 3
#
import matplotlib.pyplot as plt  # as plt to skrót nazwy modułu; wymaga wcześniejszej instalacji: python -m pip install matplotlib

x = []  # typ: pusta list; trafią do niej wartości argumentu
y = []  # typ: pusta list; trafią do niej wartości funkcji

# create x values
for n in range(-100, 101):  # range() to funkcja wbudowana; 101, bo górna granica nie wchodzi do zakresu, a 100 ma się znaleźć na wykresie
    x = x + [n]  # operator + skleja dwie listy; [n] to jednoelementowa lista, więc n ląduje na końcu x (int)

# create y values
for n in x:  # pętla for bierze po kolei każdą wartość x; n jest typu int
    y = y + [n ** 2 - 3]  # ** to potęgowanie, więc n ** 2 - 3 to f(n); wynik trafia do y na tej samej pozycji co n w x, dzięki czemu obie listy mają tyle samo elementów, a plot() tego wymaga

# print chart
plt.plot(x, y)  # plot() rysuje linię przez punkty złożone z kolejnych par (x, y)
plt.show()  # show() otwiera okno z wykresem; bez tego nic się nie wyświetli