###
# Transposes matrices (rows become columns) and prints them in rows and columns
#
def transpose_matrix(m):  # funkcja własna; parametr to list list (macierz), zwraca NOWĄ list list; oryginał się nie zmienia
    rows = len(m)  # len() to funkcja wbudowana; zwraca liczbę wierszy (int)
    cols = len(m[0])  # m[0] to pierwszy wiersz (list), więc len(m[0]) to liczba kolumn (int)
    result = [[0 for j in range(rows)] for i in range(cols)]  # macierz po transpozycji ma ODWROTNE wymiary: tyle wierszy, ile było kolumn, i tyle kolumn, ile było wierszy; lista składana tworzy każdy wiersz jako osobną listę
    for i in range(rows):  # range() to funkcja wbudowana; indeksy wierszy oryginału
        for j in range(cols):  # indeksy kolumn oryginału
            result[j][i] = m[i][j]  # to jest właśnie transpozycja: pole z wiersza i, kolumny j trafia do wiersza j, kolumny i, czyli indeksy zamieniają się miejscami
    return result

def print_matrix(matrix):  # funkcja własna; parametr to list list, nic nie zwraca (zwraca None)
    for row in matrix:  # pętla zewnętrzna bierze po kolei każdy wiersz; row jest typu list
        for value in row:  # pętla wewnętrzna bierze po kolei każdą wartość wiersza; value jest typu int
            print(value, end=' ')  # print() to funkcja wbudowana; end=' ' zamiast nowej linii wypisuje spację
        print()  # pusty print() kończy wiersz

matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
    [[5, 6, 7, 8]],
]  # typ: list zawierająca 3 macierze, a każda z nich to list list; trzecia to jeden wiersz, więc dwa nawiasy [[...]] są konieczne, żeby była dwuwymiarowa

for m in matrices:
    print('Matrix:')
    print_matrix(m)
    print('Transposed matrix:')
    print_matrix(transpose_matrix(m))  # wynik jednej funkcji (list list) trafia od razu jako argument drugiej
    print()  # pusty print() wypisuje pustą linię między macierzami