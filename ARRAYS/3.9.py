###
# Compares two arrays: they are the same if they have the same number
# of elements and equal values at the same indexes
#
def compare(array1, array2):  # funkcja własna; parametry to dwie list, zwraca bool
    if len(array1) != len(array2):  # len() to funkcja wbudowana; zwraca liczbę elementów (int); różna długość wystarczy, żeby tablice były różne, więc kończę od razu
        return False
    for i in range(len(array1)):  # range() to funkcja wbudowana; daje indeksy, bo trzeba porównywać elementy z tych samych pozycji obu list
        if array1[i] != array2[i]:  # != zwraca bool; jeden niezgodny element wystarczy, żeby tablice były różne
            return False  # return kończy funkcję od razu, więc dalsze elementy nie są już sprawdzane
    return True  # pętla przeszła przez wszystkie elementy i nic się nie różniło

def print_array(array):  # funkcja własna; wypisuje elementy w jednym wierszu, nic nie zwraca (zwraca None)
    for value in array:  # value może być typu str, bool lub int, zależnie od tablicy
        print(value, end=' ')  # print() to funkcja wbudowana; end=' ' to parametr nazwany, który zamiast nowej linii wypisuje spację
    print()  # pusty print() kończy wiersz

pairs = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2]),
]  # typ: list zawierająca 4 krotki (tuple), a każda krotka to para list do porównania

for array1, array2 in pairs:  # w każdym obrocie krotka rozpakowuje się na dwie zmienne, każda typu list
    print('Array1:', end=' ')
    print_array(array1)
    print('Array2:', end=' ')
    print_array(array2)
    if compare(array1, array2):  # compare() zwraca bool, więc wystarczy wstawić ją wprost do if
        print('Comparison: arrays are the same')
    else:
        print('Comparison: arrays are different')
    print()  # pusta linia oddziela kolejne pary