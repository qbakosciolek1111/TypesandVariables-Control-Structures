###
# Modifies array values and prints the array after each change
#
arr = [1, 2, 3, 4, 5]  # typ: list (lista) zawierająca elementy typu int (liczby całkowite)
print('Array:', arr)  # print() to funkcja wbudowana; wypisuje napis (str) i listę (list)

arr[0] = arr[0] - 1  # arr[0] to int pod indeksem 0; listy są modyfikowalne, więc można podmienić element
print('Array:', arr)

arr[len(arr) - 1] = arr[len(arr) - 1] + 4  # len() to funkcja wbudowana, zwraca int (5), więc ostatni indeks to 4
print('Array:', arr)

middle = len(arr) // 2  # // to dzielenie całkowite, wynik typu int (2), czyli indeks środkowego elementu
arr[middle] = arr[middle] * 2  # mnożenie int * int daje int
print('Array:', arr)