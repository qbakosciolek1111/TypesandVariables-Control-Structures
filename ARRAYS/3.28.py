###
# Calculates the sum of values in the last column of a two-dimensional array
#
arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]  # typ: list zawierająca 4 elementy, a każdy z nich to list z 5 elementami typu int; to lista dwuwymiarowa: 4 wiersze i 5 kolumn

last_column = len(arr[0]) - 1  # len() to funkcja wbudowana; arr[0] to pierwszy wiersz (list), więc len(arr[0]) to liczba kolumn (5); indeksy zaczynają się od 0, więc ostatnia kolumna ma indeks 4
total = 0  # typ: int; suma, zaczynam od 0

for row in arr:  # pętla for bierze po kolei każdy wiersz; row w każdym obrocie jest typu list
    total += row[last_column]  # row[last_column] to jedna wartość z ostatniej kolumny (int); wystarczy jedna pętla, a nie dwie, bo z każdego wiersza potrzebuję tylko jednego pola

print('Last column values:', end=' ')  # print() to funkcja wbudowana; end=' ' zamiast nowej linii wypisuje spację
for row in arr:
    print(row[last_column], end=' ')
print()
print('Sum of the last column:', total)