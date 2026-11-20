###
# Finds the maximum and minimum number in an array
# without using the built-in max() and min() functions
#
arr = [-15, 8, -31, 47, -2, 19]  # typ: list zawierająca 6 elementów typu int (także ujemnych)

max_value = arr[0]  # typ: int; zaczynam od pierwszego elementu, a nie od 0, bo gdyby wszystkie liczby były ujemne, zero byłoby błędnie uznane za największą
min_value = arr[0]  # typ: int; z tego samego powodu zaczynam od pierwszego elementu, a nie od 0

for value in arr:  # pętla for bierze po kolei każdy element listy; value w każdym obrocie jest typu int
    if value > max_value:  # nowa liczba większa od dotychczasowej największej, więc ją zastępuje
        max_value = value
    if value < min_value:  # to osobny if, a nie elif, bo każdą liczbę sprawdzam pod kątem obu rekordów
        min_value = value

print('Array:', arr)  # print() to funkcja wbudowana
print('Maximum number:', max_value)
print('Minimum number:', min_value)