###
# Counts the even values in an array using the while loop
#
arr = [34, 7, 19, 4, 21, 8]  # typ: list zawierająca 6 elementów typu int
even_count = 0  # typ: int; licznik parzystych wartości
i = 0  # typ: int; indeks, który w while trzeba ustawić ręcznie przed pętlą

while i < len(arr):  # len() to funkcja wbudowana; zwraca liczbę elementów (6), więc pętla przejdzie przez indeksy 0-5
    if arr[i] % 2 == 0:  # arr[i] to element typu int; % zwraca resztę z dzielenia, a reszta 0 przy dzieleniu przez 2 oznacza liczbę parzystą; porównanie zwraca bool
        even_count += 1
    i += 1  # bez zwiększania indeksu warunek byłby zawsze prawdziwy i program zapętliłby się w nieskończoność

print('Array:', arr)  # print() to funkcja wbudowana
print('Number of even values:', even_count)