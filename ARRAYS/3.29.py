###
# Creates a two-dimensional array filled with zeros
#
def create_2d_arr(x, y):  # funkcja własna; parametry to dwa int (liczba wierszy i kolumn), zwraca list list
    return [[0 for j in range(y)] for i in range(x)]  # wewnętrzna lista składana tworzy jeden wiersz z y zer, a zewnętrzna powtarza to x razy, więc każdy wiersz jest OSOBNĄ listą; zapis [[0] * y] * x byłby błędem, bo powtórzyłby ten sam wiersz x razy i zmiana jednego pola zmieniłaby całą kolumnę

arr = create_2d_arr(3, 5)  # typ: list zawierająca 3 elementy, a każdy z nich to list z 5 elementami typu int
print(arr)  # print() to funkcja wbudowana; wypisuje całą listę list w jednej linii

for row in arr:  # pętla zewnętrzna bierze po kolei każdy wiersz; row jest typu list
    for value in row:  # pętla wewnętrzna bierze po kolei każdą wartość; value jest typu int
        print(value, end=' ')  # end=' ' to parametr nazwany, który zamiast nowej linii wypisuje spację
    print()  # pusty print() kończy wiersz