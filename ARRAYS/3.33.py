###
# Swaps the first and the last column of a 3x5 two-dimensional array
# and prints the array before and after the change
#
def print_array(array):  # funkcja własna; parametr to list list, nic nie zwraca (zwraca None); wypisuje tablicę w wierszach i kolumnach, żeby nie powtarzać tej samej pętli przed zmianą i po niej
    for row in array:  # pętla zewnętrzna bierze po kolei każdy wiersz; row jest typu list
        for value in row:  # pętla wewnętrzna bierze po kolei każdą wartość wiersza; value jest typu int
            print(f'{value:2}', end=' ')  # print() to funkcja wbudowana; :2 dopełnia liczbę spacjami do szerokości 2 znaków, więc kolumny są równe; end=' ' zamiast nowej linii wypisuje spację
        print()  # pusty print() kończy wiersz

arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]  # typ: list zawierająca 3 elementy, a każdy z nich to list z 5 elementami typu int; to lista dwuwymiarowa: 3 wiersze i 5 kolumn

print('Before:')
print_array(arr)

last = len(arr[0]) - 1  # len() to funkcja wbudowana; arr[0] to pierwszy wiersz (list), więc len(arr[0]) to liczba kolumn (5); indeksy zaczynają się od 0, więc ostatnia kolumna ma indeks 4
for row in arr:  # w przeciwieństwie do zamiany wierszy (3.32), kolumna nie jest jednym obiektem; składa się z jednego pola w każdym wierszu, więc zamianę trzeba zrobić w KAŻDYM wierszu osobno
    row[0], row[last] = row[last], row[0]  # zamiana pierwszego i ostatniego pola wiersza w jednej linii; prawa strona jest liczona przed przypisaniem, więc nie trzeba zmiennej pomocniczej

print('After:')
print_array(arr)