###
# Computes the second power of each array element
#
arr = [8, 2, 5, 1, 9]  # typ: list zawierająca 5 elementów typu int
squares = []  # typ: pusta list; dołożę do niej po jednym kwadracie na każdy element

for value in arr:  # pętla for bierze po kolei każdy element listy; value w każdym obrocie jest typu int
    squares.append(value ** 2)  # ** to operator potęgowania, więc value ** 2 to value do kwadratu (int); append() to metoda listy, która dopisuje element na koniec

print('Array:', end=' ')  # print() to funkcja wbudowana; end=' ' to parametr nazwany, który zamiast nowej linii wypisuje spację, więc liczby pojawią się w tym samym wierszu
for value in arr:
    print(value, end=' ')
print()  # pusty print() kończy wiersz

print('2nd power:', end=' ')
for square in squares:
    print(square, end=' ')
print()