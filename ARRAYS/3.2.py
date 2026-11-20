###
# Prints an array in reverse order
#
arr = [15, 8, 31, 47, 2, 19]  # typ: list zawierająca 6 elementów typu int

print('existed array:', end=' ')  # print() to funkcja wbudowana; end=' ' to parametr nazwany, który zamiast nowej linii wypisuje spację, więc liczby pojawią się w tym samym wierszu
for value in arr:  # pętla for bierze po kolei każdy element listy; value w każdym obrocie jest typu int
    print(value, end=' ')
print()  # pusty print() kończy wiersz

print('reverse array:', end=' ')
for i in range(len(arr) - 1, -1, -1):  # len() zwraca 6; range(5, -1, -1) daje 5, 4, 3, 2, 1, 0, czyli indeksy od ostatniego do pierwszego; trzeci argument -1 to krok w dół, a -1 jako koniec, bo górna granica nie wchodzi do zakresu, więc 0 jeszcze się liczy
    print(arr[i], end=' ')  # arr[i] to element typu int pod indeksem i
print()