###
# Replaces the main diagonal of a square matrix with 1
#
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]  # typ: list zawierająca 3 elementy, a każdy z nich to list z 3 elementami typu int; to lista dwuwymiarowa, czyli macierz kwadratowa 3 na 3

for i in range(len(matrix)):  # len() to funkcja wbudowana; zwraca liczbę wierszy (3), a range() daje indeksy 0, 1, 2
    matrix[i][i] = 1  # przekątna główna to pola, w których numer wiersza jest równy numerowi kolumny, czyli [0][0], [1][1], [2][2]; dlatego wystarczy jedna pętla, a nie dwie zagnieżdżone; matrix[i] to cały wiersz (list), a drugi indeks wybiera w nim jedno pole (int)

for row in matrix:  # pętla zewnętrzna bierze po kolei każdy wiersz; row jest typu list
    for value in row:  # pętla wewnętrzna bierze po kolei każdą wartość wiersza; value jest typu int
        print(value, end=" ")  # print() to funkcja wbudowana; end=" " zamiast nowej linii wypisuje spację, więc wartości wiersza stoją obok siebie
    print()  # pusty print() kończy bieżący wiersz