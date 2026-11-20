###
# Converts a two-dimensional array into a one-dimensional array
#
def flatten(array_2d):  # funkcja własna; parametr to list list, zwraca list z samymi wartościami (typu int)
    result = []  # typ: pusta list; trafią do niej wszystkie wartości po kolei
    for row in array_2d:  # pętla zewnętrzna bierze po kolei każdy wiersz; row jest typu list
        for value in row:  # pętla wewnętrzna bierze po kolei każdą wartość wiersza; value jest typu int
            result.append(value)  # append() to metoda listy; dopisuje wartość na koniec, więc wiersze ustawiają się jeden za drugim
    return result

arrays = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5], [7, 4], [2, 6]],
]  # typ: list zawierająca 3 tablice dwuwymiarowe, a każda z nich to list list z liczbami typu int

for array_2d in arrays:  # pętla for bierze po kolei każdą tablicę; array_2d w każdym obrocie jest typu list
    print('2D array:', array_2d)  # print() to funkcja wbudowana
    print('1D array:', flatten(array_2d))  # wynik funkcji (list) trafia od razu jako argument print()
    print()  # pusty print() wypisuje pustą linię między tablicami