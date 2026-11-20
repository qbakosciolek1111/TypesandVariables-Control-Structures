###
# Counts the number of occurrences of any value in a tuple
#
numbers = (50, 20, 40, 50, 30, 50)  # typ: tuple (krotka) zawierająca 6 elementów typu int; krotki nie da się zmienić po utworzeniu
value = int(input('Value: '))  # input() zwraca str, a int() zamienia go na liczbę, bo porównujemy z liczbami w krotce

counter = 0  # typ: int; licznik wystąpień
for number in numbers:  # pętla for bierze po kolei każdy element krotki; number w każdym obrocie jest typu int
    if number == value:  # porównanie zwraca bool
        counter += 1

print('Tuple:', ','.join(map(str, numbers)))  # join() to metoda napisu i skleja tylko napisy (str), a elementy krotki to int, więc map(str, ...) najpierw zamienia każdą liczbę na napis; print() to funkcja wbudowana
print('Value:', value)
print('Number of occurrences:', counter)