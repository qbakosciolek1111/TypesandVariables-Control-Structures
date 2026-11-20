###
# Creates identity matrices and prints them in rows and columns
#
def identity_matrix(n):  # funkcja własna; parametr n to int (rozmiar), zwraca list list (macierz n na n)
    matrix = [[0 for j in range(n)] for i in range(n)]  # lista składana tworzy n wierszy, a każdy z nich to OSOBNA lista z n zerami; zapis [[0] * n] * n byłby błędem, bo powtórzyłby ten sam wiersz n razy
    for i in range(n):  # range() to funkcja wbudowana; daje indeksy 0 do n-1
        matrix[i][i] = 1  # macierz jednostkowa ma jedynki tylko na przekątnej głównej, czyli tam, gdzie numer wiersza jest równy numerowi kolumny; dlatego wystarczy jedna pętla, a nie dwie
    return matrix

def print_matrix(matrix):  # funkcja własna; parametr to list list, nic nie zwraca (zwraca None)
    for row in matrix:  # pętla zewnętrzna bierze po kolei każdy wiersz; row jest typu list
        for value in row:  # pętla wewnętrzna bierze po kolei każdą wartość wiersza; value jest typu int
            print(value, end=' ')  # print() to funkcja wbudowana; end=' ' zamiast nowej linii wypisuje spację
        print()  # pusty print() kończy wiersz

for size in [3, 5, 8]:  # typ: list zawierająca 3 elementy typu int, czyli rozmiary z polecenia
    print(f'Identity matrix {size}x{size}:')
    print_matrix(identity_matrix(size))  # wynik jednej funkcji (list list) trafia od razu jako argument drugiej
    print()  # pusty print() wypisuje pustą linię między macierzami