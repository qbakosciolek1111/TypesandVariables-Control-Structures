###
# Sorts three arrays using the Bubble Sort algorithm
#
def bubblesort(array):  # funkcja własna; parametr to list z liczbami, zwraca tę samą listę po posortowaniu
    n = len(array)  # len() to funkcja wbudowana; zwraca liczbę elementów (int)
    for i in range(n):  # każdy obrót zewnętrznej pętli "wypycha" jedną największą wartość na właściwe miejsce na końcu listy
        for j in range(n - i - 1):  # wewnętrzna pętla porównuje sąsiadów; n - i - 1, bo ostatnie i elementów jest już na swoich miejscach, a indeks j + 1 nie może wyjść poza listę
            if array[j] > array[j + 1]:  # lewy sąsiad większy od prawego, więc są w złej kolejności
                array[j], array[j + 1] = array[j + 1], array[j]  # zamiana miejscami w jednej linii; prawa strona jest liczona przed przypisaniem, więc nie trzeba zmiennej pomocniczej
    return array

arrays = [
    [5, 2, 9, 1, 7],
    [10, -3, 4, 0, 8, -7],
    [3, 3, 1, 2],
]  # typ: list zawierająca 3 elementy, a każdy z nich to list z liczbami typu int; trzecia tablica ma powtórzoną wartość, żeby sprawdzić, że sortowanie radzi sobie z duplikatami

for array in arrays:  # pętla for bierze po kolei każdą tablicę; array w każdym obrocie jest typu list
    print('Before:', array)  # print() to funkcja wbudowana; wypisuje napis (str) i listę (list)
    print('After: ', bubblesort(array))  # bubblesort() zmienia listę w miejscu, więc wypisanie "Before" musi być PRZED wywołaniem, inaczej pokazałoby już posortowaną
    print()  # pusty print() wypisuje pustą linię między tablicami