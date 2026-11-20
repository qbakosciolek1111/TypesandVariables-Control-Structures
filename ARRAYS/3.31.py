###
# Finds the smallest and largest values in a two-dimensional array
# and prints the row and column in which they are located
#
arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]  # typ: list zawierająca 4 elementy, a każdy z nich to list z 2 elementami typu int; to lista dwuwymiarowa: 4 wiersze i 2 kolumny

min_value = arr[0][0]  # typ: int; zaczynam od pierwszego pola, a nie od 0, bo przy samych liczbach ujemnych lub dodatnich zero byłoby błędnym rekordem
max_value = arr[0][0]
min_row = 0  # typ: int; indeks wiersza dotychczasowego minimum
min_col = 0  # typ: int; indeks kolumny dotychczasowego minimum
max_row = 0
max_col = 0

for i in range(len(arr)):  # len() to funkcja wbudowana; zwraca liczbę wierszy (4), a range() daje indeksy wierszy; indeksy są potrzebne, bo oprócz wartości trzeba zapamiętać jej POŁOŻENIE
    for j in range(len(arr[i])):  # arr[i] to jeden wiersz (list), więc len(arr[i]) to liczba kolumn; j to indeks kolumny
        if arr[i][j] < min_value:  # nowe pole mniejsze od dotychczasowego minimum, więc zapamiętuję jego wartość i położenie
            min_value = arr[i][j]
            min_row = i
            min_col = j
        if arr[i][j] > max_value:  # osobny if, a nie elif, bo każde pole sprawdzam pod kątem obu rekordów
            max_value = arr[i][j]
            max_row = i
            max_col = j

print('Array:', arr)  # print() to funkcja wbudowana
print(f'Smallest value: {min_value} (row {min_row + 1}, column {min_col + 1})')  # +1, bo indeksy zaczynają się od 0, a numery rzędów i kolumn dla człowieka od 1
print(f'Largest value: {max_value} (row {max_row + 1}, column {max_col + 1})')