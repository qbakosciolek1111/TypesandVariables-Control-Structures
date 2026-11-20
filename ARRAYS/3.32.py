###
# Swaps the first and the last row of a 3x5 two-dimensional array
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

arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]  # arr[0] i arr[2] to całe wiersze (list), więc zamieniam je jednym przypisaniem; prawa strona jest liczona PRZED przypisaniem, więc nie trzeba zmiennej pomocniczej; len() zwraca 3, więc ostatni wiersz ma indeks 2

print('After:')
print_array(arr)