###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])  # indeksy zaczynają się od 0, więc pierwszy element to arr[0], a nie arr[1]
print('Second value', arr[1])
print('Last value', arr[len(arr) - 1])  # ostatni indeks to długość minus 1 (dla 5 elementów jest to 4), bo liczymy od zera
print('Last but one value', arr[len(arr) - 2])  # polecenie zabrania indeksów ujemnych, więc przedostatni to długość minus 2
print('Sum of the first and last value', arr[0] + arr[len(arr) - 1])
print('Middle value', arr[len(arr) // 2])  # // to dzielenie całkowite: 5 // 2 daje 2, czyli indeks środkowego elementu; działa dla tablic o nieparzystej liczbie elementów

print('All values:', end=' ')
for value in arr:  # pętla po liście bierze po kolei każdy element
    print(value, end=' ')  # end=' ' zamienia koniec linii na spację, żeby wszystko było w jednym wierszu
print()  