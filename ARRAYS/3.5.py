###
# Calculates the arithmetic mean of array values using the for loop
#
arr = [15, 8, 31, 47, 2, 19]  # typ: list zawierająca 6 elementów typu int

total = 0  # typ: int; suma elementów, zaczynam od 0, żeby pierwsze dodawanie nie zafałszowało wyniku
for value in arr:  # pętla for bierze po kolei każdy element listy; value w każdym obrocie jest typu int
    total += value  # skrót od total = total + value

mean = total / len(arr)  # len() to funkcja wbudowana; zwraca liczbę elementów (6); operator / zawsze zwraca float, więc średnia ma część ułamkową

print('Array:', arr)  # print() to funkcja wbudowana
print('Arithmetic mean:', round(mean, 2))  # round() to funkcja wbudowana; drugi argument 2 oznacza dwa miejsca po przecinku, żeby nie wypisywać 20.333333333333332