###
# Prints a tuple in reverse order
#
numbers = (10, 20, 30, 40, 50)  # typ: tuple (krotka) zawierająca 5 elementów typu int; krotki nie da się zmienić po utworzeniu, więc odwrócenie tworzy nową krotkę
reversed_numbers = numbers[::-1]  # [::-1] to wycinek z krokiem -1, który odwraca kolejność; zwraca NOWĄ krotkę (tuple) i nie zmienia oryginału

print('Tuple:', ','.join(map(str, numbers)))  # join() to metoda napisu i skleja tylko napisy (str), a elementy krotki to int; dlatego map(str, ...) najpierw zamienia każdą liczbę na napis; ',' to separator wstawiany między elementy
print('Reverse order:', ','.join(map(str, reversed_numbers)))  # print() to funkcja wbudowana