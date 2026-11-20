###
# Fills a 5x5 array with a multiplication table and prints it
#
arr = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]  # typ: list zawierająca 5 elementów, a każdy z nich to list z 5 elementami typu int; to lista dwuwymiarowa 5 na 5

for i in range(len(arr)):  # len() to funkcja wbudowana; zwraca liczbę wierszy (5), a range() daje indeksy wierszy 0-4
    for j in range(len(arr[i])):  # arr[i] to jeden wiersz (list), więc len(arr[i]) to liczba kolumn; j to indeks kolumny
        arr[i][j] = (i + 1) * (j + 1)  # indeksy zaczynają się od 0, a tabliczka od 1, więc do obu dodaję 1; pole w wierszu i kolumnie j dostaje ich iloczyn; arr[i][j] = ... zapisuje wartość do konkretnego pola (int)

for row in arr:  # pętla zewnętrzna bierze po kolei każdy wiersz; row jest typu list
    for value in row:  # pętla wewnętrzna bierze po kolei każdą wartość wiersza; value jest typu int
        print(f'{value:2}', end=' ')  # print() to funkcja wbudowana; :2 dopełnia każdą liczbę spacjami do szerokości 2 znaków, dzięki czemu kolumny są równe, jak w przykładzie z polecenia; end=' ' zamiast nowej linii wypisuje spację
    print()  # pusty print() kończy bieżący wiersz