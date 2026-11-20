###
# Calculates the arithmetic mean of array values using the while loop
#
arr = [15, 8, 31, 47, 2, 19]  # typ: list zawierająca 6 elementów typu int

total = 0  # typ: int; suma elementów, zaczynam od 0
i = 0  # typ: int; indeks, który w while trzeba ustawić ręcznie przed pętlą (w for robił to sam range)
while i < len(arr):  # len() to funkcja wbudowana; zwraca liczbę elementów (6), więc pętla przejdzie przez indeksy 0-5
    total += arr[i]  # arr[i] to element typu int pod indeksem i
    i += 1  # bez zwiększania indeksu warunek byłby zawsze prawdziwy i program zapętliłby się w nieskończoność

mean = total / len(arr)  # operator / zawsze zwraca float, więc średnia ma część ułamkową

print('Array:', arr)  # print() to funkcja wbudowana
print('Arithmetic mean:', round(mean, 2))  # round() to funkcja wbudowana; drugi argument 2 oznacza dwa miejsca po przecinku