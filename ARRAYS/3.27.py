###
# Prints the values of a 2x4 two-dimensional array in rows and columns
#
arr = [
    [4, 8, 15, 16],
    [23, 42, 7, 3]
]  # typ: list zawierająca 2 elementy, a każdy z nich to list z 4 elementami typu int; to lista dwuwymiarowa: wiersz to jedna wewnętrzna lista, kolumna to pozycja w niej

for row in arr:  # pętla zewnętrzna bierze po kolei każdy wiersz; row w każdym obrocie jest typu list
    for value in row:  # pętla wewnętrzna bierze po kolei każdą wartość wiersza; value jest typu int
        print(value, end=' ')  # print() to funkcja wbudowana; end=' ' to parametr nazwany, który zamiast nowej linii wypisuje spację, więc wartości jednego wiersza stoją obok siebie
    print()  # pusty print() kończy bieżący wiersz i przechodzi do następnego